from django.db import models

# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=50, null=True, blank=True)

    def str(self):
        return self.name

class Value(models.Model):
    currency = models.ForeignKey("main.Currency", on_delete=models.CASCADE)
    unit = models.PositiveIntegerField()
    buying = models.DecimalField(max_digits=50,decimal_places=10)
    selling = models.DecimalField(max_digits=50,decimal_places=10, null=True, blank=True)
    announced_at = models.DateTimeField(null=True, blank=True)

    def str(self):
        return '{}TRY rates at {}'.format(self.currency.code, self.announced_at)