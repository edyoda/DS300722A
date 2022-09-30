from admin_panel import *
class Main:
    def __init__(self,admin):
        self.admin=admin
    
    def execute(self,choice):
        if choice==1:
            print("************Admin Login*************")
            username=input("Enter Admin Username : ")
            password=input("Enter Admin Password : " )
            flag=self.admin.admin_login(username,password)
            if flag:
                print("Logged in Successfully!..")
                while True:
                    choice=int(input("Enter \n1.Add Module \n2.Add Trainer \n3.Add Student \n4.Add Batch \n5.View Module \n6.View Trainer \n7.View Student \n8.View Batch \n9.Remove Module \n10.Update Trainers Profile \n" ))
                    if choice==1:
                        print("Add Module".center(50,"*"))
                        module_name=input("Enter the Module Name\n")
                        duration=input("Enter the Duration of the module\n")
                        temp=self.admin.add_module(module_name,duration)
                        if temp:
                            print("Module Added Succesfully")
                        else:
                            print("Something went wrong")
                    if choice==2:
                        print("Add Trainer Module".center(50,"*"))
                        temp=self.admin.add_trainer()
                        if temp:
                            print("Trainer Added Succesfully")
                        else:
                            print("Something went wrong")
                    
                    if choice==3:
                        print("Add Student Module".center(50,"*"))
                        temp=self.admin.add_student()
                        if temp:
                            print("Student Added Succesfully")
                        else:
                            print("Something went wrong")

            else:
                print("Invalid Crediantels")


if __name__=="__main__":
    Admin=Admin_Panel()
    main=Main(Admin)
    while True:
        choice=int(input("Login as : \n1.Admin Login \n2.Trainer Login \n3.Student Login \n4.Exit \n"))
        main.execute(choice)
        break