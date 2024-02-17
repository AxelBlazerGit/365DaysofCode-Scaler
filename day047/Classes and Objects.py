class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
    
    def printfunction(self):
        print(self.name + " " + self.branch)

def main():
    # Create instances of the Student class
    stud1 = Student("Robin", "CSE")
    stud2 = Student("Rahul", "ECE")

    # Call the printfunction method for each student
    stud1.printfunction()
    stud2.printfunction()

    return 0

if __name__ == '__main__':
    main()
