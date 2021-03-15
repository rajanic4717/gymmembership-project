from members import GymMembership

obj = GymMembership()
while True:
    type_of_user = input('Enter Member / Superuser :')
    if type_of_user == 'member':
        print("1- my regimen")
        print("2- my profile")
        options=input("choose option :")
        if options=="1":
            obj.view_regimen()
        elif options=="2":
            obj.view_member()
    elif type_of_user == 'superuser':
        while True:
            print('Choose the option')
            print('1 - create new member')
            print("2 - view member")
            print('3 - delete member')
            print('4 - update member')
            print("5 - create regimen")
            print('6 - view regimen')
            print('7 - delete regimen')
            print('8 - update regimen')
            print("0 - exit ")
            key = int(input("Enter the option :"))
            if key == 1:
                obj.create_member()
            elif key == 2:
                obj.view_member()
            elif key == 3:
                obj.delete_member()
            elif key == 4:
                obj.update_member()
            elif key == 5:
                obj.create_regimen()
            elif key == 6:
                obj.view_regimen()
            elif key == 7:
                obj.delete_regimen()
            elif key == 8:
                obj.update_regimen()
            elif key ==0:
                break
    elif type_of_user == "exit":
        break
