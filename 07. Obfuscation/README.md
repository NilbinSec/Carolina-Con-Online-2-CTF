# Obfuscation
This was File Fun with a few extra steps.

# Bit Wave
**Point Value:** 50

**Prompt**
_Riddle me this: How many bits are in a WAV?_

Flag: **flag{qriouser_AND_Qr10us3r}**

**Methodology**
Lots of initial time was wasted based on the prompt. We looked at sampling rates and the possibility of something hidden in spectrograph or steganography. Ultimately, unzip output.wav revealed the file real.question which was a binary. Because the first bit was a 1, it was apparent it wasn't going to be BIN2ASCII. Dropping the binary into CyberChef and running the magic recipe revealed a QR code of the flag. CyberChef can automatically parse QR codes so that was good enough to move on.


![image](https://user-images.githubusercontent.com/85370905/166157124-c556ac06-bb03-4777-a2d9-ed3ce1611a27.png)
