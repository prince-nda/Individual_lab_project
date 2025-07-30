class GradeCalculator:
    def __init__(self):
        self.assignments = []   # list to store all assignments details
        self.FA_total_weight = 0      # Tracks the total weight of all Formative Assignments
        self.SA_total_weight = 0      # Tracks the total weight of all Summative Assessments
        self.max_FA_weight = 60       # Maximum allowed weight for Formative Assignment
        self.max_SA_weight = 40       # Maximum allowed weight for summative assessments
    
    # Validates category of the assignments
    def assignment_category(self, category):         
        category = category.strip().upper()
        if category not in ["FA", "SA"]:
            print("Error: category must be 'FA' (Formative) or 'SA' (Summative)")
            return None
        return category
    
    # Validates the weight of assignment based on category
    def assignment_weight(self, weight, category):
        try:
            weight = float(weight)
            if weight <= 0:
                print("Error: please weight must be positive!")
                return None
            # check if the weight exceeds the maximum limit 
            if category == "FA":
                if self.FA_total_weight + weight > self.max_FA_weight:
                    print(f"FA weight cannot be greater than {self.max_FA_weight}% total (currently {self.FA_total_weight}% total)")
                    return None
            else:
                if self.SA_total_weight + weight > self.max_SA_weight:
                    print(f"SA weight cannot be greater than {self.max_SA_weight}% total (currently {self.SA_total_weight}% total)")
                    return None
                
            return weight
        except ValueError:
            print("Error: please weight has to be a number!")
            return None
    
    # Validates the Grade of assignments
    def assignment_grade(self, grade):
        try:
            grade = float(grade)
            if not (0 <= grade <= 100):
                print("Error: please grade must be between 0-100%")
                return None
            return grade
        except ValueError:
            print("Error: please grade must be a number (e.g 75.08)")
            return None
        
    # Prompts the user for assignment details, validates them, and adds them to the list
    def add_assignments(self):
        print("\n" + "="*30)
        print("Add New Assignment (FA/SA)")
        print("="*30)

         # name validation
        name = input("Enter New Assignment name: ").strip()
        if not name:
            print("Error: sorry assignment name cannot be empty")
            return
        
        if not any(char.isalpha() for char in name):
            print("Error: Assignment name must contain any alphabet letter")
            return

        # category validation 
        category = None
        while not category:
            category_input = input("Category (FA/SA): ").strip().upper()
            category = self.assignment_category(category_input)

        # weight validation
        weight = None 
        while not weight:
            weight_input = input("Weight (%): ").strip()
            weight = self.assignment_weight(weight_input, category)

        # grade validation
        grade = None 
        while not grade:
            grade_input = (input("Grade (%): ")).strip()
            grade = self.assignment_grade(grade_input)
        
        # weighted grade calculation for the assignment
        weighted_grade = (grade * weight) / 100
        
        # adding the assignment to the list and store them
        self.assignments.append({'name':name, 'category': category, 'weight': weight, 'grade': grade, 'weighted_grade': weighted_grade})

        # update category weights
        if category == "FA":
            self.FA_total_weight += weight
        else:
            self.SA_total_weight += weight
            
        print("\nAssignment added successful!")
        print(f"{name} ({category}): {grade}% x {weight}% = {weighted_grade:.2f}%")

    # calculates the total weighted grade 
    def calculate_totals(self):
        FA_sum = sum(a['weighted_grade'] for a in self.assignments if a['category'] == 'FA')
        SA_sum = sum (a['weighted_grade'] for a in self.assignments if a['category'] == 'SA')

        FA_percentage = (FA_sum / self.max_FA_weight *100) if self.FA_total_weight else 0
        SA_percentage = (SA_sum / self.max_SA_weight * 100) if self.SA_total_weight else 0

        total_grade = FA_sum + SA_sum
        gpa = (total_grade / 100) * 5 # GPA scale is on 5.0

        # Pass/Fail Determination
        pass_status = "Pass" if FA_percentage >= 50 and SA_percentage >= 50 else "FAIL AND REPEAT"

        return{'FA_total': FA_sum, 'SA_total': SA_sum, 'FA_percentage': FA_percentage, 'SA_percentage': SA_percentage, 'total_grade': total_grade, 'gpa': gpa, 'pass_status': pass_status}
    
    # Displays a transcript of all assignments and all details
    def show_transcript(self):
        print("\n" + "-"*60)
        print("ALU_TRANSCRIPT".center(60))
        print("-"*60)
        print(f"{'Assignment':<20} {'Category':<10} {'Grade(%)':<10} {'Weight':<10} {'Points':<10}")
        print("-"*60)

        for assignment in self.assignments:
            print(f"{assignment['name']:<20} {assignment['category']:<10} {assignment['grade']:<10.1f} {assignment['weight']:<10.1f} {assignment['weighted_grade']:<10.2f}")

        totals = self.calculate_totals()

        print(f"{'Formatives (60)':<20} {'':<30} {totals['FA_total']:<10.2f}")
        print(f"{'Summatives (40)':<20} {'':<30} {totals['SA_total']:<10.2f}")
        print("-"*60)
        print(f"{'Total Grade':<20} {'':<10} {totals['total_grade']:.2f}/100")
        print(f"{'GPA (5.0)scale':<20} {'':<10} {totals['gpa']:.2f}")
        print(f"{'Status':<20} {'':<10} {totals['pass_status']}")
        print("-"*60)

# Main function that runs the GradeCalculator program
def main():
    calculator = GradeCalculator()
        
    print("=== WELCOME TO ALU GRADE CALCULATOR! ===")
    print("FA = Formative Assignment (Max 60% weight)")
    print("SA = Summative Assignment ( Max 40% weight)\n")

    try:
        while True:
            calculator.add_assignments()
            cont = input("\nYou want to Add another assignment? (y/n): ").lower()
            if cont == 'y':
                continue
            elif cont == 'n':
                calculator.show_transcript()
                return
            else:
                print("invalid input. please enter 'y' or 'n'")

    except KeyboardInterrupt:
        print("\nProgram interrupted by user (Ctrl + c). Exiting clearly")
    
    if not calculator.assignments:
        print("\nNo valid assignments were added.")
        return
    
    calculator.show_transcript()

if __name__ == "__main__":
    main()

