import datetime
import time
dob_year = raw_input('Enter DOB in %d-%m-%y formate')
dob_year_obj = datetime.datetime.strptime(dob_year,'%d-%m-%Y')
Current_year = datetime.date.today()
#Current_year_obj = datetime.datetime.strptime(Current_year,'%d-%m-%Y')
your_age = Current_year.year - dob_year_obj.year
print 'your age is :', your_age