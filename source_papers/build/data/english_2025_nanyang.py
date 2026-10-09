PAPER = dict(key="2025-nanyang-english-eoy", subject="English", school="Nanyang Primary School", year=2025, exam="EOY (SA2)",
             title="Nanyang P5 English EOY 2025 (Paper 2)", pdf="2025/P5_English_2025_SA2_nanyang.pdf")
PASSAGES = {
 "goh": dict(img=[(21,185,200,775,630)]),
 "aircon": dict(img=[(22,165,180,770,1110),(23,165,105,800,580)]),
 "choy": dict(img=[(28,95,105,820,1100)]),
 "gratitude": dict(img=[(29,120,105,820,1060)]),
 "hawker": dict(img=[(30,120,125,800,1085)]),
 "space": dict(img=[(26,120,105,830,1050)]),
}
def mcq(n, topic, text, opts, ans, **kw): return dict(n=n, topic=topic, type="MCQ", marks=1, text=text, options=opts, answer=opts[ans-1], **kw)
Q = [
 mcq("A Q1","Grammar","Jenny was worried about the upcoming test ________ she did not revise enough.",["if","as","unless","therefore"],2),
 mcq("A Q2","Grammar","Rachel has a small appetite, so she ordered a dish without ________ meat.",["less","little","many","much"],4),
 mcq("A Q3","Grammar","Sarah goes for this enrichment class, ________ she?",["has","does","hasn't","doesn't"],4),
 mcq("A Q4","Grammar","Either Daisy or her cousins ________ prepared the cake for the party this weekend.",["did","will","has","have"],4),
 mcq("A Q5","Grammar","The most memorable experience Ms Tan had last summer was ________ her bicycle across the island.",["rode","rides","riding","ridden"],3),
 mcq("A Q6","Grammar","Mary, ________ friend owns a restaurant, works as a reporter.",["who","which","whom","whose"],4),
 mcq("A Q7","Grammar","Amy ________ wide awake in bed the whole night and could not go to sleep.",["lie","lay","laid","lain"],2),
 mcq("A Q8","Grammar","Ravi looked ________ his older brother for support when he asked their mother if they could keep a pet.",["to","into","over","after"],1),
 mcq("A Q9","Grammar","Not only ________ Amir ________ his dinner early, but he also washed the dishes.",["did ... finish","is ... finishing","does ... finish","was ... finishing"],1),
 mcq("A Q10","Grammar","All the furniture ________ moved to the store room last Friday to prepare for the repainting next week.",["has","was","have","were"],2),
 mcq("A Q11","Vocabulary","The paramedics did a/an ________ to show how first aid should be administered in case of injury.",["exhibit","display","experiment","demonstration"],4),
 mcq("A Q12","Vocabulary","A delay in travelling time is ________ due to the flashflood. Please be patient on the road.",["expected","regarded","proposed","speculated"],1),
 mcq("A Q13","Vocabulary","John looked at the ________ feast and frowned. \"There's going to be lots of leftovers and wastage tonight,\" he thought woefully.",["vacant","modest","excessive","invaluable"],3),
 mcq("A Q14","Vocabulary","Zara was ________ at a loss for words when asked to answer a question that she was not paying attention to.",["legibly","promptly","momentarily","ambiguously"],3),
 mcq("A Q15","Vocabulary","Fatigue began to ________ as Sandy stopped to catch her breath after completing the marathon.",["set in","set up","set off","set out"],1),
 mcq("A Q16","Vocabulary","Vocabulary cloze: choose the word(s) closest in meaning to 'various' (16) in the passage.",["a few notable","many different","numerous similar","some recognisable"],2, passage="goh"),
 mcq("A Q17","Vocabulary","Choose the word closest in meaning to 'shaping' (17) in the passage.",["growing","sustaining","influencing","manipulating"],3, passage="goh"),
 mcq("A Q18","Vocabulary","Choose the word closest in meaning to 'foundation' (18) in the passage.",["future","bottom","outline","groundwork"],4, passage="goh"),
 mcq("A Q19","Vocabulary","Choose the word closest in meaning to 'spearheaded' (19) in the passage.",["led","attacked","prioritised","challenged"],1, passage="goh"),
 mcq("A Q20","Vocabulary","Choose the word closest in meaning to 'prosperous' (20) in the passage.",["rising","serene","renowned","successful"],4, passage="goh"),
 mcq("A Q21","Comprehension (MCQ)","Visual text. According to the advertisement in Text 1, which of the following is true of BreezyCon air-conditioners?",["They barely use electricity.","They can be purchased online.","They do not affect the environment.","They have served some customers well."],4, passage="aircon"),
 mcq("A Q22","Comprehension (MCQ)","\"A better future starts with smarter choices.\" The writer included this statement in Text 1 ________.",["to give people a glimpse of BreezyCon's benefits","to tell people that they have control over the future","to convince people that they should choose BreezyCon","to get people to think about the choices they have made"],3, passage="aircon"),
 mcq("A Q23","Comprehension (MCQ)","According to Text 2, when shopping for an air-conditioner, consumers should ________.",["visit different shops to compare prices for different models and brands","look for the most eco-friendly models by asking companies for evidence of their efficiency","select air-conditioners which are advertised to be eco-friendly and have the best advertising campaigns","refer to official certifications and energy ratings issued by the authorities and reviews given by users"],4, passage="aircon"),
 mcq("A Q24","Comprehension (MCQ)","According to Text 2, which of the following statements is NOT true?",["Eco-friendly air-conditioners are very popular among consumers.","Buying eco-friendly air-conditioners reduces our carbon footprint significantly.","Shoppers should consider the maintenance costs before buying air-conditioners.","Advertisements do not consider whether the air-conditioners save energy in the long run."],2, passage="aircon"),
 mcq("A Q25","Comprehension (MCQ)","We cannot trust the way Text 1 promotes BreezyCon air-conditioners because Text 2 says ________.",["the impact on carbon footprint is always limited","such companies only highlight the efficiency of their products","it makes more sense to purchase air-conditioners that are durable and easy to maintain","consumers must study carefully advertising campaigns that label air-conditioners as eco-friendly"],2, passage="aircon"),
]
gc = [("H","most",[]),("K","that",["which"]),("L","to",[]),("F","her",[]),("M","was",[]),("Q","yet",[]),("E","despite",[]),("B","as",[]),("N","what",[]),("D","can",[])]
for i,(letter,w,alt) in enumerate(gc):
    d = dict(n=f"B Q{26+i}", topic="Grammar", type="Short Answer", marks=1, text=f"Grammar cloze: which word from the list best fits blank ({26+i})? Type the word (not the letter).", answer=w + (" (also accepted: which)" if alt else ""), solution=f"({letter}) {w}", passage="choy")
    if alt: d["accept"] = [w] + alt
    Q.append(d)
