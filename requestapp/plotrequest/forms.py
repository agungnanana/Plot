from django import forms
from .import options

def get_options(kind):
    form_choices = None
    if kind == 'edm':
        form_choices = EDMChoicesForm()
    elif kind == 'gps':
        form_choices = GPSChoicesForm()
    elif kind == 'magnitude':
        form_choices = MagnitudeChoicesForm()
    elif kind == 'seismicity':
        form_choices = SeismicityChoicesForm()
    elif kind == 'borehole':
        form_choices = BoreholeChoicesForm()
    elif kind == 'platform':
        form_choices = PlatformChoicesForm()
    elif kind == 'rsam':
        form_choices = RSAMChoicesForm()
    return form_choices


class GraphChoicesForm(forms.Form):
    kind = forms.ChoiceField(
        label='Select graph:',
        choices=options.GRAPH_CHOICES,
        initial=options.GRAPH_CHOICES[0][0],
        widget=forms.Select(attrs={'class': 'form-control ra-dropdown'})
    )


class PeriodChoicesForm(forms.Form):
    period = forms.ChoiceField(
        label='Select period:',
        choices=options.PERIOD_CHOICES,
        initial=options.PERIOD_CHOICES[0][0],
        widget=forms.Select(attrs={'class': 'form-control ra-dropdown'})
    )


class GPSChoicesForm(forms.Form):
    station = forms.MultipleChoiceField(
        choices=options.GPS_STATIONS,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )


class RSAMChoicesForm(forms.Form):
    station = forms.MultipleChoiceField(
        choices=options.RSAM_STATIONS,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )


class BoreholeChoicesForm(forms.Form):
    station = forms.MultipleChoiceField(
        choices=options.TILTMETER_BOREHOLE_STATIONS,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )


class PlatformChoicesForm(forms.Form):
    station = forms.MultipleChoiceField(
        choices=options.TILTMETER_PLATFORM_STATIONS,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )


class SeismicityChoicesForm(forms.Form):
    event_type = forms.MultipleChoiceField(
        choices=options.SEISMIC_EVENT_TYPES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )


class EDMChoicesForm(forms.Form):
    reflector = forms.MultipleChoiceField(
        choices=options.EDM_REFLECTORS,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
    )


class RequestForm(forms.Form):
    starttime = forms.DateTimeField(
        label='Start date:',
        required=True,
        widget=forms.DateTimeInput(attrs={'class': 'form-control'})
    )
    endtime = forms.DateTimeField(
        label='End date:',
        required=True,
        widget=forms.DateTimeInput(attrs={'class': 'form-control'})
    )
