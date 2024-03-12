def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI) using weight (in kilograms) and height (in meters).
    Formula: BMI = weight / (height^2)
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret the BMI value and provide a corresponding message.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Interpret BMI
    interpretation = interpret_bmi(bmi)

    # Display results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {interpretation}")

if __name__ == "__main__":
    main()
