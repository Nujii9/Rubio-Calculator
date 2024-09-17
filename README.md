<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rubio's Calculator</title>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #3c3744;
            text-align: center;
            padding: 20px;
        }
        .container {
            background-color: #111;
            color: #fff;
            max-width: 500px;
            margin: 30px auto;
            padding: 30px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #a54b4b;
            border-radius: 5px;
        }
        button {
            background-color: #ad2828;
            color: #000;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            font-size: 16px;
        }
        button:hover {
            background-color: #d83535;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background-color: #7a2020;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Grade Calculator</h1>
        <p>Enter your prelim grade to calculate the required midterm and finals grade to pass.</p>

        <input type="number" id="prelimGrade" placeholder="Enter prelim grade (0-100)">
        <button id="calculateButton" py-click="calculate()">Calculate</button>

        <div id="result" class="result"></div>
    </div>

    <py-script>
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
            # Assume that midterm and finals grades are the same to simplify
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

        def calculate():
            # Get the prelim grade from the input field
            prelim_grade_input = Element('prelimGrade').value
            
            try:
                # Convert input to float and calculate the result
                prelim_grade = float(prelim_grade_input)
                result = calculate_required_grades(prelim_grade)
            except ValueError:
                result = "Error: Please enter a valid numerical value for the prelim grade."
            
            # Display the result in the result div
            Element('result').write(result)
    </py-script>

</body>
</html>
