from django.db import models


class Mark(models.Model):
    name = models.CharField(max_length=100)
    producer_country_name = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['producer_country_name']),
        ]


class Model(models.Model):
    name = models.CharField(max_length=100)
    mark = models.ForeignKey(Mark, related_name='models', on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]


class Part(models.Model):
    name = models.CharField(max_length=100)
    mark = models.ForeignKey(Mark, related_name='parts', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name='parts', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    json_data = models.JSONField(blank=True, default=dict)
    is_visible = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
            models.Index(fields=['is_visible']),
        ]
