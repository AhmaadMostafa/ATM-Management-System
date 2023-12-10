def WriteRecord():
    with open('ATM_User_Records.txt', 'a') as file:
        c = 'y'
        while c == 'y':
            Acc_Num = input('Enter Your Account Number : ')
            Password = input('Enter Your Password : ')
            Balance = int(input('Enter Your Balance : '))
            with open('ATM_User_Records.txt', 'r') as tempfile:
                flag = False
                for line in tempfile:
                    st = line.split('\t\t')
                    if Acc_Num == st[0]:
                        flag = True
            tempfile.close()
            if not flag:
                if len(Password) <= 4:
                    if Balance <= 100000:
                        file.write(Acc_Num + '\t\t' +
                                    Password + '\t\t' + str(Balance) + '\n')
                    else:
                        print('Budget exceeded')
                else:
                    print('Password Must be 4 Numbers OR Less!!')
            else:
                print('Account Number is ALREADY EXIST!!!')
            c = input('Do you want to Enter Another Account? (y / n): ')
        print('Operation Completed Successfully!')


def ReadRecord():
    with open('ATM_User_Records.txt', 'r') as file:
        print('Account Number\tPassword\tBalance')
        for line in file:
            print(line, end='')


def SearchRecord():
    id = input('Enter Your Account Number: ')
    password = input('Enter The Correct Password: ')
    found = False
    found_pass = False
    with open('ATM_User_Records.txt' , 'r') as file:
        for line in file:
            user = line.split('\t\t')
            if id == user[0]:
                found = True
                if password == user[1]:
                    found_pass = True
                    print('Account Number\tBalance')
                    print(user[0] + '\t\t' + user[2] , end='')
                    break
        if not found:
            print('Account number not found')
        elif not found_pass:
            print('Incorrect password')


def DeleteRecord():
    import os
    Acc_Num = input('Enter Account You want to Delete: ')
    password = input('Enter your Password: ')
    file = open('ATM_User_Records.txt', 'r')
    tempfile = open('Temp_ATM_User_Records.txt', 'w')
    found = False
    for line in file:
        user = line.split('\t\t')
        if user[0] == Acc_Num:
            if user[1] == password:
                found = True
            else:
                print('Incorrect password!')
                return
        else:
            tempfile.write(line)
    if not found:
        print('Account not found!')
        return
    file.close()
    tempfile.close()
    os.remove('ATM_User_Records.txt')
    os.rename('Temp_ATM_User_Records.txt', 'ATM_User_Records.txt')
    print('Account deleted successfully!')



def UpdateRecord():
    import os
    Acc_num = input('Enter your Account Number: ')
    password = input('Enter your Password: ')
    flag = False
    file = open('ATM_User_Records.txt', 'r')
    tempfile = open('Temp_ATM_User_Records.txt', 'w')
    for line in file:
        st = line.split('\t\t')
        if Acc_num == st[0]:
            if password == st[1]:
                flag = True
                balance = int(st[2])
                operation = input('the operation (1: deposit, 2: withdraw): ')
                if operation == "1":
                    amount = int(input('Enter the deposit amount: '))
                    balance += amount
                    if balance <= 100000:
                        line = str(Acc_num) + '\t\t' + \
                            str(password) + '\t\t' + str(balance) + '\n'
                    else:
                        print("Budget exceeded! please don't exceed 100000")
                elif operation == "2":
                    amount = int(input('Enter the withdrawal amount: '))
                    if amount <= balance:
                        balance -= amount
                        line = str(Acc_num) + '\t\t' + \
                            str(password) + '\t\t' + str(balance) + '\n'
                    else:
                        print("Insufficient balance")
        tempfile.write(line)
    file.close()
    tempfile.close()
    os.remove('ATM_User_Records.txt')
    os.rename('Temp_ATM_User_Records.txt', 'ATM_User_Records.txt')
    if flag:
        print('thank you')
    else:
        print('you entered Invalid Account_Number or Password')


def Home():
    c = 'y'
    while c == 'y':
        print('1: To add new Account.')
        print('2: To read all Accounts.')
        print('3: To search for Account.')
        print('4: To update an Account.')
        print('5: To delete an Account.')
        c = input('Your Choice: ')
        if c == '1':
            WriteRecord()
        if c == '2':
            ReadRecord()
        if c == '3':
            SearchRecord()
        if c == '4':
            UpdateRecord()
        if c == '5':
            DeleteRecord()
        c = input('Perform another operation (y / n): ')


Home()
