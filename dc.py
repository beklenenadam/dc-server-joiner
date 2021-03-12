import requests

yazi = """       _ _  __            _                                
  __ _| (_)/ _|_   _ _ __| | ____ _ _ __    ___  _ __ __ _ 
 / _` | | | |_| | | | '__| |/ / _` | '_ \  / _ \| '__/ _` |
| (_| | | |  _| |_| | |  |   < (_| | | | || (_) | | | (_| |
 \__,_|_|_|_|  \__,_|_|  |_|\_\__,_|_| |_(_)___/|_|  \__, |
                                                     |___/ """
print (yazi)

davet = input('Discord Davet daveti: ')
if len(davet) > 6:
    davet = davet[19:]
apidavet = "https://discordapp.com/api/v6/invite/" + str(davet)


print (davet)


with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'İşlem': token
                }
            requests.post(apidavet, headers=headers)
        print ("Tamamlandı!")
