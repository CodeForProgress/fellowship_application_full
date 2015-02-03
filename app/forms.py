from django import forms
from django.forms import CharField, Form, PasswordInput, IntegerField, ChoiceField, BooleanField, FileField, Textarea, RadioSelect, EmailField, DateField, FileField
from django.contrib.auth.models import User
from app.models import User, Applicant, Recommender, Recommendation, Evaluation
from django.forms.extras.widgets import SelectDateWidget
from django_countries.fields import CountryField
from django_countries import countries
from localflavor.us.us_states import STATE_CHOICES
from django.contrib.auth import authenticate, login, logout


# Adds the 'Select' placeholder to fields using countries
places = ()
select = ('','Select...')
places +=select,
for c in countries:
    places +=c,

states = ()
states +=select,
for s in STATE_CHOICES:
    states +=s,
states += ('O','Other'),


class CustomLoginForm(Form):
    username = CharField(required=True, max_length=75, label="Username or email")
    password = CharField(widget=PasswordInput(), required=True, max_length=45, label = "Password")

    def clean(self):
        username = self.cleaned_data.get('username')[0:30]
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Hmm, that wasn't the right username or password.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')[0:30]
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user



class CreateAccountForm(Form):
    first_name = CharField(required=True, max_length=30, label="First name(s)")
    last_name = CharField(required=True, max_length=30, label = "Last name(s)")
    email = EmailField(required=True, max_length=75, label = "Email")
    password = CharField(widget=PasswordInput(), required=True, max_length=45, label = "Password")
    retype_password = CharField(widget=PasswordInput(), required=True, max_length=45, label = "Retype password")

    def clean_password(self):
        if self.data['password'] != self.data['retype_password']:
            raise forms.ValidationError("The two passwords you typed don't quite match!")
        if len(self.data['password'])<8:
            raise forms.ValidationError("Please enter a password that's at least 8 characters long.")
        return self.data['password']

    def clean_email(self):
        email = self.data['email']
        if len(email)>30:
            username = email[0:30]
        else:
            username = email
        user = User.objects.filter(username = username).first()
        recommender = Recommender.objects.filter(user = user).first()
        applicant = Applicant.objects.filter(user = user).first()
        if recommender:
            raise forms.ValidationError("This email address is already associated with a recommender's account. We ask that applicants do not also serve as recommenders for the same calendar year.")
        if applicant:
            raise forms.ValidationError("We already have an account registered for this email address!") 
        return self.data['email']



class ProfileForm(Form):
    first_name = CharField(required=True, max_length=30, label = "First name(s)")
    last_name = CharField(required=True, max_length=30, label = "Last name(s)")
    city = CharField(required=False, max_length=45)
    state = ChoiceField(required=False, choices=states)
    country = ChoiceField(required=False, choices=places)
    zipcode = CharField(required=False, max_length=5)
    dob = CharField(required=False, max_length=15)
    phone = CharField(required=False, max_length=15)
    languages = CharField(required=False, widget=forms.Textarea)
    communities = CharField(required=False, widget=forms.Textarea)
    working_now = CharField(required=False, widget=forms.Textarea)
    school_now = CharField(required=False, widget=forms.Textarea)
    time_commitment = CharField(required=False, widget=forms.Textarea)
    past_applicant = ChoiceField(choices=(('0','Select...'),('1', 'No'),('2', 'Yes')), required=False)
    referral = CharField(required=False, widget=forms.Textarea)

    def clean_dob(self):
        for char in self.data['dob']:
            if char.isalpha():
                raise forms.ValidationError('Please enter your date of birth using only numbers and the "-" or "/" characters.')
        return self.data['dob']

    def clean_zipcode(self):
        for char in self.data['zipcode']:
            if not char.isnumeric():
                raise forms.ValidationError("Please enter a zipcode that contains only numbers.")
        return self.data['zipcode']

    def clean_phone(self):
        for char in self.data['phone']:
            if char.isalpha():
                raise forms.ValidationError("Please enter a phone number that does not contain letters.")
        return self.data['phone']


