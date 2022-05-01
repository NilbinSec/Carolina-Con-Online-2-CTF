# Brew Overview
OSINT is probably one of the strongest areas for NilbinSec based on our background in ARGs. These were great questions and we would love to see more and more difficult ones as well to help us shine.

# Lovely
**Point Value:** 30

**Prompt**
_(The flag for this challenge is NOT in the 'flag{XXXXXXXXXXXXXXXX}' format)_

_In what city was this picture taken?_

![osint1](https://user-images.githubusercontent.com/85370905/166160229-69c37ffb-7806-4a2b-a294-ef948240f2ed.jpg)


Flag: **Locarno**

**Methodology**
Google Reverse Image search was enough and yandex was not required. After looking through the results, the flag was quickly found.
# lcamera
**Point Value:** 40

**Prompt**
_(The flag for this challenge is NOT in the 'flag{XXXXXXXXXXXXXXXX}' format)_

_What Year and Month (in MM/YYYY format) did the taker of this photo announce they were leaving Google_

![osint2](https://user-images.githubusercontent.com/85370905/166160237-36daf118-af1f-4a80-ab73-39f502d119fd.png)

Flag: **03/2018**

**Methodology**
Another google image search allowed the photo taker's twitter to be found. Searching their twitter for "Google" found the correct date for the flag.

# killerwatt
**Point Value:** 50

**Prompt**
_(The flag for this challenge is NOT in the 'flag{XXXXXXXXXXXXXXXX}' format)_

_According to the Federal Energy Regulation Commission, What is the Authorized Capacity (in kWs) of Project Number P-2216_

Flag: **2755500**

**Methodology**
After figuring out what the Federal Energy Regulation Commission's website was google dorking provided the solution because P-2216 by itself does not provide good search results.

Google Dork: _site:ferc.gov "P-2216"_. 3rd Result is an excel of active powerplant licenses with authorized capacity, filter to P-2216.

# lost and found
**Point Value:** 50

**Prompt**
_(The flag for this challenge is NOT in the 'flag{XXXXXXXXXXXXXXXX}' format)_

_Who planted this:_

_-33.867886, -63.987_

Flag: **Pedro Ureta**

**Methodology**
Searching the geocoordinates on google maps revealed a park/monument in Argentina that was in the shape of a guitar. Searching google about the location quickly found the creator of the park.
