from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda sum_of_credits, attempt: sum_of_credits + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    filtered = filter(lambda attempt: attempt.grade >= 1, attempts)
    return reduce(lambda sum_of_credits, attempt: sum_of_credits + attempt.credits, filtered, 0)

def average(attempts: list):
    filtered = list(filter(lambda attempt: attempt.grade >= 1, attempts))
    num_attempts = len(filtered)
    return reduce(lambda sum_of_grades, attempt: sum_of_grades + attempt.grade, filtered, 0)/num_attempts

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)
