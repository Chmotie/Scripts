 # -*- coding: utf8 -*- 
 #Создатель - chmotie
 #Во вопросам пиши в личку)
#  ___              _          _        
# / __|  __   _ _  (_)  _ __  | |_   ___
# \__ \ / _| | '_| | | | '_ \ |  _| (_-<
# |___/ \__| |_|   |_| | .__/  \__| /__/
#                      |_|              
#Version:0.1      
import vk_api
import colorama
import init
import os
import socket
from sys import platform
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
import requests
import time
import datetime
import urllib.request
from vk_api import audio
from vk_api import VkUpload

colorama.init()



def check_os():
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "win32":
       os.system("cls")

raid_bot = ['''
  ___          _      _   ___         _   
 | _ \  __ _  (_)  __| | | _ )  ___  | |_ 
 |   / / _` | | | / _` | | _ \ / _ \ |  _|
 |_|_\ \__,_| |_| \__,_| |___/ \___/  \__|
                                                       
''']

scan_port = ['''
  \033[31m
  ___                      ___               _   
 / __|  __   __ _   _ _   | _ \  ___   _ _  | |_ 
 \__ \ / _| / _` | | ' \  |  _/ / _ \ | '_| |  _|
 |___/ \__| \__,_| |_||_| |_|   \___/ |_|    \__| 
              \033[33mЕсли поставить port "auto" 
              Он сам просканирует популярные порты.                                   
             
''']



hello = [
'''
\033[31m
  ___              _          _        
 / __|  __   _ _  (_)  _ __  | |_   ___
 \__ \ / _| | '_| | | | '_ \ |  _| (_-<
 |___/ \__| |_|   |_| | .__/  \__| /__/
                      |_|              
        
                        author:chmotie
                        version:0.1
                                            
'''
]

vktool = ['''
 __   __  _     _____               _      
 \ \ / / | |__ |_   _|  ___   ___  | |  ___
  \ V /  | / /   | |   / _ \ / _ \ | | (_-<
   \_/   |_\_\   |_|   \___/ \___/ |_| /__/
                                           
                                                    
''']

damp = ['''
[1] - Скачать все диалоги
[2] - Скачать диалог с определенным человеком      
      ''']
damp_ph = ['''
[1] - Скачать вложения с определенным человеком
[2] - Скачать все вложения с профиля
''']

deanon = ['''
  ___                                   
 |   \   ___   __ _   _ _    ___   _ _  
 | |) | / -_) / _` | | ' \  / _ \ | ' \ 
 |___/  \___| \__,_| |_||_| \___/ |_||_|
                                                  
''']
vktool_func = ['''
[1] - Накрутка смс
[2] - Накрутка фотографий
[3] - Накрутка коментов
[4] - Накрутка постов
[5] - Скачивание переписок в TXT
[6] - Скачивание фотографи с профиля человека
[7] - Скачивание музыки
[8] - Удаление всех ваших друзей
[9] - Парсер стикеров
[10] - В разработке
[99] - Выход
''']

comments = ['''
[1] - Прочитать все токены
[2] - Добавить токен
[3] - Начать накрутку            
''']

deanon_func = ['''
[1] - Пробив IP
[2] - Пробив Номера                
''']



scripts = ["""
\033[31m
[1] - Scan Port
[2] - Raid Bot VK
[3] - Deanon
[4] - VkTools                       
           """]

print(hello[0] + scripts[0])

vibor = input("-->")

