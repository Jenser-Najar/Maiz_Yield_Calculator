from django.db import models

# Create your models here.
class ProductionData(models.Model):
    area_m2 = models.FloatField(help_text="Total land area (in square meters)")
    seeds_per_m2 = models.IntegerField(help_text="Number of plants per square meter")
    cobs_per_plant = models.FloatField(help_text="Average number of corn per plant")
    price_per_cob = models.FloatField(help_text="Price per ear of corn (in córdobas or USD)")

    def total_plants(self):
        return self.area_m2 * self.seeds_per_m2

    def total_cobs(self):
        return self.total_plants() * self.cobs_per_plant

    def total_income(self):
        return self.total_cobs() * self.price_per_cob

    def __str__(self):
        return f"Area: {self.area_m2} m² | Revenue: ${self.total_income():.2f}"
