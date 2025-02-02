import random
from parts.models import Mark, Model, Part

# Создаем марки
marks = [Mark(name='Honda', producer_country_name='Япония', is_visible=True),
         Mark(name='Toyota', producer_country_name='Япония', is_visible=True),
         Mark(name='Ford', producer_country_name='США', is_visible=True),
         Mark(name='BMW', producer_country_name='Германия', is_visible=True),
         Mark(name='Audi', producer_country_name='Германия', is_visible=True)]
Mark.objects.bulk_create(marks)

# Создаем модели и связываем с марками
models = [Model(name='Civic', mark=marks[0], is_visible=True),
          Model(name='Camry', mark=marks[1], is_visible=True),
          Model(name='Mustang', mark=marks[2], is_visible=True),
          Model(name='X5', mark=marks[3], is_visible=True),
          Model(name='R8', mark=marks[4], is_visible=True)]
Model.objects.bulk_create(models)

# Список наименований запчастей
part_names = ['Бампер', 'Фара', 'Капот', 'Боковое стекло', 'Двигатель']
parts = []

for iteration in range(10000):
    selected_mark = random.choice(marks)
    selected_model = random.choice([model for model in models if model.mark == selected_mark])
    price = random.uniform(100, 5000)
    new_part = Part(
        name=random.choice(part_names),
        mark=selected_mark,
        model=selected_model,
        price=price,
        is_visible=random.choice([True, False]),
        json_data={
            'color': random.choice(['red', 'green', 'blue']),
            'is_new': random.choice([True, False]),
            'count': random.choice([1, 10])
        }
    )
    parts.append(new_part)

Part.objects.bulk_create(parts)