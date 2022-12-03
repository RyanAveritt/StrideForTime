from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Relationship
from .forms import ProfileModelForm, NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User 
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@login_required
def my_profile_view(request):
	profile = Profile.objects.get(user=request.user)
	form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
	confirm = False

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			confirm = True

	context = {
		'profile': profile,
		'form': form,
		'confirm': confirm
	}
	return render(request, 'profiles/myprofile.html', context)

class ProfileListView(LoginRequiredMixin, ListView):
	model = Profile
	template_name = 'profiles/profile_list.html'
		
	def get_queryset(self):
		qs = Profile.objects.get_all_profiles(self.request.user)
		return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = User.objects.get(username__iexact=self.request.user)
		profile = Profile.objects.get(user=user)
		rel_r = Relationship.objects.filter(sender=profile)
		rel_s = Relationship.objects.filter(receiver=profile)
		rel_receiver = [(item.receiver.user) for item in rel_r]
		rel_sender = [(item.sender.user) for item in rel_s]
		context["rel_receiver"] = rel_receiver
		context["rel_sender"] = rel_sender
		context['is_empty'] = False
		if len(self.get_queryset()) == 0:
			context['is_empty'] = True
		return context

class ProfileDetailView(LoginRequiredMixin, DetailView):
	model = Profile
	template_name = 'profiles/detail.html'

	def get_object(self):
		slug = self.kwargs.get('slug')
		profile = Profile.objects.get(slug=slug)
		return profile

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = User.objects.get(username__iexact=self.request.user)
		profile = Profile.objects.get(user=user)
		rel_r = Relationship.objects.filter(sender=profile)
		rel_s = Relationship.objects.filter(receiver=profile)
		rel_receiver = [(item.receiver.user) for item in rel_r]
		rel_sender = [(item.sender.user) for item in rel_s]
		context["rel_receiver"] = rel_receiver
		context["rel_sender"] = rel_sender
		context['calendars'] = self.get_object().get_calendars()
		context['len_calendars'] = True if self.get_object().get_calendars_no() > 0 else False
		return context

@login_required
def sent_invites_view(request):
	#invite_profiles_list_view
	user = request.user
	qs = Profile.objects.get_all_profiles_invited(user)

	context = {'qs': qs}

	return render(request, 'profiles/invited_list.html', context)

@login_required
def profiles_list_view(request):
	user = request.user
	qs = Profile.objects.get_all_profiles(user)

	context = {'qs': qs}

	return render(request, 'profiles/profile_list.html', context)

@login_required
def invites_received_view(request):
	profile = Profile.objects.get(user=request.user)
	qs = Relationship.objects.invatations_received(profile)
	results = list(map(lambda x: x.sender, qs))
	is_empty = False
	if len(results) == 0:
		is_empty = True

	context = {
		'qs': results,
		'is_empty': is_empty,
	}

	return render(request, 'profiles/my_invites.html', context)
	
@login_required
def send_invatation(request):
	if request.method=='POST':
		pk = request.POST.get('profile_pk')
		user = request.user
		sender = Profile.objects.get(user=user)
		receiver = Profile.objects.get(pk=pk)

		rel = Relationship.objects.create(sender=sender, receiver=receiver, status='sent')

		return redirect(request.META.get('HTTP_REFERER'))
	return redirect('profiles:my-profile-view')

@login_required
def accept_invatation(request):
	if request.method=="POST":
		pk = request.POST.get('profile_pk')
		sender = Profile.objects.get(pk=pk)
		receiver = Profile.objects.get(user=request.user)
		rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
		if rel.status == 'sent':
			rel.status = 'accepted'
			rel.save()
	return redirect('profiles:my-invites-view')

@login_required
def reject_invatation(request):
	if request.method=="POST":
		pk = request.POST.get('profile_pk')
		receiver = Profile.objects.get(user=request.user)
		sender = Profile.objects.get(pk=pk)
		rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
		rel.delete()
	return redirect('profiles:my-invites-view')

@login_required
def remove_from_friends(request):
	if request.method=='POST':
		pk = request.POST.get('profile_pk')
		user = request.user
		sender = Profile.objects.get(user=user)
		receiver = Profile.objects.get(pk=pk)

		rel = Relationship.objects.get(
			(Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender))
		)
		rel.delete()
		return redirect(request.META.get('HTTP_REFERER'))
	return redirect('profiles:my-profile-view')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("/")