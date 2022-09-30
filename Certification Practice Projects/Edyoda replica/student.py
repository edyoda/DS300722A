class Student:
    def __init__(self,ID,name,gender,age,qualification,experience,mobile_no,email_ID,password):
        self.ID = ID
        self.name = name
        self.gender = gender
        self.age = age
        self.qualification = qualification
        self.experience = experience
        self.mobile_no = mobile_no
        self.email_ID = email_ID
        self.password = password

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self,gender):
        self.gender = gender

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age
    
    def get_qualification(self):
        return self.qualification

    def set_qualification(self,qualification):
        self.qualification = qualification

    def get_experience(self):
        return self.experience

    def set_experience(self,experience):
        self.experience = experience

    def __str__(self):
        return f"Name : {self.name} \nGender : {self.gender} \nAge : {self.age} \nQualification : {self.qualification} \nExperience : {self.experience} \nMobile No : {self.mobile_no} \nEmail ID : {self.email_ID}"
        