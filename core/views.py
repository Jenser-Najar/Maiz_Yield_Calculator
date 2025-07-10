from django.shortcuts import render
from .forms import ProductionDataForm

# Create your views here.
def calculator_view(request):
    result = None

    if request.method == 'POST':
        form = ProductionDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            result = {
                'total_plants': data.total_plants(),
                'total_cobs': data.total_cobs(),
                'total_income': data.total_income(),
            }
    else:
        form = ProductionDataForm()

    return render(request, 'core/index.html', {'form': form, 'result': result})
