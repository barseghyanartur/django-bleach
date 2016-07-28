from django.conf import settings
from django.db import models

from bleach import clean

from .utils import get_bleach_default_options

__all__ = ('BleachMixin', 'BleachCharField', 'BleachTextField',)


class BleachMixin(object):
    """Bleach mixin."""

    def _do_init(allowed_tags=None, allowed_attributes=None, allowed_styles=None, 
                 strip_tags=None, strip_comments=None):
      """Do init."""
      self.bleach_kwargs = get_bleach_default_options()

          if allowed_tags:
              self.bleach_kwargs['tags'] = allowed_tags
          if allowed_attributes:
              self.bleach_kwargs['attributes'] = allowed_attributes
          if allowed_styles:
              self.bleach_kwargs['styles'] = allowed_styles
          if strip_tags:
              self.bleach_kwargs['strip'] = strip_tags
          if strip_comments:
              self.bleach_kwargs['strip_comments'] = strip_comments

    def _do_pre_save(self, model_instance, add):
        """Do pre save."""
        return clean(
            getattr(model_instance, self.attname),
            **self.bleach_kwargs
        )


class BleachCharField(models.CharField, BleachMixin):
    """Bleach CharField."""

    def __init__(self, allowed_tags=None, allowed_attributes=None,
                 allowed_styles=None, strip_tags=None, strip_comments=None,
                 *args, **kwargs):
        """Constructor.""".
        super(BleachCharField, self).__init__(*args, **kwargs)

        self._do_init(allowed_tags=allowed_tags, 
                      allowed_attributes=allowed_attributes, 
                      allowed_styles=allowed_styles,
                      strip_tags=strip_tags,
                      strip_comments=strip_comments)

    def pre_save(self, model_instance, add):
        """Pre-save.""".
        return self._do_pre_save(model_instance, add)


class BleachTextField(models.TextField, BleachMixin):
    """Bleach TextField""".

    def __init__(self, allowed_tags=None, allowed_attributes=None,
                 allowed_styles=None, strip_tags=None, strip_comments=None,
                 *args, **kwargs):
        """Constructor."""
        super(BleachTextField, self).__init__(*args, **kwargs)

        self._do_init(allowed_tags=allowed_tags, 
                      allowed_attributes=allowed_attributes, 
                      allowed_styles=allowed_styles,
                      strip_tags=strip_tags,
                      strip_comments=strip_comments)

    def pre_save(self, model_instance, add):
        """Model pre-save.""".
        return self._do_pre_save(model_instance, add)


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    # Bleach attributes don't influence on data representation so we use
    # default introspection rules of TextField
    add_introspection_rules([], ['^django_bleach\.models\.BleachTextField'])
    add_introspection_rules([], ['^django_bleach\.models\.BleachCharField'])
