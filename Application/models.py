from django.db import models

# Create your models here.


#Tables Utilisateurs(Facultatifs)
class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    nomComplet = models.CharField(max_length = 150)
    email = models.EmailField(max_length=100)
    motPass = models.CharField(max_length = 50)

class Personnel(models.Model):
    nom = models.CharField(max_length=50)
    utilisateur = models.ForeignKey(Utilisateur, on_delete = models.CASCADE)
    matricule = models.CharField(max_length=50)
    sexe = models.CharField(max_length = 50)
    hierarchie = models.CharField(max_length = 50)
    fonction = models.CharField(max_length=80)
    grade = models.CharField(max_length=50)
    diplome = models.CharField(max_length=70)
    telephone = models.CharField(max_length= 30)
    adresse = models.CharField(max_length=80)
    dateNaissance = models.DateField()
    salaire = models.FloatField()
    service = models.CharField(max_length=80)
    observation = models.TextField()

#La Table de documents : Cette pages enregistre tous les documents administrations 

class Document(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete = models.CASCADE)
    nomDocument = models.CharField(max_length = 30)
    typeDocument = models.CharField(max_length = 30)
    dateEnregistrement = models.DateField()
    
    
#La Table Congés : cette page permet d'enregistre les congés 

class Conge(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete = models.CASCADE)
    typeconges = models.CharField(max_length = 50)
    dateDeb = models.DateField()
    dateFin = models.DateField()
    etatAvancement = models.FloatField()
    
    
#La Table de Sanctions 

class Sanction(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete = models.CASCADE)
    typeSanction = models.CharField(max_length = 30)
    dateSanction = models.DateField()
    explication = models.TextField()
    
#La Table de Formations 

class Formation(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete = models.CASCADE)
    programmeFormation = models.CharField(max_length = 30)
    dateDeb = models.DateField()
    dateFin = models.DateField()
    
