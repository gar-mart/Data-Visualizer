from django import forms
from .models import Document



class DocumentForm(forms.ModelForm):
    table_name = forms.CharField(max_length=100)
    category_name = forms.CharField(max_length=100)

    class Meta:
        model = Document
        fields = ('upload', 'table_name', 'category_name')

        
class ReviewForm(forms.Form):
    user_name = forms.CharField()


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


