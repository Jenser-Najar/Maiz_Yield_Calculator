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
                'total_plants': f"{data.total_plants():.2f}",
                'total_cobs': f"{data.total_cobs():.2f}",
                'total_income': f"{data.total_income():.2f}",
            }
    else:
        form = ProductionDataForm()

    return render(request, 'core/index.html', {'form': form, 'result': result})
