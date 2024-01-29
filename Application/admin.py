from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin
@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
     list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'poste')
    
@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ['nom','prenom', 'matricule', 'sexe', 
                    'hierarchie', 'fonction', 'grade', 'diplome',
                    'telephone', 'email', 'dateNaissance', 
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

