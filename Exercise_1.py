students_list=[]
students_dict={}
def add_student():
  #This function adds a new student to the system.
  name = input("Enter student name: ")
  age = int(input("Enter student age: "))
  grade = int(input("Enter student grade: "))

   # Check for duplicate names before adding
  if name in students_list:
    print("Student with that name already exists!")
    return
  students_list.append(name)
  students_dict[name] = {"age": age, "grade": grade}
  print(f"Student '{name}' added successfully!")
  print_student_details()  # Call function to display details

def search_student():
  #This function searches for a student by name.
  name = input("Enter student name to search: ")
  if name in students_dict:
    student = students_dict[name]
    print(f"Student Found: Name: {name}, Age: {student['age']}, Grade: {student['grade']}")
  else:
    print("Student not found!")

def remove_student():
  
 #This function removes a student from the system.
  
  name = input("Enter student name to remove: ")
  if name in students_list:
    students_list.remove(name)
    del students_dict[name]
    print(f"Student '{name}' removed successfully!")
  else:
    print("Student not found!")
def print_student_details():

#This function displays information of all students.
 
  if not students_list:
    print("No students added yet!")
    return
  print("Students:")
  for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

def main():
  """
  This function drives the main program loop.
  """
  while True:
    print("\nStudent Information Management System")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Remove Student")
    print("4. View Students")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
      add_student()
    elif choice == "2":
      search_student()
    elif choice == "3":
      remove_student()
    elif choice == "4":
      print_student_details()
    elif choice == "5":
      print("Exiting...")
      break
    else:
      print("Invalid choice!")


if __name__ == "__main__":
  main()