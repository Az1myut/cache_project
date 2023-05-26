from django.core.cache import cache
from django.core.mail import send_mail, send_mass_mail
from django.db import models
from django.db.models.signals import (
    post_delete, post_save, pre_delete, pre_save,
)
from django.dispatch import receiver
from django.utils import timezone

from .email import email_template
from .transliterator import transliterator

# from django.template.defaultfilters import slugify
# from pytils.translit import slugify


# Create your models here.

class Genre(models.Model):
    genre = models.CharField(
        'Название жанра', max_length=150, default='', null=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f"Название жанра \"{self.genre}\""

    def get_absolute_url(self):
        return self.pk


class Book(models.Model):
    name = models.CharField(
        'Название книги', max_length=150, default='', null=True)
    slug = models.CharField('slug', max_length=150, default="", blank=True)
    is_published = models.BooleanField('Опубликовано', default=False)
    pub_date = models.DateTimeField('Дата заполнения', default=timezone.now,
                                    blank=True)
    genre = models.ForeignKey(
        'Genre', on_delete=models.CASCADE, default='Без категории', verbose_name="Жанры")

    def __str__(self):
        return f"Название книги {self.name}"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        # db_table = 'books'

    def get_absolute_url(self):
        return self.pk


@receiver(pre_save, sender=Book)
def book_pre_created_or_saved(sender, instance, **kwargs):

    instance.slug = transliterator.latinizator(
        instance.name, transliterator.legend).lower()

    for book in Book.objects.all():
        if book.pk != instance.pk:
            print(book.name)
            # instance.slug = slugify(instance.name)


@receiver(post_save, sender=Book)
def book_created_or_saved(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject=email_template.new_book['subject'],
            message=email_template.new_book['message'],
            from_email=email_template.from_email,
            recipient_list=email_template.recipient_list,
            fail_silently=False,
            html_message=email_template.new_book['html_message'],
        )
    else:
        message1 = (
            email_template.saved_book['subject'],
            email_template.saved_book['html_message'].format(
                name=instance.name),
            email_template.from_email,
            email_template.recipient_list,
        )
        message2 = (
            email_template.testing_message['subject'],
            email_template.testing_message['html_message'].format(
                name=instance.name),
            email_template.from_email,
            email_template.recipient_list.append(email_template.testing_email),
        )
        send_mass_mail((message1, message2), fail_silently=False)
    # cache.set('book::%(id)d' % {'id': instance.id}, instance)


@ receiver(pre_delete, sender=Book)
def book_deleted(sender, instance, **kwargs):
    send_mail(
        subject=email_template.deleted_book['subject'],
        message=email_template.deleted_book['message'].format(
            name=instance.name),
        from_email=email_template.from_email,
        recipient_list=email_template.recipient_list,
        fail_silently=False,
        html_message=email_template.deleted_book['html_message'].format(
            name=instance.name),
    )
    books = Book.objects.filter(pk__ne=instance.pk).count()
    print(books)


@ receiver(post_delete, sender=Book)
def book_deleted(sender, instance, **kwargs):
    send_mail(
        subject=email_template.deleted_book['subject'],
        message=email_template.deleted_book['message'].format(
            name=instance.name),
        from_email=email_template.from_email,
        recipient_list=email_template.recipient_list,
        fail_silently=False,
        html_message=email_template.deleted_book['html_message'].format(
            name=instance.name),
    )
    # cache.delete('book::%(id)d' % {'id': instance.id})
