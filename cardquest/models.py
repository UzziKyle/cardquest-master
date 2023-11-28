from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta: 
        abstract = True
        
    
class Trainer(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    birthdate =models.DateField(null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True) 
    email = models.EmailField(max_length=100, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    