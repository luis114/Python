from django import forms
from .pqrsf import pqrsf 

#Creamos las clases  con los formularios pertinentes

class ContactForm(forms.Form):
    
    tipomsj =  forms.ChoiceField(label="Tipo de Petición", required=True, choices=pqrsf, widget=forms.Select(attrs={'class':'form-control'}))
    usuario = forms.CharField(label="Tu nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe Tú nombre Completo'}))
    correo = forms.EmailField(label="Correo Electronico", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe Tú Correo'}))
    mensaje = forms.CharField(label="Mensaje", required=True, widget =forms.Textarea(attrs={'class':'form-control','rows':'5','placeholder':'Escribe Tú Mensaje'})) 