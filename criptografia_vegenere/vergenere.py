# alphabet so far
class Vegenere:
    
    abcdary_en=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    abcdary_es=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    selected_alphabet=""
    
    mod_x=0
    key_gen=""
    
    message=""
    message_enc=""
    
    def __init__(self,message,key,isEspanish) -> None:
        self.message=message
        # obtiene la cantidad le carácteres del mensaje (sólo letras en este caso)
        self.get_mod_x(message)
        # la clave para encriptar y desencriptar
        self.get_key_gen(key)
        # El mensaje puede estar en castellano o inglés
        if(isEspanish==True):
            self.selected_alphabet=self.abcdary_es
        else:
            self.selected_alphabet=self.abcdary_en            
        
    def get_mod_x(self,message):
        message=message.replace(" ","")
        self.mod_x=len(message)
    
    def get_key_gen(self,key):
        key_aux=""
        # agrega cada una de las letras de la clave hasta completar el total largo total del mensaje.
        for i in range(0,self.mod_x):
            key_aux+=key[i%len(key)]
        self.key_gen=key_aux
    
    def encrypt(self):
        message=self.message.replace(" ","").lower()
        message_encrypted=""
        for i in range(0,len(message)):
            # selecciono el INDICE de la letra del mensaje
            index_message=self.selected_alphabet.index(message[i])
            # selecciono el INDICE de la letra de la clave
            index_key=self.selected_alphabet.index(self.key_gen[i])
            
            # Sumo los índice para obtener la letra de reemplazo.
            index=(index_message+index_key)%len(self.selected_alphabet)
            # Agrego la letra al string
            message_encrypted+=self.selected_alphabet[index]
        print(f"message [ E ] {message} => {message_encrypted}")
        self.message_enc=message_encrypted
    
    def decrypt(self):
        # si el mensaje no fue encriptado previamente entonces debe ser el string que recibe en el constructor
        if self.message_enc != "":
            message=self.message_enc
        else:
            message=self.message
            
        message=message.replace(" ","").lower()
        message_decrypted=""
        for i in range(0,self.mod_x):
            # selecciono el INDICE de la letra del mensaje
            index_message=self.selected_alphabet.index(message[i])
            # selecciono el INDICE de la letra de la clave
            index_key=self.selected_alphabet.index(self.key_gen[i])
            
            # Resto los índice para obtener la letra original.
            index=(index_message-index_key)%len(self.selected_alphabet)
            # Agrego la letra al string
            message_decrypted+=self.selected_alphabet[index]
        print(f"message [ D ] {message} => {message_decrypted}")
            
            

v=Vegenere("Hola pepe","clave",True)
v.encrypt()
v.decrypt()

v2=Vegenere("EXRWHSLQRTSQEPDSDOGSLBDFUEVOGLONDEPGXIJRE","enredadera",True)
v2.decrypt()