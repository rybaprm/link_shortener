from django.db import models
import uuid
from django.contrib.auth import get_user_model

class ShortLink(models.Model):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	long_link = models.URLField()
	short_link = models.CharField(max_length=6, unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
	

# Create your models here.
