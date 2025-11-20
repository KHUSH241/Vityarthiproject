def calculate_status(subject_name, attended, total):
    if total == 0:
        print("Error: Total classes cannot be zero.")
        return

    current_percentage = (attended / total) * 100
    print(f"\n--- Analysis for {subject_name} ---")
    print(f"Current Attendance: {current_percentage:.2f}%")

    required_criteria = 75.0

    if current_percentage >= required_criteria:
        bunks_possible = 0
        temp_total = total
        while True:
            temp_total += 1 
            new_percent = (attended / temp_total) * 100
            
            if new_percent < required_criteria:
                break
            else:
                bunks_possible += 1
        
        if bunks_possible > 0:
            print(f"✅ Good News! You can safely skip the next {bunks_possible} classes.")
        else:
            print("✅ You are safe, but you cannot skip any upcoming classes right now.")

    else:
        classes_needed = 0
        temp_attended = attended
        temp_total = total
        
        while True:
            new_percent = (temp_attended / temp_total) * 100
            
            if new_percent >= required_criteria:
                break
            temp_attended += 1
            temp_total += 1
            classes_needed += 1
            
        print(f"⚠️ ALERT! You need to attend the next {classes_needed} classes consecutively to recover.")

def main():
    print("========================================")
    print("    COLLEGE ATTENDANCE MANAGER 1.0      ")
    print("========================================")
    my_subjects = {}

    while True:
        print("\nMAIN MENU:")
        print("1. Add a Subject & Check Status")
        print("2. View Summary of All Subjects")
        print("3. Exit")
        
        user_choice = input("Enter your choice (1-3): ")

        if user_choice == '1':
            try:
                sub = input("Enter Subject Name (e.g., Python): ")
                held = int(input("Total Classes Held: "))
                present = int(input("Classes Attended: "))

                if present > held:
                    print("❌ Error: You can't attend more classes than held!")
                else:
                    my_subjects[sub] = {'held': held, 'present': present}
                    calculate_status(sub, present, held)

            except ValueError:
                print("❌ Please enter valid numbers only.")

        elif user_choice == '2':
            if len(my_subjects) == 0:
                print("No subjects added yet.")
            else:
                print("\nYOUR ATTENDANCE SUMMARY:")
                print(f"{'Subject':<15} | {'Attended':<10} | {'Total':<10} | {'%':<5}")
                print("-" * 50)
                
                for name, data in my_subjects.items():
                    p = data['present']
                    t = data['held']
                    perc = (p / t) * 100
                    print(f"{name:<15} | {p:<10} | {t:<10} | {perc:.1f}%")
                print("-" * 50)

        elif user_choice == '3':
            print("Exiting program. Maintain your attendance! 👋")
            break
        
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
