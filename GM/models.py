from django.db import models
from django.utils import timezone

class Blog(models.Model):
    sarlavha = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, db_index=True)
    tasvir = models.TextField()
    main_banner = models.ImageField(upload_to='images/main_banner/')
    views = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_main = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.sarlavha + ' ' + str(self.date_posted)
    
    @property
    def format_date_created(self):
        return self.date_posted.strftime("%B %d, %Y")
    
    
class Category(models.Model):
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    
    
class Stories(models.Model):
    img = models.ImageField(upload_to='images/stories/')
    nom = models.CharField(max_length=50)


