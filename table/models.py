from django.db import models

# Create your models here.
class Teacher(models.Model):
      T_id=models.IntegerField(primary_key=True)
      T_name=models.CharField(max_length=100 )
class Course(models.Model):
    c_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=100,null=True )
    T_id=models.ForeignKey(Teacher,on_delete=models.CASCADE) 
    
