import amino
from colorama import init, Fore, Back, Style
init(autoreset=True)
print(Fore.LIGHTCYAN_EX + "bot e e e")

client = amino.Client()
print(Fore.LIGHTGREEN_EX)
def loginc():
    try:
        email = input("Email - ")
        em = input("Passw - ")
        client.login(email, em)
    except amino.exceptions.InvalidEmail:
        print(Fore.LIGHTRED_EX + "Invalid email")
    except amino.exceptions.InvalidPassword:
        print(Fore.LIGHTRED_EX + "Invalid password")
    except amino.exceptions.FailedLogin:
        print(Fore.LIGHTRED_EX + "Fail login")
    except amino.exceptions.ActionNotAllowed:
        print(Fore.LIGHTRED_EX + "Change deviceId")
    except: pass
loginc()


print(Fore.LIGHTYELLOW_EX + "Communities:")
for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
    print (name, id)
    
comm = input("CommunityId - ")
subclient = amino.SubClient(comId=comm, profile=client.profile)
    



print(Fore.LIGHTYELLOW_EX + "Chats:")
for name, id in zip(subclient.get_chat_threads().title, subclient.get_chat_threads().chatId):
    print(name, id)
        
chatsel = input("chatId - ")
print(Fore.LIGHTYELLOW_EX + "wait...")
s = subclient.get_chat_thread(chatsel)
s1 = s.chatId
s2 = s.content
s3 = s.icon
s4 = s.backgroundImage
s5 = s.membersCount
s6 = s.title
s7 = s.createdTime
print(f"""
chatId - {s1}
title - {s6}
createdTime - {s7}
content - {s2}
iconLink - {s3}
backgroundLINK - {s4}
membersCount - {s5}\n
Done...""")