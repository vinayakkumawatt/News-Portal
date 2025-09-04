from django.db import models
from tinymce.models import HTMLField

class Categories(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='category/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title

class News(models.Model):
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='news/')
    heading = models.CharField(max_length=250)
    description = HTMLField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.heading
    class Meta:
        verbose_name_plural = 'News'

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField()