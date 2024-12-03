from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=70)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Categories'

class Books(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=350,default='')
    category=models.ManyToManyField(Category)
    writer=models.CharField(max_length=50)
    published=models.DateTimeField(auto_now_add=True)
    descriptions=models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='Books'
    
    
STAR_CHOICE=[
    
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
    
class Review(models.Model):
    image=models.CharField(max_length=350,default="")
    name=models.CharField(max_length=20)
    books=models.ForeignKey(Books,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(choices=STAR_CHOICE, max_length=10)
    
    def __str__(self):
        return self.name  