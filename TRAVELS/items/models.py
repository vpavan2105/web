from django.db import models

# Create your models here.
class agencies(models.Model):
    agency=models.CharField(max_length=225)
    rating=models.IntegerField()
    def __str__(self):
        return str(self.agency)
       
class destination(models.Model):
    name=models.ForeignKey(agencies,on_delete=models.CASCADE,max_length=225)       
    destination_id=models.IntegerField()
    travel=models.TextField()
    agency_id=models.IntegerField()
    
    def __str__(self):
        return str(self.destination_id)
    
class booking(models.Model):
    name=models.CharField(max_length=225)
    email=models.EmailField()
    phone_number=models.IntegerField()
    
    Destination_id=models.IntegerField(default=None)
    total_memebers=models.IntegerField()
    vehicle_choices=[
        ('suv','SUV'),
        ('Hatchback','HATCHBACK'),
        ('minivan','MINIVAN'),
        ('jeep','JEEP'),
    ]
    vehicle_type=models.CharField(max_length=50,choices=vehicle_choices)
    date=models.DateField()
    no_of_days=models.IntegerField()
    staying_type=[
        ('hotel','HOTEL'),
        ('vacation rentals','VECATION RENTALS'),
        ('resorts','RESORTS'),
        ('camping','CAMPING'),   
    ]
    residency1=models.CharField(max_length=50,choices=staying_type)
    residency2=models.CharField(max_length=50,choices=staying_type,null=True)
    def __str__(self):
        return str(self.date.strftime('%Y-%m-%d'))
    
    
    
        