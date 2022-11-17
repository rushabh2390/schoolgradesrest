from django.db import models

# Create your models here.


class User(models.Model):
    name = models.EmailField(max_length=300)
    password = models.CharField(max_length=200)

    class Meta:
        abstract = True

    @staticmethod
    def get_user_for_login(email,password):
        try:
            return User.objects.get(userEmail = email,userPwd = password)
        except:
            return False
    
    @staticmethod
    def get_user(email):
        try:
            return User.objects.get(userEmail = email)
        except:
            return False
            
    @staticmethod
    def is_duplicate(email):
        try:
            return User.objects.get(userEmail = email)
        except:
            return False
