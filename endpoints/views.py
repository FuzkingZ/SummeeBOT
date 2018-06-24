from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Profile, account, timeline_msg, message_msg, message, timeline
from .forms import ProfileForm, accountForm, timeline_msgForm, message_msgForm, messageForm, timelineForm
from linepy import *
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import *
import sys
import subprocess
import shlex
from django.template.response import TemplateResponse
from django.core import serializers
from django.shortcuts import get_object_or_404 as orig_get_object_or_404
from django.contrib.auth.decorators import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .consolelog import *


def get_object_or_404(klass, format='json', *args, **kwargs):
    try:
        return orig_get_object_or_404(klass, *args, **kwargs)
    except http.Http404 as e:
        raise ViewException(format, str(e), 404)

@login_required(login_url='/accounts/login/')
def getPinByID(request, id ):
    acc = get_object_or_404(account,pk=id)
    pinCode = acc.pinCode
    return  HttpResponse(pinCode)

#def loginline_view(request , email , password , auth_type):
@login_required(login_url='/accounts/login/')

def loginline_view(request, id ):
    # ...
    acc = get_object_or_404(account,pk=id)
    #password = get_object_or_404(password, pk=id)
    id = acc.id
    email = acc.email
    password = acc.password
    html = ''
    owner = acc.owner_id
    currentUser = request.user.id
    authToken = acc.auth_token
    if owner is not currentUser:
        return  HttpResponse(str("คุณไม่ใช้เจ้าของ LINE ACCOUNT ไม่สามารถล๊อคอินได้นะจ๊ะ"))
    
   

    if email and password is not None:
        try:
            
            line = LINE(email, password,idAccount=id,systemName="EDZ-GamingZPC")
            
            # return HttpResponse("Code IS : " + line.args + line.kwargs + line.__dir__ + line.__str__)
        except Exception as e:
           # data = serializers.serialize('json', str(e.__dict__))
           # return HttpResponse(data, mimetype='application/json')
            return HttpResponse(str(e.__dict__))
        #output = line.log(">>> : " + str(line.__dict__))
        if line is not None:
            #acc_obj = account.object.get(id)
            
           
            acc.auth_token = str(line.authToken)
            acc.timeline_token = str(line.authToken)
            acc.mid = str(line.profile.mid)
            acc.timeline_token = str(line.channelResult.channelAccessToken)
            acc.qrcodeurl = str(line.profile.picturePath)
            acc.Name =  str(line.profile.displayName)
            acc.save()

            profile_obj = Profile(userid=str(line.profile.userid),phone=str(line.profile.phone),email=str(line.profile.email),regionCode=str(line.profile.regionCode),displayName=str(line.profile.displayName),phoneticName=str(line.profile.phoneticName),pictureStatus=str(line.profile.pictureStatus),thumbnailUrl=str(line.profile.thumbnailUrl),statusMessage=str(line.profile.statusMessage),allowSearchByUserid=str(line.profile.allowSearchByUserid),allowSearchByEmail=str(line.profile.allowSearchByEmail),picturePath=str(line.profile.picturePath),musicProfile=str(line.profile.musicProfile),videoProfile=str(line.profile.videoProfile),mid=acc)
            profile_obj.save()
            #html = "LOGIN เรียบร้อย"
            return HttpResponse('Login Success please re-load page!')
        else:
             html = "M.toast({html: '" + str(line.__dict__) +"'!'})"  #
        
       
        
        # {% if PINCODE %}
        #     
        # {% endif %}
        #html = "<html><body>Login Result </body></html>" + "<br>" + str(line.__dict__) #
        #return HttpResponse(html)
        
       # return render(request, 'endpoints/account_detail.html', {'PINCODE': )
        #result = line.getProfile()
        #return HttpResponse('<h1>Profile Is</h1>'+ result)
        return HttpResponse('No Method Avaliable!')
    else:
        return HttpResponseNotFound('<h1>Page was found</h1>')


def logoutline_view(request, id ):
    # ...
    acc = get_object_or_404(account,pk=id)
    #password = get_object_or_404(password, pk=id)
    email = acc.email
    password = acc.password

    if email and password is not None:
        line = LINE(email, password)
        line.logout()   
        output = line.log(">>> : " + str(line.__dict__))
        
        # {% if PINCODE %}
        #     
        # {% endif %}
        #html = "<html><body>Input this PIN code   %s on your LINE for smartphone in 2 minutes </body></html>" % output#
        #return HttpResponse(html)
        return HttpResponseRedirect('/endpoints/account/')
       # return render(request, 'endpoints/account_detail.html', {'PINCODE': )
        #result = line.getProfile()
        #return HttpResponse('<h1>Profile Is</h1>'+ result)
    else:
        return HttpResponseNotFound('<h1>Page was found</h1>')


