# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class BlogBlogcategory(models.Model):
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=2000)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_blogcategory'


class BlogBlogpost(models.Model):
    comments_count = models.IntegerField()
    keywords_string = models.CharField(max_length=500)
    rating_count = models.IntegerField()
    rating_sum = models.IntegerField()
    rating_average = models.FloatField()
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=2000)
    field_meta_title = models.CharField(db_column='_meta_title', max_length=500, blank=True, null=True)  # Field renamed because it started with '_'.
    description = models.TextField()
    gen_description = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    publish_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    short_url = models.CharField(max_length=200, blank=True, null=True)
    in_sitemap = models.IntegerField()
    content = models.TextField()
    allow_comments = models.IntegerField()
    featured_image = models.CharField(max_length=255, blank=True, null=True)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    user = models.ForeignKey('NewuserNewuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_blogpost'


class BlogBlogpostCategories(models.Model):
    blogpost = models.ForeignKey(BlogBlogpost, models.DO_NOTHING)
    blogcategory = models.ForeignKey(BlogBlogcategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_blogpost_categories'
        unique_together = (('blogpost', 'blogcategory'),)


class BlogBlogpostRelatedPosts(models.Model):
    from_blogpost = models.ForeignKey(BlogBlogpost, models.DO_NOTHING)
    to_blogpost = models.ForeignKey(BlogBlogpost, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_blogpost_related_posts'
        unique_together = (('from_blogpost', 'to_blogpost'),)


class ConfSetting(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=2000)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'conf_setting'


class CoreSitepermission(models.Model):
    user = models.ForeignKey('NewuserNewuser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'core_sitepermission'


class CoreSitepermissionSites(models.Model):
    sitepermission = models.ForeignKey(CoreSitepermission, models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_sitepermission_sites'
        unique_together = (('sitepermission', 'site'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('NewuserNewuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCommentFlags(models.Model):
    flag = models.CharField(max_length=30)
    flag_date = models.DateTimeField()
    comment = models.ForeignKey('DjangoComments', models.DO_NOTHING)
    user = models.ForeignKey('NewuserNewuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_comment_flags'
        unique_together = (('user', 'comment', 'flag'),)


class DjangoComments(models.Model):
    object_pk = models.TextField()
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=254)
    user_url = models.CharField(max_length=200)
    comment = models.TextField()
    submit_date = models.DateTimeField()
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    is_public = models.IntegerField()
    is_removed = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    user = models.ForeignKey('NewuserNewuser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_comments'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoRedirect(models.Model):
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    old_path = models.CharField(max_length=200)
    new_path = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'django_redirect'
        unique_together = (('site', 'old_path'),)


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class FormsField(models.Model):
    field_order = models.IntegerField(db_column='_order', blank=True, null=True)  # Field renamed because it started with '_'.
    label = models.TextField()
    field_type = models.IntegerField()
    required = models.IntegerField()
    visible = models.IntegerField()
    choices = models.CharField(max_length=1000)
    default = models.CharField(max_length=2000)
    placeholder_text = models.CharField(max_length=100)
    help_text = models.TextField()
    form = models.ForeignKey('FormsForm', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forms_field'


class FormsFieldentry(models.Model):
    field_id = models.IntegerField()
    value = models.CharField(max_length=2000, blank=True, null=True)
    entry = models.ForeignKey('FormsFormentry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forms_fieldentry'


class FormsForm(models.Model):
    page_ptr = models.ForeignKey('PagesPage', models.DO_NOTHING, primary_key=True)
    content = models.TextField()
    button_text = models.CharField(max_length=50)
    response = models.TextField()
    send_email = models.IntegerField()
    email_from = models.CharField(max_length=254)
    email_copies = models.CharField(max_length=200)
    email_subject = models.CharField(max_length=200)
    email_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'forms_form'


class FormsFormentry(models.Model):
    entry_time = models.DateTimeField()
    form = models.ForeignKey(FormsForm, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forms_formentry'


class GalleriesGallery(models.Model):
    page_ptr = models.ForeignKey('PagesPage', models.DO_NOTHING, primary_key=True)
    content = models.TextField()
    zip_import = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'galleries_gallery'


class GalleriesGalleryimage(models.Model):
    field_order = models.IntegerField(db_column='_order', blank=True, null=True)  # Field renamed because it started with '_'.
    file = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    gallery = models.ForeignKey(GalleriesGallery, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'galleries_galleryimage'


class GenericAssignedkeyword(models.Model):
    field_order = models.IntegerField(db_column='_order', blank=True, null=True)  # Field renamed because it started with '_'.
    object_pk = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    keyword = models.ForeignKey('GenericKeyword', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'generic_assignedkeyword'


class GenericKeyword(models.Model):
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=2000)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'generic_keyword'


class GenericRating(models.Model):
    value = models.IntegerField()
    rating_date = models.DateTimeField(blank=True, null=True)
    object_pk = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    user = models.ForeignKey('NewuserNewuser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generic_rating'


class GenericThreadedcomment(models.Model):
    comment_ptr = models.ForeignKey(DjangoComments, models.DO_NOTHING, primary_key=True)
    rating_count = models.IntegerField()
    rating_sum = models.IntegerField()
    rating_average = models.FloatField()
    by_author = models.IntegerField()
    replied_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generic_threadedcomment'


class MeetingApplication(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    workplace = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(primary_key=True, max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    demand = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting_application'


class NewuserNewuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    name = models.CharField(max_length=20)
    workplace = models.CharField(max_length=30)
    gender = models.CharField(max_length=2)
    mobile = models.CharField(max_length=11)
    duty = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    resume = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newuser_newuser'


class NewuserNewuserGroups(models.Model):
    newuser = models.ForeignKey(NewuserNewuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'newuser_newuser_groups'
        unique_together = (('newuser', 'group'),)


class NewuserNewuserUserPermissions(models.Model):
    newuser = models.ForeignKey(NewuserNewuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'newuser_newuser_user_permissions'
        unique_together = (('newuser', 'permission'),)


class PagesLink(models.Model):
    page_ptr = models.ForeignKey('PagesPage', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pages_link'


class PagesPage(models.Model):
    keywords_string = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=2000)
    field_meta_title = models.CharField(db_column='_meta_title', max_length=500, blank=True, null=True)  # Field renamed because it started with '_'.
    description = models.TextField()
    gen_description = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    publish_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    short_url = models.CharField(max_length=200, blank=True, null=True)
    in_sitemap = models.IntegerField()
    field_order = models.IntegerField(db_column='_order', blank=True, null=True)  # Field renamed because it started with '_'.
    in_menus = models.CharField(max_length=100, blank=True, null=True)
    titles = models.CharField(max_length=1000, blank=True, null=True)
    content_model = models.CharField(max_length=50, blank=True, null=True)
    login_required = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pages_page'


class PagesRichtextpage(models.Model):
    page_ptr = models.ForeignKey(PagesPage, models.DO_NOTHING, primary_key=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'pages_richtextpage'


class TestappSitealert(models.Model):
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'testapp_sitealert'


class TwitterQuery(models.Model):
    type = models.CharField(max_length=10)
    value = models.CharField(max_length=140)
    interested = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'twitter_query'


class TwitterTweet(models.Model):
    remote_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    profile_image_url = models.CharField(max_length=200, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    retweeter_profile_image_url = models.CharField(max_length=200, blank=True, null=True)
    retweeter_user_name = models.CharField(max_length=100, blank=True, null=True)
    retweeter_full_name = models.CharField(max_length=100, blank=True, null=True)
    query = models.ForeignKey(TwitterQuery, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'twitter_tweet'
