from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.contrib.auth.models import User




class Profile(models.Model):

    # Fields
    userid = models.TextField(blank=True)
    phone = models.TextField( blank=True )
    email = models.EmailField( blank=True )
    regionCode = models.CharField(max_length=30)
    displayName = models.TextField(max_length=255 ,  blank=True )
    phoneticName = models.TextField(max_length=255 , blank=True )
    pictureStatus = models.TextField(max_length=255 , blank=True )
    thumbnailUrl = models.URLField( blank=True )
    statusMessage = models.TextField(max_length=255 , blank=True )
    allowSearchByUserid = models.BooleanField(max_length=255 , blank=True )
    allowSearchByEmail = models.BooleanField(max_length=255 , blank=True )
    picturePath = models.TextField(max_length=255 , blank=True )
    musicProfile = models.TextField(max_length=255 , blank=True )
    videoProfile = models.TextField(max_length=255 , blank=True )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    mid = models.ForeignKey(
        'account', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('endpoints_profile_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('endpoints_profile_update', args=(self.pk,))


class account(models.Model):

    # Fields
    owner = models.ForeignKey(User, editable=False,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    password = models.CharField(max_length=30)
    auth_token = models.TextField()
    timeline_token = models.TextField(max_length=255 )
    qrcodeurl = models.URLField()
    pinCode = models.TextField(max_length=255 , blank=True )
    mid = models.CharField(max_length=255)
    Name = models.TextField(max_length=255 , blank=True )


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('endpoints_account_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('endpoints_account_update', args=(self.pk,))


class timeline_msg(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    code = models.TextField(max_length=100)
    message = models.TextField(max_length=100)
    result = models.TextField()
    writerMid = models.TextField()
    appSn = models.TextField()
    homeId = models.TextField()
    postId = models.TextField()
    status = models.TextField()
    likeCount = models.CharField(max_length=30)
    commentCount = models.CharField(max_length=30)
    postInfo_msg = models.TextField()

    # Relationship Fields
    timelineid = models.ForeignKey(
        'timeline', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('endpoints_timeline_msg_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('endpoints_timeline_msg_update', args=(self.slug,))


class message_msg(models.Model):

    # Fields
    from_mid = models.TextField(max_length=255)
    to_mid = models.TextField()
    createdTime = models.TextField(editable=False)
    deliveredTime = models.CharField(max_length=30)
    text = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    hasContent = models.BooleanField()
    contentType = models.TextField(max_length=255)
    contentPreview = models.TextField(max_length=255)
    contentMetadata = models.TextField(max_length=255)
    sessionId = models.CharField(max_length=30)
    chunks = models.TextField(max_length=255)
    relatedMessageId = models.TextField(max_length=255)
    messageRelationType = models.TextField(max_length=255)
    readCount = models.TextField(max_length=255)
    relatedMessageServiceCode = models.TextField(max_length=255)
    result_code = models.TextField(max_length=100)
    result_msg = models.TextField()

    # Relationship Fields
    msgid = models.ForeignKey(
        'message', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('endpoints_message_msg_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('endpoints_message_msg_update', args=(self.pk,))


class message(models.Model):

    # Fields
    owner = models.ForeignKey(User, editable=False,on_delete=models.CASCADE)
    name = models.TextField(max_length=255)
    text = models.TextField( blank=True )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    msgid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=2)
    packageid = models.CharField(max_length=30)
    stickerid = models.CharField(max_length=30)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('endpoints_message_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('endpoints_message_update', args=(self.pk,))


class timeline(models.Model):

    # Fields
    owner = models.ForeignKey(User, editable=False,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='slug')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    timelineid = models.AutoField(primary_key=True)
    text = models.TextField( )
    picture = models.ImageField(upload_to="./upload/images/")
    stickerID = models.CharField(max_length=30)
    packageID = models.CharField(max_length=30)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('endpoints_timeline_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('endpoints_timeline_update', args=(self.slug,))


