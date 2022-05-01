# Network Theory Overview
By far the most challenging flags in the CTF. Essentially none of the participants really went after them. It felt a bit out of scope of the CTF compared to the rest of the flags.

# one.pcap
**Point Value:** 40

**Prompt**
_Submit challenges to @stryngs_

_Modify one.pcap and then create solution-one.pcap_

_Change the IP and MAC of the device sending a ping (ICMP Request) to_

_192.168.100.137
4e:40:cd:16:5a:1e
Code is required to meet the requirements of this challenge and the human participant is not allowed to submit a solution that requires interactive usage beyond the normal entry of user input for starting a program such as ./foo.bar. The code is meant to be ran as mostly stand alone and not have a human looking at something such as Wireshark while figuring out what to do next. The less human interaction past inception, the better. Solutions of more than one piece of code are acceptable. If it requires Bash and then Python, so be it. Pipes are preferred if chaining is needed, but what matters in the end is the code._

_Submit challenges to @stryngs Use #stryngs-pcap-zone for help_

_House rules 42_

_All checksums must match
Ask if you are unsure
Challenges 4-7 require a detailed description of the encryption type used
Challenges 8-11 require the submission encryption to work with the original encryption session
Do not be shy, ask questions
Ensure timestamps match the original
Only include the decrypted packet within solution-four.pcap, solution-five.pcap, solution-six.pcap, solution-seven.pcap
Radiotap headers ought match
Speed matters if that is a question
Wireshark with all checks turned on will most likely settle any disagreements
log Challenge_

_Has been known to supercede the house in terms of rule
Checksums
The calculated hash of something based upon other things which yields math and a signature.
Decrypted content
The act of taking something such as a Alice, converting it to Bob and then creating an object or pcap which can be opened in something such as Wireshark, where the content is presented without the need for any Wireshark decrypting; made to order and ready to consume.
Horses
299792458; anything else and this measures the tie.
Radiotap headers
Defined as per IEEE and whatever other source you find. Inspect what you expect and compare across whatever programs you can find. Some say tomato while others hear tomato; the splats are what matter, we will splat.
Time
Use it all to your advantage and don't be shy; go out and learn something!_

Flag: **flag{UERcIQ-zn_xopJ4pjm77lSPEjbYguauE}**

**Methodology**
We really had no interest in doing these challenges, but the creator of the network theory flags threw out a freebie script after some strife so we of course made sure to go and get the points. Look on the Carolina Con discord for their script if you want it.
