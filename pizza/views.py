from django.shortcuts import render
from pizza.forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from pizza.models import Pizza
def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_id = created_pizza.id

            note = 'Thanks for ordering! Your %s, %s and %s Pizza is on its way.' %(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'])
            filled_form = PizzaForm()
        else:
            created_pizza_id = None
            note = 'Pizza order has failed. Try Again'
        return render(request, 'pizza/order.html', {'pizzaform': filled_form, 'note': note,
            'multiple_form': multiple_form,
            'created_pizza_id': created_pizza_id })
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form, 'multiple_form': multiple_form })


def pizzas(request):
    num_pizza = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)

    if (filled_multiple_pizza_form.is_valid()):
        num_pizza = filled_multiple_pizza_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=num_pizza)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_form_set = PizzaFormSet(request.POST)
        if (filled_form_set.is_valid()):
            for form in filled_form_set:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered'
        else:
            note = 'Order was not created. Please try again.'
        return render(request, 'pizza/pizzas.html', { 'note': note, 'formset': formset})
    else:
        form = PizzaFormSet()
        multiple_form = MultiplePizzaForm()
        return render(request, 'pizza/pizzas.html', { 'formset': formset})


def edit_order(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated'
            return render(request, 'pizza/edit_order.html', { 'pizzaform': form, 'pizza': pizza, 'note': note })
    return render(request, 'pizza/edit_order.html', { 'pizzaform': form, 'pizza': pizza})

