import re

print("=" * 50)
print("        WiFi Password Security Auditor")
print("=" * 50)

password = input("\nEnter your WiFi Password: ")

score = 0
suggestions = []

# Length Check
if len(password) >= 12:
    score += 1
else:
    suggestions.append("Password should contain at least 12 characters.")

# Uppercase Check
if re.search(r"[A-Z]", password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter.")

# Lowercase Check
if re.search(r"[a-z]", password):
    score += 1
else:
    suggestions.append("Add at least one lowercase letter.")

# Number Check
if re.search(r"[0-9]", password):
    score += 1
else:
    suggestions.append("Add at least one number.")

# Special Character Check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    suggestions.append("Add at least one special character.")

print("\n" + "=" * 50)

if score <= 2:
    print("Password Strength : WEAK")
elif score == 3 or score == 4:
    print("Password Strength : MEDIUM")
else:
    print("Password Strength : STRONG")

print("=" * 50)

if suggestions:
    print("\nSuggestions to Improve Password:")
    for item in suggestions:
        print("- " + item)
else:
    print("\nExcellent! Your WiFi password is highly secure.")

print("\nThank you for using WiFi Password Security Auditor.")
