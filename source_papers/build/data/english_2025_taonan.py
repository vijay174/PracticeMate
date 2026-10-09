PAPER = dict(key="2025-taonan-english-eoy", subject="English", school="Tao Nan School", year=2025, exam="EOY (SA2)",
             title="Tao Nan P5 English EOY 2025 (Paper 2)", pdf="2025/P5_English_2025_SA2_taonan.pdf")
# Passages kept as cropped page images (page, x0,y0,x1,y1) so the wording is exactly the school's.
PASSAGES = {
 "jenna": dict(img=[(19,150,150,800,600)]),
 "chocolate": dict(img=[(20,140,255,760,1135),(21,140,210,795,545)]),
 "screen": dict(img=[(26,95,215,800,1085)]),
 "editing": dict(img=[(27,95,105,800,1085)]),
 "food": dict(img=[(28,125,155,775,1135)]),
 "elina": dict(img=[(24,115,135,805,1095)]),
}
def mcq(n, topic, text, opts, ans, **kw): return dict(n=n, topic=topic, type="MCQ", marks=1, text=text, options=opts, answer=opts[ans-1], **kw)
Q = [
 mcq("A Q1","Grammar","It was the students, and not Mdm Goh, that kept the equipment by ________.",["himself","herself","ourselves","themselves"],4),
 mcq("A Q2","Grammar","The hikers made their way ________ the forest to explore the trails.",["in","over","along","through"],4),
 mcq("A Q3","Grammar","Mei Lin ________ at a wildlife rehabilitation centre since she was seven. She enjoys caring and feeding injured birds and small animals.",["volunteers","volunteered","was volunteering","has been volunteering"],4),
 mcq("A Q4","Grammar","The virus ________ rapidly before anyone realised what was happening.",["spread","has spread","had spread","is spreading"],3),
 mcq("A Q5","Grammar","The children let the puppy ________ around the garden just now.",["run","ran","runs","running"],1),
 mcq("A Q6","Grammar","Samuel, as well as his teammates, ________ watching the upcoming movie.",["is","are","was","were"],1),
 mcq("A Q7","Grammar","There is ________ evidence that this medicine is safe for consumption. More tests need to be carried out before it can be approved.",["few","little","much","several"],2),
 mcq("A Q8","Grammar","The mischievous boy broke the vase. ________, he owned up to his mistake immediately.",["Instead","Otherwise","Furthermore","Nevertheless"],4),
 mcq("A Q9","Grammar","By the end of this month, our team ________ the Science project.",["completes","is completing","will have completed","would have completed"],3),
 mcq("A Q10","Grammar","\"You'll remember to bring your student handbook, ________?\" the teacher asked.",["will you","won't you","would you","wouldn't you"],2),
 mcq("A Q11","Vocabulary","The ________ of freshly made coffee wafted from the kitchen every morning.",["scent","aroma","texture","essence"],2),
 mcq("A Q12","Vocabulary","To save the goal, the ________ goalkeeper lunged forward in one fluid motion to catch the ball.",["agile","tardy","defensive","spontaneous"],1),
 mcq("A Q13","Vocabulary","The editor spent hours checking all the articles ________ to ensure that they were flawless.",["hastily","effortlessly","thoughtfully","painstakingly"],4),
 mcq("A Q14","Vocabulary","The heavy rain flooded the field. As a result, the match had to be ________ until the next fine day.",["put off","held up","given up","called off"],1),
 mcq("A Q15","Vocabulary","Refraining from all forms of exercise for a week can help ________ the pain and swelling on Lynn's ankle.",["avoid","lighten","prevent","alleviate"],4),
 mcq("A Q16","Vocabulary","Choose the word closest in meaning to 'a futile attempt' (16) in the passage.",["risky","pointless","ineffective","challenging"],2, passage="jenna"),
 mcq("A Q17","Vocabulary","Choose the phrase closest in meaning to 'with bated breath' (17) in the passage.",["in fear","in surprise","with anxiety","with frustration"],3, passage="jenna"),
 mcq("A Q18","Vocabulary","Choose the word closest in meaning to 'put up with' (18) in the passage.",["face","handle","tolerate","manage"],3, passage="jenna"),
 mcq("A Q19","Vocabulary","Choose the word closest in meaning to 'Slowly but surely' (19) in the passage.",["Gradually","Concurrently","Subsequently","Simultaneously"],1, passage="jenna"),
 mcq("A Q20","Vocabulary","Choose the word closest in meaning to 'steeling' (20) in the passage.",["bracing","calming","preparing","steadying"],1, passage="jenna"),
 mcq("A Q21","Comprehension (MCQ)","Visual text. According to the poster in Text 1, which of the following is true of the performance?",["Bryan Wong is the director.","The story is adapted from a book.","Star Drama Club is the sole organiser.","The performance features children dreaming about chocolate."],2, passage="chocolate"),
 mcq("A Q22","Comprehension (MCQ)","\"Who can resist the temptation of chocolate?\" The picture supports this by giving the impression that the children are ________.",["attentive and lively","eager and delighted","bold and hardworking","inquisitive and hopeful"],2, passage="chocolate"),
 mcq("A Q23","Comprehension (MCQ)","\"What will they discover?\" Why did the writer ask the question in Text 1?",["to give people a preview of the show","to entice children to purchase the novel","to draw people to watch the performance","to encourage children to join the drama club"],3, passage="chocolate"),
 mcq("A Q24","Comprehension (MCQ)","Based on the poster in Text 1, which of the following best describes the performance you expect to watch?",["Opera","Musical","Comedy","Orchestra"],2, passage="chocolate"),
 mcq("A Q25","Comprehension (MCQ)","We cannot trust the way Text 1 portrays chocolate because Text 2 states that ________.",["chocolate has widespread popularity","not all children enjoy eating chocolate","eating dark chocolate is good for health","chocolate is not readily available everywhere"],2, passage="chocolate"),
]
gc = [("P","whether"),("F","has"),("Q","while"),("G","may"),("D","even"),("L","these"),("C","by"),("A","between"),("B","but"),("K","their")]
for i,(letter,w) in enumerate(gc):
    Q.append(dict(n=f"B Q{26+i}", topic="Grammar", type="Short Answer", marks=1, text=f"Grammar cloze: which word from the list best fits blank ({26+i})? Type the word (not the letter).", answer=w, solution=f"({letter}) {w}", passage="screen"))
