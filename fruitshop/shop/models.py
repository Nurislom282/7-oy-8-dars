from django.core.validators import FileExtensionValidator
from django.db import models

class Ctegory(models.Model):
    name = models.CharField(max_length=150,unique=True,verbose_name="Category name")
    slug = models.SlugField(max_length=100,unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class Subcategory(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name="hillarni kiriting")
    category = models.ForeignKey(Ctegory,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100,unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tur"
        verbose_name_plural = "turlar"


class Product(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name="produt nomini kiriting")
    description = models.TextField(null=True,blank=True,verbose_name="product haqida malumot kiriting")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="narxi",default=10)
    quantity = models.SmallIntegerField(verbose_name="Ombordagi soni",default=100)
    weight = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="ogirligi",default=10)
    category = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Productlar"

class ProductImg(models.Model):
    img = models.ImageField(upload_to='product/images/')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='productimgset')

    def __str__(self):
        return str(self.product.pk)

class ProductVidio(models.Model):
    video = models.FileField(upload_to="post/videos/", validators=[
        FileExtensionValidator(['mp4', 'avi'], message="Faqat mp4 va avi formatidagilarni kiritolasiz!")
    ], null=True, blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.pk)