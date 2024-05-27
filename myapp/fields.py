from django.db import models
from django.core.exceptions import ValidationError
import re

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            return value
        if not isinstance(value, str):
            raise ValidationError("This field requires a string value.")
        if not re.match(r'^#[0-9A-Fa-f]{6}$', value):
            raise ValidationError("This field requires a valid hexadecimal color code.")
        return value

    def get_prep_value(self, value):
        return str(value)

    def formfield(self, **kwargs):
        from django.forms import CharField
        defaults = {
            'form_class': CharField,
            'max_length': self.max_length,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
