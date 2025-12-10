from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'rating', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1000,
                'max': 9999,
                'placeholder': 'e.g., 2024'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 10,
                'placeholder': 'Enter 1-10'
            }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class SearchBookForm(forms.Form):
    book_id = forms.IntegerField(
        label="Enter Book ID",
        required=True,
        widget=forms.NumberInput(attrs={'id': 'book_id'})
    )
