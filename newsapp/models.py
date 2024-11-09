from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(null=True,unique=True,blank=True,db_index=True,editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class News(models.Model):
    title=models.CharField(max_length=50)
    description=RichTextField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)  # Yeni alan
    is_active=models.BooleanField(default=True)
    slug=models.SlugField(null=True,unique=True,blank=True,db_index=True,editable=False)
    category=models.ForeignKey(Category,default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

