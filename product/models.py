from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description_short = models.TextField(max_length=255)
    description_long = models.TextField()
    image = models.ImageField(upload_to='product_image/%Y/%m', blank=True, null=True) 
    slug = models.SlugField(unique=True)
    price_marketing = models.FloatField()
    price_marketing_promotion = models.FloatField(default=0)
    product_type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variable'),
            ('S', "Simple"),
        ) 
    )
    
    @staticmethod
    def resize_image(img, new_width = 800):
        print(img.name)
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        max_image_size = 800
        
        if self.image:
            self.resize_image(self.image, max_image_size)
    
    def __str__(self):
        return self.name