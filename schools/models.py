from django.db import models

# Create your models here.
class Ecole(models.Model):
    nom = models.CharField(max_length=100)
    adress = models.TextField()

    def __str__(self):
        return self.nom
    



class Classe(models.Model):
    nom = models.CharField(max_length=20)
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    


class Eleve(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=2, decimal_places=0)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    