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
        # Function to calculate required grades
        def calculate_required_grades(prelim_grade):
            prelim_weight = 0.20
            midterm_weight = 0.30
            finals_weight = 0.50
            passing_grade = 75
            deans_lister_grade = 90

            if not isinstance(prelim_grade, (int, float)):
                return "Error: Please enter a valid numerical grade for prelim."
            
            if prelim_grade < 0 or prelim_grade > 100:
                return "Error: Please enter a grade between 0 and 100."
            
            prelim_contribution = prelim_grade * prelim_weight

            remaining_to_pass = passing_grade - prelim_contribution
            remaining_to_deans = deans_lister_grade - prelim_contribution

            if remaining_to_pass > 0:
                required_midterm_to_pass = remaining_to_pass / midterm_weight if remaining_to_pass / midterm_weight <= 100 else 100
                required_finals_to_pass = (remaining_to_pass - (required_midterm_to_pass * midterm_weight)) / finals_weight
                if required_finals_to_pass > 100:
                    return "It is difficult to pass."

                result = f"To pass, you need Midterm Grade: {required_midterm_to_pass:.2f}, Finals Grade: {required_finals_to_pass:.2f}."
            else:
                result = "You have already passed based on your Prelim grade!"

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

        # Function to handle button click
        def calculate():
            prelim_grade_input = Element('prelimGrade').value
            try:
                prelim_grade = float(prelim_grade_input)
                result = calculate_required_grades(prelim_grade)
            except ValueError:
                result = "Error: Please enter a valid numerical value for the prelim grade."
            
            Element('result').write(result)
    </py-script>

</body>
</html>
