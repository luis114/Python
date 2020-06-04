from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos
# Create your models here:
#Crear la estructura de la aplicacion en el modelo de datos:

class Roles(models.Model):
    RoleName = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Perfiles de Usuarios"
        verbose_name_plural = "Perfiles"



    #AQUI CREO LA FNCION PARA LLAMAR LOS ATRIBUTOS:
    def __str__(self):
        return self.RoleName

#Modelo  ''datos de usuario''

class DatosUser(models.Model):
    userDNI = models.CharField(max_length = 20,verbose_name = 'Identificaciòn')
    nombUser = models.CharField(max_length = 200, null=True,verbose_name ='Nombre')
    apelUser = models.CharField(max_length = 200, null=True,verbose_name = 'Apellido')
    profUser = models.CharField(max_length = 200, null= True,verbose_name='Profesión' )
    fotoUser = models.ImageField(default='user.png',verbose_name = 'Foto de perfil' )
    teleUser = models.CharField(max_length = 20,verbose_name = 'Nùmero de Telèfono')
    geneUser = models.CharField(max_length = 20, choices = Generos,default ="Otro" ,verbose_name = 'Gènero')
    adddata = models.DateTimeField(auto_now_add = True, null=True)
    modifiat = models.DateTimeField(auto_now = True, null=True)

    class Meta:
        verbose_name ="Datos de Ususrios"
        verbose_name_plural ="Información"
    
    

    #se define la funcion, y cada clase tiene que tener un metodo
    def __str__(self):
        return self.nombUser

#Modelo ''habilidades''

class HabiUser(models.Model):

    NombreHabilidad = models.CharField(max_length=50)
    DescHabil = models.TextField(max_length = 2000, verbose_name="Descripcion de la habilidad")

    class Meta:
        verbose_name ="Habilidades de Usuarios"
        verbose_name_plural ="Competencias"


    def __str__(self):
        return self.NombreHabilidad



# Agregamos los modelos de detalles
class DataRoles(models.Model):
    idRole = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name="Identificador de rol")
    IdUser = models.ForeignKey(DatosUser, on_delete=models.CASCADE) 
    addUser = models.DateTimeField(auto_now_add = True,auto_now = False)
    udTuser = models.DateTimeField(auto_now =True)
    estaRol = models.CharField(max_length=10)

    class Meta:
        verbose_name ="Roles de Usuarios"
        verbose_name_plural ="Roles"

    #funcion mostrar
    def __str__(self):
        return self.addUser

#modelo rates

class Rates(models.Model):
    idHabil = models.ForeignKey(HabiUser, on_delete=models.CASCADE)
    idUser = models.ForeignKey(DatosUser, on_delete=models.CASCADE)
    pcrHabil = models.DecimalField(max_digits=2, decimal_places=1) #99,9
    udtHabil = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ="Nivel de habilidad"
        verbose_name_plural ="Niveles de Usuarios"

#Función para envocar
    def __str__(self):
        return self.idHabil


        

