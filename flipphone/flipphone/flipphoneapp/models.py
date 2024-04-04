from django.db import models

# Create your models here.
class category(models.Model):
    name= models.CharField(max_length=250,unique = True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'categories'
        verbose_name_plural = 'categories'

class register_table(models.Model):
    nam=models.CharField(max_length=20)
    eml=models.EmailField()
    pas=models.CharField(max_length=20)

class product_tbl(models.Model):
    product_name=models.CharField(max_length=80)
    c_name=models.CharField(max_length=30,null=True)
    stock=models.IntegerField(null=True)
    product_image=models.FileField(upload_to='picture')
    product_price=models.IntegerField()
    product_des=models.TextField(null=True)
    product_build=models.TextField(null=True)
    product_Ram=models.TextField(null=True)
    product_Rom=models.TextField(null=True)
    product_Display=models.TextField(null=True)
    product_Operatingsystem=models.TextField(null=True)
    product_Processor=models.TextField(null=True)
    product_Battery=models.TextField(null=True)
    product_connectivity=models.TextField(null=True)
    product_camera=models.TextField(null=True)
    
    
    
    def __str__(self):
        return self.product_name
    
class brand(models.Model):
    name = models.CharField(max_length=250,unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'brands'
        verbose_name_plural = 'brands'
    def __str__(self):
        return'{}'.format(self.name)
        