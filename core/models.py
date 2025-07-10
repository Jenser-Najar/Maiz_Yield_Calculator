from django.db import models

# Create your models here.
class ProductionData(models.Model):
    area_m2 = models.FloatField(help_text="Área total del terreno (en metros cuadrados)")
    seeds_per_m2 = models.IntegerField(help_text="Cantidad de matas por metro cuadrado")
    cobs_per_plant = models.FloatField(help_text="Promedio de elotes por planta")
    price_per_cob = models.FloatField(help_text="Precio por elote (en córdobas o USD)")

    def total_plants(self):
        return self.area_m2 * self.seeds_per_m2

    def total_cobs(self):
        return self.total_plants() * self.cobs_per_plant

    def total_income(self):
        return self.total_cobs() * self.price_per_cob

    def __str__(self):
        return f"Área: {self.area_m2} m² | Ganancia: ${self.total_income():.2f}"
