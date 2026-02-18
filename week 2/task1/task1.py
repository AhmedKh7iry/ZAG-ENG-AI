class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self._password = password


    def set_password(self, new_password):
        if len(new_password) >= 6:
            self._password = new_password
            print(f"Password updated for {self.name}.")
        else:
            print("Error: Password must be at least 6 characters.")

    
    def check_password(self, password_input):
        return self._password == password_input

    
    def show_info(self):
        print(f"User: {self.name} | Email: {self.email}")


class Student(User):
    def __init__(self, name, email, password, student_id):
        
        super().__init__(name, email, password)
        self.student_id = student_id

    
    def show_info(self):
        print(f"[Student] ID: {self.student_id} | Name: {self.name} | Email: {self.email}")


class Instructor(User):
    def __init__(self, name, email, password, subject):
        super().__init__(name, email, password)
        self.subject = subject

    def show_info(self):
        print(f"[Instructor] Subject: {self.subject} | Name: {self.name} | Email: {self.email}")


s = Student("Ali", "ali@email.com", "1234", "Beginner")
i = Instructor("Mona", "mona@email.com", "abcd", "Machine Learning")

print(s.show_info())
print(i.show_info())
print(s.check_password("1234"))