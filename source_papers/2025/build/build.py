import fitz, json, importlib.util, glob, os, re
ROOT = "/Users/vijay/Documents/Vedant/Claude"
SRC = f"{ROOT}/source_papers/2025"
FIG = f"{SRC}/figs"
REL = "source_papers/2025/figs"
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(FIG, exist_ok=True)
order = ["maths_taonan","maths_henrypark","science_taonan","science_nanyang","english_henrypark","english_taonan"]
papers, flat, skipped = [], [], []
first_crop = {}

def crop(pdf, key, name, page, box, dpi=170):
    d = fitz.open(pdf); p = d[page-1]; s = p.rect.width/910
    r = fitz.Rect(box[0]*s, box[1]*s, box[2]*s, box[3]*s) & p.rect
    fn = f"{key}-{name}.png"
    p.get_pixmap(dpi=dpi, clip=r, colorspace=fitz.csGRAY).save(f"{FIG}/{fn}")
    return f"{REL}/{fn}"

for mod in order:
    spec = importlib.util.spec_from_file_location(mod, f"{DATA}/{mod}.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    P = m.PAPER; pdf = f"{SRC}/{P['pdf']}"; key = P["key"]
    passages = {}
    for pid, pv in getattr(m, "PASSAGES", {}).items():
        if isinstance(pv, str): passages[pid] = {"id": f"{key}-{pid}", "text": pv, "images": []}
        else: passages[pid] = {"id": f"{key}-{pid}", "text": pv.get("text",""), "images": [crop(pdf, key, f"passage-{pid}-{i+1}", *([b[0]] + [list(b[1:])]), dpi=200) for i,b in enumerate(pv["img"])]}
    uses = {}
    for q in m.Q:
        f = q.get("fig") or []
        for t in ([f] if isinstance(f, tuple) else f): uses[tuple(t)] = uses.get(tuple(t), 0) + 1
    qs = []
    for q in m.Q:
        if "skip" in q: skipped.append(f"{P['title']} {q['n']}: {q['skip']}"); continue
        slug = re.sub(r"[^a-z0-9]+","-",q["n"].lower()).strip("-")
        figs = q.get("fig") or []
        if isinstance(figs, tuple): figs = [figs]
        images = []
        for i, f in enumerate(figs):
            shared = uses.get(tuple(f), 0) > 1
            path = crop(pdf, key, slug + (f"-{i+1}" if len(figs) > 1 else ""), f[0], f[1:], dpi=300 if shared else 170)
            # The same crop used by several questions (e.g. a poster) points at one file, so print shows it once.
            images.append(first_crop.setdefault((key, tuple(f)), path))
        sol = q.get("solution","")
        text = q["text"]
        if q.get("note"):
            sol = (sol + "  " if sol else "") + "Note: " + q["note"]
            text += "\n(Part of the original question is not included here.)"
            skipped.append(f"{P['title']} {q['n']} (part): {q['note']}")
        out = {
            "subject": P["subject"], "topic": q["topic"], "type": q["type"], "difficulty": "Medium",
            "text": text, "options": q.get("options", []), "answer": q["answer"], "solution": sol,
            "images": images,
            "source": {"school": P["school"], "year": P["year"], "exam": P["exam"], "paper": P["title"], "paperKey": key, "qno": q["n"], "marks": q.get("marks",1)},
        }
        if q.get("accept"): out["accept"] = q["accept"]
        shared_imgs = [first_crop[(key, tuple(f))] for f in figs if uses.get(tuple(f), 0) > 1]
        if shared_imgs: out["sharedImages"] = shared_imgs
        if q.get("passage"): out["passage"] = passages[q["passage"]]
        assert q["type"] != "MCQ" or out["answer"] in out["options"], (key, q["n"])
        qs.append(out)
    papers.append({"key": key, "title": P["title"], "subject": P["subject"], "school": P["school"], "year": P["year"], "exam": P["exam"],
                   "sourcePdf": f"source_papers/2025/{P['pdf']}", "sourceSite": "testpapersfree.com", "questions": qs})
    flat += qs

js = "// Generated from free 2025 P5 papers on testpapersfree.com (see source_papers/2025/). Loaded by p5_practice_app.html.\nwindow.P5_PAST_PAPERS = " + json.dumps(papers, ensure_ascii=False, indent=1) + ";\n"
open(f"{SRC}/p5_past_papers_2025.js","w").write(js)
json.dump(flat, open(f"{SRC}/p5_past_papers_2025_questions.json","w"), ensure_ascii=False, indent=1)
open(f"{SRC}/SKIPPED.txt","w").write("\n".join(skipped)+"\n")
for p in papers:
    c = {}
    for q in p["questions"]: c[q["type"]] = c.get(q["type"],0)+1
    print(p["title"], len(p["questions"]), c)
print("total", len(flat), "figs", len(os.listdir(FIG)), "skipped", len(skipped))
