from question import Question
question_prompts=["what are the colors of bananas? : \n a)red \n (b) black \n (c) yellow \n (d) white \n\n",
"what are the colors of tomatoes? : \n a)red \n (b) black \n (c) yellow \n (d) white \n\n",
"what are the colors of oranges? : \n a)red \n (b) black \n (c) yellow \n (d) white \n\n"]

question=[Question(question_prompts[0],"c"),
Question(question_prompts[1],"a"),
Question(question_prompts[2],"c")]
def run (questions):
    score=0
    answer=input(question.prompt())
    for x in question_prompts:
        
        if answer==question.answer():
            score+=1
    
    print(score)
    run(questions)
    print("you got ",str(score),"/",str(len(question),"correct")) 