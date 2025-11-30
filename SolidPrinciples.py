'''
SOLID:

S--> Single Responsibilty Principle

Rule: A classs should have one and only one reasom to change
'''

#Problem(violated SRP)
class UserManager:
    def create_user(me,name,email):
        #create user in db
        print(f"Saving {name} to DB")
        #send welcome email
        print(f"Sending welcome to {email}")

#this class both manages persistence and send email-two responsibilities.

#Refactor (follows SRP):
class UserRepo:
    def save(me,name,email):
        print(f"Saving {name} ({email}) to DB")

class EmailSender:
    def sendWelcome(me,email):
        print(f"Sending welcome email to {email}")

class userMan:
    def __init__(me,repo:UserRepo,mailer:EmailSender):
        me.repo=repo
        me.mailer=mailer
    
    def createUser(me,name,email):
        me.repo.save(name,email)
        me.mailer.sendWelcome(email)

#usage
repo=UserRepo()
mailer=EmailSender()
um=userMan(repo,mailer)
um.createUser("Pookie","pookie@princess.com")
        