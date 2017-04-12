# Insert random 30 records into mysql tables

import json
import MySQLdb
import random
import string

conn = MySQLdb.connect(host= "127.0.0.1", user="root",passwd="password",db="t1")
cursor = conn.cursor()

from datetime import datetime
import random

def random_date():
	year = random.randint(1990, 2016)
	month = random.randint(1, 12)
	day = random.randint(1, 27)
	return datetime(year, month, day)

def random_datetime():
	year = random.randint(2017, 2017)
	month = random.randint(1, 3)
	day = random.randint(1, 27)
	return datetime(year, month, day)

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def insert_data(q,d):
	try:
		cursor.executemany(q, d)
		conn.commit()
		print "*"*30
		print q[20]
	except Exception, e:
		print "#"*30
		print e
		conn.rollback()
	return True


#Zip Codes
with open('zip_codes.json') as data_file:
	data = json.load(data_file)
zip_cache = []
zip_data = []
z = 99501
for each in data:
	each[0] =  z
	zip_data.append(tuple(each))
	zip_cache.append(z)
	z = z+1

query =  """INSERT INTO zips (zip, state, city, lat, lng) VALUES (%s, %s, %s, %s, %s)"""
insert_data(query,zip_data)


# Insert Users
with open('users.json') as data_file:
	data = json.load(data_file)
user_data = []
user_cache = []
u = 1000
for each in data:
	each[0] = u
	each[1] = randomword(5).title()
	each[2] = randomword(5)
	each[4] = "%s_%s@%smail.com"%(each[1],each[2],randomword(3))
	each[5] = "1[%s]%s"%(random.randrange(101, 999,1),random.randrange(1234567,7654321,1))
	each[6] = random.randint(1234567891234567,9876543211234567)
	each[7] = "%s-0%s"%(random.randrange(2010, 2030,1),random.randrange(1,9,1))
	each[8] = random.choice(zip_cache)
	user_data.append(each)
	user_cache.append(u)
	u = u+1

query =  """insert into user (user_id, first_name, last_name, user_address, user_email, user_telephone, card_details, card_valid_thru, user_zip) values (%s, %s, %s, %s, %s,%s, %s, %s, %s) """
insert_data(query,user_data)


# Local Driver
local_driver_cache = []
local_driver_data = []
for i in range(31,61):
	driver_id = "{0}-{1}-{2}".format(i,random.randrange(100,999,1),random.randrange(1000,9999,1))
	driver_name = randomword(10)
	zip_code = str(random.choice(zip_cache))
	local_driver_data.append((driver_id,driver_name,zip_code))
	local_driver_cache.append(driver_id)

query =  """insert into Local_Driver (LocalDriver_ID, Driver_Name,Zip_Code) values (%s, %s, %s) """
insert_data(query,tuple(local_driver_data))


# State Driver
state_driver_cache = []
state_driver_data = []
for i in range(61,91):
	driver_id = "{0}-{1}-{2}".format(i,random.randrange(100,999,1),random.randrange(1000,9999,1))
	driver_name = randomword(10)
	zip_code = str(random.choice(zip_cache))
	state_driver_data.append((driver_id,driver_name,zip_code))
	state_driver_cache.append(driver_id)

query =  """insert into State_Driver (StateDriver_ID, Driver_Name,Zip_Code) values (%s, %s, %s) """
insert_data(query,tuple(state_driver_data))



# State Driver
driver_cache = []
driver_data = []
for i in range(41,71):
	#driver_id = "{0}-{1}-{2}".format(i,random.randrange(100,999,1),random.randrange(1000,9999,1))
	driver_id = i
	fname = randomword(6)
	lname = randomword(10)
	address = "%s-%s, Road No: %s, %s"%(i,random.randint(1,100),random.randint(30,60),randomword(20))
	phone = "1[%s]%s"%(random.randrange(101, 999,1),random.randrange(1234567,7654321,1))
	zip_code = str(random.choice(zip_cache))
	car_id = i-30
	lic = "{0}-{1}-{2}".format(i,random.randrange(100,999,1),random.randrange(1000,9999,1))
	login_id = "{0}-{1}-{2}".format(i,random.randrange(10,99,1),random.randrange(1000000,9999999,1))
	state_driver_id = random.choice(state_driver_cache)
	local_driver_id = random.choice(local_driver_cache)
	driver_data.append((driver_id,fname,lname,address,phone,zip_code,car_id,lic,login_id,local_driver_id,state_driver_id,local_driver_id,state_driver_id))
	driver_cache.append(driver_id)

query =  """insert into drivers (driver_id, driver_first_name, driver_last_name, driver_address, driver_telephone, driver_zip, car_id, driver_license_num, driver_login_id, Localdriver_ID,StateDriver_ID,Local_Driver_LocalDriver_ID,State_Driver_StateDriver_ID) values (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s) """
insert_data(query,tuple(driver_data))


# Cars
cars_cache = []
cars_data = []

for i in range(1,31):
	car_id = i
	ctype = random.randint(1,4)
	driver_id = i+40
	car_no = "%s%s"%(randomword(3), random.randint(1000,9999))
	car_year = random_date().strftime("%Y-%m-%d")
	cars_car_id = i
	cars_cache.append(car_id)
	cars_data.append((car_id,ctype,driver_id,car_no,car_year,cars_car_id))
query =  """ insert into cars (car_id, car_type, driver_id, car_no, car_year, cars_car_id) values (%s, %s, %s,%s, %s,%s) """
insert_data(query,tuple(cars_data))