ed = [("express","expressing"),("physicle","physical"),("reselient","resilient"),("helping","helps"),("komplaineing","complaining"),("happy","happier"),("in","of"),("kompesionate","compassionate"),("and","but"),("greytious","gracious")]
for i,(wrong,right) in enumerate(ed):
    Q.append(dict(n=f"B Q{36+i}", topic="Grammar", type="Short Answer", marks=1, text=f"Editing for spelling and grammar: the underlined word '{wrong}' ({36+i}) contains an error. Write the correct word.", answer=right, passage="gratitude"))
cc = [["gather","congregate","meet"],["they","these"],["sell","offer","serve","provide"],["back"],["originated","originates"],["could"],["taste","tastes","palate","palates","preference","preferences"],["marked","marks","was","is"],["have"],["how"],["than"],["share","tell"],["over"],["sense"],["significance","value","importance","worth"]]
for i,ws in enumerate(cc):
    Q.append(dict(n=f"B Q{46+i}", topic="Comprehension (Open-Ended)", type="Short Answer", marks=1, text=f"Comprehension cloze: fill in blank ({46+i}) with a suitable word.", answer=ws[0] + ("" if len(ws)==1 else " (also accepted: " + ", ".join(ws[1:]) + ")"), accept=ws, passage="hawker"))
