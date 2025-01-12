from django.db import models
from django.utils import timezone

class Category (models.Model):
    cat_name=models.CharField(max_length=50)

class Ingredient(models.Model):
    ing_name=models.CharField(max_length=50)

class product (models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField(max_length=10)
    created_at=models.DateTimeField(auto_now=True)
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)
    ings=models.ManyToManyField(Ingredient, related_name="prods")

    def  __str__(self):
        return self.name + " ("+ str(self.price)+"Da)"
    
class Commande(models.Model):
    Description_cmd = models.CharField(max_length=50) 
    Date_cmd = models.DateField(default=timezone.now) #Par défaut, la date actuelle
    Produit_cmd = models.ForeignKey(product, on_delete=models.CASCADE)

    def __str__(self):
        return self.Description_cmd    


