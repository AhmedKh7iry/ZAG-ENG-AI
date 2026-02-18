# Importing classes from our package
from school_system.students.student_model import Student
from school_system.teachers.teacher_model import Teacher
from school_system.courses.course_model import Course

def main():
    # 1. Create a Teacher
    t1 = Teacher(teacher_id=1, name="Prof. Snape", specialty="Potions")
    
    # 2. Create a Course (assigning the Teacher object 't1' to it)
    c1 = Course(course_id=101, title="Advanced Potions", teacher=t1)
    
    # 3. Create a Student (initially with no courses)
    s1 = Student(student_id=500, name="Harry Potter")

    # 4. Demonstrate Relationships
    print("--- System Setup ---")
    print(t1)
    print(s1)
    
    print("\n--- Enrollment ---")
    s1.enroll(c1)  # Add course object to student's list

    print("\n--- Verifying Data ---")
    # Check the first course in the student's list
    enrolled_course = s1.courses[0] 
    
    print(f"Student: {s1.name}")
    print(f"Enrolled In: {enrolled_course.title}")
    print(f"Instructor: {enrolled_course.teacher.name}")  # Accessing Teacher via Course

if __name__ == "__main__":
    main()