class TechForm(Form):
    tech1b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech2b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech3b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech4b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech5b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech6b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech7b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech8b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech9b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech10b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech11b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech12b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech13b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech14b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech15b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech16b = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech1s = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech2s = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech3s = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech1c = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech2c = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech3c = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech4c = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))
    tech5c = ChoiceField(required=False, choices=(('0','Select...'),('1', '1'),('2', '2'),('3', '3'),('4', '4'), ('5', '5')))


class ShortAnswersForm(Form):
    shortanswer1 = CharField(widget=Textarea(), required=False)
    shortanswer2 = CharField(widget=Textarea(), required=False)
    shortanswer3 = CharField(widget=Textarea(), required=False)
    shortanswer4 = CharField(widget=Textarea(), required=False)
    shortanswer5 = CharField(widget=Textarea(), required=False)
    shortanswer6 = CharField(widget=Textarea(), required=False)
    shortanswer7 = CharField(widget=Textarea(), required=False)
    shortanswer8 = CharField(widget=Textarea(), required=False)
    shortanswer9 = CharField(widget=Textarea(), required=False)
    shortanswer10 = CharField(widget=Textarea(), required=False)
    shortanswer11 = CharField(widget=Textarea(), required=False)
    shortanswer12 = CharField(widget=Textarea(), required=False)
    shortanswer13 = CharField(widget=Textarea(), required=False)
    anything_else = CharField(widget=Textarea(), required=False)


class RecommendersForm(Form):
    rec1firstname = CharField(required=False, max_length=30, label="First recommender's first name(s)")
    rec1lastname = CharField(required=False, max_length=30, label="First recommender's last name(s)")
    rec1email = EmailField(required=False, max_length=75, label="First recommender's email address")
    rec1relationship = CharField(max_length=140, required=False, label="How do you know your first recommender?")
    rec2firstname = CharField(required=False, max_length=30, label="Second recommender's first name(s)")
    rec2lastname = CharField(required=False, max_length=30, label="Second recommender's last name(s)")
    rec2email = EmailField(required=False, max_length=75, label="Second recommender's email address")
    rec2relationship = CharField(max_length=140, required=False, label="How do you know your second recommender?")
    rec3firstname = CharField(required=False, max_length=30, label="Third recommender's first name(s)")
    rec3lastname = CharField(required=False, max_length=30, label="Third recommender's last name(s)")
    rec3email = EmailField(required=False, max_length=75, label="Third recommender's email address")
    rec3relationship = CharField(max_length=140, required=False, label="How do you know your third recommender?")

    def clean_rec1email(self):
        if (self.data['rec1email'] == self.data['rec2email'] and len(self.data['rec1email'])>0 and len(self.data['rec2email'])>0) or (self.data['rec1email'] == self.data['rec3email'] and len(self.data['rec1email'])>0 and len(self.data['rec3email'])>0):
            raise forms.ValidationError("Please give us a different email address for each recommender.")
        user = User.objects.filter(email = self.data['rec1email']).first()
        applicant = Applicant.objects.filter(user = user).first()
        if applicant:
            raise forms.ValidationError("This email address is already associated with an applicant's account. We ask that applicants do not serve as recommenders for the fellowship application.")
        return self.data['rec1email']


    def clean_rec2email(self):
        if (self.data['rec2email'] == self.data['rec3email'] and len(self.data['rec2email'])>0 and len(self.data['rec3email'])>0):
            raise forms.ValidationError("Please give us a different email address for each recommender.")
        user = User.objects.filter(email = self.data['rec2email']).first()
        applicant = Applicant.objects.filter(user = user).first()
        if applicant:
            raise forms.ValidationError("This email address is already associated with an applicant's account. We ask that applicants do not serve as recommenders for the fellowship application.")
        return self.data['rec2email']


    def clean_rec3email(self):
        user = User.objects.filter(email = self.data['rec3email']).first()
        applicant = Applicant.objects.filter(user = user).first()
        if applicant:
            raise forms.ValidationError("This email address is already associated with an applicant's account. We ask that applicants do not serve as recommenders for the fellowship application.")
        return self.data['rec3email']



