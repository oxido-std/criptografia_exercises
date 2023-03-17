# abcdary=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
abcdary=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

# ROT es un sistema de cifrado posicional. Desde la posición de la letra se suma un número y el resultante de ese número será la letra que la sustituya

# ende (encrypt) / (decrypt)
def ende_crypt_rot(rot,message,ende):
    message_ende=""
    message_aux=message.lower()

    for char in message_aux:
        if char in abcdary:
            # encrypt
            if(ende==True):
                new_char=(abcdary.index(char)+rot)%len(abcdary)
                message_ende+=abcdary[int(new_char)]
            # decrypt
            else:
                new_char=(abcdary.index(char)-rot)%len(abcdary)
                message_ende+=abcdary[int(new_char)]
        else:
            message_ende+=char
    
    return message_ende

rot=1
# EJEMPLO
# message_send="Tomate un té con flatte y 915 invitados en la casa de flora."
message_enc="DHLZWKESFHLLWSFNFAVHLIHKJNWWLSWLDSDWQIKAEWKSMWFYSFNFAHFÑWKVSVWKSWFUNSDJNAWKMAWEIHJNWLWSIHKJNWLAWFMKWWDDHLIWDWSFDHLVWÑHKSFDHLVWSXNWK"

# message_encripted=ende_crypt_rot(rot,message_send,True)
# message_decripted=ende_crypt_rot(rot,message_encripted,False)
message_decripted=""

for i in range(1,203):
    message_decripted=ende_crypt_rot(i,message_enc,False)
    print(f"{i} - {message_decripted}")

print(message_enc)
# print(message_encripted)
print(message_decripted)