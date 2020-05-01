from fbchat import log, Client
from fbchat.models import *
from getpass import getpass




class HomieBot(Client):
    #overriding event handler to heart react each 
    #message my kings send me

        

    def fetchGenderById(self, user_id):
        users = self.fetchAllUsers()
        genders = [user.gender for user in users]
        ids     = [user.uid for user in users]
        db = dict(zip(ids, genders))
        return db[user_id]
 
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        gender = self.fetchGenderById(thread_id)
        print("Sender gender: %s" %(gender))
        log.info("Message object:\n %s\n from\n ThreadID: %s \nin\n %s" %(str(message_object), str(thread_id), str(thread_type.name)))
        if author_id != self.uid:
            if gender == "male_singular":
                print("Message shoud be heart reacted!")
                self.reactToMessage(message_object.uid, MessageReaction.LOVE)
            elif gender == "female_singular":
                print("Message should be angry reacted!")
                self.reactToMessage(message_object.uid, MessageReaction.ANGRY)
        
        
    

def startHomieBot(attempts = 3):
    try:
        username = input("Enter your Facebook username: ")
        #check if not email - TODO
        client = HomieBot(username, getpass())
        client.listen()
    except KeyboardInterrupt:
        print("Loging out the client!")
        print("Goodbye!")
        client.logout()




def main():
    startHomieBot()



if __name__ == "__main__":
    main()
