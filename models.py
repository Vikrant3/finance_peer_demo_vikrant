from django.db import models


class FinancePeerUserData(models.Model):
    user_id = models.IntegerField(db_index=True)
    item_id = models.IntegerField(db_index=True)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