@login_required(login_url='/accounts/login/')
def postTimeline_view(request, id ,timeline_id ):
    acc = get_object_or_404(account,pk=id)
    authToken = acc.auth_token
    timelines = get_object_or_404(timeline,pk=timeline_id)
    if owner is not currentUser:
        return  HttpResponse(str("คุณไม่ใช้เจ้าของ LINE ACCOUNT ไม่สามารถล๊อคอินได้นะจ๊ะ"))
    
    textToPost = timelines.text
    line = LINE(authToken)
    line.createPost(textToPost)

class ProfileListView(LoginRequiredMixin,ListView):
    model = Profile
    def get_queryset(self):
        return Profile.objects.filter(mid__owner=self.request.user)

class ProfileCreateView(LoginRequiredMixin,CreateView):
    model = Profile
    form_class = ProfileForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Profile, self).form_valid(form)

class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = Profile


class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileForm


class accountListView(LoginRequiredMixin,ListView):
    model = account
    def get_queryset(self):
        return account.objects.filter(owner=self.request.user)

class accountCreateView(LoginRequiredMixin,CreateView):
    model = account
    form_class = accountForm
    def form_valid(self, form):
        """Force the user to request.user"""
        self.object = form.save(commit=False)
        self.object.owner_id = self.request.user.id
        self.object.save()
        return HttpResponseRedirect('/endpoints/account/')

class accountDetailView(LoginRequiredMixin,DetailView):
    model = account



class accountUpdateView(LoginRequiredMixin,UpdateView):
    model = account
    form_class = accountForm
    def form_valid(self, form):
        """Force the user to request.user"""
        self.object = form.save(commit=False)
        self.object.owner_id = self.request.user.id
        self.object.save()
        return HttpResponseRedirect('/endpoints/account/')

class timeline_msgListView(LoginRequiredMixin,ListView):
    model = timeline_msg


class timeline_msgCreateView(LoginRequiredMixin,CreateView):
    model = timeline_msg
    form_class = timeline_msgForm
    

class timeline_msgDetailView(LoginRequiredMixin,DetailView):
    model = timeline_msg


class timeline_msgUpdateView(LoginRequiredMixin,UpdateView):
    model = timeline_msg
    form_class = timeline_msgForm


class message_msgListView(LoginRequiredMixin,ListView):
    model = message_msg
    def get_queryset(self):
        return message_msg.objects.filter(owner=self.request.user)

class message_msgCreateView(LoginRequiredMixin,CreateView):
    model = message_msg
    form_class = message_msgForm


class message_msgDetailView(LoginRequiredMixin,DetailView):
    model = message_msg


class message_msgUpdateView(LoginRequiredMixin,UpdateView):
    model = message_msg
    form_class = message_msgForm


class messageListView(LoginRequiredMixin,ListView):
    model = message
    def get_queryset(self):
        return message.objects.filter(owner=self.request.user)

class messageCreateView(LoginRequiredMixin,CreateView):
    model = message
    form_class = messageForm
    def form_valid(self, form):
        """Force the user to request.user"""
        self.object = form.save(commit=False)
        self.object.owner_id = self.request.user.id
        self.object.save()
        return HttpResponseRedirect('/endpoints/message/')

class messageDetailView(LoginRequiredMixin,DetailView):
    model = message


class messageUpdateView(LoginRequiredMixin,UpdateView):
    model = message
    form_class = messageForm


class timelineListView(LoginRequiredMixin,ListView):
    model = timeline
    def get_queryset(self):
        return timeline.objects.filter(owner=self.request.user)

class timelineCreateView(LoginRequiredMixin,CreateView):
    model = timeline
    form_class = timelineForm
    def form_valid(self, form):
        """Force the user to request.user"""
        self.object = form.save(commit=False)
        self.object.owner_id = self.request.user.id
        self.object.save()
        return HttpResponseRedirect('/endpoints/timeline/')

class timelineDetailView(LoginRequiredMixin,DetailView):
    model = timeline


class timelineUpdateView(LoginRequiredMixin,UpdateView):
    model = timeline
    form_class = timelineForm

