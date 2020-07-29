from fbchat import log, Client
from fbchat.models import *
from getpass import getpass 
from os import path
import random 




def spin_that_shit(msg, thread_id):
    president_speech = [
            "Vučić: Pogledajte gradjani Srbije, oni kazu da " + msg + " kad smo već dobre rezultate postigli u petom kvartalu ove godine za " + msg + ". Najbolji smo u zapadnom delu Istočne Evrope. Evo ako meni ne verujete evo rezultati pokazuju."
            , "Vučić: A da nismo tako postupili, šta bi onda rekli? Vučić diktator ne dozvoljava slobodu medija i " + msg + "Na njima je da pričaju i kritikuju, a na nama samo da radimo i da Srbija ide u boljem pravcu."
            , "Vučić: Recite vi meni @mention, kako vi mislite da rešimo problem za " + msg + " pošto očigledno ja ne znam."
            , "Vučić: Pa normalno da smo to dozvolili, šta mislite vi? Investitor koji je doneo " + msg + "nudi 500 novih mesta za posao, video sam ja te kancelarije. Imaju i bazen i lazybagove, najopremljenije kancelarije u regionu za " + msg + ". Za vreme onih pre, kojima ni ime neću da spominjem je Srbija bila u deficitu za " + msg + ", a sad smo lideri u regionu."
            , "Vučić: Nemojte molim Vas da mi upadate u reč dok objašnjavam građanima Srbije kako smo podigli najnefunkcionalnije zemljište Donjeg Brijanja na 2.6% kumulativnog profita za ovu nedelju. Računajući ulaganje od ranije, kumulativnom sumom se dolazi do 60% dodatnog profita za taj region. I nemojte misliti da ne znam šta je vaša ideja, @mention. Vaša je ideja da dobijete poene na Tviteru. Da ljudi pričaju \"Vidite samo kako je napičila Vučića u emisiji. Svaka čast\". Ali neće vam uspeti prošlo je vreme kad je Srbija bila slaba."
            , "Vučić: Ne bih o tome šta pišu neki stručnjaci iz Evrope za Dojče Vele o " + msg + ". Kako se beše zove Rihard Maj, kako se beše zove on Suzana, ma nije ni važno. Sve ću reći kad prođe sve ovo i moja dela će više govoriti o meni nego ja što pričam."
            , "Vučić: Recite vi meni, @mention, kako to da za vreme Dragana Đilasa i Vuka Jeremića niste postavljali pitanja o " + msg + ". Pa nije vas ni zanimalo, znamo gde ste radili i šta. Kako to da danas Srbija je u mnogo boljem položaju što se tiče i unutrašnje i spoljne politike nego pre osam godina. A nemate odgovor, pa dobro."
            , "Vučić: Evo, @mention, da vidite slike kako izgleda policijski centar koji ćemo graditi do 2031e godine. Najmodernija tehnologija će se koristiti, Huavei kamere i najbitnije je da ulažemo u policiju jer se u nju nije ulagalo 30 godina. Sad srpska policija ima pendreke od najkvalitetnije kože. Najkvalitetnije kacige u regionu."
            ]

    president_reaction = [
              "https://thumbs.gfycat.com/FemaleHotKingfisher-max-1mb.gif"
            , "https://i.makeagif.com/media/12-16-2014/cUNzGt.gif"
            , "https://media.tenor.com/images/6df3715db6cdf98dfae4a70573e84764/tenor.gif"
            , "https://thumbs.gfycat.com/DismalRichDore-small.gif"
            ]
    random_speech = random.choice(president_speech)
    random_reaction = random.choice(president_reaction)
    
    if (random_speech.find("@mention") != -1):
            new_msg = Message(text=random_speech, mentions=[Mention(thread_id, offset=10, length=8)])
    else:
            new_msg = Message(text=random_speech)

    return (random_reaction, new_msg)



class PresidenteBot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        log.info("Message object:\n%s\nfrom\nThreadID: %s\nin\n%s"
                %(str(message_object), str(thread_id), str(thread_type.name)))

        if author_id != self.uid:
            msg = spin_that_shit(message_object.text, thread_id)
            print("Sending %s" %(msg[1]))
            self.sendRemoteFiles(msg[0], msg[1], thread_id=thread_id, thread_type=thread_type) 
            






def initTextBot():
    try:
        username = input("Enter your facebook username: ")
        client = PresidenteBot(username, getpass())
        print("Žvalo b0t init.")
        client = client.listen()

    except KeyboardInterrupt:
        print("Logging out the client!")
        print("Goodbye, fren!")
        client.logout()

    

def main():
    initTextBot()



if __name__ == "__main__":
    main()
