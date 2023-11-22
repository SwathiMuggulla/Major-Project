from django.db import models
from usersapp.models import *

# Create your models here.
class AttackerModel(models.Model):
  
    user_name=models.CharField(help_text='file_name',max_length=50,null=True)
    file_type=models.CharField(help_text='file_type',max_length=50,null=True)
    file_name=models.CharField(help_text='file_name',max_length=50,null=True)
    att_date=models.DateTimeField(help_text='att_date', auto_now_add=True,null=True)
    att_status=models.CharField(help_text='att_status',max_length=50,null=True)
    att_ip=models.CharField(help_text='att_ip',max_length=50,null=True)
    att_url=models.CharField(help_text='att_url',max_length=100,null=True)
    att_pc=models.TextField(help_text='att_pc',default='pc',null=True)
    
    
    
    file_enc=models.ForeignKey(FileModel,on_delete=models.CASCADE,related_name='data_file_details')

   
    class Meta:
        db_table='attacker_file_details'
