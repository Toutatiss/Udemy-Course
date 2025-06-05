class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        
    def next_question(self):
        # Retrieve next question
        current_question = self.question_list[self.question_number]
        # Increment question number
        self.question_number += 1
        # Show question and ask for user input
        self.user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False?): ")
        