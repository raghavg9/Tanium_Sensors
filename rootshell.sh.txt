#linux and mac

#!/bin/bash
getent|grep ^$USER|cut -f: -f7

#This sensor script helps to find the default shell of a user. The echo $SHELL is not accurate as it returns the #current running shell. If the need to find the base shell exists, this is found in the /etc/passwd user #directory. By using getent, we can parse the file to the last line of the user, as the last line will always be #the root shell. The delimiters of this is the colon(:).


