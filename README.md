# College Attendance Manager (The Smart "Bunk" Calculator)

**Domain:** Productivity & Automation  
**Language:** Python 3.14.0 
**Submission Date:** November 2025

## 📖 Project Overview
In college, maintaining the mandatory **75% attendance threshold** is a constant source of stress for students. Calculating exactly how many classes one can afford to miss (or how many must be attended to recover) involves complex mental math often leading to errors.

The **College Attendance Manager** is a Python-based CLI (Command Line Interface) tool designed to solve this specific real-world problem. It acts as a strategic planner, telling students exactly how many classes they can safely "bunk" or how many they must attend consecutively to stay safe.

## 🎯 Objectives
1.  **Real-World Application:** Eliminate the fear of detainment due to low attendance.
2.  **Accuracy:** Provide exact numbers for "safe skips" or "recovery classes" rather than just a percentage.
3.  **Simplicity:** A user-friendly text interface that requires no complex setup.

## ⚙️ Features
* **Dynamic Calculation:** Calculates current attendance percentage instantly.
* **"Safe Zone" Logic:** Tells you exactly how many future classes you can skip while remaining above 75%.
* **"Danger Zone" Recovery:** If attendance is low, it calculates the exact number of consecutive classes required to reach the 75% mark.
* **Summary Dashboard:** View a tabular report of all subjects entered.
* **Error Handling:** Prevents crashes if the user enters text instead of numbers or invalid data (e.g., Attended > Total).

## 🛠️ Technical Implementation
This project applies fundamental programming concepts learned in the course:
* **Control Structures:** `While` loops are used for the menu system and the prediction algorithm.
* **Data Structures:** A Python **Dictionary** is used to store subject data (`{'Subject': {'held': x, 'present': y}}`).
* **Modular Functions:** The code is split into specific functions (`calculate_status`, `main`) for better readability (Top-Down Design).
* **Exception Handling:** Uses `try-except` blocks to handle `ValueError` for invalid user inputs.

## 🚀 How to Run
1.  Ensure you have Python installed.
2.  Download the file `attendance_manager.py`.
3.  Run the following command in your terminal/command prompt:
    ```bash
    python attendance_manager.py
    ```

## 🧩 Algorithm / Logic
Unlike standard calculators that use algebra, this program uses an **Iterative Simulation Approach**:

1.  **If Safe (Percent >= 75%):**
    * The program runs a loop, incrementing the "Total Classes" by 1 (simulating a skip) while keeping "Attended" constant.
    * It stops when the percentage drops below 75%.
    * *Result:* The number of loop iterations = Safe Bunks.

2.  **If Unsafe (Percent < 75%):**
    * The program runs a loop, incrementing *both* "Total Classes" and "Attended" by 1 (simulating attending).
    * It stops when the percentage reaches 75%.
    * *Result:* The number of loop iterations = Classes Needed.

## 📸 Screenshots
### Main Menu
![Main Menu View](./screenshots/menu_view.png)

### Calculation Result
![Calculation Example](./screenshots/calculation.png)


## 👤 Author
* **Name:** Khush M Lohar
* **Reg No:** 25BAI11336 # Vityarthiproject
