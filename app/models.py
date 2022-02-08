from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="create_time",help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True,verbose_name="last_time",help_text="上次登录时间")
    token = models.CharField(max_length=36,verbose_name="token",help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete",help_text="是否删除")
    czy = models.CharField(max_length=32,verbose_name="czy",help_text="操作人员")

    username = models.CharField(max_length=32,verbose_name="username",help_text="公司账号")
    password = models.CharField(max_length=32,verbose_name="password",help_text="公司密码")
    address = models.CharField(max_length=32,verbose_name="address",help_text="公司地址")

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="create_time",help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True,verbose_name="last_time",help_text="上次登录时间")
    token = models.CharField(max_length=36,verbose_name="token",help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete",help_text="是否删除")
    czy = models.CharField(max_length=32,verbose_name="czy",help_text="操作人员")

    image_url = models.CharField(max_length=255,verbose_name="image_url",help_text="存放图片的url")
    video_url = models.CharField(max_length=255, verbose_name="video_url", help_text="存放视频的url")
    name = models.CharField(max_length=36, verbose_name="name", help_text="课程名称")
    kcjj = models.TextField(verbose_name="kcjj", help_text="课程简介")


class Course_time(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="create_time",help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True,verbose_name="last_time",help_text="上次登录时间")
    token = models.CharField(max_length=36,verbose_name="token",help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete",help_text="是否删除")
    czy = models.CharField(max_length=32,verbose_name="czy",help_text="操作人员")

    start_time = models.DateTimeField(auto_now=False,verbose_name="start_time",help_text="课程开始时间")
    end_time = models.DateTimeField(auto_now=False, verbose_name="end_time", help_text="课程结束时间")
    teacher = models.ManyToManyField('teacher')
    course = models.ForeignKey('Course',on_delete=models.CASCADE)


class Course_choose(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="create_time",help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True,verbose_name="last_time",help_text="上次登录时间")
    token = models.CharField(max_length=36,verbose_name="token",help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete",help_text="是否删除")
    czy = models.CharField(max_length=32,verbose_name="czy",help_text="操作人员")

    User = models.ForeignKey('User',on_delete=models.CASCADE)
    course = models.ForeignKey('Course',on_delete=models.CASCADE)
    teacher = models.ForeignKey('teacher', on_delete=models.CASCADE)
    course_time = models.ForeignKey('Course_time', on_delete=models.CASCADE)


class teacher(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create_time", help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True, verbose_name="last_time", help_text="上次登录时间")
    token = models.CharField(max_length=36, verbose_name="token", help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete", help_text="是否删除")
    czy = models.CharField(max_length=32, verbose_name="czy", help_text="操作人员")

    image_url = models.CharField(max_length=255, verbose_name="image_url", help_text="存放图片的url")
    name = models.CharField(max_length=16, verbose_name="name", help_text="老师名字")
    phone = models.CharField(max_length=11,verbose_name="phone", help_text="老师手机号")
    emails = models.CharField(max_length=128,verbose_name="emails",help_text="电子邮箱")
    lsjj = models.TextField(verbose_name="lsjj", help_text="老师简介")

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create_time", help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True, verbose_name="last_time", help_text="上次登录时间")
    token = models.CharField(max_length=36, verbose_name="token", help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete", help_text="是否删除")
    czy = models.CharField(max_length=32, verbose_name="czy", help_text="操作人员")

    username = models.CharField(max_length=32, verbose_name="username", help_text="管理账号")
    password = models.CharField(max_length=32, verbose_name="password", help_text="密码")







#账款管家
class Zkgj(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create_time", help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True, verbose_name="last_time", help_text="上次登录时间")
    token = models.CharField(max_length=36, verbose_name="token", help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete", help_text="是否删除")
    czy = models.CharField(max_length=32, verbose_name="czy", help_text="操作人员")

    ywlx = models.ForeignKey('Ywlx', on_delete=models.CASCADE)
    khmc = models.ForeignKey("Khgl", on_delete=models.CASCADE)
    htmc = models.CharField(max_length=64, verbose_name="htmc", help_text="合同名称")
    htbh = models.CharField(max_length=64, verbose_name="htbh", help_text="合同编号")
    htbq = models.ForeignKey('Htbq', on_delete=models.CASCADE)
    htrq = models.DateTimeField(auto_now=False, verbose_name="htrq", help_text="合同日期")
    dqrq = models.DateTimeField(auto_now=False, verbose_name="dqrq", help_text="到期日期")
    qyrq = models.DateTimeField(auto_now=False, verbose_name="qyrq", help_text="签约日期")
    ssxm = models.ForeignKey('Xmgl', on_delete=models.CASCADE)
    jd = models.CharField(max_length=64, verbose_name="jd", help_text="街道")
    sq = models.CharField(max_length=64, verbose_name="sq", help_text="社区")
    htje = models.DecimalField( max_digits=10, decimal_places=2,verbose_name="htje", help_text="合同金额")
    xksgl = models.ForeignKey('Xksgl', on_delete=models.CASCADE)
    fwmj = models.DecimalField(max_digits=10,decimal_places=2, verbose_name="fwmj", help_text="服务面积")






#业务类型
class Ywlx(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create_time", help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True, verbose_name="last_time", help_text="上次登录时间")
    token = models.CharField(max_length=36, verbose_name="token", help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete", help_text="是否删除")
    czy = models.CharField(max_length=32, verbose_name="czy", help_text="操作人员")

    ywmc = models.CharField(max_length=32, verbose_name="ywmc", help_text="业务名称")

#客户管理
class Khgl(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create_time", help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True, verbose_name="last_time", help_text="上次登录时间")
    token = models.CharField(max_length=36, verbose_name="token", help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete", help_text="是否删除")
    czy = models.CharField(max_length=32, verbose_name="czy", help_text="操作人员")

    Khmc = models.CharField(max_length=32, verbose_name="Khmc", help_text="客户名称")
    Khbh = models.CharField(max_length=32, verbose_name="Khbh", help_text="客户编号")
    Khxz = models.CharField(max_length=32, verbose_name="Khxz", help_text="客户性质")


#合同标签
class Htbq(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create_time", help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True, verbose_name="last_time", help_text="上次登录时间")
    token = models.CharField(max_length=36, verbose_name="token", help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete", help_text="是否删除")
    czy = models.CharField(max_length=32, verbose_name="czy", help_text="操作人员")

    bqmc = models.CharField(max_length=32, verbose_name="bqmc", help_text="标签名称")


#项目管理
class Xmgl(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create_time", help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True, verbose_name="last_time", help_text="上次登录时间")
    token = models.CharField(max_length=36, verbose_name="token", help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete", help_text="是否删除")
    czy = models.CharField(max_length=32, verbose_name="czy", help_text="操作人员")

    xmmc = models.CharField(max_length=64, verbose_name="xmmc", help_text="项目名称")

#消控室管理
class Xksgl(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create_time", help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True, verbose_name="last_time", help_text="上次登录时间")
    token = models.CharField(max_length=36, verbose_name="token", help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete", help_text="是否删除")
    czy = models.CharField(max_length=32, verbose_name="czy", help_text="操作人员")

    xksmc = models.CharField(max_length=64, verbose_name="xksmc", help_text="消控室名称")


#部门管理
class Bmgl(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create_time", help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True, verbose_name="last_time", help_text="上次登录时间")
    token = models.CharField(max_length=36, verbose_name="token", help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete", help_text="是否删除")
    czy = models.CharField(max_length=32, verbose_name="czy", help_text="操作人员")

    bmmc = models.CharField(max_length=32, verbose_name="bmmc", help_text="部门名称")

#部门人员
class Bmry(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create_time", help_text="创建时间")
    last_time = models.DateTimeField(auto_now=True, verbose_name="last_time", help_text="上次登录时间")
    token = models.CharField(max_length=36, verbose_name="token", help_text="uuid")
    is_delete = models.BooleanField(verbose_name="is_delete", help_text="是否删除")
    czy = models.CharField(max_length=32, verbose_name="czy", help_text="操作人员")

    bm = models.ForeignKey('Bmgl', on_delete=models.CASCADE)
    rymc = models.CharField(max_length=32, verbose_name="rymc", help_text="人员名称")
    phone = models.CharField(max_length=11, verbose_name="phone", help_text="手机号")
    zw = models.CharField(max_length=32, verbose_name="zw", help_text="职位")


#     name = models.CharField(max_length=32)
#     city = models.CharField(max_length=64)
#     email = models.EmailField()
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=32)
#     age = models.SmallIntegerField()
#     au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)
#
#
# class AuthorDetail(models.Model):
#     gender_choices = (
#         (0, "女"),
#         (1, "男"),
#         (2, "保密"),
#     )
#     gender = models.SmallIntegerField(choices=gender_choices)
#     tel = models.CharField(max_length=32)
#     addr = models.CharField(max_length=64)
#     birthday = models.DateField()