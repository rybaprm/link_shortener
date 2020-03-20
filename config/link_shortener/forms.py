from django import forms
from django.forms import ModelForm
from .models import ShortLink

class LinkForm(forms.Form):
	login_uri = forms.URLField()
	
class ShortLinkForm(ModelForm):

	
	
	
	class Meta:
		model = ShortLink
		fields = ('long_link',)
		
	
		