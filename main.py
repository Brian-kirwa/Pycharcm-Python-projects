questions=("1:Who is the president of Kenya?",
           "2:Which Church teaches the testimony of Christ?",
           "3:Who is Jesus?",
           "4:Which Language is your best",
           "5:What is your favourite food")
options=(("A.Ruto","B.Uhuru","C.Kibaki","D.Moi"),
         ("A.Catholic","B.SDA","C.Methodists","D.AIC"),
         ("A.Son of Joseph","B.Just a person","C.The sinner","D.Son of God"),
         ("A.English","B.French","C.Kiswahili","D.Kalenjin"),
         ("A.Pizza","B.Chapati","C.Rice","D.Beans"))

answers=("A","B","D","D","B")
question_no=0
score=0
guesses=[]

for question in questions:
    print("--------******-------")
    print(question)

    for option in options[question_no]:
      print(option)
    quess=input("Enter your answer: ").upper()
    if quess==answers[question_no]:
        score+=1
        print("You answered correctly")
    else:
        print("You answered incorrectly")
        print(f"The correct answer is {answers[question_no]}")
    question_no+=1
score = int((score / len(questions)) * 100)
print(f"You answered correctly in {score}% guesses")













