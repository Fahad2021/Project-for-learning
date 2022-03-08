import phonenumbers
from test import number
# Country Number
from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))
# operator name
from phonenumbers import carrier
service_name=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_name,"en"))
# time zone
from phonenumbers import timezone
phoneNumber = phonenumbers.parse(number,"TZ")
print(timezone.time_zones_for_number(phoneNumber))

# location
from phonenumbers import length_of_geographical_area_code
phoneNumber=phonenumbers.parse(number,"LG")
print((length_of_geographical_area_code)(phoneNumber))




# import phonenumbers
# numobj = phonenumbers.parse("16502530000", "US")
# nsn = phonenumbers.national_significant_number(numobj)
# ac_len = phonenumbers.length_of_geographical_area_code(numobj)
# if ac_len > 0:
#     area_code = nsn[:ac_len]
#     subscriber_number = nsn[ac_len:]
# else:
#     area_code = ""
#     subscriber_number = nsn




