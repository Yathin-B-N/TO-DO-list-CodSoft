from django.forms import ModelForm
from app.models import TODO

class TODOform(ModelForm):
    class Meta:
        model = TODO
        fields = ['title','priority','status']