#3!/usr/bin/env python

from distutils.log import warn as printf
from random import randrange as rand
from pymongo import Connection, errors
from ushuffle_dbU import DBNAME,randName,FIELDS,tformat,cformat

COLLECTION = 'users' #Table. Collections have documents for each record.
#Create a connection  and raise exceotion if connection cannot be reached

class MongoTest(object):
	def __init__(self):
		try:
			cxn = Connection()
		except errors.AutoReconnect:
			raise RunTimeError()
		self.db = cxn[DBNAME] #reuse an existing DB
		self.users = self.db[COLLECTION]
		
	def insert(self): #Add values to a mongo collection
		self.users.insert(
			dict(login=who,userid=uid,projid=rand(1,5)) for who,uid in randName()) #create reord by using dict and stream into collections insert method
			
		
	def update(self):
		fr = rand(1,5)
		to = rand(1,5)
		i = -1
		for i,user in enumerate(self.users.find({'projid':fr})): #Before updating an existing value use find to query users in the systemwith proj id that  matches group we want to update
			self.users.update(user,{'$set':{'projid':to}})
		return fr,to,i+1

	def delete(self):
		rm = rand(1,5)
		i = -1
		for i,user in enumerate(self.users.find({'projid':rm})):
			self.users.remove(user)
		return rm,i+1
		
	def dbDump(self):
		printf('\n%s'% ' '.join(map(cformat,FIELDS)))
		for user in self.users.find():
			printf(''.join(map(tformat,(user[k] for k in FIELDS))))
	
	def finish(self):
		self.db.connection.disconnect()
		
def main():
	printf('***Connect to %r database' % DBNAME)
	try:
		mongo = MongoTest()
	except RuntimeError:
			printf('\nERROR: MongoDB Server unreachable, exit')
			return
			
	printf('\n*** Insert names into table')
	mongo.insert()
	mongo.dbDump()
		
		
		
	printf('\n*** Move users to a random group')
	fr,to,num = mongo.update()
	printf('\t(%d users moved) from (%d) to (%d)' %(num,fr,to))
	mongo.dbDump()
		
	printf('\n*** Randomly delete group')
	rm,num = mongo.delete()
	printf('\t(group #%d;%d users removed)' % (rm,num))
	mongo.dbDump()
		
	printf('\n*** Drop users table')
	#mongo.db.drop_collection(COLLECTION)
	printf('\n*** Close cxns')
	mongo.finish()
		
if __name__ == '__main__':
	main()
