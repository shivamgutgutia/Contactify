# import phonenumbers

# def validatePhoneNumber(number):
#     try:
#         parsedNumber = phonenumbers.parse(number)
#         return phonenumbers.is_valid_number(parsedNumber)
#     except phonenumbers.phonenumberutil.NumberParseException as e:
#         return False