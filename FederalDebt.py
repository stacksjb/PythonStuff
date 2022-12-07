#!/usr/bin/env python3

from pprint import pprint
import requests
import json
import datetime
#Welcome and print today's date
print('Welcome to the the current US Federal Debt Tracking App')
today = datetime.datetime.now().strftime('%Y-%m-%d')
print("Today's date is", today)
# Get the data from the API
response = requests.get('https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?fields=record_date,debt_held_public_amt,intragov_hold_amt,tot_pub_debt_out_amt&page[size]=1&sort=-record_date')
#load the JSON response
r = json.loads(response.content)
record_date=r['data'][0]['record_date']
#Parse values into a float
debt_held_public_amt=float(r['data'][0]['debt_held_public_amt'])
intragov_hold_amt=float(r['data'][0]['intragov_hold_amt'])
tot_pub_debt_out_amt=float(r['data'][0]['tot_pub_debt_out_amt'])
# Population data
response = requests.get("https://api.census.gov/data/2021/pep/natmonthly?get=POP,NAME&for=us:*")
r = json.loads(response.content)
# example response:
# [['POP', 'NAME', 'us'], ['331893745', 'United States', '1']]
us_population = int(r[1][0])
debt_per_person=tot_pub_debt_out_amt/us_population
#Print the values
print("Retrieved the following data from the API: ")
print('Record Date: ', record_date)
#Use printf to format the output to $ with commas
print('Debt Held by the Public $', end='')
print(f"{(debt_held_public_amt):,.2f}")
print('Intragovernmental Holdings $', end='')
print(f"{(intragov_hold_amt):,.2f}")
print('Total Public Debt Outstanding $', end='')
print(f"{(tot_pub_debt_out_amt):,.2f}")
print('Total Public Debt Per Person $', end='')
print(f"{(debt_per_person):,.2f}")
print('Thank you for using the current US Federal Debt Tracking App')
