"""
email_id="saketh@codegnan.com"
v=email_id[7:15]
print(v)

email_id=['meghana07@gmail.com','saketh@codegnan.com','ceo@codegnan.com','info@codegnan.com']
print(len(email_id))
#last two email
print(email_ids[-2:])

#Store 3 more email id """
email_id=['meghana07@gmail.com','saketh@codegnan.com','ceo@codegnan.com','info@codegnan.com']

"""email_id.extend(['durga@gmail.com','yamini@gmail.com','a@yahoo.com'])
print(email_id)
#Access each email_id one by one -->loops 
for mail in email_id:
    #print(mail)
    print(f'Mail of a person is {mail}')

#Get the above email-ids into the above users dict 
users={}
users=dict.fromkeys(email_id)
print(users)
users['meghana07@gmail.com']=2345
print(users)

users={}
for i in range(len(email_id)):
    users[i+1]=email_id[i]
print(users) """

#ENUMERATE : It Provides by default a counter object (you can store in desired collection)
data=dict(enumerate(email_id,1))
print(data)
