from django import forms
#from .models import NIKKEI,SP500,USDJPY,BITCOIN
from django.contrib.admin.widgets import AdminDateWidget
"""
class StartDateForm(forms.Form):
    class Meta:
        model = NIKKEI
        date_search_start = 'date'
        widgets = {
            'created_at': forms.SelectDateWidget
        }
"""
class StartDateForm(forms.Form):
    #name_search = forms.CharField(label='名前検索',required=False)
    date_search_start = forms.DateField(label='開始日時',required=True,widget=forms.DateInput(attrs={"type":"date"}))




class EndDateForm(forms.Form):
    #name_search = forms.CharField(label='名前検索',required=False)
    date_search_end = forms.DateField(label='終了日時',required=True,widget=forms.DateInput(attrs={"type":"date"}))

class SP500StartDateForm(forms.Form):
    #name_search = forms.CharField(label='名前検索',required=False)
    date_search_start = forms.DateField(label='開始日時',required=False)

class SP500EndDateForm(forms.Form):
    #name_search = forms.CharField(label='名前検索',required=False)
    date_search_end = forms.DateField(label='終了日時',required=False)

"""
class NIKKEIForm(forms.ModelForm):
    class Meta:
        model = NIKKEI
        fields = ['date', 'close']

"""