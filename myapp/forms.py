
from django import forms 
from django.forms import ModelForm 
from .models import BookDetails 
class bookform(ModelForm): 
    class Meta: 
        model=BookDetails 
        fields=('title','author' ,'isbn10','isbn13','overview1','overview2','image_url','authorImage_url','category','pdf',) 
        labels={ 
            'title':'  Book Title   ', 
            'author':'Author Name ', 
            'isbn10':'Book ID (10) ', 
            'isbn13':'Book ID (13) ', 
            'overview1':'Description 1 ', 
            'overview2':'Description 2 ', 
            'image_url':'Book Cover ', 
            'authorImage_url':'Author image ', 
            'category':'Category ', 
            'pdf' : 'PDF', 
            } 
         
        widgets= { 
            'title':forms.TextInput(attrs ={'class':'form-control','placeholder':'Enter Book Title'}), 
            'author':forms.TextInput(attrs ={'class':'form-control','placeholder':'Enter Author Name'}), 
            'isbn10':forms.TextInput(attrs ={'class':'form-control','placeholder':'Enter Book ID 10'}), 
            'isbn13':forms.TextInput(attrs ={'class':'form-control','placeholder':'Enter Book ID 13'}), 
            'overview1':forms.Textarea(attrs ={'class':'form-control','placeholder':'Enter Book Description part1'}), 
            'overview2':forms.Textarea(attrs ={'class':'form-control','placeholder':'Enter Book Description part2'}), 
            'image_url':forms.FileInput(attrs ={'class':'form-controlp'}), 
            'authorImage_url':forms.FileInput(attrs ={'class':'form-control'}), 
            'category':forms.TextInput(attrs ={'class':'form-control','placeholder':'Enter Book cotegory'}), 
            'pdf' :forms.FileInput(), 
            }