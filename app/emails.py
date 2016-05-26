from app.models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail


def application_created(user_id):
    user = User.objects.get(id = user_id)
    subject = "Thanks for creating an application."
    signature = "\n\n\nThe Code For Progress team\n\n\nCode for Progress\nwww.codeforprogress.org\n((202) 810-1027n\n1726 Connecticut Ave NW #400\nWashington, DC 20009"
    body_text = "Hi "+user.first_name+",\n\nThanks for creating an application for the 2016 Code For Progress fellowship! You can return to your application any time by visiting apply.codeforprogress.org.\n\nRemember that we'll need your completed application and three recommendations by June 12th, 2016. \n\nIf you have questions about the program or the application before the deadline, please email programs@codeforprogress.org and we will get back to you as soon as possible.\n\nThanks for applying to Code For Progress!"+signature
    send_mail(subject, body_text, 'Code For Progress Staff', [user.email], fail_silently=False)


def password_sent(user_id, password):
    user = User.objects.get(id = user_id)
    subject = "Your new account password"
    signature = "\n\n\nThe Code For Progress team\n\n\nCode For Progress\nwww.codeforprogress.org\n(202) 810-1027\n\n1726 Connecticut Ave NW #400\nWashington, DC 20009"
    body_text = "Hi "+user.first_name+",\n\nHere's a new password that you can use to log into the Code For Progress fellowship application portal (apply.codeforprogress.org). Once you're logged in, you can reset your password to something that's easier to remember.\n\n\tUsername: "+user.email+"\n\tPassword: "+password+"\n\nWe look forward to reading your submission,"+signature
    send_mail(subject, body_text, 'Code For Progress Staff', [user.email], fail_silently=False)


def application_received(user_id):
    user = User.objects.get(id = user_id)
    subject = "We've received your application for the 2016 Code For Progress fellowship"
    signature = "\n\n\nThe Code For Progress team\n\n\nCode For Progress\nwww.codeforprogress.org\n(202) 810-1027\n\n1726 Connecticut Ave NW #400\nWashington, DC 20009"
    body_text = "Hi "+user.first_name+",\n\nThanks for applying to the 2015 Code For Progress fellowship! We've received your complete application, and we've sent emails to your recommenders with login information and instructions for completing their recommendations.\n\nRemember that we must receive all three of your recommendations by June 12th, so please check to make sure your recommenders will be able to meet the deadline. You can also always log back in to the application site to see your recommenders' progress on your dashboard.\n\nSincerely,"+signature
    send_mail(subject, body_text, 'Code For Progress Staff', [user.email], fail_silently=False)


def recommendation_requested(user_id, recommender_id, password):
    user = User.objects.get(id = user_id)
    recommender = Recommender.objects.get(id = recommender_id)
    subject = user.first_name+" "+user.last_name+" has asked for your recommendation."
    signature = "\n\n\nThe Code For Progress team\n\n\nCode For Progress\nwww.codeforprogress.org\n(202) 810-1027\n\n1726 Connecticut Ave NW #400\nWashington, DC 20009"
    body_text = "Hi "+recommender.user.first_name+",\n\n"+user.first_name+" "+user.last_name+" is applying to the 2016 Code For Progress fellowship, and has asked for your recommendation.\n\nYou can log into the application website using the following information:\n\n\tLogin page: http://apply.codeforprogress.org\n\n\tUsername: "+recommender.user.email+"\n\tPassword: "+password+"\n\nOnce you log in, you'll be asked to answer a few short questions that draw on your experiences with the applicant. Applicants will not be able to see the text of your recommendation, but will be able to see if it has been submitted.\n\nWe must receive your recommendation by June 12th, 2016 in order to consider "+user.first_name+"'s application, so please let them know if you will not be able to meet the deadline and will need a replacement.\n\nThanks for supporting a Code For Progress applicant!"+signature
    send_mail(subject, body_text, 'Code For Progress Staff', [recommender.user.email], fail_silently=False)


def recommendation_requested_existing_recommender(user_id, recommender_id):
    user = User.objects.get(id = user_id)
    recommender = Recommender.objects.get(id = recommender_id)
    subject = user.first_name+" "+user.last_name+" has asked for your recommendation."
    signature = "\n\n\nThe Code For Progress team\n\n\nCode For Progress\nwww.codeforprogress.org\n(202) 810-1027\n\n1726 Connecticut Ave NW #400\nWashington, DC 20009"
    body_text = "Hi "+recommender.user.first_name+",\n\n"+user.first_name+" "+user.last_name+" is applying to the 2016 Code For Progress fellowship, and has asked for your recommendation.\n\nYou do not need to create a new account - please simply use the login information sent to you earlier to log into the site at http://apply.codeforprogress.org.\n\nAs a reminder, we must receive your recommendation by June 12th,2016 in order to consider "+user.first_name+"'s application, so please let them know if you will not be able to meet the deadline and will need a replacement.\n\nThanks for supporting a Code For Progress applicant!"+signature
    send_mail(subject, body_text, 'Code For Progress Staff', [recommender.user.email], fail_silently=False)


def recommendation_request_sent(user_id, recommender_id):
    user = User.objects.get(id = user_id)
    recommender = Recommender.objects.get(id = recommender_id)
    subject = "We've sent a recommendation request to "+recommender.user.first_name+" "+recommender.user.last_name
    signature = "\n\n\nThe Code For Progress team\n\n\nCode For Progress\nwww.codeforprogress.org\n(202) 810-1027\n\n1726 Connecticut Ave NW #400\nWashington, DC 20009"
    body_text = "Hi "+user.first_name+",\n\nWe've sent an email to "+recommender.user.first_name+" "+recommender.user.last_name+" at "+recommender.user.email+" with login information and instructions for completing a recommendation to accompany your fellowship application.\n\nRemember that we must receive all three of your recommendations by June 12th, so please check to make sure they will be able to meet the deadline. You can also always log back in to the application site to see their progress on your dashboard.\n\nSincerely,"+signature
    send_mail(subject, body_text, 'Code For Progress Staff', [user.email], fail_silently=False)


def recommendation_received(applicant_id, recommender_id):
    applicant = Applicant.objects.get(id = applicant_id)
    recommender = Recommender.objects.get(id = recommender_id)
    subject = "We've received your recommendation for "+applicant.user.first_name+" "+applicant.user.last_name
    signature = "\n\n\nThe Code For Progress team\n\n\nCode for Progress\nwww.codeforprogress.org\n(202) 810-1027\n\n1726 Connecticut Ave NW #400\nWashington, DC 20009"
    body_text = "Hi "+recommender.user.first_name+",\n\n"+"We've just received your recommendation for "+applicant.user.first_name+" "+applicant.user.last_name+".We'll be notifying them of our decision in late June.\n\nThanks for supporting a Code For Progress applicant!"+signature
    send_mail(subject, body_text, 'Code For Progress Staff', [recommender.user.email], fail_silently=False)
