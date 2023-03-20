use std::{vec, io};

pub struct OxiCrpyt{
    key:u16,
}

impl OxiCrpyt{
    
    pub fn new(key:&String) -> OxiCrpyt{
        let inner_key=key.clone();
        let key_encripted=OxiCrpyt::convert_key(inner_key);
        return OxiCrpyt {
            key:key_encripted,
        }
    }
    /// Función para encriptar el texto
    pub fn encrypt(&self, text:&String) -> String{
        let inner_text=text.clone();
        return self.parse_text(&inner_text,true);
    }
    
    /// Desencriptar los datos
    pub fn decrypt(&self, text:String) -> String{
        let inner_text=text.clone();
        return self.parse_text(&inner_text,false);
    }

    fn convert_key(text:String) -> u16{
        let key_utf8=text.into_bytes();
        let mut key_add:u16=0;
        
        // suma cada valor u16 de cada carácter que pone password.
        // let key_len=key_utf8.len() as u16;
        for i in key_utf8{
            key_add+=i as u16;
        }
        key_add=key_add%255;
        key_add
    }

    fn char_encrypt_from_key(&self,char_to_enc:u8) -> String{
        // suma el varlo de cada letra a encriptar al valor de la clave.
        let char_encripted=(char_to_enc.wrapping_add(self.key as u8))%127;
        let s=String::from_utf8(vec![char_encripted]).expect("Error durante la encriptación");
        s
    }

    fn char_decrypt_from_key(&self,char_to_dec:u8) -> String{
        // suma el varlo de cada letra a encriptar al valor de la clave.
        let char_decrypted=char_to_dec.wrapping_sub(self.key as u8)%127;
        let s=String::from_utf8(vec![char_decrypted]).expect("Se esperaba un string y obtengo un error DEC");

        s
    }

    /// La función encripta o desencripta. si to_encrypt es false encripta, sino desencripta
    fn parse_text(&self,text:&String,to_encrypt:bool) -> String{
       let text_aux=text.to_owned();
       let mut new_text=String::from("");
        if to_encrypt==true{
            println!("==============ENC==============");
            for ch in text_aux.into_bytes(){
                new_text.insert_str(new_text.len(),&self.char_encrypt_from_key(ch));
            }
        }else{
            println!("==============DEC==============");
            for ch in text_aux.into_bytes(){
                new_text.insert_str(new_text.len(),&self.char_decrypt_from_key(ch));
            }
        }
        return new_text;
    }
}

fn main() {
    println!("Bienvend@ a tu encriptador favorito 😊🦀");
    loop{
        println!("Escribe un texto a encriptar, por favor: ");
        let mut input_text = String::new();
        io::stdin()
        .read_line(&mut input_text)
        .expect("Error al leer el texto");

        println!("Escribe una clave para encriptar por favor: ");
        let mut input_key = String::new();
        io::stdin()
            .read_line(&mut input_key)
            .expect("failed to read from stdin");

        let input_text = input_text.trim();
        let input_key = input_key.trim();
        
        // dbg!(input_text);
        // dbg!(input_key);
        let encripter=OxiCrpyt::new(&input_key.to_string());
        let text_encripted=encripter.encrypt(&input_text.to_string());
        println!("TEXTO ENC => {}",text_encripted);
        let text_decripted=encripter.decrypt(text_encripted.to_string());
        println!("TEXTO DEC => {}",text_decripted);
    }



}

// fn prueba_manual(){
    
//     let text=String::from("199 Mi texto es super piola");
//     // let my_key=String::from("mi password secreto");
//     let my_key=String::from("mi password secreto es demasiado largo para este planeta hermoso, a vos te parece juancito?@|_  a");
//     // let my_key=String::from("mi::passwor");
//     dbg!(my_key.len());
//     // let my_key=String::from("pepe");
    
//     dbg!(&my_key);
//     dbg!(&text);
    
//     let encripter=OxiCrpyt::new(&my_key);
//     let text_encripted=encripter.encrypt(&text);
//     println!("TEXTO ENC => {}",text_encripted);
//     let text_decripted=encripter.decrypt(text_encripted.to_string());
//     println!("TEXTO DEC => {}",text_decripted);
// }
