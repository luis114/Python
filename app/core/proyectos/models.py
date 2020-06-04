from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from userdata.models import DatosUser

# Create your models here.


#Crear la estructura de la aplicacion en el modelo de datos:

#modelo de tipo documento

class TipoDocu(models.Model):
  idTipoDocumento = models.CharField(max_length = 200,verbose_name ='Tipo Documento')
  nomDocumento  = models.CharField(max_length = 200,verbose_name ='Documento')

  class Meta:
     verbose_name ="Tipo De Documento"
     verbose_name_plural ="Documento"
    
    

#se define la funcion, y cada clase tiene que tener un metodo
  def __str__(self):
    return self.nomDocumento



# modelo de categoria

class CateProyecto(models.Model):

  idCategoriaProyecto = models.CharField(max_length = 20,verbose_name = 'Identificador')
  lenguaje = models.CharField(max_length = 200, verbose_name ='Lenguaje')
  motorBd = models.CharField(max_length = 200, verbose_name ='Motor De Base De Datos')
  arquitectura  = models.CharField(max_length = 200, verbose_name ='Arquitectura')


  class Meta:
    verbose_name ="Datos de Categoria"
    verbose_name_plural ="Categoria"
    
    

#se define la funcion, y cada clase tiene que tener un metodo
  def __str__(self):
    return self.lenguaje



class Proyecto(models.Model):
  nomProyecto = models.CharField(max_length = 200, null=True,verbose_name ='Nombre de Proyecto')
  desProyecto = models.TextField(max_length = 200, null=True,verbose_name ='Descripcion de Proyecto')
  imgProyecto = models.ImageField(max_length = 200, null=True,verbose_name ='Imagen de Proyecto')
  fechaInicial = models.DateTimeField(auto_now=True)
  fechaFinal = models.DateTimeField(auto_now=True)
  urlReposotorio = models.CharField(max_length = 200, null=True,verbose_name ='Url Repositorio')
  estProyecto = models.CharField(max_length = 200, null=True,verbose_name ='Estado del Proyecto')
  idCategoriaProyecto = models.ForeignKey(CateProyecto, on_delete = models.CASCADE, )


  class Meta:
    verbose_name ="Datos del Proyecto"
    verbose_name_plural ="Proyecto"
    
    

#se define la funcion, y cada clase tiene que tener un metodo
  def __str__(self):
    return self.nomProyecto

#modelo para documento

class Documento(models.Model):
  nomDocumento = models.CharField(max_length = 200, null=True,verbose_name ='Nombre de Documento')
  pathDocument = models.CharField(max_length = 200, null=True,verbose_name ='Path Documento')
  idTipoDocumento = models.ForeignKey(TipoDocu, on_delete=models.CASCADE)
  idProyectoa =models.ForeignKey(Proyecto, on_delete=models.CASCADE)
  idUsuario =models.ForeignKey(DatosUser, on_delete=models.CASCADE)



  class Meta:
    verbose_name ="Datos del Documento"
    verbose_name_plural ="Documento"
    
    

 #se define la funcion, y cada clase tiene que tener un metodo
  def __str__(self):
    return self.nomDocumento









        




    
