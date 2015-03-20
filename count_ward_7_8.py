from app.models	import *

applicants = Applicant.objects.all()

counter	= 0

for a in applicants:
  if a.zipcode is not None:    
    if '20019' in a.zipcode or '20020' in a.zipcode or '20032' in a.zipcode:
      counter +=1
      print a.user.first_name, a.user.last_name, a.zipcode


print counter
