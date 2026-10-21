from django.http import JsonResponse
from django.views.decorators.http import require_GET

CAR_MODELS_DATA = [
    {"CarModel": "Corolla", "CarMake": "Toyota"},
    {"CarModel": "Camry", "CarMake": "Toyota"},
    {"CarModel": "RAV4", "CarMake": "Toyota"},
    {"CarModel": "Yaris", "CarMake": "Toyota"},
    {"CarModel": "Altima", "CarMake": "Nissan"},
    {"CarModel": "Rogue", "CarMake": "Nissan"},
    {"CarModel": "Maxima", "CarMake": "Nissan"},
    {"CarModel": "Versa", "CarMake": "Nissan"},
    {"CarModel": "A4", "CarMake": "Audi"},
    {"CarModel": "A6", "CarMake": "Audi"},
    {"CarModel": "Q5", "CarMake": "Audi"},
    {"CarModel": "Q7", "CarMake": "Audi"},
    {"CarModel": "C-Class", "CarMake": "Mercedes"},
    {"CarModel": "E-Class", "CarMake": "Mercedes"},
    {"CarModel": "GLC", "CarMake": "Mercedes"},
    {"CarModel": "Optima", "CarMake": "Kia"},
    {"CarModel": "Sportage", "CarMake": "Kia"},
    {"CarModel": "Telluride", "CarMake": "Kia"},
]

@require_GET
def get_cars(request):
    return JsonResponse({"CarModels": CAR_MODELS_DATA})