from django.db import models


class {{cookiecutter.app_class_name}}(models.Model):
    name = models.CharField(verbose_name='Name', max_length=60)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = '{{cookiecutter.app_class_name}}'
        verbose_name_plural = '{{cookiecutter.app_class_name}}s'
