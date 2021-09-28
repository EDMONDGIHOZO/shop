from typing import ClassVar
from django.contrib.auth.forms import UserCreationForm


class CustomerCreationForm (UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
