from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Album
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class create_album(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class update_album(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class delete_album(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')



class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # Display Blank Form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    # Process Form Data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # Normalized Data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Returns User Object if Credentials are Correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})