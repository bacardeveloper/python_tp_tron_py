from tronpy import Tron
import random
import string

# config
client_tron = Tron()


def genere_string(length = 7):
    letters = string.ascii_lowercase
    resultat_string = ''.join(random.choice(letters) for i in range(length))
    return resultat_string

def address_validity(adresse):
    is_address = client_tron.is_address(adresse)
    return is_address

class TronBlock:

    def __init__(self) -> None:
        pass

    def create_wallet_and_save_in_file(self):
        portefeuille = client_tron.generate_address()
        name_file = genere_string()
        fichier = open(name_file+'.txt', 'w')
        fichier.write('adresse : '+portefeuille['base58check_address'] +
                      '\n'+'private key : '+portefeuille['private_key'])
        fichier.close()
