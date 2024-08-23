    
def newgame():
    correctguesses=0
    guesses=[]
    question_no=1
    for key in questions:
        print(key)
        print("--------------------------------------")
        
        for i in options[question_no-1]:
            print(i)
        guess=input("Enter (A,B,C or D):").upper()
        guesses.append(guess)
        
        correctguesses+=check_answer(questions.get(key),guess)
        question_no+=1
    displayscore(guesses,correctguesses)
    

def check_answer(answer,guess):
    if answer==guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0



def displayscore(guesses,correctguesses):

    print()
    print("-----RESULT------")
    print("Answers:",end=" ")
    for i in questions:
        print(questions.get(i),end="  ")
    print()
    print("guesses:",end=" ")
    for i in guesses:
        print(i,end="  ")
    print()
    score=int((correctguesses/len(questions))*100)
    print("you score is "+str(score)+"%")

def playagain():
    result=input("Do you want to play again(y/n)").lower()
    if result=='y':
        return True
    else:
        return False

#dictionary
questions={
    "who created python?:":"A",
    "what year was python created?":"B",
    "who is the world riches man?":"C",
    "is earth round?:":"A"
}

#2d list      
options=[["A.Guido van ","B.Elon mask","C.Rober mugabe","D.van devure"],["A.1889","B.1991","2000",'D.2016'],["A.Elon mask","B.Alamudin","C.mark zukemberg","D.Antonio joshua"],["A.True","B.False","C.sometimes","D.what's Earth!"]]


newgame()

while playagain():
    newgame()
    
print("Good Bye!")