Q += [
 dict(n="B Q61", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence beginning with 'Mary asked me': \"Where will you be travelling to in December?\" Mary asked me.", answer="Mary asked me where I would be travelling to in December."),
 dict(n="B Q62", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence using 'prefers': Daisy would rather eat a banana cake than drink strawberry milk.", answer="Daisy prefers eating a banana cake to drinking strawberry milk."),
 dict(n="B Q63", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence beginning with 'Much to': Amy was embarrassed. She forgot the lines in the storytelling contest.", answer="Much to Amy's embarrassment, she forgot the lines in the storytelling contest.", accept=["Much to her embarrassment, Amy forgot the lines in the storytelling contest."]),
 dict(n="B Q64", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence using 'upon': When my brother won the competition, he jumped for joy.", answer="My brother jumped for joy upon winning the competition."),
 dict(n="B Q65", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence beginning with 'Little did': Ben never knew that he would top the class in the English test.", answer="Little did Ben know that he would top the class in the English test."),
 dict(n="B Q66", topic="Comprehension (Open-Ended)", type="Short Answer", marks=1, text="Why was the Space Explorers Club in \"tense silence\" in paragraph 1?", answer="The team could not agree on how to present their project.", passage="space"),
 dict(n="B Q67", topic="Comprehension (Open-Ended)", type="Short Answer", marks=1, text="Pick out a three-word phrase from paragraph 2 that tells us that the team had different opinions.", answer="found themselves divided", passage="space"),
 dict(n="B Q68", topic="Comprehension (Open-Ended)", type="Structured", marks=2, text="Based on paragraphs 4 and 5, give two actions that showed how Mr Tan tried to calm the situation.", answer="(a) He raised his hand.  (b) He asked gently (what was going on).", passage="space"),
 dict(n="B Q69", topic="Comprehension (Open-Ended)", type="Structured", marks=2, text="(a) Based on what Mia had suggested, how could the team \"get the best of both worlds\" (lines 28-29)?\n(b) From Mia's suggestion, which word best describes her for the part she played in helping the team: avoider, instigator, bystander or problem-solver?", answer="(a) She meant that the team could begin the presentation with the explanation and end it with the skit.  (b) problem-solver", passage="space"),
 dict(n="B Q70", topic="Comprehension (Open-Ended)", type="Structured", marks=3, text="What do these words from the passage refer to? (a) 'the event' (line 3)  (b) 'a creative twist' (line 9)  (c) 'their model' (line 33)", answer="(a) the Science Fair presentation / the Space Explorers Club's presentation at the Science Fair  (b) a skit for the presentation  (c) the Science Explorers' toy rocket", passage="space"),
 dict(n="B Q71", topic="Comprehension (Open-Ended)", type="Short Answer", marks=2, text="In paragraph 3, why did Arjun choose to stay silent even though he had supported the idea of the skit at first?", answer="Arjun chose to stay silent because the arguments had become intense and he did not want the group to break up.", passage="space"),
 dict(n="B Q72", topic="Comprehension (Open-Ended)", type="Structured", marks=3, text="Based on the story, state whether each statement is true or false, then give one reason.\n(a) Completing the model was a lengthy process for the team.\n(b) Calvin refused to give in even on the day of their event.\n(c) The visitors were entertained by the team's presentation.", answer="(a) True — the team (had) built their toy rocket over a few months.  (b) False — in the end, Calvin agreed to include the skit.  (c) True — they laughed.", passage="space"),
 dict(n="B Q73", skip="Tick-two question (how Siti felt): the scanned answer key shows only one ticked box ('defeated'), so the full answer can't be confirmed."),
 dict(n="B Q74", topic="Comprehension (Open-Ended)", type="Structured", marks=2, text="(a) Which changed behaviour best explains the reason behind the team's success: a willingness to give and take; a persistence in their individual beliefs; or a strong sense of confidence during the presentation?\n(b) Quote the sentence that shows how the team failed to demonstrate this changed behaviour before Mr Tan stepped in.", answer="(a) a willingness to give and take  (b) \"No one wanted to back down.\"", passage="space"),
 dict(n="B Q75", topic="Comprehension (Open-Ended)", type="Short Answer", marks=2, text="Explain clearly how conflicts should be handled according to Mr Tan.", answer="To handle conflicts, the team should synergise with one another through listening, adapting and bringing out the best in one another.", passage="space"),
]
