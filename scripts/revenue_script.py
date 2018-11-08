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
db = connection.airplane_company.revenue

# create a dictionary to hold documents in the collection "pilots"

# create dictionary
revenue_record = {}

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

emp1= 
        {
        'empId':'Double'
        'empName':'String'
        'dateOfJoining':'date'
        'department':'String'
        'deptId':'Double'
        'reportingManager':'string'
        'salary':'Double'
        'mobileNo':'Double'
        'emailId':'String'
        'empAddress':'String'
        }


emp2= 
        {
        'empId':'Double'
        'empName':'String'
        'dateOfJoining':'date'
        'department':'String'
        'deptId':'Double'
        'reportingManager':'string'
        'salary':'Double'
        'mobileNo':'Double'
        'emailId':'String'
        'empAddress':'String'
        }

emp3= 
        {
        'empId':'Double'
        'empName':'String'
        'dateOfJoining':'date'
        'department':'String'
        'deptId':'Double'
        'reportingManager':'string'
        'salary':'Double'
        'mobileNo':'Double'
        'emailId':'String'
        'empAddress':'String'
        }

emp4= 
        {
        'empId':'Double'
        'empName':'String'
        'dateOfJoining':'date'
        'department':'String'
        'deptId':'Double'
        'reportingManager':'string'
        'salary':'Double'
        'mobileNo':'Double'
        'emailId':'String'
        'empAddress':'String'
        }

emp5= 
        {
        'empId':'Double'
        'empName':'String'
        'dateOfJoining':'date'
        'department':'String'
        'deptId':'Double'
        'reportingManager':'string'
        'salary':'Double'
        'mobileNo':'Double'
        'emailId':'String'
        'empAddress':'String'
        }

emp6= 
        {
        'empId':'Double'
        'empName':'String'
        'dateOfJoining':'date'
        'department':'String'
        'deptId':'Double'
        'reportingManager':'string'
        'salary':'Double'
        'mobileNo':'Double'
        'emailId':'String'
        'empAddress':'String'
        }

emp7= 
        {
        'empId':'Double'
        'empName':'String'
        'dateOfJoining':'date'
        'department':'String'
        'deptId':'Double'
        'reportingManager':'string'
        'salary':'Double'
        'mobileNo':'Double'
        'emailId':'String'
        'empAddress':'String'
        }


emp8= 
        {
        'empId':'Double'
        'empName':'String'
        'dateOfJoining':'date'
        'department':'String'
        'deptId':'Double'
        'reportingManager':'string'
        'salary':'Double'
        'mobileNo':'Double'
        'emailId':'String'
        'empAddress':'String'
        }


db.insert(employee_record)

# close the connection to MongoDB
connection.close()
