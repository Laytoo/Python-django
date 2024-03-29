from django.db import models

# Create your models here.
class Category(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    parentid=models.IntegerField()
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)
    image=models.ImageField()
    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    STATUS =(
        (1, 'True'),
        (0, 'False'),
    )
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)
    image=models.ImageField(upload_to='images/')
    price=models.FloatField()
    amount = models.IntegerField()
    detail=models.TextField()

    status=models.IntegerField(choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title