from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(verbose_name='标题', max_length=128, default='无题')
    text = models.TextField(verbose_name='内容')
    create_date = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    pub_date = models.DateTimeField(verbose_name='发布时间', blank=True, null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
