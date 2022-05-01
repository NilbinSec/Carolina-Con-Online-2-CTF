# Crypto Overview
Cryptography is one of NilbinSec's strong points. These challenges were very enjoyable and created challenges we previously had not encountered.

# RSA
**Point Value:** 30

**Prompt**
_Decypher the weak RSA cipher_

_e: 13 c: 122080087404771029659632929399991170201651863861173941090008186 n: 730227127272331613301012744533184236831358631713393776098161527_

Flag: **flag{math_is_fun!}**

**Methodology**
Given the small e value this should be fast. Dcode.fr is our go to tool site for simple stuff.

![image](https://user-images.githubusercontent.com/85370905/166155843-d0a15b28-d997-48d5-ac74-2a881f66a2ee.png)


# Triple Stream Cipher
**Point Value:** 30

**Prompt**
_By the pricking of my thumbs, Something wicked this way comes._

_Keys in order used to encrypt message:_

_Key 1 hint: Name of the play the phrase is from. Key 2 hint: Name of the author of the play. Key 3 hint: Son of the author of the play. Flag: flag{<first lastname of message's speaker>}_

_Do NOT include spaces in keys and flag!_

_Python and txt file included above_

Flag: **flag{MarcAntony}**

**Methodology**
This was not much of an actual crypto problem. Due to misconfiguration of the python script, the plaintext of the Friends Romans Countrymen... speech was visible. A few issues were faced in getting the correct flag based on spelling Mark/Marc or Marcus Antonius.

# xor4more
**Point Value:** 32

**Prompt**
_A hacker has breached our system and left this file. See if you can decrypt it and find any leads._

_Included the .xor file_

Flag: **flag{K9QLxjLYJCmyIIIfpOvdGgpuy7thWm56}**

**Methodology**
This was the most difficult/challenging flag in the section. Because the file included .png as well as .xor an initial assumption was that it was a XOR'd image. All PNGs begin with the HEX 89 50 4E 47 0D 0A 1A 0A for the first 8 bytes. Because our file began with 7E 47 22 48 F3 EF 4F AE, we could rely on the normal PNG header as a crib to brute force at least the start of the key. Using Dcode's XOR cipher tool, the starting key in HEX was F7 17 6C 0F FE E5 55 A4; this required going byte by byte in Dcode and searching for the proper key. Figuring out what to do with this took a little while. Ultimately, importing the file into CyberChef and using just the XOR recipe was enough to identify a proper PNG based on header and footer. Saving as a PNG revealed:

![image](https://user-images.githubusercontent.com/85370905/166156271-80ae5868-167f-4348-858f-08026187792d.png)


