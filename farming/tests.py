from django.test import TestCase
from .models import Admin,Farmers, Suppliers
from django.contrib.auth.models import User
# Create your tests here.




class AdminTest(TestCase):
    def setUp(self):
        self.fridah = User(username = 'fridah',email = 'fridah@gmail.com')
        self.fridah = Admin(user = Self.fridah,user_id = 1,bio = 'farm', email='test@gmail.com',profile_pic = 'image.jpg',location='Nairobi', neighbourhood='caren')

    def test_instance(self):
        self.assertTrue(isinstance(self.fridah,Admin))

    def test_save_Admin(self):
        self.save_admin()
        all_admins = Admin.objects.all()
        self.assertTrue(len(all_Admins),0)

    def test_delete_admin(self):
        self.fridah.delete_admin()
        all_admins = Admin.objects.all()
        self.assertEqual(len(all_admins),0)



class FarmersTestCase(TestCase):
    def setUp(self):
        self.new_ farmers= Project(name ='caren',location = 'Nairobi',image = 'trial.jpg',description = 'I like your my farm',user = fridah,farm_logo= 'logo.jpeg', emergency_contact= '911',occupants_count ='10')


    def test_save_image(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        image_list = Image.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.image.save_image()
        all_images = Image.get_all_images()
        self.assertTrue(len(all_pictures) < 1)

    def test_get_one_image(self):
        self.food.save_image()
        one_pic = Image.get_one_image(self.food.id)
        self.assertTrue(one_pic.name == self.picture.name)



class SuppliersTestCase(TestCase):
    self.new_ farm= Project(name = 'company',user = 'fridah',email = 'test@gmail',farm = 'Nairobi',descrption='This Farm')


    def test_save_image(self):
        self.name.save_name()
        name = Suppliers.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.name.save_image()
        self.name.delete_image()
        image_list = Suppliers.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.name.save_name()
        all_names = Suppliers.get_all_images()
        self.assertTrue(len(all_names) < 1)

    def test_get_one_image(self):
        self.food.save_image()
        one_name = Suppliers.get_one_name(self.food.id)
        self.assertTrue(one_name.name == self.name.name)


