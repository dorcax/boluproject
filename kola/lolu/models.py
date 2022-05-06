from django.db import models
from django.contrib.auth.models import User

# Create your models here.



CATEGORY=(
    ('stationary','stationary'),
    ('electronics','electronics'),
    ('food','foods'),
)
#class Tag(models.Model):
    #name=models.CharField(max_length=100,null=True)

class product(models.Model):
    name=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity=models.IntegerField (null=True)
    #tags= models.ManyToManyField(Tag)
    class Meta:
        verbose_name_plural='product'



    def __str__(self):
        return f'{self.name} = {self.quantity}'

class staff(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=20,null=True)
    phone=models.IntegerField (null=True)    



class Order(models.Model):
    status=(
        ('pending','pending'),
        ('delivered','delivered'),
        ('out for delivery','out for delivery'),

    )
    
    product= models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    staff= models.ForeignKey(User,models.CASCADE,null=True)
    quantity= models.PositiveIntegerField(null=True)
    date= models.DateTimeField(auto_now_add=True) 
    status=models.CharField(max_length=200,choices=status,null=True)    
    class Meta:
        verbose_name_plural='Order'
    def __str__(self):
          return f'{self.product}ordered by {self.staff.username}' 