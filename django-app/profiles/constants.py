from django.utils.translation import ugettext_lazy as _

# Errors 
ERROR_INCORRECT_CREDENTIALS = _('Incorrect email or password')
ERROR_WEAK_PASSWORD = _("""Your password must consist of at least {} characters and two of the following types: 
uppercase letter / number / special symbol.""")
ERROR_LONG_PASSWORD  = _("Your password is too long. Password should be up to {} characters long.")
ERROR_IS_NOT_DEMO_USER  = _("Yout account type is not a demo type.")