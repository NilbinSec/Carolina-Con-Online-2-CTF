# Space Weather Overview
With a few HAM licenses in NilbinSec, we also love radio challenges, these were good, but we had computer issues due to our VMs.

# fldigi
**Point Value:** 20

**Prompt**
_System Test_

Flag: **flag{an2p1YKqIsiu85TJkoc4M7wQFVCB0rm6}**

**Methodology**
The name, fldigi is an obvious hint you should use the radio program fldigi to decode these. Unfortunately early in the CTF fldigi was giving us issues but luckily the signal was good enough that the phone app PSK31 Pad worked just fine listening on the computer speakers to identify and demodulate the signal.

![image](https://user-images.githubusercontent.com/85370905/166158996-3d0dbbaf-ec8c-45ea-bfac-c9336dcb6c97.png)


# Lunar Weather Report
**Point Value:** 30

**Prompt**
_In this modern world of space tourism, a fledgling startup with only a modest VC backing, has started a guerilla marketing campaign to lure high-income tourists to an "out of this world" destination with their lunar based radio station._

_Advertised ROI of the campaign is 400%_

Flag: **flag{HTeUgoREi7SZu8pMbf6NacyYQVFLn3lr}**

**Methodology**
When it was clear more signals were going to be released, including ones like Melissa which allow for low signal-noise-ratio we set up fldigi on Windows instead which worked. 

![image](https://user-images.githubusercontent.com/85370905/166159088-79727819-ac3b-4d3c-861c-b048b4a9fbae.png)

Messing with the noise filter eventually decoded a link to a survey with multiple flags. There may have been a smart way to identify the correct flag but we just tried them all until we found the correct one.


# Baton Pass
**Point Value:** 30

**Prompt**
_QR codes are the apex predator of the marketing world_

_Hint: You don't need to go deep into changing settings from the default. Just enable a basic setting_

Flag: **flag{8ETvSGkhOafA2V7NM1FB9wK0qiJRmDcl}**

**Methodology**
Using the QR code hint, began looking at different modulations that would provide an image. Eventually MFSK64 proved correct and provided this:

![image](https://user-images.githubusercontent.com/85370905/166160131-7d941cef-f1b5-4c95-b3c2-53ac86ca399f.png)

