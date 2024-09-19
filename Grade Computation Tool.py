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

    # Calculate remaining grades needed to pass
    remaining_to_pass = passing_grade - prelim_contribution
    remaining_to_deans = deans_lister_grade - prelim_contribution

    # Check if it's possible to pass based on the remaining grades
    if remaining_to_pass > 0:
        required_midterm_to_pass = remaining_to_pass / midterm_weight if remaining_to_pass / midterm_weight <= 100 else 100
        required_finals_to_pass = (remaining_to_pass - (required_midterm_to_pass * midterm_weight)) / finals_weight
        if required_finals_to_pass > 100:
            return "It is difficult to pass."

        result = f"To pass, you need Midterm Grade: {required_midterm_to_pass:.2f}, Finals Grade: {required_finals_to_pass:.2f}."
    else:
        result = "You have already passed based on your Prelim grade!"

    # Check if it's possible to be a Dean's Lister based on the remaining grades
    if remaining_to_deans > 0:
        required_midterm_to_deans = remaining_to_deans / midterm_weight if remaining_to_deans / midterm_weight <= 100 else 100
        required_finals_to_deans = (remaining_to_deans - (required_midterm_to_deans * midterm_weight)) / finals_weight
        if required_finals_to_deans <= 100:
            result += f"\nTo qualify for Dean's Lister, you need Midterm Grade: {required_midterm_to_deans:.2f}, Finals Grade: {required_finals_to_deans:.2f}."
        else:
            result += "\nThe student cannot qualify for Dean's Lister."
    else:
        result += "\nYou are qualified for Dean's Lister!"

    return result

# Input: Prelim grade
try:
    prelim_grade_input = input("Enter the Prelim grade (0 to 100): ")
    
    # Convert input to a float
    prelim_grade = float(prelim_grade_input)

    # Ensure the prelim grade is between 0 and 100
    if prelim_grade < 0 or prelim_grade > 100:
        print("Error: Please enter a grade between 0 and 100.")
    else:
        # Calculate the required midterm and finals grades
        result = calculate_required_grades(prelim_grade)
        print(result)
    
except ValueError:
    print("Error: Please enter a valid numerical value for the prelim grade.")
