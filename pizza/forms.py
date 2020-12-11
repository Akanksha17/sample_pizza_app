from django import forms
from pizza.models import Pizza, Size


# class PizzaForm(forms.Form):
#     size_options = [('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')]
#     # topping_options = [('pep', 'Pepproni'), ('cheese', 'Cheese'), ('olives', 'Olives')]
#     topping1 = forms.CharField(label='Topping1:', max_length=100, widget=forms.PasswordInput)
#     topping2 = forms.CharField(label='Topping2:', max_length=100)
#     # toppings = forms.MultipleChoiceField(choices=topping_options, widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label='Size:', choices=size_options)

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza 
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2'
        }

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)


