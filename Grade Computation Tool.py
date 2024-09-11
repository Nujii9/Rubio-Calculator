# Function to calculate the grades from prelim, midterm and finals
def calculate_required_grade(prelim_grade):
    try:
        # Convert input to float (if possible)
        prelim_grade = float(prelim_grade)
        
        # Calculate the prelim component (20% of the prelim grade)
        prelim_component = prelim_grade * 0.20
        
        # Set the required overall grade to pass the subject (75%)
        required_overall_grade = 75
        
        # Use the formula: prelim_component + 0.8 * x = 75, where x is the required Midterm/Finals grade
        remaining_grade_needed = required_overall_grade - prelim_component
        required_midterm_finals_grade = remaining_grade_needed / 0.80
        
        # Ensure the required grade is valid
        if required_midterm_finals_grade <= 100:
            return f"With a prelim grade of {prelim_grade}, you need a Midterm/Finals grade of {required_midterm_finals_grade:.2f}% to pass."
        else:
            return f"With a prelim grade of {prelim_grade}, even a Midterm/Finals grade of 100% is not enough to pass."
    
    except ValueError:
        return "Invalid input! Please enter a numerical value for the prelim grade."

# Results of grade calculation
prelim_input = input("Enter the prelim grade: ")
result = calculate_required_grade(prelim_input)
print(result)
