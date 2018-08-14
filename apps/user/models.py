from django.db import models
from Wh1802Django.settings import SEX_CHOICES, DB_FIELD_VALID_CHOICES, \
   DINNER_CHOICES, PAY_CHOICES, ACTIVATE_CHOICES
# Create your models here.
from django.utils import timezone


'''
会员信息
'''
class ArtsUser(models.Model):
   username = models.CharField(max_length=50, verbose_name="用户名")
   password = models.CharField(max_length=80, verbose_name="密码")
   email = models.EmailField(verbose_name="邮箱")
   token = models.CharField(default='', max_length=50, verbose_name="token字段")
   is_active = models.IntegerField(default=0, verbose_name="是否激活", choices=ACTIVATE_CHOICES)
   createtime = models.DateTimeField(default=timezone.now, db_index=True,
                           verbose_name="添加时间")
   flag = models.IntegerField(default=0, verbose_name="控制字段", choices=DB_FIELD_VALID_CHOICES)

   def __str__(self):
      return self.username


   class Meta:
      verbose_name = "会员信息"
      verbose_name_plural = verbose_name
      db_table = "arts_user"
      ordering = ["-createtime"]




