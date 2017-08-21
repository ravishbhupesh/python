from django.db import models

# Create your models here.

class StockQuote(models.Model):
    sq_symbol = models.CharField(max_length=25)
    sq_date = models.DateTimeField('date of quote')
    sq_open = models.FloatField(default=0.0)
    sq_high = models.FloatField(default=0.0)
    sq_low = models.FloatField(default=0.0)
    sq_close = models.FloatField(default=0.0)
    sq_volume = models.IntegerField(default=0)

    def __str__(self):
        return self.sq_symbol
