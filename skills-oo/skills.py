class Student(object):
    """Creates a Student object with first_name, last_name and address"""
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Creates Question object with an ask_and_evaluate method"""
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = raw_input(self.question)
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """Creates Exam object with a name and a list of questions"""
    def __init__(self, name, questions=[]):
        self.name = name
        self.questions = questions

    def add_question(self, question, correct_answer):
        # create instance of Question class
        new_question = Question(question, correct_answer)
        # append the new question to the questions list
        self.questions.append(new_question)

    def administer(self):
        # keep track of score
        score = 0
        # iterate through question in questions list
        for question in self.questions:
            # provide the question to the student and see if response is correct
            if question.ask_and_evaluate():
                # answer is right, increment score
                score += 1.0

        return score


class Quiz(Exam):
    """Creates Quiz class, subclass of Exam. Overrides Exam's administer method"""
    def administer(self):
        # starting, the student hasn't passed the test yet
        passed = False
        # highest score possible is the number of test questions
        max_score = len(self.questions)
        # administer the quiz to get the score
        score = Exam.administer(self)
        # passing is 50% or higher
        if score / max_score >= 0.5:
            passed = True

        return passed


def take_test(exam, student):
    """Takes an exam and a student, binds student score to the return of exam's administer method"""
    # administer the exam to the student
    # assign score to student as new attribute score
    student.score = exam.administer()


def example():
    """Test case for our classes."""
    # create exam
    # add a few questions to exam
    new_exam = Exam("skills assessment")
    new_exam.add_question("Which cat is derpy? ", "Turtle")
    new_exam.add_question("Which cat is talkative? ", "Mini")
    new_exam.add_question("Who do we love more? ", "We love them both!")
    # creates student
    katie = Student('Katie', 'Simmons', '419 Thornton')
    # administers test to that student
    take_test(new_exam, katie)
    print katie.score

example()
