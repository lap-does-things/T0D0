from django import forms
from datetime import *
#from models import *
#class NameForm(forms.Form):
 #   your_name = forms.CharField(label='Your name', max_length=100)

class CreateNewList(forms.Form):
    #check = forms.BooleanField()
    name = forms.CharField(label='Name', max_length=200)

    #date = datetime.now()
    #class Meta:
    #    model= ToDoList()
   #     fields=[]