class RecommendationForm(Form):
    known_applicant = CharField(widget=Textarea(), required=False)
    commitment_to_justice_rating = ChoiceField(choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    commitment_to_justice = CharField(widget=Textarea(), required=False)
    problem_solving_rating = ChoiceField(choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    problem_solving = CharField(widget=Textarea(), required=False)
    obstacles_rating = ChoiceField(choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    obstacles = CharField(widget=Textarea(), required=False)
    teaching_rating = ChoiceField(choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    teaching = CharField(widget=Textarea(), required=False)
    curiosity_rating = ChoiceField(choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    curiosity = CharField(widget=Textarea(), required=False)
    help_rating = ChoiceField(choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    help = CharField(widget=Textarea(), required=False)
    accommodations = CharField(widget=Textarea(), required=False)
    support = CharField(widget=Textarea(), required=False)
    anything_else = CharField(widget=Textarea(), required=False)


class EvaluationForm(Form):
    criteria_1_rating = ChoiceField(widget=RadioSelect, choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    criteria_2_rating = ChoiceField(widget=RadioSelect, choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    criteria_3_rating = ChoiceField(widget=RadioSelect, choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    criteria_4_rating = ChoiceField(widget=RadioSelect, choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    criteria_5_rating = ChoiceField(widget=RadioSelect, choices=(('0','Select...'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=False)
    notes = CharField(required=False, widget=Textarea())
    recommend = ChoiceField(choices=(('0','Select...'),('1', 'No'),('2', 'Yes')), required=True, label="Overal recommendation")


class EditRecommenderForm(Form):
    def __init__(self, *args, **kwargs):
            self.request = kwargs.pop("request")
            super(EditRecommenderForm, self).__init__(*args, **kwargs)

    first_name = CharField(required=True, max_length=30, label="First name(s)")
    last_name = CharField(required=True, max_length=30, label="Last name(s)")
    email = EmailField(required=True, max_length=75, label = "Email")
    relationship = CharField(required=True, label="How do you know this recommender?")


    def clean_email(self):
        count = 0
        inputted_rec_user = User.objects.filter(email = self.data['email']).first()
        registered_applicant = Applicant.objects.filter(user = inputted_rec_user)
        current_recommendations = self.request.user.applicant.recommendation_set.all()
        for recommendation in current_recommendations:
            if recommendation.recommender.user.email==self.data['email']:
                count+=1
        if count>0:
            raise forms.ValidationError("That email address is already being used by another one of your recommenders, or is already on file for this recommender. Please enter a different email address, or return to the previous screen and choose Edit Info if you only want to change this recommender's name or relationship.")
        if registered_applicant:
            raise forms.ValidationError("That email address is already being used by an applicant - please choose someone who isn't applying to the fellowship this year.")
        return self.data['email']


class ForgotPasswordForm(Form):
    email = EmailField(required=True, label="Email")


class ResetPasswordForm(Form):
    password = CharField(widget=PasswordInput(), required=True, label="Password")
    password_confirmation = CharField(widget=PasswordInput(), required=True, label="Retype password")

    def clean_password(self):
        if self.data['password'] != self.data['password_confirmation']:
            raise forms.ValidationError("The two passwords you typed don't quite match!")
        if len(self.data['password'])<8:
            raise forms.ValidationError("Please enter a password that's at least 8 characters long.")
        return self.data['password']



class AssignEvaluatorForm(Form):
    evaluator_email = EmailField(required=True, label="Evaluator's email address")
