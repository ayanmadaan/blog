from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import userregisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import UpdateView




def register(request):
    if request.method == 'POST':
        form = userregisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username} !😃; You can now Log In.')
            return redirect('login')
    else:
        form = userregisterForm()
    return render(request, 'userreg/register.html', {'form': form})

@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)


        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile has been successfully updated, keep surfing!')
            return redirect('profile')
        else:
            print('tf?')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'userreg/profile.html', context)


class ProfileListView(ListView):
    model = Profile
    template_name = 'userreg/main.html'
    context_object_name = 'userreg'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'userreg/detail.html'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)

        if view_profile.user in my_profile.following.all():
            follow = True

        else:
            follow = False
        context["follow"] = follow
        return context

def follow_unfollow_profile(request):
    if request.method=="POST":
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
                my_profile.following.remove(obj.user)
        else:
                my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:profile-list-view')
