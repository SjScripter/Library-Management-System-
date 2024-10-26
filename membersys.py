import csv

def add_member():
    try:
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        with open('members.csv', 'a', newline='') as f1:
            b = csv.writer(f1)
            b.writerow([name, email, phone])

    except Exception as e:
        print("An error occurred:", e)

def display_members():
    try:
        with open('members.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            print("Members:")
            for row in reader:
                print("\t".join(row))
    except FileNotFoundError:
        print("File 'members.csv' not found.")
    except Exception as e:
        print("An error occurred:", e)

def search_member_by_name(member_name):
    try:
        with open('members.csv', 'r', newline='') as csvfile:
            found = False
            for line in csvfile:
                fields = line.strip().split(',')
                if fields[0].lower() == member_name.lower():
                    found = True
                    print("Yes, this member exists in the records.")
                    break
            if not found:
                print("Member not found in records.")
    except FileNotFoundError:
        print("File 'members.csv' not found.")
    except Exception as e:
        print("An error occurred:", e)


def remove_member_by_name(member_name):
    try:
        temp_members = []
        with open('members.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            found = False
            for row in reader:
                if row[0].lower() == member_name.lower():
                    found = True
                else:
                    temp_members.append(row)
        
        if found:
            with open('members.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(temp_members)
            print("Member removed successfully.")
        else:
            print("Member not found in records.")
    except FileNotFoundError:
        print("File 'members.csv' not found.")
    except Exception as e:
        print("An error occurred:", e)

