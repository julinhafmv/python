import forcaGame
import adivinhacaoGame

def escolha_game():
    print("*******************************")
    print ("*ǫᴜᴀʟ ᴊᴏɢᴏ ᴠᴏᴄᴇ ᴅᴇsᴇᴊᴀ ᴊᴏɢᴀʀ?*")
    print ("*****************************")
    print ("(1)ғᴏʀᴄᴀ ɢᴀᴍᴇ, (2)ᴀᴅɪᴠɪɴʜᴀᴄᴀᴏ ɢᴀᴍᴇ")
    
    jogo = int(input("ᴇsᴄᴏʟʜᴀ ᴜᴍ ᴅᴏs ᴊᴏɢᴏs."))

    if (jogo == 1):
        print ("ᴠᴏᴄᴇ ᴇsᴄᴏʟʜᴇᴜ ғᴏʀᴄᴀ ɢᴀᴍᴇ")
        forcaGame.jogar()

    elif (jogo == 2):
        print ("ᴠᴏᴄᴇ ᴇsᴄᴏʟʜᴇᴜ ᴏ ᴊᴏɢᴏ ᴅᴇ ᴀᴅɪᴠɪɴʜᴀᴄᴀᴏ")
        adivinhacaoGame.jogar()
        
if(__name__ == "__main__"):
    escolha_game()