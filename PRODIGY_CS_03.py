import re


def password_strength_checker(password):
    # Criteria checks
    length = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Strength calculation
    score = 0
    if length:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Feedback based on score
    if score == 5:
        feedback = "Strong password!"
    elif score >= 3:
        feedback = "Moderate password."
    else:
        feedback = "Weak password. Try again."

    return feedback, score


# Loop until the password is moderate or strong
while True:
    password = input("Enter a password: ")
    feedback, score = password_strength_checker(password)
    print(feedback)

    # Break loop if password is moderate or strong
    if score >= 3:
        break
