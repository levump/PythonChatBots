from fbchat import log, Client
from fbchat.models import *
from getpass import getpass 
from os import path




def convert_to_b(msg):
    new_msg = ''.join(list(map(lambda x: '0' if x in "AEIOUaeiou" else x, msg)))
    return "Brn0b0 b0t pr0v0d: " + new_msg 



class TextBot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        log.info("Message object:\n%s\nfrom\nThreadID: %s\nin\n%s"
                %(str(message_object), str(thread_id), str(thread_type.name)))

        if author_id != self.uid:
            msg = convert_to_b(message_object.text)
            print("Sending %s" %(msg))
            self.sendRemoteFiles(file_urls="https://nova.rs/wp-content/uploads/2020/06/Ana_Brnabic_Hit_Tvit_Screenshot-725x491.jpg", message=Message(text=msg), thread_id=thread_id, thread_type=thread_type)







def initTextBot():
    try:
        username = input("Enter your facebook username: ")
        client = TextBot(username, getpass())
        print("Brn0b0 b0t init.")
        client = client.listen()

    except KeyboardInterrupt:
        print("Logging out the client!")
        print("Goodbye, fren!")
        client.logout()

    

def main():
    initTextBot()



if __name__ == "__main__":
    main()
