class GymMembership:
    global catalog
    catalog = {}
    global data
    data = {}


    def create_member(self):
        global catalog
        global data
        print("*******welcome to Gym*******")
        data = {}
        name = input("Enter full name :")
        age = input('Enter age :')
        gender = input('Gender :')
        mobile_no = input("Enter your mobile no :")
        email = input("Enter your Email :")
        BMI = input("enter your BMI :")
        membership_duration = int(input('enter membership_duration 3/6/9/12 :'))
        data['name'] = name
        data['age'] = age
        data['gender'] = gender
        data['mobileno'] = mobile_no
        data['email'] = email
        data['BMI'] = BMI
        data['membership_duration'] = membership_duration
        if data['BMI'] < str(18.5):
            data['regimen'] = {'mon': "chest", "tue": "biceps", "wed": "rest", 'thu': "back", "fri": "triceps",
                               "sat": "rest", "sun": "rest"}
        elif data['BMI'] < str(25):
            data['regimen'] = {'mon': "chest", "tue": "biceps", "wed": "cardio/abs", 'thu': "back", "fri": "triceps",
                               "sat": "legs", "sun": "rest"}
        elif data['BMI'] < str(30):
            data['regimen'] = {'mon': "chest", "tue": "biceps", "wed": "cardio/abs", 'thu': "back", "fri": "triceps",
                               "sat": "legs", "sun": "cardio"}

        elif data['BMI'] > str(30):
            data['regimen'] = {'mon': "chest", "tue": "biceps", "wed": "cardio", 'thu': "back", "fri": "triceps",
                               "sat": "cardio", "sun": "cardio"}
        catalog[mobile_no] = data
        print("created succesfully")

    def view_member(self):
        global catalog
        mobile_no = input("enter mobile no")
        if mobile_no in catalog and "regimen" in catalog[mobile_no]:
            print("name     -", (catalog[mobile_no]['name']))
            print("age      -", (catalog[mobile_no]['age']))
            print("gender   -", (catalog[mobile_no]['gender']))
            print("mobileno -", (catalog[mobile_no]['mobileno']))
            print("email    -", (catalog[mobile_no]['email']))
            print("BMI      -", (catalog[mobile_no]['BMI']))
            print("membership duration  -", (catalog[mobile_no]["membership_duration"]))
        else:
            print("not found")

    def delete_member(self):
        global catalog
        mobile_no = input("enter mobile no")
        if mobile_no in catalog:
            del catalog[mobile_no]
            print("deleted succesfully")

    def update_member(self):
        global catalog
        mobile_no = input("enter mobile no")
        if mobile_no in catalog:
            print("membership duration-", (catalog[mobile_no]["membership_duration"]))
            while True:
                ask1 = input("you want to revoke or extend membership :")
                if ask1 == "revoke":
                    catalog[mobile_no]['membership_duration'] = 0
                    print('*update done*')
                    break
                if ask1 == "extend":
                    new = int(input("enter the extended duration :"))
                    catalog[mobile_no]['membership_duration'] +=new
                    print(' update done')
                    break


    def create_regimen(self):
        global catalog
        mobile_no = input("enter mobile number")
        new_regimen = {}
        new_regimen['mon'] = input("enter monday workout")
        new_regimen['tue'] = input("enter tuesdays workout")
        new_regimen['wed'] = input("enter wednesdays workout")
        new_regimen['thu'] = input("enter thrusdays workout")
        new_regimen['fri'] = input("enter fridays workout")
        new_regimen['sat'] = input("enter saturdays workout")
        new_regimen['sun'] = input("enter sundays workout")
        if mobile_no in catalog:
            catalog[mobile_no]['regimen'] = new_regimen
            print("created regimen succesfully")

    def view_regimen(self):
        global catalog
        mobile_no = input("enter mobile no")
        if mobile_no in catalog:
            if "regimen" in catalog[mobile_no]:
                for i in catalog[mobile_no]['regimen']:
                    print(i,catalog[mobile_no]['regimen'][i])
            else:
                print("regimen not found")
        else:
            print("no regimen found")

    def delete_regimen(self):
        global catalog
        mobile_no = input("enter mobile no")
        if mobile_no in catalog:
            del catalog[mobile_no]['regimen']
            print("deleted sucesfully")

    def update_regimen(self):
        global catalog
        mobile_no = input("enter your mobile no")
        change_day = input("enter the  day")
        if mobile_no in catalog:
            catalog[mobile_no]['regimen'][change_day] = input("enter workout")
            print('updated regimen  succesfullu')
