from django.db import models
from django.contrib.auth.models import User
import datetime
from django_countries.fields import CountryField


# Django has a built-in User model that works well with the out-of-the-box authentication functions, so we are using it/them.
# That model is created via User.objects.create(username, email, password), and can then also hold first_name and last_name.


class Applicant(models.Model):
    user = models.OneToOneField(User)
    role = models.IntegerField(default=1)
    city = models.CharField(max_length=45, null=True, blank=True)
    state = models.CharField(max_length=45, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    zipcode = models.CharField(max_length=5, null=True, blank=True)
    dob = models.CharField(max_length=15, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    languages = models.TextField(null=True, blank=True)
    communities = models.TextField(null=True, blank=True)
    working_now = models.TextField(null=True, blank=True)
    school_now = models.TextField(null=True, blank=True)
    time_commitment = models.TextField(null=True, blank=True)
    past_applicant = models.IntegerField(null=True, blank=True)
    referral = models.TextField(null=True, blank=True)

    #  Tech responses
    tech1b = models.IntegerField(null=True, blank=True)
    tech2b = models.IntegerField(null=True, blank=True)
    tech3b = models.IntegerField(null=True, blank=True)
    tech4b = models.IntegerField(null=True, blank=True)
    tech5b = models.IntegerField(null=True, blank=True)
    tech6b = models.IntegerField(null=True, blank=True)
    tech7b = models.IntegerField(null=True, blank=True)
    tech8b = models.IntegerField(null=True, blank=True)
    tech9b = models.IntegerField(null=True, blank=True)
    tech10b = models.IntegerField(null=True, blank=True)
    tech11b = models.IntegerField(null=True, blank=True)
    tech12b = models.IntegerField(null=True, blank=True)
    tech13b = models.IntegerField(null=True, blank=True)
    tech14b = models.IntegerField(null=True, blank=True)
    tech15b = models.IntegerField(null=True, blank=True)
    tech16b = models.IntegerField(null=True, blank=True)
    tech1s = models.IntegerField(null=True, blank=True)
    tech2s = models.IntegerField(null=True, blank=True)
    tech3s = models.IntegerField(null=True, blank=True)
    tech1c = models.IntegerField(null=True, blank=True)
    tech2c = models.IntegerField(null=True, blank=True)
    tech3c = models.IntegerField(null=True, blank=True)
    tech4c = models.IntegerField(null=True, blank=True)
    tech5c = models.IntegerField(null=True, blank=True)


    #  Shortanswer responses
    shortanswer1 = models.TextField(null=True, blank=True)
    shortanswer2 = models.TextField(null=True, blank=True)
    shortanswer3 = models.TextField(null=True, blank=True)
    shortanswer4 = models.TextField(null=True, blank=True)
    shortanswer5 = models.TextField(null=True, blank=True)
    shortanswer6 = models.TextField(null=True, blank=True)
    shortanswer7 = models.TextField(null=True, blank=True)
    shortanswer8 = models.TextField(null=True, blank=True)
    shortanswer9 = models.TextField(null=True, blank=True)
    shortanswer10 = models.TextField(null=True, blank=True)
    shortanswer11 = models.TextField(null=True, blank=True)
    shortanswer12 = models.TextField(null=True, blank=True)
    shortanswer13 = models.TextField(null=True, blank=True)
    shortanswer14 = models.TextField(null=True, blank=True)
    anything_else = models.TextField(null=True, blank=True)

    # Recommender info
    rec1firstname = models.CharField(max_length=30, null=True, blank=True)
    rec1lastname = models.CharField(max_length=30, null=True, blank=True)
    rec1email = models.CharField(max_length=75, null=True, blank=True)
    rec1relationship = models.CharField(max_length=140, null=True, blank=True)
    rec2firstname = models.CharField(max_length=30, null=True, blank=True)
    rec2lastname = models.CharField(max_length=30, null=True, blank=True)
    rec2email = models.CharField(max_length=75, null=True, blank=True)
    rec2relationship = models.CharField(max_length=140, null=True, blank=True)
    rec3firstname = models.CharField(max_length=30, null=True, blank=True)
    rec3lastname = models.CharField(max_length=30, null=True, blank=True)
    rec3email = models.CharField(max_length=75, null=True, blank=True)
    rec3relationship = models.CharField(max_length=140, null=True, blank=True)

    application_submitted = models.IntegerField(default = 0)
    is_approved = models.IntegerField(default = 0)

    created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def is_authenticated(self):
        return True

    def __unicode__(self):
        return self.user.email

    def profile_complete(self):
        if self.city and self.state and self.country and self.zipcode and self.dob and self.phone and self.languages and self.communities and self.working_now and self.school_now and self.time_commitment and self.past_applicant>0 and self.referral:
            return True
        return False

    def tech_questions_complete(self):
        if self.tech1b>0 and self.tech2b>0 and self.tech3b>0 and self.tech4b>0 and self.tech5b>0 and self.tech6b>0 and self.tech7b>0 and self.tech8b>0 and self.tech9b>0 and self.tech10b>0 and self.tech11b>0 and self.tech12b>0 and self.tech13b>0 and self.tech14b>0 and self.tech15b>0 and self.tech16b>0:
            return True
        return False

    def short_answers_complete(self):
        if self.shortanswer1 and self.shortanswer2 and self.shortanswer3 and self.shortanswer4 and self.shortanswer5 and self.shortanswer6 and self.shortanswer7 and self.shortanswer8 and self.shortanswer9 and self.shortanswer10 and self.shortanswer11 and self.shortanswer12 and self.shortanswer13:
            return True
        return False

    def recommenders_complete(self):
        if self.rec1firstname and self.rec1lastname and self.rec1email and self.rec1relationship and self.rec2firstname and self.rec2lastname and self.rec2email and self.rec2relationship and self.rec3firstname and self.rec3lastname and self.rec3email and self.rec3relationship:
            return True
        return False

    def application_complete(self):
        if self.profile_complete() and self.tech_questions_complete() and self.short_answers_complete() and self.recommenders_complete():
            return True
        return False

    def num_evaluators(self):
        evals = self.evaluation_set.all()
        return len(evals)

    def has_evaluations(self):
        evaluations = self.evaluation_set.all()
        return evaluations

    def average_score(self):
        evaluations = self.evaluation_set.all()
        total_score = 0.00
        num_evals = len(evaluations)
        for e in evaluations:
            if e.criteria_1_rating:
                total_score+=(e.criteria_1_rating+e.criteria_2_rating+e.criteria_3_rating+e.criteria_4_rating+e.criteria_5_rating)
        average_long = float(total_score)/float(num_evals)
        return round(average_long,3)

    def all_submitted(self):
        applicants = Applicant.objects.raw("SELECT * FROM app_applicants WHERE application_submitted = 1")
        return applicants


class Recommender(models.Model):
    user = models.OneToOneField(User)
    role = models.IntegerField(default=2)

    created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.user.email

    def num_applicants(self):
        recs = self.recommendation_set.all()
        return len(recs)

    def has_recommendations(self):
        recommendations = self.recommendation_set.all()
        return recommendations

    def num_incomplete_recommendations(self):
        recommendations = self.recommendation_set.all()
        counter = 0
        for r in recommendations:
            if r.submitted==0:
                counter+=1
        return counter

    def all_recs_complete(self):
        recommendations = self.recommendation_set.all()
        for r in recommendations:
            if not r.is_complete():
                return False
        return True



class Recommendation(models.Model):
    applicant = models.ForeignKey(Applicant)
    recommender = models.ForeignKey(Recommender)
    known_applicant = models.TextField(null=True, blank=True)
    commitment_to_justice_rating = models.IntegerField(null=True, blank=True)
    commitment_to_justice = models.TextField(null=True, blank=True)
    problem_solving_rating = models.IntegerField(null=True, blank=True)
    problem_solving = models.TextField(null=True, blank=True)
    obstacles_rating = models.IntegerField(null=True, blank=True)
    obstacles = models.TextField(null=True, blank=True)
    teaching_rating = models.IntegerField(null=True, blank=True)
    teaching = models.TextField(null=True, blank=True)
    curiosity_rating = models.IntegerField(null=True, blank=True)
    curiosity = models.TextField(null=True, blank=True)
    help_rating = models.IntegerField(null=True, blank=True)
    help = models.TextField(null=True, blank=True)
    accommodations = models.TextField(null=True, blank=True)
    support = models.TextField(null=True, blank=True)
    anything_else = models.TextField(null=True, blank=True)
    submitted = models.IntegerField(default=0)

    def __unicode__(self):
        return "Recommendation " + str(self.id)

    def is_complete(self):
        if self.known_applicant and self.commitment_to_justice_rating>0 and self.commitment_to_justice and self.problem_solving_rating>0 and self.problem_solving and self.obstacles_rating>0 and self.obstacles and self.teaching_rating>0 and self.teaching and self.curiosity_rating>0 and self.curiosity and self.help_rating>0 and self.help and self.accommodations and self.support:
            return True
        return False


class Evaluator(models.Model):
    user = models.OneToOneField(User)
    role = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.user.email

    def num_applicants(self):
        evals = self.evaluation_set.all()
        return len(evals)

    def num_incomplete_evaluations(self):
        evaluations = self.evaluation_set.all()
        counter = 0
        for e in evaluations:
            if not e.is_complete():
                counter+=1
        return counter


    def has_evaluations(self):
        evaluations = self.evaluation_set.all()
        return evaluations

    def all_evals_complete(self):
        evaluations = self.evaluation_set.all()
        for e in evaluations:
            if not e.is_complete():
                return False
        return True

    def add_new_evaluation(self):
        applicant = Applicant.objects.raw("""
                SELECT *
                FROM app_applicant
                WHERE id NOT IN (
                    SELECT applicant_id
                    FROM app_evaluation
                    WHERE criteria_1_rating IS NOT NULL
                    AND criteria_2_rating IS NOT NULL
                    AND criteria_3_rating IS NOT NULL
                    AND criteria_4_rating IS NOT NULL
                    AND criteria_5_rating IS NOT NULL
                    AND recommend IS NOT NULL
                    GROUP BY applicant_id
                    HAVING count(*) >= 3
                )
                AND is_approved = 1
                ORDER BY random();
        """)[0]

        evaluation = Evaluation(applicant = applicant, evaluator = self)
        evaluation.save()



class Evaluation(models.Model):
    applicant = models.ForeignKey(Applicant)
    evaluator = models.ForeignKey(Evaluator)
    criteria_1_rating = models.IntegerField(null=True, blank=True)
    criteria_2_rating = models.IntegerField(null=True, blank=True)
    criteria_3_rating = models.IntegerField(null=True, blank=True)
    criteria_4_rating = models.IntegerField(null=True, blank=True)
    criteria_5_rating = models.IntegerField(null=True, blank=True)
    criteria_6_rating = models.IntegerField(null=True, blank=True)
    criteria_7_rating = models.IntegerField(null=True, blank=True)
    criteria_8_rating = models.IntegerField(null=True, blank=True)
    criteria_9_rating = models.IntegerField(null=True, blank=True)
    criteria_10_rating = models.IntegerField(null=True, blank=True)
    criteria_11_rating = models.IntegerField(null=True, blank=True)
    criteria_12_rating = models.IntegerField(null=True, blank=True)
    recommend = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def is_complete(self):
        if self.criteria_1_rating and self.criteria_2_rating and self.criteria_3_rating and self.criteria_4_rating and self.criteria_5_rating and self.criteria_6_rating and self.criteria_7_rating and self.criteria_8_rating and self.criteria_9_rating and self.criteria_10_rating and self.criteria_11_rating and self.criteria_12_rating and self.recommend:
            return True
        return False

    def __unicode__(self):
        return "Evaluation "+ str(self.id)



class Staff(models.Model):
    user = models.OneToOneField(User)
    role = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.user.email