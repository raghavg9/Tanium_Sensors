#Linux and Mac
import os
import sys

os.system("lspci>>output.text")
file1=open('output.txt','r')
lines=file1.readlines()
for line in lines:
  if "VGA" in line:
    vga_controller_val=line.split(':')[2]
print(vga_controller_val)
os.system("rm output.txt")


#Windows
#Get-Wmi win32_VideoController | Format-List Name


#Returns graphics card/vga adapter, which is found in the result of the lspci command. Parsing this for VGA will #give the desired card value.


#After writing this, I saw that there was a similar implementation of this in the existing Tanium sensors.

