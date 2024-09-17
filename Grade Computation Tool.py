def calculate_required_grades(prelim_grade):
    # Check if the input is numeric
    if not isinstance(prelim_grade, (int, float)):
        return "Error: Please enter a valid numerical grade for prelim."
    
    # Check if the prelim grade is within the valid range
    if prelim_grade < 0 or prelim_grade > 100:
        return "Error: Please enter a grade between 0 and 100."
    
    # Define constants for the weight of each grade
    prelim_weight = 0.20
    midterm_weight = 0.30
    finals_weight = 0.50
    passing_grade = 75
    deans_lister_grade = 90

    # Calculate the grade contribution from the prelim
    prelim_contribution = prelim_grade * prelim_weight

    # Determine the required remaining grade
    required_remaining = passing_grade - prelim_contribution
    
    if required_remaining > (midterm_weight + finals_weight) * 100:
        return "The student has no chance to pass."

    # Calculate the required grades for midterms and finals to pass
    required_midterm_finals = required_remaining / (midterm_weight + finals_weight)

    # Check if it's possible to be a Dean's Lister
    required_deans_lister_remaining = deans_lister_grade - prelim_contribution
    required_midterm_finals_deans = required_deans_lister_remaining / (midterm_weight + finals_weight)
    
    if required_midterm_finals > 100:
        return "The student has no chance to pass."
    
    result = f"To pass, you need at least {required_midterm_finals:.2f} in both midterms and finals."
    
    if required_midterm_finals_deans <= 100:
        result += f"\nTo qualify for Dean's Lister, you need at least {required_midterm_finals_deans:.2f} in both midterms and finals."
    else:
        result += "\nThe student cannot qualify for Dean's Lister."

    return result

# Input: Prelim grade
try:
    prelim_grade_input = input("Enter the Prelim grade: ")
    
    # Convert input to a float
    prelim_grade = float(prelim_grade_input)
    
    # Calculate the required midterm and finals grades
    result = calculate_required_grades(prelim_grade)
    print(result)
    
except ValueError:
    print("Error: Please enter a valid numerical value for the prelim grade.")
