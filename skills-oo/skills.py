class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init___(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = raw_input(self.question)
        if answer == self.correct_answer:
            print True
        else:
            print False


class Exam(object):

    def __init__(self, name, questions=[]):
        self.name = name
        self.question = questions

    def add_question(self, question, correct_answer):
        question = Question(question, correct_answer)
        questions.append(question)   

    def administer(self):
        # for question in Exam
        # ask_and_evaluate
        return score