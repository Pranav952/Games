class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}:{current_question.text}(True/False)")
        if ans.capitalize() == "True" or ans.capitalize() == "False":
            if ans.capitalize() == current_question.answer:
                print(f"you are right,you guessed {self.question_number} / {self.question_number}")
                self.next_question()
            else:
                print(f"Wrong answer,Your answer was {current_question.answer}")
                print(f"you guessed {self.question_number - 1} / {self.question_number}")
                option = input("Do you want to continue?")
                if option.lower() == 'yes':
                    self.next_question()
                else:
                    print("Thank,You for playing the game")
        else:
            print("invalid choice chose either true or false")
            self.question_number -= 1
            self.next_question()
