# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from newuser.models import NewUser
# from testapp.models import MyProfile
#
#
# @receiver(post_save, sender=MyProfile)
# def user_save(sender, instance, created, **kwargs):
#     if created and instance:
#         print(instance)
#         NewUser.objects.filter(id=instance.user_id).update(name=instance.name)
#     else
#         print("no")
