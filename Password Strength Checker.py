import math
import re

def calculate_entropy(password):
    """
    Calculates the entropy of a password using Shannon's entropy formula.
    """
    password_length = len(password)
    character_pool = len(set(password))
    entropy = password_length * math.log(character_pool, 2)
    return entropy

def is_strong_password(password):
    """
    Determines whether a password is strong or weak based on its entropy score.
    """
    entropy_threshold = 50
    entropy = calculate_entropy(password)
    if entropy >= entropy_threshold:
        return True
    else:
        return False

def password_strength_report(password):
    """
    Generates a report on the strength of a password and provides recommendations for making it more secure.
    """
    if is_strong_password(password):
        print(f"Password strength: Strong")
    else:
        print(f"Password strength: Weak")
        print(f"Suggested improvements: Use a longer password with a mix of uppercase and lowercase letters, numbers, and symbols.")

if __name__ == '__main__':
    password = input("Enter a password to check its strength: ")
    password_strength_report(password)
