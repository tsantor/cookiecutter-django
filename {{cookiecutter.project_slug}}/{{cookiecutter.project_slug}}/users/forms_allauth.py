from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms


class CustomSignupForm(SignupForm):
    """Override allauth default SignupForm."""

    # Add our custom form fields to the ones that already exist
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    address = forms.CharField(max_length=255)
    address_line2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    zip_code = forms.CharField(max_length=255)
    home_phone = forms.CharField(max_length=255)

    opt_in = forms.BooleanField(required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        user.address = self.cleaned_data["address"]
        user.address_line2 = self.cleaned_data["address_line2"]
        user.city = self.cleaned_data["city"]
        user.state = self.cleaned_data["state"]
        user.zip_code = self.cleaned_data["zip_code"]
        user.home_phone = self.cleaned_data["home_phone"]

        user.save()
        return user


class CustomSocialSignupForm(SocialSignupForm):
    """Override allauth default SignupForm."""

    # Add our custom form fields to the ones that already exist
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    address = forms.CharField(max_length=255)
    address_line2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    zip_code = forms.CharField(max_length=255)
    home_phone = forms.CharField(max_length=255)

    opt_in = forms.BooleanField(required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        user.address = self.cleaned_data["address"]
        user.address_line2 = self.cleaned_data["address_line2"]
        user.city = self.cleaned_data["city"]
        user.state = self.cleaned_data["state"]
        user.zip_code = self.cleaned_data["zip_code"]
        user.home_phone = self.cleaned_data["home_phone"]

        user.save()
        return user
