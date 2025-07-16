from django.shortcuts import render
from django.http import JsonResponse
from .forms import ProductionDataForm

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
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'result': result})
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors.as_json()}, status=400)
    else:
        form = ProductionDataForm()

    return render(request, 'core/index.html', {'form': form, 'result': result})
