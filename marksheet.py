class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def calcutate_score(self, subject, score):
        self.scores[subject] = score

    def calculate_average(self):
    
        return sum(self.scores.values()) / len(self.scores)

    def IsPass(self):
        average = self.calculate_average()
        if average >= 60:
            return "Pass"
        else:
            return "Fail"
        
    def display(self):
        print(f"Student Name : {self.name}")
        print("Subject Scores")
        for subject,score in self.scores.items():
            print(f"{subject}: {score}")
        print(f"Average Score: {self.calculate_average():.2f}")
        print(f"Grade: {self.IsPass()}")

name = input("Enter student name: ")
student = Student(name)

num_subjects = int(input("Enter number of subjects: "))

for _ in range(num_subjects):
    subject = input("Enter subject name: ")
    score = float(input(f"Enter score of {subject}: "))
    student.calcutate_score(subject, score)

print("\nStudent Report:")
student.display()