from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    poste = models.CharField(max_length=100)

class Personnel(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    matricule = models.CharField(max_length=50)
    sexe = models.CharField(max_length=50)
    hierarchie = models.CharField(max_length=50)
    fonction = models.CharField(max_length=80)
    grade = models.CharField(max_length=50)
    diplome = models.FileField(upload_to='diplome_personnel', max_length=100)
    telephone = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    dateNaissance = models.DateField()
    lieuNaissace = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='Image_Profil_Personnel', max_length=100)
    salaire = models.FloatField()
    service = models.CharField(max_length=80)
    observation = models.TextField()

class Document(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    nomDocument = models.CharField(max_length=30)
    typeDocument = models.CharField(max_length=30)
    dateEnregistrement = models.DateField()

class Conge(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    typeconges = models.CharField(max_length=50)
    dateDeb = models.DateField()
    dateFin = models.DateField()

class Sanction(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    typeSanction = models.CharField(max_length=30)
    dateSanction = models.DateField()
    explication = models.TextField()

class Formation(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    programmeFormation = models.CharField(max_length=30)
    dateDeb = models.DateField()
    dateFin = models.DateField()

class HFormation(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    observation = models.CharField(max_length=50) 