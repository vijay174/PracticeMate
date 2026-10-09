PAPER = dict(key="2023-raffles-english-eoy", subject="English", school="Raffles Girls' Primary School", year=2023, exam="EOY (SA2)",
             title="Raffles Girls' P5 English EOY 2023 (Paper 2)", pdf="2023/P5_English_2023_SA2_Raffles.pdf")
PASSAGES = {
 "vocab": dict(img=[(9,120,170,810,560)]),
 "flyer": dict(img=[(10,120,228,800,1150),(11,120,170,800,1150)]),
 "animals": dict(img=[(16,100,190,820,1090)]),
 "ozone": dict(img=[(17,110,140,830,1075)]),
 "brain": dict(img=[(18,110,130,800,1045)]),
 "billy": dict(img=[(14,120,170,800,1085)]),
}
def mcq(n, topic, text, opts, ans, **kw): return dict(n=n, topic=topic, type="MCQ", marks=1, text=text, options=opts, answer=opts[ans-1], **kw)
Q = [
 mcq("A Q1","Grammar","Mr Johnson saw Melvin ________ an injured boy cross the road two days ago.",["help","helps","helped","had helped"],1),
 mcq("A Q2","Grammar","My sisters and I ________ this trip to Japan to visit our grandparents since last month.",["plan","planned","has been planning","have been planning"],4),
 mcq("A Q3","Grammar","I had much respect ________ Jana because he was a strong competitor who showed good sportsmanship.",["of","for","over","around"],2),
 mcq("A Q4","Grammar","Either Ali or his sisters ________ decorating the house. They will be hosting a party later.",["is","are","has","have"],2),
 mcq("A Q5","Grammar","All the girls went to the park, ________ they?",["do","did","don't","didn't"],4),
 mcq("A Q6","Grammar","\"You are ________ my way. Please move aside so that we can get past!\" Mary exclaimed at the man standing in the hallway.",["in","at","on","with"],1),
 mcq("A Q7","Grammar","Mrs Tan, as well as her pupils, ________ performing a dance at the upcoming graduation concert.",["is","are","was","were"],1),
 mcq("A Q8","Grammar","________ the wedding ceremony is about to start, most of the guests have not arrived yet.",["As","Since","Despite","Although"],4),
 mcq("A Q9","Grammar","Do you know that the lady ________ you spoke to at the lobby is the principal of the school?",["which","whom","where","whose"],2),
 mcq("A Q10","Grammar","Li Li and Sheela invited ________ friend, Andrew, to join them at the library.",["his","her","their","them"],3),
 mcq("A Q11","Vocabulary","John and Weiming are no longer arguing as they have decided to ________ and become friends again.",["buy some time","face the music","bury the hatchet","read between the lines"],3),
 mcq("A Q12","Vocabulary","As Lina was busy with work, she had to ________ the time she spent on her hobbies.",["cut in","cut up","cut back","cut away"],3),
 mcq("A Q13","Vocabulary","Harmful ultra-violet rays from the sun can easily damage the baby's ________ skin.",["weary","dainty","feeble","delicate"],4),
 mcq("A Q14","Vocabulary","The school has ________ plans to build a new library near the courtyard.",["unveiled","untangled","unearthed","uncombed"],1),
 mcq("A Q15","Vocabulary","I ________ remember that Hannah was not in school last week but I am not certain.",["vaguely","formally","distinctly","raucously"],1),
 mcq("A Q16","Vocabulary","Vocabulary cloze: choose the word closest in meaning to 'with ease' (16) in the passage.",["entirely","effortlessly","abundantly","appropriately"],2, passage="vocab"),
 mcq("A Q17","Vocabulary","Choose the word closest in meaning to 'naivety' (17) in the passage.",["wisdom","innocence","experience","sophistication"],2, passage="vocab"),
 mcq("A Q18","Vocabulary","Choose the word closest in meaning to 'incredible' (18) in the passage.",["hysterical","exhilarating","superfluous","unbelievable"],4, passage="vocab"),
 mcq("A Q19","Vocabulary","Choose the word closest in meaning to 'a second thought' (19) in the passage.",["resolution","discussion","speculation","consideration"],4, passage="vocab"),
 mcq("A Q20","Vocabulary","Choose the word closest in meaning to 'pleasure' (20) in the passage.",["joy","wonder","distress","contempt"],1, passage="vocab"),
 mcq("A Q21","Comprehension (MCQ)","Visual text. In most countries, calligraphy was first used ________.",["to write religious texts","to create event invitations","as a form of decorative art","as a means of self-expression"],1, passage="flyer"),
 mcq("A Q22","Comprehension (MCQ)","Which of the following statements is NOT true about the classes?",["All classes will be held at the same venue.","Classes are only held during the Singapore Art Month.","Participants can choose to learn any type of calligraphy.","Participants must have prior experience before attending the class."],4, passage="flyer"),
 mcq("A Q23","Comprehension (MCQ)","Jason wants to sign up for a calligraphy class. He should ________.",["email the person in-charge","make a call to Jasmine Lee","visit the Westwood Community Club website","go personally to the Singapore Arts Association"],1, passage="flyer"),
 mcq("A Q24","Comprehension (MCQ)","The paper needed for calligraphy ________.",["is given to participants","is part of the beginner's calligraphy set","must be pre-ordered from the organiser","must be prepared by the participants before the class"],1, passage="flyer"),
 mcq("A Q25","Comprehension (MCQ)","Zikri has signed up for the Chinese Calligraphy class. He will get a free ________.",["sketch pen","practice booklet","calligraphy brush","bottle of black ink"],2, passage="flyer"),
 mcq("A Q26","Comprehension (MCQ)","According to the flyer, Anika said she \"was mistaken\". She meant it was wrong of her to think that ________.",["she would pick up calligraphy in a short time","she had to follow instructions given by her instructor","she could practise and produce calligraphy while at home","she needed to have beautiful handwriting to learn calligraphy"],4, passage="flyer"),
 mcq("A Q27","Comprehension (MCQ)","According to Alex Ang, Chinese calligraphy ________.",["is meant to be enjoyed privately","enables him to exercise his mind","can be mastered during the course","helps to keep him calm and relaxed"],4, passage="flyer"),
 mcq("A Q28","Comprehension (MCQ)","What is the main purpose of the calligraphy classes?",["to teach the art of calligraphy writing","to introduce the history of calligraphy","to appreciate the beauty of calligraphy","to showcase the different types of calligraphy"],1, passage="flyer"),
]
gc = [("P","while"),("F","from"),("N","to"),("J","these"),("H","them"),("E","for"),("A","a"),("C","at"),("Q","with"),("L","this")]
for i,(letter,w) in enumerate(gc):
    Q.append(dict(n=f"B Q{29+i}", topic="Grammar", type="Short Answer", marks=1, text=f"Grammar cloze: which word from the list best fits blank ({29+i})? Type the word (not the letter).", answer=w, solution=f"({letter}) {w}", passage="animals"))
