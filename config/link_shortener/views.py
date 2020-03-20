from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import LinkForm, ShortLinkForm
from .services import short_link_generator
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse
from .models import ShortLink
from .services import get_long_link,check_recaptcha

class MainView(View):
	def get(self,request):
		return HttpResponse("Главная")

class LinkShortenerFormView(FormView):
	template_name = 'link_shortener/main.html'
	#form_class = LinkForm
	form_class = ShortLinkForm
	#success_url = '/my_links'
	def form_valid(self,form):
		if check_recaptcha(self.request.POST.get('g-recaptcha-response')):
			instance = form.save(commit=False)
			if self.request.user.is_authenticated:
				instance.user = self.request.user
			instance.short_link = short_link_generator()
			instance.save()
			#return redirect(self.get_success_url())
			return HttpResponseRedirect(reverse('link_shortener:detail',args=[instance.id]))
		else:
			return HttpResponse(status=403)
	def dispatch(self, request):
		short_link_url = self.request.GET.get('l')
		if short_link_url:
			long_link_url = get_long_link(short_link_url)
			if long_link_url:
				return redirect(long_link_url)
			else:
				return redirect('link_shortener:maine')
		return super(LinkShortenerFormView,self).dispatch(request)

class ShortLinkList(ListView):
	model = ShortLink
	paginate_by = 10
	
class ShortLinkUpdate(UpdateView):
	model = ShortLink
	fields = ['short_link']
	template_name_suffix = '_update_form'
	success_url = '/my_links'

class ShortLinkDelete(DeleteView):
	model = ShortLink
	success_url = '/my_links'	

class ShortLinkDetail(DetailView):
		model = ShortLink
# Create your views here.
