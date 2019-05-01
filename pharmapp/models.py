from django.db import models
from django.contrib.auth.models import User

class Pharmacy(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    area = models.CharField(max_length=50)     
    # location = GIS.PointField()
    image = models.ImageField(upload_to='')
    phone_number = models.IntegerField()
    email_address = models.EmailField() 

    def __str__(self):
        return self.name

    def save_pharmacy(self):
        self.save()

    def delete_pharmacy(self):
        self.delete()

    @classmethod
    def get_by_id(cls):
        pharmacy = cls.objects.get(user=id)
        return pharmacy
 
    def update_pharmacy(self,bio):
        self.pharmacy = pharmacy
        self.save()
        
class Insurance(models.Model):
    name = models.CharField(max_length=50)  
    pharmacy = models.ManyToManyField(Pharmacy)

    # class Meta:
    #     ordering = ('name')

class Med_category(models.Model):
     name = models.CharField(max_length=50)  


class Medicine(models.Model):
    name = models.CharField(max_length=50)  
    med_category = models.ForeignKey(Med_category,on_delete=models.PROTECT)
    price = models.IntegerField()

    # class Meta:
    #     ordering = ('name',)

    def save_medecine(self):
        self.save()
    
    @classmethod
    def update_price(cls, update):
        pass  
  

 
  

 

     
