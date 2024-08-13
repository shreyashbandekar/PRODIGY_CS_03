import re

def assess_password_strength(password):
    # Define the strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Check the password strength
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    # Provide feedback based on the score
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    elif score == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Return the results
    return {
        'password': password,
        'length': length_criteria,
        'uppercase': uppercase_criteria,
        'lowercase': lowercase_criteria,
        'number': number_criteria,
        'special_char': special_char_criteria,
        'strength': strength
    }

def display_password_strength(password_assessment):
    print(f"Password: {password_assessment['password']}")
    print(f"Length requirement met: {'Yes' if password_assessment['length'] else 'No'}")
    print(f"Uppercase letter present: {'Yes' if password_assessment['uppercase'] else 'No'}")
    print(f"Lowercase letter present: {'Yes' if password_assessment['lowercase'] else 'No'}")
    print(f"Number present: {'Yes' if password_assessment['number'] else 'No'}")
    print(f"Special character present: {'Yes' if password_assessment['special_char'] else 'No'}")
    print(f"Password strength: {password_assessment['strength']}")

# Example usage
password = input("Enter a password to assess: ")
assessment = assess_password_strength(password)
display_password_strength(assessment)
