from Handler import read_file, write_file

def add_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Name: ")

    member_data = f"{member_id},{name}\n"
    write_file("members.txt", member_data)
    print("Member added successfully!")

def search_member():
    member_id = input("Enter Member ID: ")
    members = read_file("members.txt")
    for member in members:
        if member.startswith(member_id):
            member_id, name = member.strip().split(",")
            print("Member found!")
            print("Member ID:", member_id)
            print("Name:", name)
            return
    print("Member not found!")

def display_all_members():
    members = read_file("members.txt")
    if members:
        print("===== All Members =====")
        for member in members:
            member_id, name = member.strip().split(",")
            print("Member ID:", member_id)
            print("Name:", name)
            print("---------------------")
    else:
        print("No members available!")