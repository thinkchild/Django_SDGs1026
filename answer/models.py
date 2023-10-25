from django.db import models

# Create your models here.
class answer0(models.Model):
  bname = models.CharField(max_length=20, null=False)

  # 網站回覆內容
  bresponse = models.TextField(blank=True, default='')

  def _str_(self):
    return self.btitle



class Person(models.Model):
  sID = models.CharField(max_length=20, null=False) # 學號
  stdName = models.CharField(max_length=30, null=False) # 姓名
  stdPasswd = models.CharField(max_length=10, default="passwd", null=False) # 密碼
  stdSex = models.CharField(max_length=2, default="M", null=False) # 性別
  stdGrade = models.CharField(max_length=10, default="5", null=False) # 年級
  stdClass = models.CharField(max_length=255, default="class", null=False) # 班級
  CP = models.CharField(max_length=200, null=True) # 國家能力值
  CV  = models.CharField(max_length=200, null=True) #貢獻值

  def __str__(self):
    return self.sID