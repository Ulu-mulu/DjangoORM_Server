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
        data = json.loads(request.body)

        parts = Part.objects.filter(is_visible=True)

        if 'mark_name' in data:
            parts = parts.filter(mark__name=data['mark_name'])
        if 'mark_list' in data:
            parts = parts.filter(mark__id__in=data['mark_list'])
        if 'part_name' in data:
            parts = parts.filter(name__icontains=data['part_name'])
        if 'price_gte' in data:
            parts = parts.filter(price__gte=data['price_gte'])
        if 'price_lte' in data:
            parts = parts.filter(price__lte=data['price_lte'])
        if 'params' in data:
            params = data['params']
            if 'color' in params:
                parts = parts.filter(json_data__color=params['color'])
            if 'is_new' in params:
                parts = parts.filter(json_data__is_new=params['is_new'])
            if 'count' in params:
                parts = parts.filter(json_data__count=params['count'])

        # Пагинация
        page = data.get('page', 1)
        parts = parts[(page - 1) * 10: page * 10]

        # Формирование результата
        parts_info = parts.select_related('mark', 'model')

        response = {
            "response": [
                {
                    "mark": {
                        "id": part.mark.id,
                        "name": part.mark.name,
                        "producer_country_name": part.mark.producer_country_name,
                    },
                    "model": {
                        "id": part.model.id,
                        "name": part.model.name,
                    },
                    "name": part.name,
                    "json_data": part.json_data,
                    "price": part.price,
                }
                for part in parts_info
            ],
            "count": parts.count(),
            "summ": sum(part.price for part in parts_info)
        }

        return JsonResponse(response)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)

