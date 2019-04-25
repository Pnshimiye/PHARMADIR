from django.db import models

class Pharmacy(models.Model):
    name = models.CharField(max_length = 100)
    area = models.CharField(max_length=50)     
    longitude = models.IntegerField() 
    latitude = models.IntegerField() 
    image = models.ImageField(upload_to='')
    phone_number = models.IntegerField()
    email_address = models.EmailField() 


    def save_pharmacy(self):
        self.save()  

    @classmethod
    def update_pharmacy(cls, update):
        pass
 
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
  

 
  

 

     
