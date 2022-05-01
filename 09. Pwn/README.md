# Pwn Overview
Lots of different challenges, we could only solve the ELFs.

# bin_mechanic1: formattable
**Point Value:** 50

**Prompt**
_(bin mechanic challenges involve manually editing binaries to get them to run and print out the flag. They can be reversed, but that has been made deliberately more difficult than it is worth.)_

_Someone has tampered with this ELF file so it can no longer run._

_This is supposed to be an executable x86_64 ELF. It needs some fixing before it will print out the flag._

Flag: **flag{UutoI7AS9k9n0hKo7kpTNAnXtf6LxUXX}**

**Methodology**
Being given some helpful info in the prompt. A look at wikipedia's page on ELF and their formats provided enough information to slowly edit the ELF until it executed. Just had to see which were not correct bytes for an x86_64 ELF, update, and run.

![image](https://user-images.githubusercontent.com/85370905/166157859-f26fb996-9b0b-4750-bf7a-5d0f266f0551.png)


# bin_mechanic2: magic
**Point Value:** 60

**Prompt**
_(bin mechanic challenges involve manually editing binaries to get them to run and print out the flag. They can be reversed, but that has been made deliberately more difficult than it is worth.)_

_Whoops... Someone broke the header..._

_NOTE: Careful running this binary... It will actually execute something_


Flag: **flag{chwhL<DYAk^n0hKo7kpTNAnXtf6LxUXX}**

**Methodology**
Quite a bit of time was wasted trying to figure out what the proper file type should be because it had a PNG header. Eventually we went with hoping it was another ELF (it was). Using the first bin_mechanic as a crib sheet for what the bytes should be, it ran successfully using -c to recieve the correct flag.

![image](https://user-images.githubusercontent.com/85370905/166158041-fd346cf9-f276-440d-ad13-c7f1c7c9368a.png)


# bin_mechanic2: headers
**Point Value:** 70

**Prompt**
_Someone broke this binary too!_

_Looks like this time they tampered with the a different kind of header..._


Flag: **flag{eutoi7AS9k9n0hKO7kpTNAnXtf6LxUXX}**

**Methodology**
Building off an assumption this would be an ELF as well: First, fixed the load segment of PHDR segment using hex editor. Then, replaced the segment with correct segment from a different ELF file. Doing this allowed the program to run.
