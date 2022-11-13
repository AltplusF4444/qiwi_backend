from django.db import models


class AuthClients(models.Model):
    client_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    token_qiwi = models.TextField()
    token_app = models.TextField()

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return str(self.number)
