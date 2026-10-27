# Logic Box - Pattern Generator and Number Analyzer

## 📌 Project Overview
**Logic Box** is a Python-based console application designed to demonstrate control structures, loops (`for` and `while`), the `range()` function, control statements (`break`, `continue`, `pass`), and nested loops[cite: 9, 10, 11]. This project allows users to generate various geometric patterns and perform analytical operations on number ranges through an interactive menu-driven interface[cite: 9, 10, 11].

---

## 🎯 Objectives
* Master the implementation of control structures and nested loops in Python[cite: 9, 10].
* Practice logical problem-solving and user input validation[cite: 9, 12].
* Build a clean, menu-driven Python application with robust error handling[cite: 11, 12].

---

## 🚀 Features & Functionality

### 1. Pattern Generator
Generates various shapes based on user input using nested loops[cite: 9, 10]:
* **Right-angled Triangle**[cite: 10, 11]
* **Pyramid Pattern**[cite: 10, 11]
* **Left-angled Triangle**[cite: 10, 11]
* Prompts the user to enter the number of rows for each pattern[cite: 9].

### 2. Number Analyzer
Analyzes a custom range of numbers based on user specifications[cite: 10, 11]:
* Prompts the user to enter a **Start** and **End** number[cite: 10, 11].
* Utilizes a `for` loop to iterate through the range and perform the following checks[cite: 10, 11]:
  * **Odd or Even:** Displays whether each number in the range is odd or even[cite: 10, 11].
  * **Sum of All Numbers:** Calculates and displays the total sum of all numbers from start to end range[cite: 10, 11].

### 3. Control Statements Implementation
* **`break`**: Used to stop pattern generation if the user enters an invalid row count[cite: 11].
* **`continue`**: Skips certain iterations or specific numbers without operation[cite: 11].
* **`pass`**: Acts as a placeholder in sections of code where logic will be added later[cite: 11].

---

## 💻 Menu-Driven Interface & Program Flow
The program provides a clean console interface with the following options[cite: 11, 12]:
```text
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 
```[cite: 12]

---

## 🛡️ Error Handling and Input Validation
* Validates user inputs to ensure row counts for patterns are positive integers[cite: 12].
* Ensures that the end range is greater than the start range[cite: 12].
* Displays appropriate error messages and prompts the user to re-enter valid values when necessary[cite: 12].

---

## 🛠️ How to Run the Project
1. Ensure you have **Python** installed on your system.
2. Clone or download this repository.
3. Open your terminal or command prompt in the project folder and run:
   ```bash
   python main.py
