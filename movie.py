age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ")
# Determine discount eligibility
is_eligible = (age <= 12) or ((13 <= age <= 18) and (is_student.lower() == "yes"))

# Print discount eligibility message
if is_eligible:
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")
