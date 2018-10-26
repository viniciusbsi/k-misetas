from django.views.generic import *
from django.contrib.auth.models import User
from kamisetas_app.forms.usuario import UserCreateForm

class UsuarioCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'usuario/usuario_create.html'
    success_url = '/'

    # def get_context_data(self, **kwargs):
    #     context = super(UsuarioCreateView, self).get_context_data(**kwargs)
    #     return context

    def form_invalid(self, form):
        return super(UsuarioCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UsuarioCreateView, self).form_valid(form)
