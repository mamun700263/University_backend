from django.contrib.auth.models import User
from django.db import models
import uuid
from django.utils import timezone
from datetime import date
# from Departments.models import Batch
# from Departments.models import Department
class Account(models.Model):
    """
    This Account class is the base of all accounts 
    here the arguments are
    user = it strore the acounts user and as a one to one field
    data_of_birth = users birth date
    unique_id = for everry user we gonna hava a unique id . and it will be easy for any to just look at the id and you can tell his/her proffession
    bio = a little informations about the user
    mobeile = users mobile phone . as i am in bangladesh all numbers lenght 11 digis so the max leangth is 11, it can't be less than this
    profile_picture = if the user gives a profile else there will be default profile photo
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    username = models.CharField(max_length=50,unique=True,default="username")
    email = models.EmailField(null=False,blank=False,default="user@gmail.com")
    first_name = models.CharField(max_length=50,null=False,blank=False,default="name")
    last_name = models.CharField(max_length=50,null=False,blank=False,default="name")
    
    date_of_birth = models.DateField(blank=True, null=True,default=date(1000,1,1))
    unique_id = models.CharField(unique=True,  max_length=11,null=True,blank=True)
    bio = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True,default="https://i.ibb.co.com/zHJyw5w/User-Profile-PNG-Clipart.png")  

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """
        As we are using it as a one to one relations ship with the USER that't why when some one will try to create an account that will first
        come here to check is there is any user with this name or nao. if there then it will give a error message then. else we it will create accont with the users informations
        """
        if not self.user_id:
            self.user = User.objects.create(
                username=self.username,
                email=self.email,
                first_name=self.first_name,
                last_name=self.last_name,
            )
            self.user.set_password(self.password)
            self.user.save()
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        """
        sub classes will create the unique ids
        """
        raise NotImplementedError("Subclasses should implement this method.")







class StudentAccount(Account):
    """
    this function will create an unique id for each student . the first 2 characters (ST )denote that it is the uid of strudent 

    department
    batch
    section
    student_id
    cgpa
    previoush cgpas
    """
    Class_Representetive = models.BooleanField(default=False)
    batch = models.ForeignKey("Departments.Batch", verbose_name="Batch", on_delete=models.CASCADE)
    def generate_unique_id(self):
        return f"ST-{uuid.uuid4().hex[:8].upper()}"

class TeacherAccount(Account):
    Department_head = models.BooleanField(default=False)
    def generate_unique_id(self):
        return f"TE-{uuid.uuid4().hex[:8].upper()}"


class StaffAccount(Account):
    def generate_unique_id(self):
        return f"OF-{uuid.uuid4().hex[:8].upper()}"
class AuthorityAccount(Account):
    def generate_unique_id(self):
        return f"AU-{uuid.uuid4().hex[:8].upper()}"