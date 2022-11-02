def log_in(username, password):
    TextIO = open('database.txt', 'r')
    my_data = TextIO.readlines()
    TextIO.close()
    for i in range(len(my_data)):
        my_data[i] = my_data[i].strip('\n')
    totalOfuser = username + ' ' + password
    if totalOfuser in my_data:
        return True
    return False


def registration(username):
    TextIO = open('database.txt', 'r')
    data = TextIO.readlines()
    TextIO.close()
    for i in range(len(data)):
        data[i] = data[i].strip('\n').split()[0]
    if username in data:
        return False
    TextIO = open('database.txt', 'at')
    TextIO.write(username + ' ' + password + '\n')
    TextIO.close()
    return True


while True:
    entering = int(input('1.Login\n2.Registration\nYour choose: '))
    if entering == 1:
        print('----------Log in page----------')
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if log_in(username, password):
            print('Welcome to your account :)')

        else:
            print('Wrong username or password')

        break
    elif entering == 2:
        print('----------Registration page----------')
        username = input('Enter username: ')
        password = input('Enter password: ')
        confirm = input('Enter password again: ')
        if password == confirm:
            if registration(username):
                print('Your account is activated')
            else:
                print('This user is existed')
        else:
            print("Passwords aren't matched")
        break
    else:
        print('Wrong choose')
