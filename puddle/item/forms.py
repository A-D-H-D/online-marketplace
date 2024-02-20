from django import forms
from .models import Item

        
INPUT_CLASSES = 'w-full py-4 px-6 my-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-blue-500'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category':  forms.Select(attrs={
                'class':INPUT_CLASSES   
            }), 

            'name':  forms.TextInput(attrs={
                'class':INPUT_CLASSES   
            }),  

            'description':  forms.Textarea(attrs={
                'class':INPUT_CLASSES   
            }), 

            'price':  forms.TextInput(attrs={
                'class':INPUT_CLASSES   
            }),             

            'image':  forms.FileInput(attrs={
                'class':INPUT_CLASSES   
            }), 
        }    