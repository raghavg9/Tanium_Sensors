# Tanium Sensors
Building custom sensors to work on Tanium systems for endpoint management

## Raid.py
This program aims to provide a raid level for all devices which curently have a software raid on their linux and #mac systems. This python code parses the raid number and outputs it. The raid system is useful as it provides #fault tolerance and data redundancy to reduce data loss and improve performance.The raidhas many levels, the #popular ones being 0, 1,5, and 10. 

However, raid is more beneficial when implemented as a hardware raid. Software raid is good when you want to #implement raid fucntionality without special herwarew whic can be expensive. This sensor aims to see software #raid being implemented in the system. In the user path /etc/mdadm.conf, we observe that the raid details are #specified. 
#mdadm manages and monitors RAID devices using the md driver in Linux. In this config file level= will specify the #raid level. This sensor parses the script and searches for level=. It then stores the raid value in the variable #raidval and prints it.

Raid is not always useful, especially in software raid coupled with hardware raid, as it creates unnecessry #overhead and only has specific edge cases where there is a need for such a implementation. Detecting a software #raid and its values cann help to monitor reduced throughput, increased latency,reduced efficency, or lack of #storage.

## Rootshell.sh
This sensor script helps to find the default shell of a user. The echo $SHELL is not accurate as it returns the #current running shell. If the need to find the base shell exists, this is found in the /etc/passwd user #directory.

By using getent, we can parse the file to the last line of the user, as the last line will always be #the root shell. The delimiters of this is the colon(:).

## VGA.py
Returns graphics card/vga adapter, which is found in the result of the lspci command. 
Parsing this for VGA will give the desired card value. 
this result is also represented with a sepperate statement for Windows systems.


