import requests

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
        print ("Listedeki tokenlerin işlemi tamamlandı!")
