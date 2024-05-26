def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_height():
    while True:
        unit = input("Would you like to enter height in inches or centimeters? (in/cm): ").strip().lower()
        if unit == 'in':
            height = get_user_input("Enter height in inches: ")
            return height
        elif unit == 'cm':
            height = get_user_input("Enter height in centimeters: ")
            return height / 2.54  # Convert cm to inches
        else:
            print("Invalid choice. Please enter 'in' for inches or 'cm' for centimeters.")

def get_weight():
    while True:
        unit = input("Would you like to enter weight in pounds or kilograms? (lbs/kg): ").strip().lower()
        if unit == 'lbs':
            weight = get_user_input("Enter weight in pounds: ")
            return weight
        elif unit == 'kg':
            weight = get_user_input("Enter weight in kilograms: ")
            return weight * 2.20462  # Convert kg to lbs
        else:
            print("Invalid choice. Please enter 'lbs' for pounds or 'kg' for kilograms.")

def calculate_bmi(height_in_inches, weight_in_pounds):
    bmi = (weight_in_pounds / height_in_inches ** 2) * 703
    if bmi < 16:
        return 'severely underweight', bmi
    elif 16 <= bmi < 18.5:
        return 'underweight', bmi
    elif 18.5 <= bmi < 25:
        return 'healthy', bmi
    elif 25 <= bmi < 30:
        return 'overweight', bmi
    else:
        return 'obese', bmi

def display_bmi_result(height, weight):
    category, bmi = calculate_bmi(height, weight)
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

    explanations = {
        'severely underweight': "Severely underweight: This indicates a BMI less than 16. It suggests a significantly low body weight, which could pose health risks. It is advisable to consult with a healthcare provider for a thorough evaluation and potential intervention.",
        'underweight': "Underweight: This indicates a BMI between 16 and 18.5. Being underweight could mean your body weight is too low, potentially due to malnutrition or other health conditions. It is recommended to seek advice from a healthcare provider to determine the cause and appropriate actions.",
        'healthy': "Healthy: This indicates a BMI between 18.5 and 25. This range is considered normal and generally associated with a lower risk of health issues. Maintaining a balanced diet and regular physical activity can help you stay within this range.",
        'overweight': "Overweight: This indicates a BMI between 25 and 30. It suggests a higher body weight than what is considered healthy for your height. Being overweight can increase the risk of various health problems, including cardiovascular diseases and diabetes. It is advisable to consider lifestyle changes such as improved diet and increased physical activity.",
        'obese': "Obese: This indicates a BMI of 30 or above. Obesity is associated with a higher risk of serious health conditions, such as heart disease, diabetes, and certain cancers. It is strongly recommended to seek medical advice to manage your weight effectively through a combination of diet, exercise, and possibly medical intervention."
    }

    print(explanations[category])

def main():
    print("Welcome to the Detailed BMI Calculator!")

    while True:
        height = get_height()
        weight = get_weight()

        display_bmi_result(height, weight)

        another_calculation = input("\nWould you like to calculate another BMI? (y/n): ").strip().lower()
        if another_calculation != 'y':
            print("Thank you for using the BMI Calculator. Stay healthy!")
            break

if __name__ == "__main__":
    main()
