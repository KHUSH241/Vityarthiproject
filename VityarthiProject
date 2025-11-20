import tkinter as tk
from tkinter import messagebox

def calculate_strategy():
    try:
        sub_name = entry_subject.get()
        total_str = entry_total.get()
        attended_str = entry_attended.get()

        if not sub_name or not total_str or not attended_str:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        total = int(total_str)
        attended = int(attended_str)

        if attended > total:
            messagebox.showerror("Logic Error", "Attended classes cannot be more than Total classes!")
            return

        if total == 0:
            messagebox.showerror("Logic Error", "Total classes cannot be zero.")
            return

        current_percent = (attended / total) * 100
        result_text = f"Subject: {sub_name}\n"
        result_text += f"Current Attendance: {current_percent:.2f}%\n\n"
        
        required_criteria = 75.0

        if current_percent >= required_criteria:
            bunks_possible = 0
            temp_total = total
            while True:
                temp_total += 1
                new_percent = (attended / temp_total) * 100
                if new_percent < required_criteria:
                    break
                bunks_possible += 1
            
            if bunks_possible > 0:
                result_text += f"✅ SAFE: You can bunk the next {bunks_possible} classes."
                lbl_result.config(fg="green")
            else:
                result_text += "✅ ON THE EDGE: You are safe, but cannot bunk right now."
                lbl_result.config(fg="orange")

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
            
            result_text += f"⚠️ DANGER: You must attend the next {classes_needed} classes."
            lbl_result.config(fg="red") 

        lbl_result.config(text=result_text)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for classes.")

def clear_fields():
    """Clears all input boxes"""
    entry_subject.delete(0, tk.END)
    entry_total.delete(0, tk.END)
    entry_attended.delete(0, tk.END)
    lbl_result.config(text="Result will appear here...")


root = tk.Tk()
root.title("College Attendance Manager")
root.geometry("400x500") 
root.configure(bg="#f0f0f0") 

lbl_header = tk.Label(root, text="Attendance Strategist", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
lbl_header.pack(pady=20)

frame_inputs = tk.Frame(root, bg="#f0f0f0")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Subject Name:", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_subject = tk.Entry(frame_inputs, font=("Arial", 10), width=20)
entry_subject.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Total Classes Conducted:", bg="#f0f0f0", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_total = tk.Entry(frame_inputs, font=("Arial", 10), width=20)
entry_total.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Classes Attended:", bg="#f0f0f0", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_attended = tk.Entry(frame_inputs, font=("Arial", 10), width=20)
entry_attended.grid(row=2, column=1, padx=10, pady=5)

btn_calc = tk.Button(root, text="Analyze Status", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", command=calculate_strategy)
btn_calc.pack(pady=15, ipadx=10)

btn_clear = tk.Button(root, text="Clear", font=("Arial", 9), command=clear_fields)
btn_clear.pack(pady=0)

lbl_result = tk.Label(root, text="Result will appear here...", font=("Arial", 11), bg="white", fg="gray", width=40, height=8, relief="sunken")
lbl_result.pack(pady=20, padx=20)

root.mainloop()
