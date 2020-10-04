from django import forms 
from django.forms import ModelForm
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields = ['id', 'nombre', 'apellido_pat', 'apellido_mat', 'edad']
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs.update({'class' : 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
        self.fields['apellido_pat'].widget.attrs.update({'class' : 'form-control'})
        self.fields['apellido_mat'].widget.attrs.update({'class' : 'form-control'})
        self.fields['edad'].widget.attrs.update({'class' : 'form-control'})