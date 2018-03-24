
from datetime import datetime

from django.db import models

# Create your models here.

# 课程


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"课程名")
    desc = models.CharField(max_length=500, verbose_name=u"课程描述")
    detail = models.TextField( verbose_name=u"课程详情")
    degree = models.CharField(verbose_name=u"课程难度", choices=(("sj","初级"),("zj","中级"),("gj","高级")),max_length=2)
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时长(分钟)")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"封面图",max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#课程章节


class Lesson(models.Model):
    # 数据库一对多 models.ForeignKey
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节介绍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
#


class Video(models.Model):
    # 数据库一对多 models.ForeignKey
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100,verbose_name=u"视频名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name=u"下载地址")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name