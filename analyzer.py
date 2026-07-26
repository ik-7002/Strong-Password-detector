import re
import math
import string
import secrets


def analyze_password(password, username,generate_pas):

    # Basic analysis and suggestion

    if len(password) < 16:
        b_analysis = "Your password is too short."
        suggestion = "Add at least 16 characters."
    elif not re.search(r"[A-Z]", password):
        b_analysis = "Your password does not contain an uppercase letter."
        suggestion = "Add an uppercase letter."
    elif not re.search(r"[a-z]", password):
        b_analysis = "Your password does not contain a lowercase letter."
        suggestion = "Add a lowercase letter."
    elif not re.search(r"[0-9]", password):
        b_analysis = "Your password does not contain a digit."
        suggestion = "Add a digit."
    elif not re.search(r"[!@#$%./_]", password):
        b_analysis = "Your password does not contain a special character."
        suggestion = "Add a special character."
    else:
        b_analysis = "Your password satisfies the basic requirements."
        suggestion = "None"

    # Password length

    length = len(password)

    # Character checks

    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(char in "!@#$%./_" for char in password)

    # Entropy

    entropy = length * math.log2(70)

    # Password score

    if entropy <= 20:
        p_suggestion = "Super Weak"
        score = 1
    elif entropy <= 40:
        p_suggestion = "Weak"
        score = 3
    elif entropy <= 60:
        p_suggestion = "Moderate"
        score = 5
    elif entropy <= 80:
        p_suggestion = "Good"
        score = 7
    elif entropy <= 100:
        p_suggestion = "Strong"
        score = 9
    else:
        p_suggestion = "Super Strong"
        score = 10

    # Repetition detector

    repeated = False

    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            repeated = True
            break

    # Random password generator

    characters = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + "!@#$%./_"
    )

    random_password = ""

    if(generate_pas=="yes"):
        for _ in range(16):
            random_password += secrets.choice(characters)
    else:
        random_password ="Random Password not generated !!"

    # Username detector

    username_found = False

    if username:
        username_found = username.lower() in password.lower()


    return {
        "length": length,
        "entropy": round(entropy, 2),
        "score": score,
        "Passwordscore_suggestion": p_suggestion,
        "suggestion": suggestion,
        "Basic_analysis": b_analysis,
        "generated_password": random_password,
        "contains_upper": upper,
        "contains_lower": lower,
        "contains_digit": digit,
        "contains_special": special,
        "repeated": repeated,
        "username_found": username_found,
    }