if vibor.isdigit():
    if vibor == "1":
        check_os()
        print(scan_port[0])
        
        ip = input("\033[31mIP -->")
        port = input("PORT -->")
        
        sock = socket.socket()

        try:
            ports = [21, 22, 43, 80, 443, 8000, 8080]
            if port == "auto":
                for i in ports:
                    try:
                        sock.connect(((ip,i)))
                    except socket.error:
                        print("\033[31m\n[!]ПОРТ ЗАКРЫТ " + str(i))
                    else:
                        print("\033[32m\n[!]ПОРТ ОТКРЫТ " + str(i))                    

            else:
                sock.connect(((ip,int(port))))
        except socket.error:
            print("\033[31m\n[!]ПОРТ ЗАКРЫТ " + str(port))
        else:
            print("\033[32m\n[!]ПОРТ ОТКРЫТ " + str(port))
    
    elif vibor == "2":
        check_os()
        print(raid_bot[0])
        
        token = input("Token --> ") 
        idgroup = input("ID Group --> ")
        
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        longpoll = VkBotLongPoll(vk_session, idgroup)
        textraid = "🤧😲🤢😳😷😂❤💋😚😕😯😦😵🙄🤔😠😡😝😴😘😗😙😟🙁☹😬😶🤐😫☺😀😥😛😖😤😣😧😑😅😮😞😓😱🤓🤑😪🤒🤕🤥🤠😈👿👽👻😸😹😼😽😾😿😻🙀😺🙈🙉🙊💩💀👹👺👍👎☝✌👌🖕🏻🤘🏻👏👊💪✋🖐🏻🖖🏻🙏🙌✊👆👇👈👉👋👐🤞🏻🤝🤙🏻🤛🏻🤜🏻👀👂👃✍🏻👅👫👬👭💏💑👯👪👰👦👧👨👩👱👮👲👳💂👴👵👶👷👸👼🙇🤰🏻💅💄👄💃🎎🎅🚶👱‍♀️👮‍♀️👷‍♀️🕵‍♀️🙇‍♀️🙋‍♂️🙋💁‍♂️💁🙅‍♂️🙅🙆‍♂️🙆🙎‍♂️🙎💆‍♂️💆💇‍♂️💇🤷🏻‍♂️🤷🏻‍♀️🤦🏻‍♂️🤦‍♀️🙍‍♂️🚶‍♀️🤳🏻🏃‍♀️👯‍♂️🏌‍♀️🐱🤡🕺👳‍♀️💂‍♀️🤵🤴🤹‍♂️🤹‍♀️👨‍⚖️👩‍⚖️👨‍✈️👩‍✈️👨‍🚒️👩‍🚒️👨‍🎤️👩‍🎤️👨‍🎓️👩‍🎓️👨‍🏫️👩‍🏫️👨‍🌾️👩‍🌾️👨‍🍳️👩‍🍳️👨‍🔧️👩‍🔧️👨‍🏭️👩‍🏭️👨‍💼️👩‍💼️👨‍🔬️👩‍🔬️👨‍💻️👩‍💻️👨‍🎨️👩‍🎨️👨‍🚀️👩‍🚀️👨‍⚕️👩‍⚕️💓💔💕💖💗💘💙💚💛💜💝💞💟💬💭🔞⚠⛔🐩🆘🌚🖤💨🔥☀☁⛄❄⛅✨🌍🌛🌝🌞☄🌈🌖⚕🌱🌲🌳🌴🌷🌸🍅🍆🍇🍈🍉🍊🍋🍌🍍🍎🍏🍐🍑🐀🐁🐂🐃🐄🐅🐆🐇🐈🐉🐊🐋🐌🐍🐎🐏🐐🐑🐒🐓🐔🐕🐖🐗🐘🐙🐚🐛🐜🐝🐞🐟🐠🐡🐢🐣🐤🐥🐦🐧🐨🐪🐫🐬🐭🐮🐯🐰🐲🐳🐴🐵🐶🐷🐸🐹🐺🐻🐼🐽🐾🌰🌵🌹🌺🌻🌼🌽🌾🌿🍀🍁🍂🍃🍄💦💧🦉🦍🦏🦋🦊🦈🦆🦅🦇🦎🦐🦑🥀🦌🍒🍓🍔🍕🍖🍗🍚🍛🍜🍝🍧🍦🍥🍤🍣🍢🍡🍠🍟🍞🍨🍩🍪🍫🍬🍭🍮🍯🍰🍱🍻🍺🍹🍸🍷🍶🍵🍴🍳🍲🍼🥙🥝🥜🥘🥗🥖🥓🥐🥂🥛🥚🥞🥒🥔🥕🥃🥑⚽⚾🎯🎱🎽🎾🎿🏀🏁🏂🚴🚣👟🏊🏉🏈🏇🏆🏄🏃🚵⛳⛪🤽🏻‍♂️🤽🏻‍♀️🤾🏻‍♂️🤼‍♂️🤸🏻‍♂️🏋‍♀️⛹‍♀️🥅🥋🥊🛶🛴🤺🚴‍♀️🚵‍♀️🏊‍♀️🏄‍♀️🥁🚅🚆🚇🚈🚊🚌🚍🚎🚏🚐🚚🚙🚘🚗🚖🚕🚔🚓🚒🚑🚛🚜🚝🚞🚟🚠🚡🚤🚨🚧🛵🏜✈⛽🚄🚃🚂🚁🚀⛵⏰⏳☎☕♻⚡✂✉✏✒🎈🎄🎃🎂🎁🎀🌟🌂🃏🀄🎉🎊🎋🎌🎍🎏🎐🎒🎓🎣🎲🎰🎭🎬🎫🎪🎩🎨🎧🎤🎳🎴🎷🎸🎹🎺🎻👑👒👓👜👠👛👚👙👘👗👖👕👔👝👞👡👢👣👾💈💉💊💌💴💳💰💥💣💡💒💐💎💍💵💶💷💸💺💻💼💽💾💿📎📍📌📋📊📉📈📇📅📄📐📑📒📓📔📕📖📗📘📙📮📭📦📢📡📠📟📝📜📚📯🔑🔭🥇🥈🔮🔔📰📱🔖🔱🥉🛒🗿🔦📷📹🔧🚪🚬🔨📺📻🔩🚽🚿🔪📼🔆🔫🛀🥄🔬🔎🇨🇳🇺🇦🇮🇱🇳🇿🇫🇮🇮🇷🇹🇳🇲🇦🇨🇱🇳🇴🇮🇳🇰🇿🇩🇪🇪🇸🇧🇾🇮🇩🇦🇪🇨🇭🇳🇬🇵🇦🇸🇪🇵🇱🇮🇪🇦🇺🇫🇷🇬🇧🇦🇹🇨🇦🇵🇹🇿🇦🇵🇪🇷🇸🏳‍🌈️🇵🇷🇨🇴🇧🇪🇮🇹🇯🇵🇧🇷🇲🇴🇸🇦🇦🇷🇸🇳🏴󠁧󠁢󠁥󠁮󠁧󠁿🇨🇷🏴󠁧󠁢󠁥󠁮󠁧󠁿🇨🇷🇸🇬🇲🇾🇻🇳🇰🇷🇷🇺🇭🇰🇲🇽🇹🇷🇪🇬🇺🇾🇮🇸🇭🇷🇵🇭🇳🇱🇩🇰🇩🇰🇺🇸😄😁😊😃🤣😆😉😜😋🤗😍😎😒😏🙂🙃😔😢😭😩😨😐😌🤤😇😰🤧😲🤢😳😷😂❤💋😚😕😯😦😵🙄🤔😠😡😝😴😘😗😙😟🙁☹😬😶🤐😫☺😀😥😛😖😤😣😧😑😅😮😞😓😱🤓🤑😪🤒🤕🤥🤠😈👿👽👻😸😹😼😽😾😿😻🙀😺🙈🙉🙊💩💀👹👺👍👎☝✌👌🖕🏻🤘🏻👏👊💪✋🖐🏻🖖🏻🙏🙌✊👆👇👈👉👋👐🤞🏻🤝🤙🏻🤛🏻🤜🏻👀👂👃✍🏻👅👫👬👭💏💑👯👪👰👦👧👨👩👱👮👲👳💂👴👵👶👷👸👼🙇🤰🏻💅💄👄💃🎎🎅🚶👱‍♀️👮‍♀️👷‍♀️🕵‍♀️🙇‍♀️🙋‍♂️🙋💁‍♂️💁🙅‍♂️🙅🙆‍♂️🙆🙎‍♂️🙎💆‍♂️💆💇‍♂️💇🤷🏻‍♂️🤷🏻‍♀️🤦🏻‍♂️🤦‍♀️🙍‍♂️🚶‍♀️🤳🏻🏃‍♀️👯‍♂️🏌‍♀️🐱🤡🕺👳‍♀️💂‍♀️🤵🤴🤹‍♂️🤹‍♀️👨‍⚖️👩‍⚖️👨‍✈️👩‍✈️👨‍🚒️👩‍🚒️👨‍🎤️👩‍🎤️👨‍🎓️👩‍🎓️👨‍🏫️👩‍🏫️👨‍🌾️👩‍🌾️👨‍🍳️👩‍🍳️👨‍🔧️👩‍🔧️👨‍🏭️👩‍🏭️👨‍💼️👩‍💼️👨‍🔬️👩‍🔬️👨‍💻️👩‍💻️👨‍🎨️👩‍🎨️👨‍🚀️👩‍🚀️👨‍⚕️👩‍⚕️💓💔💕💖💗💘💙💚💛💜💝💞💟💬💭🔞⚠⛔🐩🆘🌚🖤💨🔥☀☁⛄❄⛅✨🌍🌛🌝🌞☄🌈🌖⚕🌱🌲🌳🌴🌷🌸🍅🍆🍇🍈🍉🍊🍋🍌🍍🍎🍏🍐🍑🐀🐁🐂🐃🐄🐅🐆🐇🐈🐉🐊🐋🐌🐍🐎🐏🐐🐑🐒🐓🐔🐕🐖🐗🐘🐙🐚🐛🐜🐝🐞🐟🐠🐡🐢🐣🐤🐥🐦🐧🐨🐪🐫🐬🐭🐮🐯🐰🐲🐳🐴🐵🐶🐷🐸🐹🐺🐻🐼🐽🐾🌰🌵🌹🌺🌻🌼🌽🌾🌿🍀🍁🍂🍃🍄💦💧🦉🦍🦏🦋🦊🦈🦆🦅🦇🦎🦐🦑🥀🦌🍒🍓🍔🍕🍖🍗🍚🍛🍜🍝🍧🍦🍥🍤🍣🍢🍡🍠🍟🍞🍨🍩🍪🍫🍬🍭🍮🍯🍰🍱🍻🍺🍹🍸🍷🍶🍵🍴🍳🍲🍼🥙🥝🥜🥘🥗🥖🥓🥐🥂🥛🥚🥞🥒🥔🥕🥃🥑⚽⚾🎯🎱🎽🎾🎿🏀🏁🏂🚴🚣👟🏊🏉🏈🏇🏆🏄🏃🚵⛳⛪🤽🏻‍♂️🤽🏻‍♀️🤾🏻‍♂️🤼‍♂️🤸🏻‍♂️🏋‍♀️⛹‍♀️🥅🥋🥊🛶🛴🤺🚴‍♀️🚵‍♀️🏊‍♀️🏄‍♀️🥁🚅🚆🚇🚈🚊🚌🚍🚎🚏🚐🚚🚙🚘🚗🚖🚕🚔🚓🚒🚑🚛🚜🚝🚞🚟🚠🚡🚤🚨🚧🛵🏜✈⛽🚄🚃🚂🚁🚀⛵⏰⏳☎☕♻⚡✂✉✏✒🎈🎄🎃🎂🎁🎀🌟🌂🃏🀄🎉🎊🎋🎌🎍🎏🎐🎒🎓🎣🎲🎰🎭🎬🎫🎪🎩🎨🎧🎤🎳🎴🎷🎸🎹🎺🎻👑👒👓👜👠👛👚👙👘👗👖👕👔👝👞КУ ОТ МАЛАХОВА ШАВКИ НАХУЙ ЕБАНЫЕ😆 😆 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐🤧😲🤢😳😷😂❤💋😚😕😯😦😵🙄🤔😠😡😝😴😘😗😙😟🙁☹😬😶🤐😫☺😀😥😛😖😤😣😧😑😅😮😞😓😱🤓🤑😪🤒🤕🤥🤠😈👿👽👻😸😹😼😽😾😿😻🙀😺🙈🙉🙊💩💀👹👺👍👎☝✌👌🖕🏻🤘🏻👏👊💪✋🖐🏻🖖🏻🙏🙌✊👆👇👈👉👋👐🤞🏻🤝🤙🏻🤛🏻🤜🏻👀👂👃✍🏻👅👫👬👭💏💑👯👪👰👦👧👨👩👱👮👲👳💂👴👵👶👷👸👼🙇🤰🏻💅💄👄💃🎎🎅🚶👱‍♀️👮‍♀️👷‍♀️🕵‍♀️🙇‍♀️🙋‍♂️🙋💁‍♂️💁🙅‍♂️🙅🙆‍♂️🙆🙎‍♂️🙎💆‍♂️💆💇‍♂️💇🤷🏻‍♂️🤷🏻‍♀️🤦🏻‍♂️🤦‍♀️🙍‍♂️🚶‍♀️🤳🏻🏃‍♀️👯‍♂️🏌‍♀️🐱🤡🕺👳‍♀️💂‍♀️🤵🤴🤹‍♂️🤹‍♀️👨‍⚖️👩‍⚖️👨‍✈️👩‍✈️👨‍🚒️👩‍🚒️👨‍🎤️👩‍🎤️👨‍🎓️👩‍🎓️👨‍🏫️👩‍🏫️👨‍🌾️👩‍🌾️👨‍🍳️👩‍🍳️👨‍🔧️👩‍🔧️👨‍🏭️👩‍🏭️👨‍💼️👩‍💼️👨‍🔬️👩‍🔬️👨‍💻️👩‍💻️👨‍🎨️👩‍🎨️👨‍🚀️👩‍🚀️👨‍⚕️👩‍⚕️💓💔💕💖💗💘💙💚💛💜💝💞💟💬💭🔞⚠⛔🐩🆘🌚🖤💨🔥☀☁⛄❄⛅✨🌍🌛🌝🌞☄🌈🌖⚕🌱🌲🌳🌴🌷🌸🍅🍆🍇🍈🍉🍊🍋🍌🍍🍎🍏🍐🍑🐀🐁🐂🐃🐄🐅🐆🐇🐈🐉🐊🐋🐌🐍🐎🐏🐐🐑🐒🐓🐔🐕🐖🐗🐘🐙🐚🐛🐜🐝🐞🐟🐠🐡🐢🐣🐤🐥🐦🐧🐨🐪🐫🐬🐭🐮🐯🐰🐲🐳🐴🐵🐶🐷🐸🐹🐺🐻🐼🐽🐾🌰🌵🌹🌺🌻🌼🌽🌾🌿🍀🍁🍂🍃🍄💦💧🦉🦍🦏🦋🦊🦈🦆🦅🦇🦎🦐🦑🥀🦌🍒🍓🍔🍕🍖🍗🍚🍛🍜🍝🍧🍦🍥🍤🍣🍢🍡🍠🍟🍞🍨🍩🍪🍫🍬🍭🍮🍯🍰🍱🍻🍺🍹🍸🍷🍶🍵🍴🍳🍲🍼🥙🥝🥜🥘🥗🥖🥓🥐🥂🥛🥚🥞🥒🥔🥕🥃🥑⚽⚾🎯🎱🎽🎾🎿🏀🏁🏂🚴🚣👟🏊🏉🏈🏇🏆🏄🏃🚵⛳⛪🤽🏻‍♂️🤽🏻‍♀️🤾🏻‍♂️🤼‍♂️🤸🏻‍♂️🏋‍♀️⛹‍♀️🥅🥋🥊🛶🛴🤺🚴‍♀️🚵‍♀️🏊‍♀️🏄‍♀️🥁🚅🚆🚇🚈🚊🚌🚍🚎🚏🚐🚚🚙🚘🚗🚖🚕🚔🚓🚒🚑🚛🚜🚝🚞🚟🚠🚡🚤🚨🚧🛵🏜✈⛽🚄🚃🚂🚁🚀⛵⏰⏳☎☕♻⚡✂✉✏✒🎈🎄🎃🎂🎁🎀🌟🌂🃏🀄🎉🎊🎋🎌🎍🎏🎐🎒🎓🎣🎲🎰🎭🎬🎫🎪🎩🎨🎧🎤🎳🎴🎷🎸🎹🎺🎻👑👒👓👜👠👛👚👙👘👗👖👕👔👝👞👡👢👣👾💈💉💊💌💴💳💰💥💣💡💒💐💎💍💵💶💷💸💺💻💼💽💾💿📎📍📌📋📊📉📈📇📅📄📐📑📒📓📔📕📖📗📘📙📮📭📦📢📡📠📟📝📜📚📯🔑🔭🥇🥈🔮🔔📰📱🔖🔱🥉🛒🗿🔦📷📹🔧🚪🚬🔨📺📻🔩🚽🚿🔪📼🔆🔫🛀🥄🔬🔎🇨🇳🇺🇦🇮🇱🇳🇿🇫🇮🇮🇷🇹🇳🇲🇦🇨🇱🇳🇴🇮🇳🇰🇿🇩🇪🇪🇸🇧🇾🇮🇩🇦🇪🇨🇭🇳🇬🇵🇦🇸🇪🇵🇱🇮🇪🇦🇺🇫🇷🇬🇧🇦🇹🇨🇦🇵🇹🇿🇦🇵🇪🇷🇸🏳‍🌈️🇵🇷🇨🇴🇧🇪🇮🇹🇯🇵🇧🇷🇲🇴🇸🇦🇦🇷🇸🇳🏴󠁧󠁢󠁥󠁮󠁧󠁿🇨🇷🏴󠁧󠁢󠁥󠁮󠁧󠁿🇨🇷🇸🇬🇲🇾🇻🇳🇰🇷🇷🇺🇭🇰🇲🇽🇹🇷🇪🇬🇺🇾🇮🇸🇭🇷🇵🇭🇳🇱🇩🇰🇩🇰🇺🇸😄😁😊😃🤣😆😉😜😋🤗😍😎😒😏🙂🙃😔😢😭😩😨😐😌🤤😇😰🤧😲🤢😳😷😂❤💋😚😕😯😦😵🙄🤔😠😡😝😴😘😗😙😟🙁☹😬😶🤐😫☺😀😥😛😖😤😣😧😑😅😮😞😓😱🤓🤑😪🤒🤕🤥🤠😈👿👽👻😸😹😼😽😾😿😻🙀😺🙈🙉🙊💩💀👹👺👍👎☝✌👌🖕🏻🤘🏻👏👊💪✋🖐🏻🖖🏻🙏🙌✊👆👇👈👉👋👐🤞🏻🤝🤙🏻🤛🏻🤜🏻👀👂👃✍🏻👅👫👬👭💏💑👯👪👰👦👧👨👩👱👮👲👳💂👴👵👶👷👸👼🙇🤰🏻💅💄👄💃🎎🎅🚶👱‍♀️👮‍♀️👷‍♀️🕵‍♀️🙇‍♀️🙋‍♂️🙋💁‍♂️💁🙅‍♂️🙅🙆‍♂️🙆🙎‍♂️🙎💆‍♂️💆💇‍♂️💇🤷🏻‍♂️🤷🏻‍♀️🤦🏻‍♂️🤦‍♀️🙍‍♂️🚶‍♀️🤳🏻🏃‍♀️👯‍♂️🏌‍♀️🐱🤡🕺👳‍♀️💂‍♀️🤵🤴🤹‍♂️🤹‍♀️👨‍⚖️👩‍⚖️👨‍✈️👩‍✈️👨‍🚒️👩‍🚒️👨‍🎤️👩‍🎤️👨‍🎓️👩‍🎓️👨‍🏫️👩‍🏫️👨‍🌾️👩‍🌾️👨‍🍳️👩‍🍳️👨‍🔧️👩‍🔧️👨‍🏭️👩‍🏭️👨‍💼️👩‍💼️👨‍🔬️👩‍🔬️👨‍💻️👩‍💻️👨‍🎨️👩‍🎨️👨‍🚀️👩‍🚀️👨‍⚕️👩‍⚕️💓💔💕💖💗💘💙💚💛💜💝💞💟💬💭🔞⚠⛔🐩🆘🌚🖤💨🔥☀☁⛄❄⛅✨🌍🌛🌝🌞☄🌈🌖⚕🌱🌲🌳🌴🌷🌸🍅🍆🍇🍈🍉🍊🍋🍌🍍🍎🍏🍐🍑🐀🐁🐂🐃🐄🐅🐆🐇🐈🐉🐊🐋🐌🐍🐎🐏🐐🐑🐒🐓🐔🐕🐖🐗🐘🐙🐚🐛🐜🐝🐞🐟🐠🐡🐢🐣🐤🐥🐦🐧🐨🐪🐫🐬🐭🐮🐯🐰🐲🐳🐴🐵🐶🐷🐸🐹🐺🐻🐼🐽🐾🌰🌵🌹🌺🌻🌼🌽🌾🌿🍀🍁🍂🍃🍄💦💧🦉🦍🦏🦋🦊🦈🦆🦅🦇🦎🦐🦑🥀🦌🍒🍓🍔🍕🍖🍗🍚🍛🍜🍝🍧🍦🍥🍤🍣🍢🍡🍠🍟🍞🍨🍩🍪🍫🍬🍭🍮🍯🍰🍱🍻🍺🍹🍸🍷🍶🍵🍴🍳🍲🍼🥙🥝🥜🥘🥗🥖🥓🥐🥂🥛🥚🥞🥒🥔🥕🥃🥑⚽⚾🎯🎱🎽🎾🎿🏀🏁🏂🚴🚣👟🏊🏉🏈🏇🏆🏄🏃🚵⛳⛪🤽🏻‍♂️🤽🏻‍♀️🤾🏻‍♂️🤼‍♂️🤸🏻‍♂️🏋‍♀️⛹‍♀️🥅🥋🥊🛶🛴🤺🚴‍♀️🚵‍♀️🏊‍♀️🏄‍♀️🥁🚅🚆🚇🚈🚊🚌🚍🚎🚏🚐🚚🚙🚘🚗🚖🚕🚔🚓🚒🚑🚛🚜🚝🚞🚟🚠🚡🚤🚨🚧🛵🏜✈⛽🚄🚃🚂🚁🚀⛵⏰⏳☎☕♻⚡✂✉✏✒🎈🎄🎃🎂🎁🎀🌟🌂🃏🀄🎉🎊🎋🎌🎍🎏🎐🎒🎓🎣🎲🎰🎭🎬🎫🎪🎩🎨🎧🎤🎳🎴🎷🎸🎹🎺🎻👑👒👓👜👠👛👚👙👘👗👖👕👔👝👞КУ ОТ МАЛАХОВА ШАВКИ НАХУЙ ЕБАНЫЕ😆 😆 卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐卐"
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_chat:
                    while True:
                        colorr = random.choice(['negative','primary', 'positive', 'secondary'])
                        color = random.choice(['negative','positive', 'primary', 'secondary'])
                        colo = random.choice(['negative','primary', 'positive', 'secondary'])
                        col = random.choice(['negative','primary', 'positive', 'secondary'])
                        textfobot = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        textfobo = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        textfob = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        textfo = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        keyboard = VkKeyboard(one_time=False)
                        keyboard.add_button(textfobot, color=colorr)
                        keyboard.add_button(textfobo, color=color)
                        keyboard.add_button(textfob, color=colo)
                        keyboard.add_button(textfo, color=col)
                        keyboard.add_line()
                        text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        col1 = random.choice(['negative','primary', 'positive', 'secondary'])
                        col2 = random.choice(['negative','primary', 'positive', 'secondary'])
                        col3 = random.choice(['negative','primary', 'positive', 'secondary'])
                        col4 = random.choice(['negative','primary', 'positive', 'secondary'])
                        keyboard.add_button(text1, color=col1)
                        keyboard.add_button(text2, color=col2)
                        keyboard.add_button(text3, color=col3)
                        keyboard.add_button(text4, color=col4)
                        keyboard.add_line()
                        text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                        keyboard.add_button(text1,color=col1)
                        keyboard.add_button(text2,color=col2)
                        keyboard.add_button(text3,color=col3)
                        keyboard.add_button(text4,color=col4)
                        keyboard.add_line()
                        text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                        keyboard.add_button(text1, color=col1)
                        keyboard.add_button(text2, color=col2)
                        keyboard.add_button(text3, color=col3)
                        keyboard.add_button(text4, color=col4)
                        keyboard.add_line()
                        text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                        keyboard.add_button(text1, color=col1)
                        keyboard.add_button(text2, color=col2)
                        keyboard.add_button(text3, color=col3)
                        keyboard.add_button(text4, color=col4)
                        keyboard.add_line()
                        text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                        keyboard.add_button(text1, color=col1)
                        keyboard.add_button(text2, color=col2)
                        keyboard.add_button(text3, color=col3)
                        keyboard.add_button(text4, color=col4)
                        keyboard.add_line()
                        text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru'])
                        text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                        keyboard.add_button(text1, color=col1)
                        keyboard.add_button(text2, color=col2)
                        keyboard.add_button(text3, color=col3)
                        keyboard.add_button(text4, color=col4)
                        keyboard.add_line()
                        text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                        keyboard.add_button(text1, color=col1)
                        keyboard.add_button(text2, color=col2)
                        keyboard.add_button(text3, color=col3)
                        keyboard.add_button(text4, color=col4)
                        keyboard.add_line()
                        text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                        keyboard.add_button(text1, color=col1)
                        keyboard.add_button(text2, color=col2)
                        keyboard.add_button(text3, color=col3)
                        keyboard.add_button(text4, color=col4)
                        keyboard.add_line()
                        text1 = random.choice(['[СТОП|sosi.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                        col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                        col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                        keyboard.add_button(text1, color=col1)
                        keyboard.add_button(text2, color=col2)
                        keyboard.add_button(text3, color=col3)
                        keyboard.add_button(text4, color=col4)
                        vk.messages.send(chat_id=event.chat_id,message=textraid,random_id='0',keyboard=keyboard.get_keyboard(),v=5.95)
                        vk.messages.send(chat_id=event.chat_id,message=textraid,random_id='0',keyboard=keyboard.get_keyboard(),v=5.95)
                        print("Raid Пошел!")
    
    elif vibor == "3":
        check_os()
        print(deanon[0] + deanon_func[0])
        
        vibord = input("--> ")
        if vibord  == '1':
            ip = input("IP --> ")
            rs = requests.get("http://ip-api.com/json/" + ip)
            gan = rs.json()
            country = gan['country']
            code = gan['countryCode']
            reg = gan['region']
            regn = gan['regionName']
            cit = gan['city']
            prova = gan['isp']
            organiz = gan['org']
            quer = gan['query']
            sta = gan['status']
            print(f'❗IP: {quer} \nСтатус: {sta} \nСтрана: {country} \nКод: {code} \nНазвание региона: {regn} \nГород: {cit} \nПровайдер: {prova} \nОрганизация: {organiz}') 
                
        if vibord == '2':   
            num = input("Number --> ") 
            num = num.replace('-','')
            num = num.replace('+','')
            num = num.replace(' ','')
            resw = requests.get(f"https://htmlweb.ru/geo/api.php?json&telcod={num}")
            js = resw.json()
            reg = js['region']['name']
            quer = js['capital']['name']
            oper = js['0']['oper']
            print('Поиск информации... ')
            time.sleep(3)
            print(f'Номер телефона: {num} \nРегион: {reg} \nОператор: {oper} \nГород: {quer}')
        
        else:
            print("[!] Ошибка.")

    elif vibor == "4":
        check_os()
        print(vktool[0] + vktool_func[0])
        
        vibortool = input("--> ")
        
        if vibortool == "1":

            token = input("Token --> ")
            kolvo = input("Кол-во SMS --> ")
            peoples = input("ID Людей которые будут в накрутке --> ")
            
            vk_session = vk_api.VkApi(token=token)
            vk = vk_session.get_api()
            
            i = 0
            try:
                while i < int(kolvo):
                    vk.messages.createChat(user_ids=peoples,title='Накрутка228')
                    i += 1
                    time.sleep(60)
                i = 0
            except vk_api.exceptions.ApiError:
                print("[!] Проверьте токен и ID Пользователей.")
            
        if vibortool == "2":
            check_os()
            print(vktool[0])
            token = input("Token --> ")
            album_id = input("Album Id --> ")
            vk_session = vk_api.VkApi(token=token)
            vks = vk_session
            upload = VkUpload(vk_session)
            try:
                while True: 
                    upload.photo(photos="photo.jpg",album_id=album_id)
            except FileNotFoundError:
                print("Здравствуйте, у вас нету файла фотки.\n Загрузите его, скиньте фотографию в папку со скриптом.\n Обязательно что бы она была под названием 'photo.jpg' ")
                
                
        if vibortool == "3":
            check_os()
            print(vktool[0] + comments[0])
            viborcomm = input("--> ")
            if viborcomm == "1":
                token_file = open("token.txt","r",encoding="utf-8")
                token_read = token_file.readlines()
                print("Найдено: " + str(len(token_read)) + " Токенов(Токена)")
            elif viborcomm == "2":
                token = input("Token который необходимо добавить --> ")
                token_file = open("token.txt","a",encoding="utf-8")
                token_file.write(str(token) + '\n')
                
                print("Вы добавили токен!")
            elif viborcomm == "3":
                owner_id = input("Id Профиля --> ")
                post_id = input("Post Id --> ")
                message = input("Текст коммента --> ")
                zaderjska = input("Задержка --> ")
                token = open("token.txt","r",encoding="utf-8")
                tokens = token.readlines()
                token_r = [i.rstrip() for i in tokens]

                i = 0 
                while True:
                    while i < len(token_r):
                        vk_session = vk_api.VkApi(token=token_r[i])
                        vk = vk_session.get_api()
                        vk.wall.createComment(owner_id=owner_id, post_id=post_id, message=message)
                        print("Накрутка запущена.")
                        time.sleep(int(zaderjska))
                        i += 1
                    i = 0
                    
        elif vibortool == "4":
            check_os()
            print(vktool[0] + comments[0])
            vibored = input("--> ")
            if vibored == "1":
                token = open("token.txt","r",encoding="utf-8")
                token_r = token.readlines()
                print("Найдено: " + str(len(token_r)) + " Токенов(Токена)")
            elif vibored == "2":
                tokens = input("Token -> ")
                token = open("token.txt","a",encoding="utf-8")
                token.write(str(tokens) + '\n')
            elif vibored == "3":      
                owner_id = input("Id Профиля --> ")
                message = input("Текст поста --> ")
                zaderjska = input("Задержка --> ")
                
                token = open("token.txt","r",encoding="utf-8")
                tokens = token.readlines()
                token_r = [i.rstrip() for i in tokens]
                i = 0 
                while True:
                    while i < len(token_r):
                        
                        vk_session = vk_api.VkApi(token=token_r[i])
                        vk = vk_session.get_api()
                        vk.wall.post(owner_id=owner_id,message=message)
                        time.sleep(int(zaderjska))
                        i += 1
                    i = 0
            else:
                print("[!] Неверный параметр!")

                    
        if vibortool == "5":
            check_os()
            print(vktool[0] + damp[0])
            vibored = input("--> ")
            if vibored == "1":
                token = input("Token --> ")
                vk_session = vk_api.VkApi(token=token)
                vk = vk_session.get_api()
             
                a = vk.friends.get(order='name',count=5000,fields='domain, first_name, last_name')
                
                for i in a["items"]:
                    k = i['id']
                    
                    firstName = vk.users.get(user_id=k)[0]["first_name"]
                    lastName = vk.users.get(user_id=k)[0]["last_name"]
                    
                    g = vk.messages.getHistory(count=1, user_id=k)
                    num_m = g['count']#кол-во сообщений
                    
                    if num_m > 0:
                        print(f'Дамп юзера - {firstName} {lastName}')
                        print('Кол-во сообщений:', num_m)
                        f = open(f'Dilog {firstName} {lastName}.txt', 'w', encoding='utf-8')
                        f.write(f'Диалог с {i["first_name"]} {i["last_name"]} \n')
                        q = 0                      
                        try:
                            while num_m > q:
                                var = vk.messages.getHistory(offset=q, count=200, user_id=k, rev=1)
                                for a in var['items']:                                  
                                    firstName = vk.users.get(user_id=a["from_id"])[0]["first_name"]
                                    lastName = vk.users.get(user_id=a["from_id"])[0]["last_name"]
                                    times = datetime.datetime.fromtimestamp(a["date"])
                                    f.write(f'От: {firstName} {lastName}\n')
                                    f.write(f'Дата: {times.strftime("%d/%m/%Y, %H:%M:%S")}\n')
                                    f.write(f'Сообщение: {a["text"]}\n')
                                    f.write('\n')
                                    
                                q +=200
                                time.sleep(0.3)                               
                            f.close()
                        except:
                            pass
                        
            if vibored == "2":
                token = input("Token --> ")
                vk_session = vk_api.VkApi(token=token)
                vk = vk_session.get_api()
                k = input("ID Пользователя --> ")
                
                firstName = vk.users.get(user_id=k)[0]["first_name"]
                lastName = vk.users.get(user_id=k)[0]["first_name"]
                g = vk.messages.getHistory(count=1, user_id=k)
                num_m = g['count']#кол-во сообщений
                
                if num_m > 0:
                    print(f'Дамп юзера - {firstName} {lastName}')
                    print('Кол-во сообщений:', num_m)
                    f = open(f'Dilog {firstName} {lastName}.txt', 'w', encoding='utf-8')
                    #f.write(f'Диалог с {i["first_name"]} {i["last_name"]} {firstName} {lastName} \n')
                    q = 0
                    try:
                        while num_m > q:
                            var = vk.messages.getHistory(offset=q, count=200, user_id=k, rev=1)
                            for a in var['items']:
                                times = datetime.datetime.fromtimestamp(a["date"])  
                                firstName = vk.users.get(user_id=a["from_id"])[0]["first_name"]
                                lastName = vk.users.get(user_id=a["from_id"])[0]["last_name"]
                                times = datetime.datetime.fromtimestamp(a["date"])
                                print("Cкачивание диалога ")
                                f.write(f'От: {firstName} {lastName}\n')
                                f.write(f'Дата: {times.strftime("%d/%m/%Y, %H:%M:%S")}\n')
                                f.write(f'Сообщение: {a["text"]}\n')
                                f.write('\n')
                            q +=200
                            time.sleep(0.3)
                        f.close()
                    except:
                        pass
            else:
                print("[!] Неверный параметр.")
                               
        elif vibortool == "6":
            check_os()
            print(vktool[0] + damp_ph[0])
            vibored = input("--> ")
            if vibored == "1":
                token = input("Token --> ")
                uid = input("ID Пользователя --> ")
                vk_session = vk_api.VkApi(token=token)
                vk = vk_session.get_api() 
                
                newpath = os.path.join(uid)
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                try:
                    responce = vk.photos.get(owner_id=uid,album_id="profile",count=50)
                    for i in range(len(responce["items"])):
                        req = str(responce["items"][i]["sizes"][-1]["url"])
                        urllib.request.urlretrieve(req, newpath + '/' + str(responce["items"][i]['id']) + '.jpg')
                        print("\033[33m Скачивание фотографий с профиля " + uid + " Пошла")
                except vk_api.exceptions.ApiError:
                    pass
                
            if vibored == "2":
                token = input("Token --> ")
                vk_session = vk_api.VkApi(token=token)
                vk = vk_session.get_api()
                file_id = open(os.path.join('users_id.txt'), 'w')
                a = vk.friends.get(order='name',count=5000,fields='domain, first_name, last_name')
                for i in a["items"]:
                    k = i['id']
                    file_id.write(str(k) + '\n')
                
                file_id = open('users_id.txt', 'r')
                data_list = file_id.readlines()
                id_list = []
                for line in data_list:
                    id_list.append(line.strip())
                    
                 
                for id_user in data_list:
                    newpath = os.path.join(id_user)
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                

                try:
                    for ie in id_list:
                        try:
                            responce = vk.photos.get(owner_id=ie,album_id="profile",count=50)
                        except:
                            continue
                        
                        for i in range(len(responce["items"])):
                            req = str(responce["items"][i]["sizes"][-1]["url"])
                            urllib.request.urlretrieve(req, newpath + '/' + str(responce["items"][i]['id']) + '.jpg')
                            print("\033[33m Скачивание фотографий с профиля " + ie + " Пошла")
                except vk_api.exceptions.ApiError:
                    print("Нету фотографии.")
                
        elif vibortool == "7":
            login = input("Login --> ")
            passw = input ("Password --> ")
            uid = input("Ваш ID --> ")
            REQUEST_STATUS_CODE = 200
            vk_session = vk_api.VkApi(login=login, password=passw)
            vk_session.auth()
            vk = vk_session.get_api() 
            
            newpath = os.path.join("Music")
            if not os.path.exists(newpath):
                os.makedirs(newpath)     
                   
            vk_audio = audio.VkAudio(vk_session)
            for i in vk_audio.get(owner_id=uid):
                try:
                    r = requests.get(i["url"])
                    if r.status_code == REQUEST_STATUS_CODE:
                        artist = i['artist']
                        title = i['title']
                        with open(f"Music/{artist}_{title}.mp3", 'wb') as output_file:
                            output_file.write(r.content)
                except OSError:
                    print(i["artist"] + '_' + i["title"])
        elif vibortool == "8":
            token = input("Token -- >")
            vk_session = vk_api.VkApi(token=token)
            vk = vk_session.get_api()
            adds =  vk.friends.get()['items']
            i = 0
            while len(adds) > i: 
                for iw in adds:
                    vk.friends.delete(user_id=iw)
                    print("\033[33m Удален человек:vk.com/id" + str(iw))
                i += 1
        elif vibortool == "9":
            token = input("Token -- >")
            vk_session = vk_api.VkApi(token=token)
            vk = vk_session.get_api()
            parse = [i for i in range(19415)]
            b = 0
            link = 'https://vk.com/sticker/1'
            
            newpath = os.path.join("Stickers")
            if not os.path.exists(newpath):
                os.makedirs(newpath)
                
            for i in parse:
                print(f'{link}-{i}-128')
                p = requests.get(f'{link}-{i}-128')
                out = open(f'Stickers/{b}.png', "wb")
                out.write(p.content)
                out.close()
                b += 1 

    elif vibor == "99":
        os.system("exit")
        print("\033[35m Спасибо за использования скрипта!")
    
    else:
        print("[!] Неверный параметр!")
