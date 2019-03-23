from django import forms

class Login(forms.Form):

	#python data type

	# integer_field = forms.IntegerField(required=False);
	# decimal_field = forms.DecimalField(required=False);
	# float_field = forms.FloatField(required=False);
	# boolean_field = forms.BooleanField(required=False);
	# char_field = forms.CharField(required=False);


	# #String Input

	# email_field = forms.EmailField(required=False)
	# ragex_field = forms.RegexField(required=False)
	# slug_field = forms.SlugField(required=False)
	# url_field = forms.URLField(required=False)
	# ip_field = forms.GeneralIpAddressField(required=False)

	# #select Input

	# PILIHAN = (

	# 		('nilai 1', 'pilihan 1'),
	# 		('nilai 2', 'pilihan 2'),
	# 		('nilai 3', 'pilihan 3'),

	# 	)

	# choice_field = forms.ChoiceField(choices=PILIHAN)
	# multi_choice_field = forms.MultipleChoiceField(choices=PILIHAN)
	# multi_type_choice = forms.TypedMultipleChoiceField(choices=PILIHAN)
	# null_boolean+field = forms.NullBooleanField(choices=PILIHAN)

	# #date time

	# date_field = forms.DateField()
	# datatime_field = forms.DateTimeField()
	# duration_field = forms.DurationField()
	# time_field = forms.TimeField()
	# splitdatetime_field = forms.SplitDateTimeField()

	# #file input

	# file_field = forms.FileField()
	# image_field = forms.ImageField()


	username = forms.CharField(required=True)
	password = forms.CharField(required=True)	