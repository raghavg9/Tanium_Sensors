import os
import sys

filepath="/etc/mdadm.conf"


if not os.path.exists(filepath):
    print("raid does not exist")
    exit(0)
raidfile=open(filepath)
lines=raidfile.readlines() 
for line in lines:
    if "level=" in line:
        linecomps=line.split(" ")
raidval=linecomps[2].split('=')
print(raidval[1])


#This program aims to provide a raid level for all devices which curently have a software raid on their linux and #mac systems. This python code parses the raid number and outputs it. The raid system is useful as it provides #fault tolerance and data redundancy to reduce data loss and improve performance.The raidhas many levels, the #popular ones being 0, 1,5, and 10. 

#However, raid is more beneficial when implemented as a hardware raid. Software raid is good when you want to #implement raid fucntionality without special herwarew whic can be expensive. This sensor aims to see software #raid being implemented in the system. In the user path /etc/mdadm.conf, we observe that the raid details are #specified. 
#mdadm manages and monitors RAID devices using the md driver in Linux. In this config file level= will specify the #raid level. This sensor parses the script and searches for level=. It then stores the raid value in the variable #raidval and prints it.

#Raid is not always useful, especially in software raid coupled with hardware raid, as it creates unnecessry #overhead and only has specific edge cases where there is a need for such a implementation. Detecting a software #raid and its values cann help to monitor reduced throughput, increased latency,reduced efficency, or lack of #storage.
