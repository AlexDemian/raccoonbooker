from django.core.exceptions import ValidationError
from profiles.constants import ERROR_WEAK_PASSWORD, ERROR_LONG_PASSWORD

class WeakPasswordValidator:
    """Generic password validator.

    This class used in settings.base and provides password validation rules.

    Attributes:
        min_length (int): minimal required password length
    """

    def __init__(self, min_length=8):
        """Inits with default min_length attribute."""

        self.min_length = min_length
        self.accepted_special_chars = "[~\!,@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        self.help_message = (ERROR_WEAK_PASSWORD).format(self.min_length)

    def validate(self, password, user=None):
        """Performs password validation.

        Args:
            password (str): password valued variable
            user (obj): optional user object kwarg(not used)

        Raises:
            ValidationError: occurs on weak password
        """

        necessary_condition = len(password) >= self.min_length
        optional_conditions = [
            any(char.isupper() for char in password),
            any(char.isdigit() for char in password),
            any(char in self.accepted_special_chars for char in password),
        ]
        if not necessary_condition or sum(optional_conditions) < 2:
            raise ValidationError(self.help_message,
                code='password_is_too_weak',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return self.help_message


class MaxLengthPasswordValidator:
    """Max length assword validator.

    This class used in settings.base and provides password validation rules.

    Attributes:
        max_length (int): required maximum password length
    """

    def __init__(self, max_length=100):
        """Inits with default max_length attribute."""

        self.max_length = max_length
        self.help_message = ERROR_LONG_PASSWORD.format(self.max_length)

    def validate(self, password, user=None):
        """Performs password validation.

        Args:
            password (str): password valued variable
            user (obj): optional user object kwarg(not used)

        Raises:
            ValidationError: occurs on password is too long case
        """

        if len(password) > self.max_length:
            raise ValidationError(self.help_message,
                code='password_is_too_long',
                params={'max_length': self.max_length},
            )

    def get_help_text(self):
        return self.help_message
