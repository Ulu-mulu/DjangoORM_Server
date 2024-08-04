import json

from django.http import JsonResponse
from .models import Mark, Model, Part


def marks_list(request):
    marks = Mark.objects.filter(is_visible=True).values('id', 'name', 'producer_country_name')
    return JsonResponse(list(marks), safe=False)


def models_list(request):
    models = Model.objects.filter(is_visible=True).values('id', 'name')
    return JsonResponse(list(models), safe=False)


def search_parts(request):
    if request.method == 'POST':
        # Получение данных из запроса
        data = json.loads(request.body)

        # Логика поиска по частям
        parts = Part.objects.filter(is_visible=True)

        # Применение фильтров
        if 'mark_name' in data:
            parts = parts.filter(mark__name=data['mark_name'])
        if 'part_name' in data:
            parts = parts.filter(name__icontains=data['part_name'])
        if 'params' in data:
            params = data['params']
            if 'color' in params:
                parts = parts.filter(json_data__color=params['color'])

        # Пагинация
        page = data.get('page', 1)
        parts = parts[(page - 1) * 10: page * 10]

        # Формирование результата
        response = {
            "response": list(parts.values('id', 'name', 'price', 'json_data')),
            "count": parts.count(),
            "summ": sum(part.price for part in parts)
        }

        return JsonResponse(response)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)