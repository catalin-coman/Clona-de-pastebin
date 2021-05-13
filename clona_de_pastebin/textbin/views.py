from django.conf.urls import url
from .models import Text, User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class HomeView(generic.ListView):
    template_name = 'textbin/home.html'
    context_object_name = 'all_users'
    def get_queryset(self):
        return User.objects.all()

class TextsView(generic.DetailView):
    model = User
    template_name = 'textbin/textlist.html'

class UserCreate(CreateView):
    model = User
    fields = ['name', 'email']

class TextCreate(CreateView):
    model = Text
    fields = ['author', 'title', 'content']

class TextUpdate(UpdateView):
    model = Text
    fields = ['title', 'content']

class TextDelete(DeleteView):
    model = Text
    success_url = reverse_lazy('textbin:home')