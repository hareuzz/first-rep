AIRTABLE_BASE_ID = 'app3irHJyR0T2g8I1'
AIRTABLE_API_KEY = 'keyYQbVw8KeVkzD3h'
AIRTABLE_TABLE_NAME = 'Freelancers'
endpoint = f' https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

from email import header
import requests 

#python request headers
'''
headers = { 
    "Authorization" : f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json" 
}

data = {
  "records": [
    {
      "fields": {
        "Invoices": "Invoice#1",
        "Name": [
          "recPgW8RwiCw5TyAY"
        ],
        "hourly Rate": 60,
        "Hours worked": 3.5,
        "Due Date": "2022-10-21",
        "Services": [
          "rechN2ZHTUOeLqKey"
        ]
      }
    },
    {
      "fields": {
        "Invoices": "Invoice#2",
        "Name": [
          "rec03XqR9hWvUBjMT"
        ],
        "hourly Rate": 50,
        "Hours worked": 3,
        "Due Date": "2022-10-19",
        "Services": [
          "recNvrvjhnYbZea0p",
          "rec2RuIgDMhiT6iNl"
        ]
      }
    }
  ]
}

#http methods
#What is the method for "create"? -> HTTP Method POST

from email import header
import requests 

r = requests.post(endpoint, json = data, headers=headers)
print(r.status_code)
'''


def add_to_airtable(Invoices=None, name="",hourly_rate="", hours_worked="", due_date=""):
    if Invoices is None:
        return
    headers = {
            "Authorization" : f"Bearer {AIRTABLE_API_KEY}",
            "Content-Type": "application/json" 
    }

    data = {
    "records": [
            {
            "fields": {
                "Invoices": Invoices,
                "Name": name,
                "hourly Rate": hourly_rate,
                "Hours worked": hours_worked,
                "Due Date": due_date
#Fields other than invoices and name are hard coded. They can be added as 
# an input request the same way invoices and names are added. 
                }
            }
        ]
    }
    r = requests.post(endpoint, json = data, headers=headers)
    print(r) #200 code is successful run, 400 is error 

#http methods
#What is the method for "create"? -> HTTP Method POST


#now i am going to make some changes to the file structure to see how git works

Invoices = input("what is the invoice #?")
name = input("what is the name ?")
hourly_rate = input("What is the hourly rate of the freelancer?")
hours_worked = input("How many hours worked (in decimal point?) ")
due_date = input("What is the due date of the payment?")

add_to_airtable(Invoices, name, hourly_rate, hours_worked, due_date)
