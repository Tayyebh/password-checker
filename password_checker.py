print("Password Checker - Please enter your password")
print()

password = input("Enter your password: ")
print()

if len(password) < 8:
    print("❌ Password is too short (minimum 8 characters)")
elif len(password) > 20:
    print("❌ Password is too long (maximum 20 characters)")
elif not any(c.isupper() for c in password):
    print("❌ Password must include at least one uppercase letter (A-Z)")
elif not any(not c.isalnum() for c in password):
    print("❌ Password must include at least one special character (!@#$%^&*)")
else:
    print("✅ Password is valid!")
