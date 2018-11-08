# Author: Pranav Thombare
# Purpose: Use python script to
# 1) Connect to a MongoDB document collection
# 2) Populate a collection with documents
# 3) Display all of the documents in a collection</code>
import pymongo
from pymongo import MongoClient

# connect to the MongoDB on MongoLab
# to learn more about MongoLab visit http://www.mongolab.com
# you can also use a local MongoDB instance
connection = MongoClient("localhost:27017")

# connect to the airplane database
db = connection.airplane_company.pilots

# create a dictionary to hold documents in the collection "pilots"

# create dictionary
pilot_record = {}

# set flag variable
flag = True

# loop for data input
#while (flag):
   # ask for input
   #pilot_name,pilot_address,pilot_contact,pilot_email,pilot_status,pilot_dot = raw_input("Enter Pilot details: ").split(',,')
   # place values in dictionary
   #pilot_record = {'name':pilot_name,'address':pilot_address, 'contact':pilot_contact,'email':pilot_email,'emp_status':pilot_status,'date_last_test':pilot_dot}
   # insert the record
   #db.insert(pilot_record)
   # should we continue?
   #flag = input('Enter another record? ')
   #if (flag[0].upper() == 'N'):
      #flag = False

pilot1= {
        'name':'Rohit Sharma'
        'address':''
        'contact':
        'email':
        'empl_status':{
            'date_of_join':
            'department':
            'status':
        }
        'last_flight':
        'last_test':
}


pilot2= {
        'name':'John Cena'
        'address':
        'contact':
        'email':
        'empl_status':{
            'date_of_join':
            'department':
            'status':
        }
        'last_flight':
        'last_test':
}

pilot3= {
        'name':'Vin Diesel'
        'address':
        'contact':
        'email':
        'empl_status':{
            'date_of_join':
            'department':
            'status':
        }
        'last_flight':
        'last_test':
}

pilot4= {
        'name':'Donald Trump'
        'address':
        'contact':
        'email':
        'empl_status':{
            'date_of_join':
            'department':
            'status':
        }
        'last_flight':
        'last_test':
}

pilot5= {
        'name':'Nicholas Cage'
        'address':
        'contact':
        'email':
        'empl_status':{
            'date_of_join':
            'department':
            'status':
        }
        'last_flight':
        'last_test':
}

pilot6= {
        'name':'Jaikiran Sawant'
        'address':
        'contact':
        'email':
        'empl_status':{
            'date_of_join':
            'department':
            'status':
        }
        'last_flight':
        'last_test':
}

pilot7= {
        'name': 'Suruchi Rastogi'
        'address':
        'contact':
        'email':
        'empl_status':{
            'date_of_join':
            'department':
            'status':
        }
        'last_flight':
        'last_test':
}


pilot8= {
        'name':'Anket Dhoble'
        'address':''
        'contact':
        'email':
        'empl_status':{
            'date_of_join':
            'department':
            'status':
        }
        'last_flight':
        'last_test':
}


db.insert(pilot_record)

# close the connection to MongoDB
connection.close()
