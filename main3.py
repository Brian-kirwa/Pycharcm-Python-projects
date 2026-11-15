
class Quiz:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts=["\n1.What is the colour of banana?\n(A).Red\n(B).Blue\n(C).Yellow\n",
               "\n2.Which animal lays the largest egg?\n(A).Ostrich\n(B).Whale\n(C).Lion \n",
               "\n3.What is the capital city of Kenya?\n(A).Nakuru\n(B).Nairobi\n(C).Kisumu\n"]

question=[
    Quiz(prompt=question_prompts[0],answer="C"),
    Quiz(question_prompts[1],"A"),
    Quiz(question_prompts[2],"B")
]

def run_tests(quiz):
    score = 0
    for i in quiz:
        answer=input(i.prompt).lower()
        if answer==i.answer:
            score+=1
    #print(f"You got {score} out of {len(quiz)} correct!")

run_tests(question)



