from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories' #verbose_name_plural: C'est une option qui permet de spécifier le nom au pluriel utilisé pour représenter ce modèle dans l'interface d'administration Django

    def __str__(self):
        return self.title 
    
class Product(models.Model):
    
    Category =  models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    #définit un champ de clé étrangère (ForeignKey) dans le modèle Product
    #related_name permet d'accéder aux objets de la catégorie
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description =  models.TextField(blank=True, null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    