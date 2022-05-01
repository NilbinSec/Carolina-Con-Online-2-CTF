# File Fun
One interesting video of a bird, what could we find?

# Examine
**Point Value:** 20

**Prompt**
_please examine this file_

Flag: **flag{vPl9NFMkXjFFQN6Yzfik}**

**Methodology**
After some false starts due to an assumption of stegonagraphy, unzip command ended up being the answer.

After opening the JAR file, it was clear ingress.class was a png file. After updating the file type the flag was found in the png. Running unzip on the video revealed a hidden file named dat. dat was filled with hundreds of lines just spelling bird differently with the exception of one line which had the flag.

![image](https://user-images.githubusercontent.com/85370905/166156458-c16ab98d-605a-431f-8e33-56de20157205.png)