ed = [("recovery","recovering"),("destroy","destroys"),("pollutents","pollutants"),("from","between"),("sheilds","shields"),("environment","environmental"),("efacts","effects"),("consentration","concentration"),("has","have"),("achieve","achieved"),("continueous","continuous"),("occurences","occurrences")]
for i,(wrong,right) in enumerate(ed):
    Q.append(dict(n=f"B Q{39+i}", topic="Grammar", type="Short Answer", marks=1, text=f"Editing for spelling and grammar: the underlined word '{wrong}' ({39+i}) contains an error. Write the correct word.", answer=right, passage="ozone"))
cc = ["like","more","that","blocks","enters","cells","result","future","task","little","when","mistakes","to","not","Even"]
for i,w in enumerate(cc):
    Q.append(dict(n=f"B Q{51+i}", topic="Comprehension (Open-Ended)", type="Short Answer", marks=1, text=f"Comprehension cloze: fill in blank ({51+i}) with a suitable word.", answer=w, passage="brain"))
Q += [
 dict(n="B Q66", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence using 'prefers': Trina would rather swim than cycle.", answer="Trina prefers swimming to cycling."),
 dict(n="B Q67", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence beginning with 'The fact that he': I was upset because he was unkind to his classmates.", answer="The fact that he was unkind to his classmates made me upset."),
 dict(n="B Q68", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence using 'unless': Keep your room tidy. Then you can find what you need.", answer="You cannot find what you need unless you keep your room tidy."),
 dict(n="B Q69", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence beginning with 'Siti asked her grandfather': Siti asked her grandfather, \"Did you grow these orchids?\"", answer="Siti asked her grandfather if he had grown those orchids."),
 dict(n="B Q70", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence using 'because of his': Ravi was a proud boy. He refused to ask anyone for help.", answer="Ravi refused to ask anyone for help because of his pride."),
 dict(n="B Q71", topic="Comprehension (Open-Ended)", type="Short Answer", marks=1, text="From paragraph 1, how did Billy show that he thought highly of the people working at the Head Office?", answer="He wanted to be like the people at the Head Office and do everything briskly.", passage="billy"),
 dict(n="B Q72", topic="Comprehension (Open-Ended)", type="Structured", marks=3, text="Based on lines 1-13, state whether each statement is true or false, then give one reason.\n(a) Billy had dressed well that day.\n(b) There was a line of shops on the wide street that Billy was walking along.\n(c) There were no street lamps anywhere.", answer="(a) True — Billy wore a fine navy-blue coat, a new brown hat and a tailored brown suit, feeling good.  (b) False — on the wide street, only a line of tall houses stood on each side, all of them identical.  (c) False — a window was brilliantly illuminated by a street lamp a few metres away.", passage="billy"),
 dict(n="B Q73", topic="Comprehension (Open-Ended)", type="Structured", marks=2, text="Using information from paragraph 2, complete the table about the way the houses lining the street looked.\n(a) THEN: ________  |  NOW: The paint was peeling from the wood on the doors and windows of the houses.\n(b) THEN: The houses had handsome white facades.  |  NOW: ________", answer="(a) The houses had been very luxurious houses.  (b) The handsome white facades were now blotchy from neglect.", passage="billy"),
 dict(n="B Q74", topic="Comprehension (Open-Ended)", type="Short Answer", marks=1, text="What had immediately caught Billy's attention when he 'peered through the glass' (line 16) and looked into the room with the sign that said BED AND BREAKFAST?", answer="A bright fire burning in the fireplace.", passage="billy"),
 dict(n="B Q75", topic="Comprehension (Open-Ended)", type="Short Answer", marks=2, text="Describe fully how, in paragraph 5, the room in the house had been furnished to appear comfortable and pleasant.", answer="The room was filled with cosy furniture. There was a big sofa and several plush-looking armchairs.", passage="billy"),
 dict(n="B Q76", topic="Comprehension (Open-Ended)", type="Structured", marks=3, text="The writer used sensory details to show how Billy was 'a little wary' (line 20) of boarding houses. Using paragraph 5, complete the table.\n(a) Taste — phrase: ________ — represents: the boarding houses served bad food.\n(b) Hearing — phrase: ________ — represents: the house guests were annoying.\n(c) Smell — phrase: 'musty smell of old socks in the living room' — represents: ________", answer="(a) bland-tasting cabbage soup  (b) noisy house guests  (c) The living room smelled bad.", passage="billy"),
 dict(n="B Q77", topic="Comprehension (Open-Ended)", type="Structured", marks=2, text="Fill in the blanks: what Billy did as a result.\n(a) Billy felt undecided because he had to have a place to stay for the night but he was wary of boarding houses. EFFECT: ________\n(b) Billy felt mesmerised because each word on the notice seemed to be forcing him to stay where he was and not walk away from that house. EFFECT: ________", answer="(a) Billy decided that he would walk on and take a look at other boarding houses before deciding on which one to stay for the night.  (b) Billy was moving across from the window to the front door of the house, climbing the steps to the front door, and reaching for the bell.", passage="billy"),
 dict(n="B Q78", topic="Comprehension (Open-Ended)", type="Structured", marks=3, text="What do these words from the passage refer to? (a) 'they' (line 4)  (b) 'them' (line 15)  (c) 'it' (line 31)", answer="(a) the people at the Head Office  (b) the green velvety curtains  (c) the front door of the house", passage="billy"),
 dict(n="B Q79", topic="Comprehension (Open-Ended)", type="Short Answer", marks=1, text="Write 1, 2 and 3 to show the order in which the events occurred, in the order the statements are listed:\n• A strange thing happened to Billy.\n• Billy went to the front door of the house.\n• Billy looked into the room with the green curtains.\n(Answer like: 2, 1, 3)", answer="2, 3, 1", passage="billy"),
 dict(n="B Q80", topic="Comprehension (Open-Ended)", type="Short Answer", marks=2, text="Which two of the following words best describe Billy? tolerant, eager, responsible, caring, observant, generous", answer="eager, observant", accept=["eager and observant","observant, eager","observant and eager"], passage="billy"),
]
