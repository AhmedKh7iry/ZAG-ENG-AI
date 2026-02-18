class Teacher:
    def __init__(self, teacher_id, name, specialty):
        self.teacher_id = teacher_id
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"Teacher: {self.name} | Specialty: {self.specialty}"