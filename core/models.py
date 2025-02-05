from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя"""
    
    class Meta:
        """Мета-класс для кореектного отображения полей пользователя в админ панели"""
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        #TODO: 'Добавить сортировку по полям'