# Driver Login
dlogin_cache = []
dlogin_data = []

for i in range(1,31):
	dlog = i
	rdtime = random_datetime().strftime("%Y-%m-%d")
	check_in = "%s %s-%s-%s"%(rdtime, random.randint(8,12),random.randint(1,59),random.randint(1,59))
	check_out = "%s %s-%s-%s"%(rdtime, random.randint(13,22),random.randint(1,59),random.randint(1,59))
	d_status = random.randint(1,2)
	lzip_code = str(random.choice(zip_cache))
	ozip_code = str(random.choice(zip_cache))
	car_id = i
	dlogin_cache.append(dlog)
	dlogin_data.append((dlog,check_in,check_out,d_status,lzip_code,ozip_code,car_id))
query =  """ insert into driver_login (driver_login_id, check_in, check_out, driver_status, driver_login_zip, driver_logout_zip, car_id) values (%s, %s, %s,%s, %s,%s,%s) """
insert_data(query,tuple(dlogin_data))


# Booking
booking_cache = []
booking_data = []
ride_cache = []
ride_data = []
for i in range(1,31):
	bid = i
	rdtime = random_datetime().strftime("%Y-%m-%d")
	bdate = "%s %s-%s-%s"%(rdtime, random.randint(1,7),random.randint(1,59),random.randint(1,59))
	pup = randomword(10).title()
	dup = randomword(12).title()
	pzip_code = str(random.choice(zip_cache))
	dzip_code = str(random.choice(zip_cache))
	uid = str(random.choice(user_cache))
	bstatus = random.randint(1,2)
	npsg = random.randint(1,3)
	booking_data.append((bid,bdate,pup,dup,pzip_code,dzip_code,uid,bstatus,npsg))
	booking_cache.append(bid)



	rid = i
	bid = i
	wtime = "%s %s-%s-%s"%(rdtime, random.randint(6,7),random.randint(1,59),random.randint(1,59))
	pup = "%s %s-%s-%s"%(rdtime, random.randint(7,10),random.randint(1,59),random.randint(1,59))
	dup = "%s %s-%s-%s"%(rdtime, random.randint(11,22),random.randint(1,59),random.randint(1,59))
	miles = 25+i
	cost = float(miles*32.28)
	dlg = random.choice(dlogin_cache)
	ride_data.append((rid,bid,wtime,pup,dup,miles,cost,dlg))
	ride_cache.append(rid)

query =  """ insert into booking (booking_id, booking_datetime, pickup_point, drop_point, pickup_zip, dropoff_zip, user_id,booking_status, no_of_passengers) values (%s, %s, %s,%s, %s,%s,%s,%s,%s) """
insert_data(query,tuple(booking_data))

query =  """ insert into ride_details (ride_details_id, booking_id, waiting_time, pickup_time, drop_time, ride_cost, no_of_miles, driver_login_id) values  (%s, %s, %s,%s, %s,%s,%s,%s) """
insert_data(query,tuple(ride_data))


# Ride Details

# ride_cache = []
# ride_data = []
# for i in range(1,31):
# 	rid = i
# 	bid = random.choice(booking_cache)
# 	wtime = "%s %s-%s-%s"%(rdtime, random.randint(6,7),random.randint(1,59),random.randint(1,59))
# 	pup = "%s %s-%s-%s"%(rdtime, random.randint(7,10),random.randint(1,59),random.randint(1,59))
# 	dup = "%s %s-%s-%s"%(rdtime, random.randint(11,22),random.randint(1,59),random.randint(1,59))
# 	miles = 25+i
# 	cost = float(miles*32.28)
# 	dlg = random.choice(dlogin_cache)
# 	ride_data.append((rid,bid,wtime,pup,dup,miles,cost,dlg))
# 	ride_cache.append(rid)


# query =  """ insert into ride_details (ride_details_id, booking_id, waiting_time, pickup_time, drop_time, ride_cost, no_of_miles, driver_login_id) values  (%s, %s, %s,%s, %s,%s,%s,%s) """
# insert_data(query,tuple(ride_data))


#payment 
payment_cache = []
payment_data = []
for i in range(1,31):
	pid = i
	rid = i
	pmod = random.randint(1,3)
	payment_data.append((pid,rid,pmod))
	payment_cache.append(pid)


query =  """ insert into payment_info (payment_info_id, ride_details_id, payment_method) values  (%s, %s, %s) """
insert_data(query,tuple(payment_data))


#rating
rating_cache = []
rating_data = []

for i in range(1,31):
	year = random.randint(2017, 2017)
	month = random.randint(4, 4)
	day = random.randint(1, 10)
	ratid = i
	ride =i
	rating = random.randint(1,3)
	feedback = randomword(20).title()
	fdate = datetime(year, month, day).strftime("%Y-%m-%d")
	rating_data.append((ratid, ride,rating,feedback,fdate))
	rating_cache.append(ratid)


query =  """ insert into Rating (rating_id, ride_details_id, ratings,feedback,feedback_date) values  (%s, %s, %s, %s, %s) """
insert_data(query,tuple(rating_data))


#commission
com_cache = []
com_data = []

for i in range(1,31):
	commission_id = i
	driver_commission = ((25+1)*30)/100
	rid = i
	com_data.append((commission_id,driver_commission,rid))

query =  """ insert into commission (commission_id, driver_commission, ride_details_id) values  (%s, %s, %s) """
insert_data(query,tuple(com_data))
