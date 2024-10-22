emails = {}

emails['ashel'] = 'as@gmail.com'
emails['craig'] = 'cragmail.com'
emails['eli'] = 'eli@gmail.com'
print(emails)
del emails['craig']
print(emails)
emails['dal'] = 'dal@gmail.com'
print(emails)
print(list(emails.keys()))
print(list(emails.values()))

pairs = list(emails.items())
print(pairs)