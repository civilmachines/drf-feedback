from django.db import models
from drfaddons.models import CreateUpdateModel


class Feedback(CreateUpdateModel):
    """
    A Feedback model for recording the user drf_feedback.
    """
    from django.utils.text import gettext_lazy as _
    from django.contrib.auth import get_user_model

    ip = models.GenericIPAddressField(_('IP'), )
    name = models.CharField(_('Name'), max_length=254)
    url = models.URLField(_('URL'), )
    email = models.EmailField(_('Email'),)
    mobile = models.CharField(_('Mobile Number'), max_length=15, blank=True)
    message = models.TextField(_('Message'),)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return 'Feedback -- ' + str(self.name)

    class Meta:
        from django.utils.text import gettext_lazy as _

        ordering = ('-create_date', )
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')
