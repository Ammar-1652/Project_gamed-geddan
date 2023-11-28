from abc import ABC, abstractmethod
from datetime import datetime
class Person():
    def __init__(self,f_name="N/A",m_name="N/A",l_name="N/A",personal_id=0,contact_num=0,email="N/A",profile_approved=False,date_of_birth="0"):
        #assign values
        self.first_name=f_name
        self.middle_name=m_name
        self.last_name=l_name
        self.personal_id=personal_id
        self.contact_num=contact_num
        self.email=email
        self.profile_approved=profile_approved
        self.date_of_birth=date_of_birth
        #handling errors of age variable (but it working now don't worry just use it)
        if self.date_of_birth!="0":
            self.age=self.calc_age()
        else:
            self.age=0
        
    
    def generate_id(self):
        pass
    
    def view_profile():
        pass
    
    #==========setters & getters=========
    
    #===========f-name===========
    def set_first_name(self,f_name):
        self.first_name=f_name
    
    def get_first_name(self):
        return self.first_name
    #=============================
    
    #=========m-name=============
    def set_middle_name(self,m_name):
        self.middle_name=m_name
    
    def get_middle_name(self):
        return self.middle_name
    #===========================
    
    #========l-name=============
    def set_last_name(self,l_name):
        self.last_name=l_name
    
    def get_last_name(self):
        return self.last_name
    #===========================
    
    #=========personal_id=========
    def set_personal_id(self,personal_id):
        self.personal_id=personal_id
    
    def get_personal_id(self):
        return self.personal_id
    #===========================
    
    #========contact_num=========
    def set_contact_num(self,contact_num):
        self.contact_num=contact_num
    
    def get_contact_num(self):
        return self.contact_num
    #==============================
    
    #==========e-mail=============
    def set_email(self,email):
        self.email=email
    
    def get_email(self):
        return self.email
    #===============================
    
    #=========profile_approved========
    def get_profile_approved(self):
        return self.profile_approved
    #==================================
    
    #===========date_of_birth==========
    def set_date_of_birth(self,date_of_birth:str):
        self.date_of_birth=date_of_birth
    
    def get_date_of_birth(self):
        return self.date_of_birth
    #=====================================
    
    def calc_age(self):
        today = datetime.now()
        birthdate= datetime.strptime(str(self.get_date_of_birth()), '%d/%m/%Y')
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

#================================End of Person class==============================================


class Student(Person):
    Student_count=0
    def __init__(self,f_name="N/A",m_name="N/A",l_name="N/A",personal_id=0,contact_num=0,email="N/A",profile_approved=False,date_of_birth=0,level=0,department="N/A"):
        #assign values
        super().__init__(f_name,m_name,l_name,personal_id,contact_num,email,profile_approved,date_of_birth)
        self.level=level
        self.department=department
        
        
        
class Instructor(Person):
    def __init__(self,f_name="N/A",m_name="N/A",l_name="N/A",personal_id=0,contact_num=0,email="N/A",profile_approved=False,date_of_birth=0,salary=0,department="N/A"):
        #assign values
        super().__init__(f_name,m_name,l_name,personal_id,contact_num,email,profile_approved,date_of_birth)
        self.salary=salary
        self.department=department
        
        
        
class Admin(Person):
    profile_approved=True
    def __init__(self,f_name="N/A",m_name="N/A",l_name="N/A",personal_id=0,contact_num=0,email="N/A",profile_approved=False,date_of_birth=0):
        super().__init__(f_name,m_name,l_name,personal_id,contact_num,email,profile_approved,date_of_birth)
        
        
        
class Professor(Instructor):
    professor_count=0
    def __init__(self,f_name="N/A",m_name="N/A",l_name="N/A",personal_id=0,contact_num=0,email="N/A",profile_approved=False,date_of_birth=0,salary=0,department="N/A",courses_teaching={}):
        #assign values
        super().__init__(f_name,m_name,l_name, personal_id, contact_num, email, profile_approved, date_of_birth, salary, department)
        self.courses_teaching=courses_teaching
        Professor.professor_count+=1
        
        
class Professor_asst(Instructor):
    professor_asst_count=0
    def __init__(self,f_name="N/A",m_name="N/A",l_name="N/A",personal_id=0,contact_num=0,email="N/A",profile_approved=False,date_of_birth=0,salary=0,department="N/A",labs_teaching={}):
        #assign values
        super().__init__(f_name,m_name,l_name, personal_id, contact_num, email, profile_approved, date_of_birth, salary, department)
        self.labs_teaching=labs_teaching
        Professor_asst.professor_asst_count+=1
        
        
        
        
        
        
        
        
        

class Courses():
    courses_num=0
    labs_num=0
    def __init__(self,course_name,course_hours,is_with_lab=False):
        #assign values
        self.course_name=course_name
        self.course_hours=course_hours
        self.is_wih_lab=is_with_lab
        Courses.courses_num+=1
        Courses.labs_num+=self.is_wih_lab
        
        

























