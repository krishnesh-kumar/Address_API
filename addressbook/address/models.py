from django.db import models
import uuid
# Create your models here.
class address_model(models.Model):
    id_add = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    addre=models.TextField(blank=False)
