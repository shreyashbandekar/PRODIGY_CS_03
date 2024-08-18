# PRODIGY_CS_03
# Password Strength Assessment

This Python script evaluates the strength of a password based on several criteria, such as length, presence of uppercase and lowercase letters, numbers, and special characters. The script provides a detailed assessment of the password, indicating whether it meets each of the criteria and assigning an overall strength rating.

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
    Password: Your_password
    Length requirement met: Yes
    Uppercase letter present: Yes
    Lowercase letter present: Yes
    Number present: Yes
    Special character present: No
    Password strength: Moderate