ed = [("proud","proudest"),("remember","remembering"),("konsistantly","consistently"),("preparing","preparation"),("enthuszestikally","enthusiastically"),("applaud","applause"),("anounzed","announced"),("achiernent","achievement"),("unbeliveable","unbelievable"),("showing","shown")]
for i,(wrong,right) in enumerate(ed):
    Q.append(dict(n=f"B Q{36+i}", topic="Grammar", type="Short Answer", marks=1, text=f"Editing for spelling and grammar: the underlined word at ({36+i}) contains an error. Write the correct word.", answer=right, passage="editing"))
cc = ["amount","serve","found","severe","bulk","contributor","wasted","resolve","example","increased","sign","smaller","expiry","participating","helped"]
for i,w in enumerate(cc):
    Q.append(dict(n=f"B Q{46+i}", topic="Comprehension (Open-Ended)", type="Short Answer", marks=1, text=f"Comprehension cloze: fill in blank ({46+i}) with a suitable word.", answer=w, passage="food"))
Q += [
 dict(n="B Q61", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence using 'enough': The wind was powerful. Many trees were uprooted.", answer="The wind was powerful enough to uproot many trees."),
 dict(n="B Q62", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence beginning with 'Peter asked': Peter asked his sister, \"Where did you go?\"", answer="Peter asked his sister where she had gone."),
 dict(n="B Q63", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence beginning with 'The last cupcake': Sanjay ate the last cupcake and doughnut in the box.", answer="The last cupcake and doughnut in the box were eaten by Sanjay."),
 dict(n="B Q64", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence using 'neither': Ranjit did not play the guitar. Ranjit also did not play the drum.", answer="Ranjit played neither the guitar nor the drum."),
 dict(n="B Q65", topic="Synthesis & Transformation", type="Short Answer", marks=2, text="Rewrite in one sentence beginning with 'It was': I chose to volunteer at the elder care centre.", answer="It was my choice to volunteer at the elder care centre."),
 dict(n="B Q66", topic="Comprehension (Open-Ended)", type="Short Answer", marks=1, text="Which word in paragraph one has the same meaning as 'dismal'?", answer="dreary", passage="elina"),
 dict(n="B Q67", topic="Comprehension (Open-Ended)", type="Structured", marks=2, text="Which two actions by Elina calmed the kitten down before she took it home?", answer="(a) She gently wrapped the kitten in her jacket.  (b) She cradled the kitten in her arms.", passage="elina"),
 dict(n="B Q68", topic="Comprehension (Open-Ended)", type="Short Answer", marks=2, text="Why was Elina unsuccessful in getting a pet?", answer="She was always turned down by her parents as they thought that taking care of a pet was a great responsibility and Elina was always busy with schoolwork.", passage="elina"),
 dict(n="B Q69", topic="Comprehension (Open-Ended)", type="Structured", marks=2, text="Based on lines 13-23, state whether each statement is true or false, then give one reason.\n(a) Elina's parents were unconcerned about her well-being after she got home.\n(b) Initially, Elina did not want her parents to find the kitten's owner.", answer="(a) False. When Elina got home, her parents looked worried to see their girl drenched.  (b) True. When her parents said that she could only keep the kitten for a few days, she wanted to rebut.", passage="elina"),
 dict(n="B Q70", topic="Comprehension (Open-Ended)", type="Short Answer", marks=2, text="Referring to lines 6-7, why did Elina say \"... I know exactly how it feels to be alone and vulnerable\"?", answer="Elina had no siblings, so she was lonely. She sometimes wished that she had one to share her secrets and worries with, instead of only the quiet companionship of her parents.", passage="elina"),
 dict(n="B Q71", topic="Comprehension (Open-Ended)", type="Structured", marks=4, text="From lines 31-42, pick out two separate phrases to show the characters' feelings and explain why they felt that way.\n(a) Two-word phrase which shows that Elina was in a dilemma.\n(b) Reason for Elina's feeling.\n(c) Three-word phrase which shows that the boy was relieved.\n(d) Reason for the boy's feeling.", answer="(a) deliberated intensely  (b) Elina had a hard time deciding whether to keep Snowy or return it to its rightful owners.  (c) exclaimed in glee  (d) He had found his kitten after it went missing.", passage="elina"),
 dict(n="B Q72", topic="Comprehension (Open-Ended)", type="Structured", marks=2, text="What do these words from the passage refer to? (a) 'doubt' (line 14)  (b) 'something' (line 28)", answer="(a) Whether her parents would be angry and refuse to let the kitten stay.  (b) The 'Missing kitten – white with a small brown patch on its tail. Answers to the name Luna.' notice put up by the owner, with a contact number.", passage="elina"),
 dict(n="B Q73", topic="Comprehension (Open-Ended)", type="Short Answer", marks=1, text="Write 1, 2 and 3 to show the order in which the events occurred in the story, in the order the statements are listed:\n• Elina was a proud pet owner.\n• Elina saw the 'Missing Kitten' poster.\n• Elina forged a bond with the kitten.\n(Answer like: 2, 1, 3)", answer="3, 2, 1", passage="elina"),
 dict(n="B Q74", topic="Comprehension (Open-Ended)", type="Short Answer", marks=2, text="Do you think the boy was a responsible pet owner? Support your answer with a reason from the text.", answer="Yes. The boy put up 'Missing Kitten' posters to find his kitten.", passage="elina"),
 dict(n="B Q75", topic="Comprehension (Open-Ended)", type="Short Answer", marks=2, text="Referring to line 44, \"... you're ready for a little responsibility of your own\", what was Elina ready for? Support your answer with a piece of evidence from the text.", answer="She knew how to prioritise her time: she fed Snowy and cleaned its bedding before going to school.", solution="This is the school key's answer, word for word; it gives the evidence only (she was ready to own and care for a pet — see the last paragraph).", passage="elina"),
]
