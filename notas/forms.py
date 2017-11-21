from django import forms

from .models import Materia, Alumno


class NotaForm(forms.ModelForm):
#todos los campos de Materia
   class Meta:
      model = Materia
      fields = ('nombre', 'descripcion', 'alumno')
def __init__ (self, *args, **kwargs):
     super(MarteriaForm, self).__init__(*args, **kwargs)

     self.fields["alumno"].widget = forms.widgets.CheckboxSelectMultiple()

     self.fields["alumno"].help_text = "Ingrese los Alumons que participaron en el curso"

     self.fields["alumno"].queryset = Alumno.objects.all()
