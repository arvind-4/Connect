"""Forms for the accounts app."""

from typing import Any

from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from django.contrib.auth.forms import (
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    UserCreationForm,
)

User = get_user_model()


class SignUpForm(UserCreationForm):
    """Sign up form."""

    email = forms.EmailField(
        max_length=30, help_text="Required. Add a valid E-mail address."
    )

    class Meta:
        """Meta class."""

        model = User
        fields = ("email", "password1", "password2")

    def clean_email(self, *_args: tuple[Any, ...], **_kwargs: dict[str, Any]) -> str:
        """Clean email."""
        form_email = self.cleaned_data.get("email")
        qs_email = User.objects.filter(email=form_email)
        if qs_email.exists() and qs_email.count() == 1:
            information = (
                "The User with the Email is Already Registered! Try Signing In."
            )
            raise forms.ValidationError(information)
        return form_email

    def clean_password2(self) -> str:
        """Clean password2."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            information = "The Passwords didn't Match! Try Again."
            raise forms.ValidationError(information)
        return password2

    def __init__(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        """Initialize the form."""
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = (
                "py-2 px-3 border border-gray-300"
                "focus:border-red-300 focus:outline-none"
                "focus:ring focus:ring-red-200 focus:ring-opacity-50"
                "rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full"
            )


class SignInForm(forms.Form):
    """Sign in form."""

    email = forms.EmailField(
        max_length=30, help_text="Required. Add a valid E-mail address."
    )
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean_password(self) -> str:
        """Clean password."""
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if not authenticate(email=email, password=password):
            msg = "Invalid Username or Password!"
            raise forms.ValidationError(msg)
        return password

    def __init__(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        """Initialize the form."""
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = (
                "py-2 px-3 border border-gray-300"
                "focus:border-red-300 focus:outline-none"
                "focus:ring focus:ring-red-200 focus:ring-opacity-50"
                "rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full"
            )


class ForgotPasswordForm(PasswordResetForm):
    """Forgot password form."""

    email = forms.EmailField(required=True)

    def clean_email(self, *_args: tuple[Any, ...], **_kwargs: dict[str, Any]) -> str:
        """Clean email."""
        form_email = self.cleaned_data.get("email") or None
        if form_email is None:
            information1 = "Email is Required!"
            raise forms.ValidationError(information1)
        qs = User.objects.filter(email=form_email)
        if not qs.exists() and qs.count != 1:
            information2 = (
                "The Entered Email does'nt have an Account!"
                "Please Sign Up for a Free Account."
            )
            raise forms.ValidationError(information2)
        return form_email

    def __init__(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        """Initialize the form."""
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = (
                "block w-full p-2 border rounded border-gray-300"
                "focus:outline-none focus:ring-1 focus:ring-gray-400"
                "focus:border-transparent"
            )


class PasswordResetConfirmForm(SetPasswordForm):
    """Password reset confirm form."""

    class Meta:
        """Meta class."""

        model = User
        fields = "__all__"

    def clean_new_password2(self) -> str:
        """Clean new password2."""
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 != password2:
            information = "The Passwords didn't Match! Try Again."
            raise forms.ValidationError(information)
        return password2

    def __init__(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        """Initialize the form."""
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = (
                "block w-full p-2 border rounded border-gray-300"
                "focus:outline-none focus:ring-1 focus:ring-gray-400"
                "focus:border-transparent"
            )


class ChangeUserPassword(PasswordChangeForm):
    """Change user password form."""

    class Meta:
        """Meta class."""

        model = User
        fields = "__all__"

    def clean_new_password2(self) -> str:
        """Clean new password2."""
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 != password2:
            information = "The Passwords didn't Match! Try Again."
            raise forms.ValidationError(information)
        return password2

    def __init__(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        """Initialize the form."""
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
