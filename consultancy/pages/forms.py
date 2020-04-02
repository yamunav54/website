from django import forms

from .models import Uploaderform
from .models import contactusform



class Uploader(forms.ModelForm):
    class Meta:
        model = Uploaderform
        fields =['FIRSTNAME','LASTNAME','QUALIFICATION','PHONENO','EMAIL','COUNTRY','RESUMEUPLOAD']

class Contactussubmit(forms.ModelForm):
    class Meta:
        model = contactusform
        fields =['FIRSTNAME','LASTNAME','PHONENO','EMAIL','MESSAGE']