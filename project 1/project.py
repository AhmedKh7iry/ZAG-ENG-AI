import os

def get_valid_input(prompt, data_type, min_val=None, max_val=None):

    while True:
        try:
            user_input = data_type(input(prompt))
            if min_val is not None and user_input < min_val:
                print(f"Error: Value must be at least {min_val}.")
                continue
            if max_val is not None and user_input > max_val:
                print(f"Error: Value must be at most {max_val}.")
                continue
            return user_input
        except ValueError:
            print(f"Error: Invalid input. Please enter a valid {data_type.__name__}.")

def get_student_details():
    
    name = input("\nEnter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return None, None, None

    age = get_valid_input("Enter age: ", int, min_val=1)
    
    scores = []
    print("Enter 3 exam scores:")
    for i in range(1, 4):
        score = get_valid_input(f"  Subject {i} Score (0-100): ", float, min_val=0, max_val=100)
        scores.append(score)
        
    return name, age, scores


def calculate_averages(student_data):
    
    averages = {}
    for name, (age, scores) in student_data.items():
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)
    return averages

def find_top_students(averages, threshold):
    
    return {name for name, avg in averages.items() if avg >= threshold}


def save_data(filename, student_data):
    try:
        with open(filename, "w") as f:
            for name, (age, scores) in student_data.items():
                scores_str = ",".join(map(str, scores))
                f.write(f"{name}|{age}|{scores_str}\n")
        print(f"Success: Data saved to '{filename}'.")
    except IOError as e:
        print(f"File Error: Could not write to file. {e}")

def load_data(filename):
    data = {}
    if not os.path.exists(filename):
        print(f"Note: File '{filename}' does not exist yet.")
        return data

    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    name = parts[0]
                    age = int(parts[1])
                    scores = [float(s) for s in parts[2].split(",")]
                    data[name] = (age, scores)
        print(f"Success: Loaded {len(data)} students from '{filename}'.")
    except (IOError, ValueError) as e:
        print(f"File Error: Corrupt data or read error. {e}")
    return data


def main():
    
    filename = "students.txt"
    students = {} 

    print("--- STUDENT MANAGEMENT SYSTEM ---")
    
    while True:
        print("\n1. Load Data | 2. Add Student | 3. Show Averages | 4. Save & Exit")
        choice = input("Select option: ")

        if choice == '1':
            students = load_data(filename)

        elif choice == '2':
            name, age, scores = get_student_details()
            if name:
                students[name] = (age, scores)
                print(f"Student '{name}' added.")

        elif choice == '3':
            if not students:
                print("No students found.")
                continue
            
            avg_data = calculate_averages(students)
            print("\n--- Class Results ---")
            for name, avg in avg_data.items():
                print(f"{name}: {avg}")

            try:
                cutoff = float(input("\nEnter threshold to see top students: "))
                top_students = find_top_students(avg_data, cutoff)
                
                if top_students:
                    print(f"Students with average >= {cutoff}: {', '.join(top_students)}")
                else:
                    print("No students met the criteria.")
            except ValueError:
                print("Invalid number entered for threshold.")

        elif choice == '4':
            if students:
                save_data(filename, students)
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()