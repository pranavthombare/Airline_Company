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
while (flag):
   # ask for input
   pilot_name,pilot_address,pilot_contact,pilot_email,pilot_status,pilot_dot = raw_input("Enter Pilot details: ").split(',,')
   # place values in dictionary
   pilot_record = {'name':pilot_name,'address':pilot_address, 'contact':pilot_contact,'email':pilot_email,'emp_status':pilot_status,'date_last_test':pilot_dot}
   # insert the record
   db.insert(pilot_record)
   # should we continue?
   flag = input('Enter another record? ')
   if (flag[0].upper() == 'N'):
      flag = False

# find all documents
results = db.find()

print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

# display documents from collection
for record in results:
# print out the document
    print(record['name'] + ',',record['address'] + ',',record['contact'] + ',',record['email'] + ',',record['emp_status'] + ',',record['date_last_test'])

print()

# close the connection to MongoDB
connection.close()
