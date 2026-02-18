class Course:
    def __init__(self, course_id, title, teacher):
        self.course_id = course_id
        self.title = title
        self.teacher = teacher  # This expects a Teacher object

    def get_details(self):
        return f"Course: {self.title} taught by {self.teacher.name}"