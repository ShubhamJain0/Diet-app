from django import forms



class detailsform(forms.Form):

	Name=forms.CharField(label='Name')
	Age=forms.IntegerField(min_value=3, max_value=50, widget=forms.NumberInput)
	weight=forms.IntegerField(min_value=0, max_value=200)
	Deficiency=forms.CharField()
