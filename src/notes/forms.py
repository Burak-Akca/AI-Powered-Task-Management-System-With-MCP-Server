from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter title',
        }),
        label='Title'
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Write note content here',
            'rows': 5,
        }),
        label='Content'
    )
    
    class Meta:
        model = Note
        fields = ['title', 'content']
