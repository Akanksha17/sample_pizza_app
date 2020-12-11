from django import forms

class PizzaForm(forms.Form):
    size_options = [('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')]
    topping1 = forms.CharField(label='Topping1:', max_length=100)
    topping2 = forms.CharField(label='Topping2:', max_length=100)
    size = forms.ChoiceField(label='Size:', choices=size_options)
