from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Profile, account, timeline_msg, message_msg, message, timeline
from .forms import ProfileForm, accountForm, timeline_msgForm, message_msgForm, messageForm, timelineForm


class ProfileListView(ListView):
    model = Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm


class ProfileDetailView(DetailView):
    model = Profile


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm


class accountListView(ListView):
    model = account


class accountCreateView(CreateView):
    model = account
    form_class = accountForm


class accountDetailView(DetailView):
    model = account


class accountUpdateView(UpdateView):
    model = account
    form_class = accountForm


class timeline_msgListView(ListView):
    model = timeline_msg


class timeline_msgCreateView(CreateView):
    model = timeline_msg
    form_class = timeline_msgForm


class timeline_msgDetailView(DetailView):
    model = timeline_msg


class timeline_msgUpdateView(UpdateView):
    model = timeline_msg
    form_class = timeline_msgForm


class message_msgListView(ListView):
    model = message_msg


class message_msgCreateView(CreateView):
    model = message_msg
    form_class = message_msgForm


class message_msgDetailView(DetailView):
    model = message_msg


class message_msgUpdateView(UpdateView):
    model = message_msg
    form_class = message_msgForm


class messageListView(ListView):
    model = message


class messageCreateView(CreateView):
    model = message
    form_class = messageForm


class messageDetailView(DetailView):
    model = message


class messageUpdateView(UpdateView):
    model = message
    form_class = messageForm


class timelineListView(ListView):
    model = timeline


class timelineCreateView(CreateView):
    model = timeline
    form_class = timelineForm


class timelineDetailView(DetailView):
    model = timeline


class timelineUpdateView(UpdateView):
    model = timeline
    form_class = timelineForm

