import csv

# ------------------- LOGIN FUNCTION -------------------
def logincheck(usernames, passwords, inputuser, inputpassword):
    if inputuser in usernames:
        index = usernames.index(inputuser)
        if passwords[index] == inputpassword:
            return "Login successful!"
        else:
            return "Invalid password!"
    else:
        return "Invalid username!"

# ------------------- WRITE FUNCTION -------------------
def write_employee():
    with open("payroll_management.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Designation", "Days", "Leave", "OT Hours", "Reg Pay", "OT Pay", "Bonus"])
        n = int(input("How many employees? "))
        for _ in range(n):
            eid = input("Employee ID: ")
            name = input("Name: ")
            desig = input("Designation: ")
            days = input("Working Days: ")
            leave = input("Leave Taken: ")
            ot = input("OT Hours: ")
            reg = input("Regular Pay: ")
            otpay = input("OT Pay: ")
            bonus = input("Bonus: ")
            writer.writerow([eid, name, desig, days, leave, ot, reg, otpay, bonus])
    print("Data saved successfully!")

# ------------------- READ FUNCTION -------------------
def view_all():
    try:
        with open("payroll_management.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("File not found.")

# ------------------- APPEND FUNCTION -------------------
def append_employee():
    with open("payroll_management.csv", "a", newline='') as f:
        writer = csv.writer(f)
        eid = input("Employee ID: ")
        name = input("Name: ")
        desig = input("Designation: ")
        days = input("Working Days: ")
        leave = input("Leave Taken: ")
        ot = input("OT Hours: ")
        reg = input("Regular Pay: ")
        otpay = input("OT Pay: ")
        bonus = input("Bonus: ")
        writer.writerow([eid, name, desig, days, leave, ot, reg, otpay, bonus])
    print("Employee added!")

# ------------------- SEARCH FUNCTION -------------------
def search_employee():
    search_id = input("Enter Employee ID to search: ")
    found = False
    with open("payroll_management.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == search_id:
                print("Found:", row)
                found = True
                break
    if not found:
        print("Employee not found.")

# ------------------- UPDATE FUNCTION -------------------
def update_employee():
    eid = input("Enter ID to update: ")
    updated = []
    found = False
    with open("payroll_management.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == eid:
                print("Updating employee:", row)
                row[1] = input("New Name: ")
                row[2] = input("New Designation: ")
                row[3] = input("Working Days: ")
                row[4] = input("Leave: ")
                row[5] = input("OT Hours: ")
                row[6] = input("Regular Pay: ")
                row[7] = input("OT Pay: ")
                row[8] = input("Bonus: ")
                found = True
            updated.append(row)
    if found:
        with open("payroll_management.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated)
        print("Employee updated!")
    else:
        print("Employee not found.")

# ------------------- DELETE FUNCTION -------------------
def delete_employee():
    eid = input("Enter ID to delete: ")
    updated = []
    found = False
    with open("payroll_management.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] != eid:
                updated.append(row)
            else:
                found = True
    if found:
        with open("payroll_management.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated)
        print("Employee deleted!")
    else:
        print("Employee not found.")

# ------------------- MAIN MENU FUNCTION -------------------
def menu():
    while True:
        print("\n--- PAYROLL MANAGEMENT MENU ---")
        print("1. Write all data (overwrite)")
        print("2. View all data")
        print("3. Append employee")
        print("4. Search employee")
        print("5. Update employee")
        print("6. Delete employee")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            write_employee()
        elif choice == '2':
            view_all()
        elif choice == '3':
            append_employee()
        elif choice == '4':
            search_employee()
        elif choice == '5':
            update_employee()
        elif choice == '6':
            delete_employee()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# ------------------- LOGIN FIRST -------------------
print("===== LOGIN =====")
usernames = ["admin", "system", "guest"]
passwords = ["admin123", "manager", "allow"]
u = input("Enter username: ")
p = input("Enter password: ")
status = logincheck(usernames, passwords, u, p)
print(status)

if status == "Login successful!":
    menu()
