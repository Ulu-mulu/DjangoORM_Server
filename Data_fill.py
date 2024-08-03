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
          Model(name='Accord', mark=marks[0], is_visible=True),
          Model(name='Camry', mark=marks[1], is_visible=True),
          Model(name='Mustang', mark=marks[2], is_visible=True),
          Model(name='X5', mark=marks[3], is_visible=True)]
Model.objects.bulk_create(models)

# Список наименований запчастей
part_names = ['Бампер', 'Фара', 'Капот', 'Боковое стекло', 'Двигатель']

# Создание запчастей
for _ in range(10000):
    Part.objects.create(
        name=random.choice(part_names),
        mark=random.choice(marks),
        model=random.choice(models),
        price=random.uniform(100, 5000),
        json_data={
            'color': random.choice(['красный', 'черный', 'белый']),
            'is_new_part': random.choice([True, False]),
            'count': random.randint(1, 10)
        },
        is_visible=True
    )