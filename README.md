#  ALU Grade Calculator
This is a simple Python command-line program that allows ALU students or staff to log assignment grades, calculate weighted scores, and determine GPA and pass/fail status.

## 📌 Features

- Add multiple assignments of two types:  
  - **FA**: Formative Assignments (Max 60% total weight)  
  - **SA**: Summative Assessments (Max 40% total weight)
- Validate assignment details: name, category, weight, and grade.
- Automatically compute:
  - Weighted grade per assignment
  - Total scores for FA and SA
  - GPA (on a 5.0 scale)
  - Pass/Fail status (requires 50% in both FA and SA)
- Display a full transcript with all assignment data and summaries.

## 🛠️ How to Use

Make sure Python 3 is installed. Then run:

```bash
python3 grade_calculator.py


---

### 5. **Usage Instructions**
- Step-by-step how to use the app
- Example input/output

```markdown
## 🧪 Example Usage

## Validation Rules
- FA max total weight: 60%
- SA max total weight: 40%
- Grade: 0 to 100
- Name must contain letters

## 📋 Sample Output

------------------------------------------------------------
                       ALU_TRANSCRIPT                       
------------------------------------------------------------
Assignment           Category   Grade(%)   Weight     Points    
------------------------------------------------------------
math                 FA         85.0       20.0       17.00     
Formatives (60)                                     17.00     
Summatives (40)                                     0.00      
------------------------------------------------------------
Total Grade                     17.00/100
GPA (5.0)scale                  0.85
Status                          FAIL AND REPEAT
------------------------------------------------------------



