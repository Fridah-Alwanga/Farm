from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Admin(models.Model):
    username = models.CharField(max_length=100, blank =True )
    bio = models.TextField(max_length=300,blank =True)
    user = models.OneToOneField(User, on_delete = models.CASCADE , related_name='admin')
    email = models.CharField(max_length=100, default = '')
    location = models.CharField(max_length=100,blank =True)
    admin_pic = models.ForeignKey("Admin",on_delete=models.CASCADE, default='', null=True, blank=True)
    admin_pic = models.ImageField( upload_to='admin/', blank ='true',default='default.png')

    def __str__(self):
     return f'{self.user.username} Admin'

    def save_admin(self):
        self.save
    
    def delete_user(self):
        self.delete()

@receiver(post_save, sender=User)
def create_user_admin(sender, instance, created, **kwargs):

    if created:
        Admin.objects.create(user=instance)
    


class Farmers(models.Model):
    name = models.CharField(max_length=50)
    location= models.CharField(max_length=60)
    farmers = models.ForeignKey("Farmers",on_delete=models.CASCADE, related_name = 'farmer')
    description = models.TextField( default = '')
    farmers_logo = models.ImageField( upload_to='images/', blank ='true',default='')
    emergency_contact=models.CharField(max_length=100,null=True, blank=True)
    occupants_count = models.IntegerField(null  = True ,blank = True)
    

    def __str__(self):
        return f'{self.name} farmers'


    def save_farmers(self):
        self.save()

    def delete_farmers(self):
        self.delete()



class Suppliers(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')
    email = models.CharField(max_length=100, default = '')
    farmers = models.ForeignKey("Farmers",on_delete=models.CASCADE, default='', null=True, blank=True)
    description = models.TextField( default = '')



    def __str__(self):
        return f'{self.name} suppliers'


    def save_suppliers(self):
        self.save()

    def delete_suppliers(self):
        self.delete()

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')
    date = models.DateField(auto_now_add=True)
    farmers = models.ForeignKey("Farmers",on_delete=models.CASCADE, default='', null=True, blank=True)
    

    @classmethod
    def farmer_post(cls,id):
        farmerpost = Post.objects.filter(farmer = id)
        return farmerpost
    
    def __str__(self):
        return f'{self.title} Post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()