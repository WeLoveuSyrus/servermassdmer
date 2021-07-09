import discord, threading
from colorama import Fore
from colored import fg, attr
from pypresence import Presence
import datetime, subprocess
import colorama
import time
import os
client_id = '862840967707230218'
RPC = Presence(client_id)
RPC.connect()
RPC.update(state='MassDmer', details='made by $Y#8300', large_image='dsfdsfdf', small_image = "dsfdsfdf", start=time.time(), large_text="v1.0.0")

class colors:

    red = fg('#ff004d8')
    reset = attr('reset')
    gray = fg('#ff4b00')

asci = """
                                            ╔═╗╔═╗╦═╗╦  ╦╔═╗╦═╗  ╔╦╗╔╦╗╔═╗╦═╗
                                            ╚═╗║╣ ╠╦╝╚╗╔╝║╣ ╠╦╝   ║║║║║║╣ ╠╦╝
                                            ╚═╝╚═╝╩╚═ ╚╝ ╚═╝╩╚═  ═╩╝╩ ╩╚═╝╩╚═
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
                                        """.replace("█", f"{Fore.LIGHTBLACK_EX}█{Fore.WHITE}")


def get_date_now(time_now):
    return time_now.strftime("%I:%M:%S")

os.system('cls & title SERVER MASSDMER')

print(asci)
                                      
print(f"{Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{Fore.WHITE}] {Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}Info{Fore.WHITE}{Fore.WHITE}] {Fore.LIGHTBLACK_EX} Launching Mass Dmer v1""")
time.sleep(1)
print(f"""{Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{Fore.WHITE}] {Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}Debug{Fore.WHITE}{Fore.WHITE}] {Fore.LIGHTBLACK_EX} Running debug process..""")
time.sleep(1)
hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
print(f"""{Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{Fore.WHITE}] {Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}Debug{Fore.WHITE}{Fore.WHITE}] {Fore.LIGHTBLACK_EX} Completed Debug task.""")
time.sleep(1)
print(f"""{Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{Fore.WHITE}] {Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}Info{Fore.WHITE}{Fore.WHITE}] {Fore.LIGHTBLACK_EX} Machine uuid ({hwid}) is now being utilized.""")
time.sleep(1)
print(f"""{Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{Fore.WHITE}] {Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}Info{Fore.WHITE}{Fore.WHITE}] {Fore.LIGHTBLACK_EX} Passed checks, moving foward.""")
time.sleep(1)
print(f"{Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{Fore.WHITE}] {Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}8300{Fore.WHITE}{Fore.WHITE}] {Fore.LIGHTBLACK_EX} Client version: 1.0.0 is up to date.")
time.sleep(1)
print(f"{Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{Fore.WHITE}] {Fore.WHITE}[{Fore.WHITE}{Fore.WHITE}8300{Fore.WHITE}{Fore.WHITE}] {Fore.LIGHTBLACK_EX} \"thank you for using MassDmer for you're task\"")
os.system('cls')

class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.to_dm = []


    async def on_ready(self):
            x = input("Server ID => ")
            z = input("What Message => ")
            guild = self.get_guild(int(x))
            if not guild:
                print("failed to find server")
            else:
                for y in range(int(guild.member_count)-1):
                    try:
                        data = await guild.members[y].create_dm()
                        print(f"created a dm for {str(guild.members[y])}")
                        threading.Thread(target=self.to_dm.append, args=(data.recipient,)).start()
                    except:
                        pass
                if self.to_dm == [] or len(self.to_dm) == 0:
                    print(f"couldn't scrape any users")
                else:
                    for recipient in self.to_dm:
                        try:
                            await recipient.send(z)
                            print(f"sent dm to {recipient}")
                        except:
                            continue
                        

    def run(self, token):
        return super().run(token, bot=False)


token = "TOKEN HERE"
client = Client(intents=discord.Intents.all())
client.run(token)