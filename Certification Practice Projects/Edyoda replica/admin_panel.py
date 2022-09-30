import random
import json
from trainers import *
from student import *
class Admin_Panel:
    student_list = []
    def __init__(self):
        self.module_details = {}
        self.trainer_details = {}
        self.student_details = {}
        self.batch_details = {}
        
    def admin_login(self,username,password):
        if username == "admin" and password == "admin":
            return True
        return False

    def add_module(self,module_name,duration):
        topic_list = []
        key = random.randint(1,100)

        topic_size = int(input("Enter the number of topics you want to add : "))
        for i in range(topic_size):
            topic =  input("Enter topic name : ")
            topic_list.append(topic)

        module_data = {
            "module_name" : module_name,
            "duration" : duration,
            "topics" : topic_list
        }
        self.module_details[key] = module_data
        with open("add_module.json","w") as f:
            json.dump(self.module_details,f)
        if self.module_details[key]:
            return True
        return False

    def add_trainer(self):
        key = random.randint(1,100)
        trainer_ID = random.randint(1,100)
        name = input("Enter Trainer name : ")
        gender = input("Enter Trainergender : ")
        qualification = input("Enter Trainer qualification : ")
        experience = input("Enter Trainer experience : ")
        mobile_no = input("Enter Trainer mobile_no : ")
        email_ID = input("Enter Trainer email_ID : ")
        password=input("Enter the password")
        self.trainer_data = {
            "Trainer_id":trainer_ID,
            "name":name,
            "gender":gender,

            "qualification":qualification,
            "experience":experience,
            "mobile_no":mobile_no,
            "email_Id":email_ID,
            "password":password
        }
        self.trainer_details[key] = self.trainer_data
        with open("add_trainer.json","w") as f:
            json.dump(self.trainer_details,f)
        if self.trainer_details[key]:
            return True
        return False

    def add_student(self):
        key = random.randint(1,100)
        student_size = int(input("Enter the number of students you want to add : "))
        for i in range(1,student_size+1):
            print(f"\n Enter the details for student {i} : \n")
            name = input("Enter student name : ")
            gender = input("Enter student gender : ")
            age = input("Enter student age : ")
            qualification = input("Enter student qualification : ")
            experience = input("Enter student experience : ")
            mobile_no = input("Enter student mobile_no : ")
            email_ID = input("Enter student email_ID : ")
            password = input("Enter student password : ")
            student = {
                "name":name,
                "gender":gender,
                "age":age,
                "qualification":qualification,
                "experience":experience,
                "mobile_no":mobile_no,
                "email_Id":email_ID,
                "password":password


            }
            Admin_Panel.student_list.append(student)
            print()
        
        self.student_details[key] = Admin_Panel.student_list
        print(self.student_details)
        if self.student_details[key]:
            return True
        return False
    
    def add_batch(self,module_key,trainer_key,student_key):
        key=random.randint(1,100)
        batch_data={
            "module_key":module_key,
            "trainer_key":trainer_key,
            "student_key":student_key
        }
        self.batch_details[key] = batch_data
        if self.batch_details[key]:
            return True
        return False
    
    def get_module(self):
        return self.module_details

    def get_trainer(self):
        count=0
        for k,v in self.trainer_details.items():
            count+=1
            print("Total Trainers are,",count,"\n")
            print(k," ",v,"\n")

    def get_student(self):
        count=0
        for k,v in self.student_details.items():
            for i in v:
                count+=1
                print("Total Student Count Details ",count,"\n")
                print(i,"\n")
    
    def get_batch(self):
        return  self.batch_details

    def remove_batch(self):
        for k,v in self.module_details.items():
            print(k,"------",v,"\n")
        module_code=int(input("Enter the Module that you want to remove"))
        self.module_details.pop(module_code)
        print("Successfully Deleted The Module!!!!!!!!! \n")
        for k,v in self.module_details.items():
            print(k,"------",v,"\n")
    
    def edit_trainer(self):
        for k,v in self.trainer_details.items():
            print(v.getID(),"----",v)
        trainer_code=int(input("Enter the Trainers code which you want to edit"))
        for k,v in self.trainer_details.items():
            if v.getID()==trainer_code:
                name = input("Enter Trainer name : ")
                gender = input("Enter Trainergender : ")
                qualification = input("Enter Trainer qualification : ")
                experience = input("Enter Trainer experience : ")
                mobile_no = input("Enter Trainer mobile_no : ")
                email_ID = input("Enter Trainer email_ID : ")
                v.set_name(name)
                v.set_gender(gender)
                v.set_qualification(qualification)
                v.set_experience(experience)
                v.set_mobile_no(mobile_no)
                v.set_email_ID(email_ID)
        print("Trainers Data is Updated Successfully......\n")
        for k,v in self.trainer_details.items():
            print(v.getID(),"----",v,"\n")






