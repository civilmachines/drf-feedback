from django.db import models
from django.utils.text import gettext_lazy as _


class Feedback(models.Model):
    """
    A Feedback model for recording the user feedback.
    """

    created = models.DateTimeField(_('Created Date'), auto_now_add=True)
    ip = models.GenericIPAddressField(_('IP'), )
    name = models.CharField(_('Name'), max_length=254)
    url = models.URLField(_('URL'), )
    form_name = models.CharField(_('Form Name'), max_length=50)
    email = models.EmailField(_('Email'), blank=True)
    phone_number = models.CharField(_('Phone Number'), max_length=15, blank=True)
    message = models.TextField(_('Message'), blank=True)

    def __str__(self):
        return 'Feedback -- ' + str(self.name)

    class Meta:
        ordering = ('-created', )
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def get_saved_data(self):
        return {
            'pk': self.pk,
            'created': self.created,
            'ip': self.ip,
            'name': self.name,
            'url': self.url,
            'form_name': self.form_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'message': self.message
        }

