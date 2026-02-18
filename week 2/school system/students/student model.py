class Student:
    def __init__(self, student_id, name, courses=None):
        self.student_id = student_id
        self.name = name
        # If no list is provided, start with an empty list
        self.courses = courses if courses is not None else []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course.title}")

    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id})"