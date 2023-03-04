from django import forms

from .models import UserReservation

class UserReservationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "type": "text",
            "name": "name",
            "class": "form-control",
            "id": "name",
            "placeholder": "Your Name",
            "data-rule": "minlen:4",
            "data-msg": "lease enter at least 4 chars"
        })
    )

    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "type": "email",
            "class": "form-control",
            "name": "email",
            "id": "email",
            "required": "required",
            "placeholder": "Your Email",
            "data-rule": "email",
            "data-msg": "Please enter a valid email"
        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "form-control",
            "name": "phone",
            "id": "phone",
            "required": "required",
            "placeholder": "Your Phone",
            "data-rule": "minlen:4",
            "data-msg": "Please enter at least 4 chars"
        })
    )

    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
        "type": "number",
        "class": "form-control",
        "name": "people",
        "id": "people",
        "required": "required",
        "placeholder": "# of people",
        "data-rule": "minlen:1",
        "data-msg": "Please enter at least 1 chars"
    }))
    #dateonly = forms.DateField(
    #    widget=forms.DateInput(attrs={
    #        "type": "text",
    #        "class": "form-control",
    #        "name": "dateonly",
    #        "id": "dateonly",
    #        "required": "required",
    #        "placeholder": "date",
    #        "data-rule": "minlen:4",
    #        "data-msg": "Please enter at least 4 chars"
    #    })
    #)

    #timeonly = forms.TimeField(
    #    widget=forms.TimeInput(attrs={
    #        "type": "text",
    #        "class": "form-control",
    #        "name": "timeonly",
    #        "id": "timeonly",
    #        "required": "required",
    #        "placeholder": "time",
    #        "data-rule": "minlen:4",
    #        "data-msg": "Please enter at least 4 chars"
    #    })
    #)

    message = forms.CharField(max_length=200,
                                      widget=forms.Textarea(attrs={
                                          "type": "message",
                                          "class": "form-control",
                                          "name": "message",
                                          "rows": "5",
                                          "required": "required",
                                          "placeholder": "Message"

                                      }))


    class Meta:
        model = UserReservation
        fields = ("name", "email", "phone", "persons", "message")