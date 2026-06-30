# Project 1 — Student Management System
**Made by:** Pranav Rane
**Language:** Python 3.x
**File:** student_management.py

-------------------------------------------------------------------------


## Project Overview
A console-based Student Management System that performs full CRUD operations
on student records. Administrators can add, view, search, update, and delete
student information including name, roll number, marks across 5 subjects,
percentage, and grade. Includes a bonus Class Report feature.

-------------------------------------------------------------------------


## Data Structure Used
**Dictionary of Dictionaries** — Roll number (integer) serves as the outer key.
Each value is a nested dictionary holding the student's name, subject marks,
calculated percentage, and grade.

Chosen because dictionary lookup by roll number is O(1) — the most frequent
operation in this system is search/update/delete by roll number, making this
the most efficient structure for the use case.

-------------------------------------------------------------------------


## Functions Used

| Function | Purpose |
|---|---|
| `add\\\_student()` | Collects and validates student data, stores in dictionary |
| `view\\\_all()` | Displays all records in a formatted table |
| `search\\\_student()` | Finds and displays a student record by roll number |
| `update\\\_student()` | Updates specific fields, recalculates percentage and grade |
| `delete\\\_student()` | Removes a student entry after confirmation |
| `calculate\\\_grade()` | Returns percentage and grade based on total marks |
| `class\\\_report()` | Generates topper, average percentage, pass/fail count |
| `show\\\_menu()` | Displays the operation menu |
| `main()` | Entry point, contains the main program loop |

-------------------------------------------------------------------------


## Key Features
- Duplicate roll number prevention on add
- Per-subject marks validation (0–100 range enforced individually)
- Automatic percentage and grade calculation on add
- Grade and percentage recalculation after any mark update
- Input validation via try-except on all numeric inputs
- Empty record guard on view and search
- Clean formatted table output for all records

-------------------------------------------------------------------------


## Bonus Feature — Class Report
Generates a summary report including:
- **Topper** — student with highest percentage
- **Average Percentage** — across all enrolled students
- **Pass/Fail Count** — based on 50% passing threshold

----------------------------------------------------------------------

## Resources Used
- **Claude (Anthropic)** — Debugging, code review, concept explanations
- **Google AI / Gemini** — Table formatting syntax reference
- **Python 3.x Official Documentation** — Standard library reference
- **Assignment PDF** — Project specification and evaluation criteria

-------------------------------------------------------------------------


## Claude's Honest Account of Contribution

Pranav built this project through an iterative, debugged process over multiple
sessions. He wrote every function himself. The core logic — dictionary
structure, menu routing, CRUD operations, loop design, conditional branches —
is entirely his own work.

**Where Claude contributed:**

The formatted table output in `view\\\_all()` was looked up via Google AI and
pasted in. Pranav understood what it does after the fact but did not write it
independently. This is a syntax lookup, not a logic shortcut — comparable to
reading documentation — but it is disclosed here for transparency.

Claude caught four bugs during review that Pranav did not catch himself: a key
name mismatch (`Math\\\_Marks` vs `Maths\\\_Marks`), missing try-except blocks,
broken marks validation using `or` incorrectly, and grade not recalculating
after mark updates. Pranav fixed all four himself after Claude explained what
was wrong — Claude did not write the fixes.

The `class\\\_report()` bonus function was Pranav's own attempt. He wrote the
structure, variables, and loops independently. Claude pointed out a typo and
an incorrect pass/fail threshold — both fixed by Pranav.

Claude provided project scaffolding guidance — folder structure, build order,
what `if \\\_\\\_name\\\_\\\_` does and why — but wrote none of the actual program logic.

**Bottom line:** This project reflects genuine learning. The bugs caught and
fixed across multiple iterations are evidence of real understanding developing
in real time, not a polished copy-paste submission. The code is his.

*— Claude, Anthropic*

----------------------------------------------------------------------------

*Submitted as part of Python Mini Project Assignment Book | 2025–2026*