# Activity Selection using Greedy Algorithm

## 📌 Overview
This project implements the **Activity Selection Problem** using a **Greedy Algorithm** approach in Python.

The goal is to select the maximum number of non-overlapping activities from a given list of activities, each having a start and finish time.

---

## 🧠 Algorithm Used
The solution follows the greedy strategy:
1. Sort all activities based on their **finish time**.
2. Always pick the activity that finishes earliest.
3. Select the next activity whose start time is greater than or equal to the last selected activity's finish time.

This ensures the maximum number of compatible (non-overlapping) activities.

---

## 📂 File Structure
```
activity_selection.py
README.md
```

---

## ▶️ How to Run

1. Make sure Python is installed (Python 3.x recommended)
2. Run the program:

```
python activity_selection.py
```

---

## 🧾 Input Format

- First, enter the number of activities.
- For each activity, provide:
  - Start time
  - Finish time

### Example Input
```
Enter number of activities: 4

Activity 1
Start time: 1
Finish time: 3

Activity 2
Start time: 2
Finish time: 5

Activity 3
Start time: 4
Finish time: 6

Activity 4
Start time: 6
Finish time: 7
```

---

## ✅ Output

The program will display the maximum set of non-overlapping activities.

### Example Output
```
Selected activities (max non-overlapping):
Activity 1: Start = 1, Finish = 3
Activity 2: Start = 4, Finish = 6
Activity 3: Start = 6, Finish = 7

Total activities selected: 3
```

---

## ⚙️ Functions Description

- `activity_selection(activities)`
  - Implements the greedy algorithm.
  - Returns the list of selected activities.

- `get_activities()`
  - Takes user input for activities.

- `display(selected)`
  - Prints the selected activities.

- `main()`
  - Driver function to execute the program.

---

## ⏱ Time Complexity
- Sorting: **O(n log n)**
- Selection: **O(n)**
- Overall: **O(n log n)**

---

## 🎯 Key Features
- Simple and efficient greedy solution
- User-friendly input/output
- Demonstrates classic algorithm design technique

---

## 📚 Concepts Covered
- Greedy Algorithms
- Scheduling Optimization
- Sorting
