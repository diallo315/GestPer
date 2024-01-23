from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['nom','prenom','poste', 'email', 'motPass']
    
@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'matricule', 'sexe', 
                    'hierarchie', 'fonction', 'grade', 'diplome',
                    'telephone', 'adresse', 'dateNaissance', 
                    'salaire', 'observation']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['personnel', 'nomDocument', 'typeDocument', 'dateEnregistrement']

@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin):
    list_display = ['personnel', 'typeconges', 'dateDeb', 'dateFin']

@admin.register(Sanction)
class SanctionAdmin(admin.ModelAdmin):
    list_display = ['personnel', 'typeSanction', 'dateSanction', 'explication']

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display =['personnel', 'programmeFormation', 'dateDeb', 'dateFin']

