country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

print("Country code of India:")
print(country_code.get('India', 'Not Found'))
print("Country code of Japan:")
print(country_code.get('Japan', 'Not Found'))