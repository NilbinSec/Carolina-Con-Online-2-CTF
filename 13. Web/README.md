# Web Overview
These challenges were a weird smorgasboard of webpage hacking. Most appear to have terminated in gaining actual access to the webserver, but we instead focused our efforts elsewhere after getting low hanging fruit.

# Linux Web Server: Confidential
**Point Value:** 20

**Prompt**
_Remember, search for text in the format of flag{SOMETHING}, and submit it for points._

Flag: **flag{gRLKx6mwndQBqGz9MQqQ}**

**Methodology**
This was the only one we got from this box and it was essentially a freebie. We couldn't find any ExploitDB options that might gain us additional access.

# wikipwn: beautiful webapp pt 2
**Point Value:** 35

**Prompt**
_Remember, search for text in the format of flag{SOMETHING}, and submit it for points._

Flag: **flag{jellybean azione}**

**Methodology**
This was a freebie, it was just sitting on the main page; just had to identify which question it was associated with.

[Wikipwn Main Page](https://user-images.githubusercontent.com/85370905/166159451-dbac33a7-eb7e-4eb0-b02d-2ae083f58c04.png)

# wikipwn: beautiful webapp pt 3
**Point Value:** 35

**Prompt**
_Remember, search for text in the format of flag{SOMETHING}, and submit it for points._

Flag: **flag{patchilynondepressedresubmergesliturgiologiesnoneconomists}**

**Methodology**
Another pseudo-freebie; scanning the QR code on the main page revealed the flag.

![image](https://user-images.githubusercontent.com/85370905/166159506-98ac0bf5-acd2-48d2-ad2f-51a0efcdb32d.png)

# wikipwn: beautiful webapp exif
**Point Value:** 40

**Prompt**
_Remember, search for text in the format of flag{SOMETHING}, and submit it for points._

Flag: **flag{rNnYnKztqZU97eMVqedMzQ}**

**Methodology**
More easy stuff; after downloading both images attached to the page and running exiftool on them, the flag was revealed in the metadata of the second image.

# wikipwn: webapp pt 3
**Point Value:** 40

**Prompt**
_Remember, search for text in the format of flag{SOMETHING}, and submit it for points._

Flag: **flag{5dc7720d9595eea9a626ffb550508afc}**

**Methodology**
The page itself didn't have anything of interest. Running dirb on the website however revealed several different pages that were not linked to the main page. Of note, _XXX.XXX.XXX.XXXX/TODO_ had this flag.

![Melancholy TODO](https://user-images.githubusercontent.com/85370905/166159698-c7b86f5b-7859-4fd2-bfed-2f6f3d352566.png)

Using some of the hints we did manage to gain access to the admin page for the box but did not go any further do to an inability to find a good, working Moinmoin exploit for the deployed version as well as a frustrating time trying to bruteforce into SSH.
