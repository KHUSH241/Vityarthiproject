# Project Statement: College Attendance Manager

## 1. Problem Statement
In many academic institutions, maintaining a mandatory attendance threshold (commonly 75%) is a prerequisite for appearing in final examinations. Students often struggle to track their attendance accurately due to manual calculation errors or lack of data visibility. 

Existing tools typically provide only the *current* percentage. They fail to answer the two most critical questions a student has:
1.  *"How many upcoming classes can I safely skip without dropping below the limit?"*
2.  *"If I am currently short on attendance, how many classes must I attend consecutively to recover?"*

This lack of strategic insight leads to unnecessary anxiety, poor planning, and in severe cases, academic detainment.

## 2. Scope of the Project
The **College Attendance Manager** is a desktop-based utility designed to bridge the gap between raw attendance data and actionable advice. 

**The scope includes:**
* **Input Management:** Accepting user inputs for multiple subjects regarding total classes conducted and classes attended.
* **Status Analysis:** Instantly calculating current attendance percentages.
* **Predictive Simulation:** Using iterative logic to simulate future scenarios (skipping vs. attending) to determine safe margins or recovery requirements.
* **User Interface:** Providing a clean, error-free interface (CLI or GUI) that validates user inputs to prevent logical errors (e.g., preventing "Attended > Total").

**The scope excludes:**
* Automatic fetching of data from university servers (the tool relies on manual user entry).
* Complex database storage (data is strictly for the current session).

## 3. Target Users
* **University & College Students:** specifically those enrolled in courses with strict attendance policies (e.g., 75% or 80% mandatory attendance).
* **Academic Mentors/Proctors:** Who need a quick way to advise students on exactly how many classes they need to attend to avoid debarment.

## 4. High-Level Features
1.  **Smart "Bunk" Calculator (Safe Zone Logic):**
    * Identifies if a student is above the threshold.
    * Calculates the maximum number of future classes the student can miss while remaining safe.

2.  **Recovery Strategist (Danger Zone Logic):**
    * Identifies if a student is below the threshold.
    * Calculates the exact number of consecutive classes required to reach the safe percentage.

3.  **Input Validation:**
    * Prevents crashes by handling non-numeric inputs.
    * Logically validates that attended classes cannot exceed total classes.

4.  **Visual Dashboard:**
    * Presents a clear summary of the subject name, current status, and strategic advice.
    * (For GUI Version) Color-coded alerts (Green for Safe, Red for Danger) for immediate visual feedback.
