from configure import acct_id, twilio_auth_key
from twilio.rest import Client

client = Client(acct_id, twilio_auth_key)

US_avail_phone_numbers = client.available_phone_numbers('US').fetch()

# lists 20 available local numbers with area code 206
list_20 = US_avail_phone_numbers.local.list(area_code='206', limit=20)
for num in list_20:
    # only list the number if it has voice capability
    # they all should
    if num.capabilities['voice'] == True:
        print(num.phone_number)
_number = input("Which phone number do you want?")

# request your new number
new_number = client.incoming_phone_numbers.create(
    phone_number= _number)

print("You've activated your new number", new_number.phone_number)

