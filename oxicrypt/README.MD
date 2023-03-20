#OxiCrypt

Este programa fue desarrollado como un ejercicio dentro de un curso de criptografía y blockchain.

_El desafío era crear un algoritmo de encriptación simétrica._

Mi solución fue tomar la clave de encriptación y sumar el valor u8 de cada uno de sus carácteres para luego sumarlos a cada uno de los carácteres del mensaje a encriptar. Al poder utilizar valores UTF8, quise que los carácteres se traduzcan por los símbolos más raros posibles.

*SPOILER ALERT: Funciona a medias, funciona bien si la clave que se le pasa es numérica y con valores bajos. Pero se rompe al utilizar claves alfanuméricas.
