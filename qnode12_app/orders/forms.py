from django import forms
from .models import Order
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .widget import DatePickerInput, TimePickerInput,  DateTimePickerInput
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput , MonthPickerInput, YearPickerInput


class MyDatePickerInput(DatePickerInput):
    template_name = 'orders/order/date-picker.html'


class OrderCreateForm(forms.ModelForm):
    agree_term= forms.BooleanField(required=True,help_text="I accept the terms and conditions of this services.")
    phone = PhoneNumberField(
        region="CA",
        widget=PhoneNumberPrefixWidget(
            country_choices=[
                 ("US", "United States"),
                 ("MX", "Mexico"),
                 ("CA", "Canada"),
                 ("PA", "Panama"),
                 ("CO", "Colombia"),
                 ("VE", "Venezuela"),
                 ("EC", "Ecuador"),
                 ("PE", "Perú"),
                 ("CL", "Chile"),
                 ("BO", "Bolivia"),
                 ("BR", "Brazil"),
                 ("AR", "Argentina"),
                 ("ES", "Spain"),
                 ("FR", "France"),
                 ("IT", "Italy"),
                 ("DE", "Germany"),
                 ("CH", "Switzeland"),
                 ("NL", "Netherlands"),
                 ("UK", "United Kingdown"),
                 ("BE", "Belgium"),
                 ("SE", "Sweden"),
                 ("DK", "Dinamark"),
                 ("RU", "Russian"),
                 ("CN", "China"),
                 ("JP", "japan"),
                 ("AU", "Australia"),

            ],
        ), help_text="Choice you local country extension number"
    )

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email','phone','arrival_date_time','departure_date_time','agree_term']
        widgets = {
            'arrival_date_time':  DateTimePickerInput(format='%m/%d/%Y %H:%M'),
            'departure_date_time':  DateTimePickerInput(format='%m/%d/%Y %H:%M'),
        #    'end_departure_date':  DateTimePickerInput(options={
        #            "format": "MM/DD/YYYY",
        #            "locale": "ec",
        #        }).end_of('event days'),
        #    'start_arrival_time': DateTimePickerInput().start_of('party time'),
        #    'end_departure_time': DateTimePickerInput(options={
        #            "format": "MM/DD/YYYY", # moment date-time format
        #            "showClose": True,
        #            "showClear": True,
        #            "showTodayButton": True,
        #        }).end_of('party time'),
        }
       # widgets = {
       #     'arrival' : DateTimePickerInput(),
       #     'departure' : DateTimePickerInput(),
       # }
