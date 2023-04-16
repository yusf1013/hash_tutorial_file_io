credentials = {}


def read_credentials():
    # file1 = open("credentials.txt", "r")
    with open("credentials.txt", "r") as file1:
        lines = file1.readlines()
        for line in lines:
            line = line.strip()
            split_result = line.split(" ")
            username = split_result[0]
            password = int(split_result[1])
            credentials[username] = password


def write_to_file(username, password):
    # with open("credentials.txt", "w") as file1:

    file1 = open("credentials.txt", "a")
    file1.write(f"{username} {password}\n")
    file1.close()


def my_hash(in_str):
    search_str = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    for char in in_str:
        sum += search_str.find(char) + 1

    return sum


def main():
    read_credentials()
    while True:
        choice = input("1. Login\n2. Register\n")
        if choice == "1":
            username = input("username: ")
            password = input("password: ")
            if username not in credentials:
                print("User does not exist")
            elif credentials[username] == my_hash(password):
                print("success")
            else:
                print("failed")
        elif choice == "2":
            username = input("username: ")
            password = input("password: ")
            credentials[username] = my_hash(password)
            write_to_file(username, my_hash(password))
        else:
            print("error")

        print(credentials)


main()
