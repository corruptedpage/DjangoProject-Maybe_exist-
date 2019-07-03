from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm
from .models import User


def register(request):

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = UserRegisterForm()

    context = {
        'form': register_form,
        'title': 'Регистрация',
        'submit_label': 'Зарегистрироваться'
    }
    return render(request, 'authuser/register.html', context)


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse('main'))

    return render(request, 'authuser/login.html', {'title': 'Войти', 'next': request.GET.get('next')})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


class EditView(UpdateView):
    model = User
    template_name = 'authuser/register.html'
    fields = 'username', 'email', 'avatar'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование профиля'
        context['submit_label'] = 'Применить'
        return context
