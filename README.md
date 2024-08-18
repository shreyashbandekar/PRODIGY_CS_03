# PRODIGY_CS_03
# Password Strength Checker

## Introduction
The Password Strength Checker is a simple tool designed to evaluate the strength of passwords based on several common security criteria. The tool provides a detailed assessment of a password's strength, helping users create more secure passwords by highlighting areas of weakness.
## Features

- **Length Requirement:** The password must be at least 8 characters long.
- **Uppercase Letter:** The password must contain at least one uppercase letter.
- **Lowercase Letter:** The password must contain at least one lowercase letter.
- **Numeric Character:** The password must include at least one number.
- **Special Character:** The password must contain at least one special character (e.g., `!@#$%^&*(),.?":{}|<>`).

## Password Strength Levels

The script categorizes the password strength into four levels:
- **Strong:** Meets all criteria (5 out of 5).
- **Moderate:** Meets 4 out of 5 criteria.
- **Weak:** Meets 3 out of 5 criteria.
- **Very Weak:** Meets fewer than 3 criteria.

## Usage

1. **Run the Script:**
   Execute the script in a Python environment.

   ```bash
   python password_strength.py
## Requirements

- **Python 3.6+**

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/shreyashbandekar/PRODIGY_CS_03.git
2. **Run the Script:**
   
    Execute the script in a Python environment:
   ```bash
   python password_strength.py
3. **Usage**

    Input the Password:
     The script will prompt you to enter a password to assess:
   ```bash
   Enter a password to assess: Your_password
4. **Review the Assessment:**
   
    The script will display a detailed assessment of the password, including whether it meets each criterion and the overall       strength rating:
   ```bash
    -Password: Your_password
    -Length requirement met: Yes
    -Uppercase letter present: Yes
    -Lowercase letter present: Yes
    -Number present: Yes
    -Special character present: No
    -Password strength: Moderate

## Code Explanation
### assess_password_strength(password)
This function takes a password as input and checks it against the following criteria:

- **Length of the password**
- **Presence of uppercase and lowercase letters**
- **Inclusion of numbers and special characters**

It returns a dictionary containing the results of these checks and the overall password strength.

### display_password_strength(password_assessment)
This function takes the output from `assess_password_strength` and prints a user-friendly summary of the password assessment.
