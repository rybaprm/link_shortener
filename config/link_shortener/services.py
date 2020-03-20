import string
import random

import requests
from django.conf import settings

from .models import ShortLink


#chars = string.digits+string.ascii_uppercase
#def short_link_generator(chars, size=6):
#	short_link = ''
#	for _ in range(size):
#		short_link += random.choice(chars)
#	return short_link
#
#print(short_link_generator(chars))

def short_link_generator(size=6,
	chars = string.digits+string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(size))

def get_long_link(short_link):
	long_link = ShortLink.objects.filter(short_link = short_link).values('long_link').first()
	return long_link.get('long_link')

def check_recaptcha(response,sekret=settings.GOOGLE_RECAPTCHA_SECRET_KEY):
	data = {'response':response	,
			'secret':sekret}
	result = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
	result_json = result.json()
	return result_json.get('success')