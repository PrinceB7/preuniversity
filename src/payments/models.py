from django.db import models


class Transaction(models.Model):
    merchant_trans_id = models.CharField(max_length=255)
    service_id = models.IntegerField()
