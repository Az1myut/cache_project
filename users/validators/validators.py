from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ValidationError
from django.utils import timezone

# def validate_age(value):
#     age = relativedelta(timezone.now().date(), value).years
#     if age < 18:
#         raise ValidationError('Вам должно быть от 18 лет.')


def validate_age(value):
    age = abs((timezone.now().date() - value)).days

    if age < (18 * 365):
        raise ValidationError('Вам должно быть от 18 лет.')
