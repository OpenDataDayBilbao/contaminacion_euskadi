# coding: utf-8

from django import forms

# Create your forms here.

PARTICLES = (
    ('Benzene', 'Benzene'),
    ('CO', 'CO'),
    ('Ethylbenzene', 'Ethylbenzene'),
    ('NH3', 'NH3'),
    ('NMHC', 'NMHC'),
    ('PM10', 'PM10'),
    ('SH2', 'SH2'),
    ('Toluene', 'Toluene'),
    ('Xylene', 'Xylene'),
)


#########################
# Class: ParticleForm
#########################

class ParticleForm(forms.Form):
    particle = forms.ChoiceField(choices = PARTICLES, initial = "Benzene", required = True)
    start_date = forms.CharField(max_length = 150, required = True)
    end_date = forms.CharField(max_length = 150, required = True)
