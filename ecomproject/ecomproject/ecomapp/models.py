from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(max_length=250,unique=True)
    image=models.ImageField(upload_to='Category')
    class Meta:
        ordering = ('name',)
        verbose_name='Category'
        verbose_name_plural='Categories'

    def get_url(self):
        return reverse('ecomapp:product_by_category', args=[self.slug])

    def __str__(self):
      return '{}'.format(self.name)




class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(max_length=250, unique=True)
    image = models.ImageField(upload_to='Product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    avaiable=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    class Meta:
        ordering = ('name',)
        verbose_name='Product'
        verbose_name_plural='Products'

    def get_url(self):
        return reverse('ecomapp:prodCatdetail',args=[self.category.slug, self.slug])

    def __str__(self):
      return '{}'.format(self.name)
