from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Сategory(models.Model):
    name = models.CharField(max_length=128, verbose_name='Раздел', db_index=True)
    tags = models.ManyToManyField(Article, related_name='scopess', through='Membership')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

    def __str__(self):
        return self.name



class Membership(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Сategory, on_delete=models.CASCADE, related_name='scopes', verbose_name='Раздел',)
    is_main = models.BooleanField(default=False, verbose_name='Основной',)

    class Meta:
        verbose_name = 'Тематики статья'
        verbose_name_plural = ' Тематики статьи'

    def __str__(self):
        return '{0}_{1}'.format(self.article, self.tag)