from django.db import models
from django.contrib.auth.models import User  
from django.db.models import Q


class Pharmacy(models.Model):
    name = models.CharField(max_length = 100)
    area = models.CharField(max_length=50)     
    longitude = models.FloatField() 
    latitude = models.FloatField()  
    image = models.ImageField(upload_to='')
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField() 
    user= models.OneToOneField(User,on_delete=models.CASCADE)

    


    def save_pharmacy(self):
        self.save()

    @classmethod
    def get_by_id(cls, id): 
        pharmacy = Pharmacy.objects.get(user = id)
        return pharmacy


    @classmethod
    def update_pharmacy(cls, update):
        pass

    
    @classmethod
    def get_pharmacy_medicines(cls,pharmacy):        
        medicines = Medicine.objects.filter(pharmacy__pk = pharmacy)
        return medicines
    
    @classmethod
    def get_pharmacies_with_medicine(cls,medicine):
        pharmacy = Pharmacy.objects.filter(id=medicine)
        return pharmacy

 


class Insurance(models.Model):
    name = models.CharField(max_length=50)  
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.CASCADE) 


    def save_insurances(self):
        self.save()
    
    @classmethod
    def update_insurance(cls, update):
        pass  

    @classmethod
    def get_pharmacy_insurances(cls,pharmacy):        
        insurances = Insurance.objects.filter(pharmacy__pk = pharmacy)
        return insurances
  

    

class Med_category(models.Model):
     name = models.CharField(max_length=50)  
    

class Medicine(models.Model):
    name = models.CharField(max_length=50)  
    med_category = models.CharField(max_length=50)  
    price = models.IntegerField()
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.CASCADE) 
    in_stock = models.BooleanField(default=True)

    

 

    def save_medecine(self):
        self.save()
    
    @classmethod
    def update_price(cls, update):
        pass  


   

  



class Request(models.Model):    
    Pharmacy_name = models.CharField(max_length=50) 
    Prefered_username = models.CharField(max_length=50) 
    Licence_document = models.ImageField(upload_to='')
    Pin_number = models.IntegerField()
    Contact_name = models.CharField(max_length=50) 
    Contact_Email = models.EmailField() 
    Contact_phone_number = models.IntegerField()
    Address = models.CharField(max_length=50) 
    Request_date = models.DateTimeField(auto_now_add=True)


    def save_request(self):
        self.save()
    
  

class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                         Q(description__icontains=query)|
                         Q(slug__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

    
class Post(models.Model):
    # user            = models.ForeignKey(settings.AUTH_USER_MODEL)
    title           = models.CharField(max_length=120)
    description     = models.TextField(null=True, blank=True)
    slug            = models.SlugField(blank=True, unique=True)
    publish_date    = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    
    objects         = PostManager()

 
  

 

     
