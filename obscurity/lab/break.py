
import string

def encrypt(text, key):
    keylen = len(key)
    keyPos = 0
    encrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr + ord(keyChr)) % 255)
        encrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen
    return encrypted


base = "Encrypting this file with your key should result in out.txt, make sure your key is correct!"
solution= "¦ÚÈêÚÞØÛÝÝ×ÐÊßÞÊÚÉæßÝËÚÛÚêÙÉëéÑÒÝÍÐêÆáÙÞãÒÑÐáÙ¦ÕæØãÊÎÍßÚêÆÝáäèÎÍÚÎëÑÓäáÛÌ×v"

index = 0
key = ""
while index < len(base):
    current = base[index]
    good = solution[index]
    letters = list(string.ascii_lowercase)+list(map(str,range(0,10)))
    key+= '.'.join([letter for letter in letters if encrypt(current,letter)==good])
    index+=1
print(key)

