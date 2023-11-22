from django.db import models

# Create your models here.
class UserModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(help_text='user_name',max_length=50,null=True)
    user_email=models.EmailField(help_text='user_email',max_length=50)
    user_password=models.CharField(help_text='user_password',max_length=50,null=True)
    user_contact=models.CharField(help_text='user_contact', max_length=50,null=True)
    user_city=models.CharField(help_text='user_city', max_length=200,null=True)
    user_dob=models.DateField(help_text='user_dob',max_length=50,null=True)
    user_ip=models.CharField(help_text='user_ip',max_length=50,null=True)
    user_image=models.ImageField(upload_to='media/',null=True)

    class Meta:
        db_table='user_complete_details'

class FileModel(models.Model):

    file_id=models.AutoField(primary_key=True)
    file_name=models.CharField(help_text='file_name',max_length=50,null=True)
    file_type=models.CharField(help_text='file_type',max_length=50,null=True)
    file_date=models.DateField(help_text='file_data', auto_now_add=True,null=True)
    file_upload=models.FileField(upload_to='media/',null=True)
    file_status=models.CharField(help_text='file_status',max_length=50,default='verification in process',null=True)
    attack_status=models.CharField(help_text='attack_status',max_length=50,null=True)
    file_path=models.CharField(help_text='file_path',max_length=100,null=True)
    user=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='user_complete_details',null=True)

    class Meta:
        db_table='data_file_details'