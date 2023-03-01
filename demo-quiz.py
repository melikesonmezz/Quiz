class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self,answer):
       return self.answer == answer
    


class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'Soru{self.questionIndex+1}:{question.text}')


        for q in question.choices:#şıkları gösterir
            print('-'+ q)

        answer=input("cevap:")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
          self.score+=1
         
        self.questionIndex+=1
        
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
         self.showScore()
        else:
         self.displayProgress()
         self.displayQuestion()

    def showScore(self):
       print("Score:",self.score)
            
       
    def displayProgress(self):
       totalQuestion=len(self.questions)
       questionNumber=self.questionIndex+1

       if questionNumber>totalQuestion:
          print("Quiz bitti")

       else:
          print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))

q1=Question("en iyi programlama dili hangisidir",["C#,python,c++"],"python")
q2=Question("en popüler programlama dili hangisidir",["C#,python,c++"],"python")
q3=Question("en çok kazandıran programlama dili hangisidir",["C#,python,c++"],"python")
questions=[q1,q2,q3]

# print(q1.checkQuestion("pyhton"))
# print(q1.checkQuestion("java"))
quiz=Quiz(questions) #Question sınıfına question dizisini parametre olarak gönderiyoruz
#question=quiz.questions[quiz.questionsIndex]#quiz objesi ile init içindeki inex nosuna ulştık

quiz.loadQuestion()