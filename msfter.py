import os
import sys
import random
from time import sleep as sl

if sys.platform == "linux" or sys.platform == "linux2":
	B = "\033[34;1m"
	Y = "\033[33;1m"
	G = "\033[32;1m"
	W = "\033[0;1m"
	R = "\033[31;1m"
	C = "\033[36;1m"
	
	rand = (B,Y,G,W,R,C)
	P = random.choice(rand)

def logo():
	print " "
	print(P+'    dMMMMMMMMb .dMMMb  dMMMMMP dMMMMMMP dMMMMMP dMMMMb')
	print(P+'   dMP"dMP"dMPdMP" VP dMP        dMP   dMP     dMP.dMP') 
	print(P+'  dMP dMP dMP VMMMb  dMMMP      dMP   dMMMP   dMMMMK"')  
	print(P+' dMP dMP dMPdP .dMP dMP        dMP   dMP     dMP"AMF')   
	print(P+'dMP dMP dMP VMMMP" dMP        dMP   dMMMMMP dMP dMP'+W)    
	print " "
 	print "         -=[01] Install Metasploit"
 	print "   + -- --=[02] Info"
 	print "   + -- --=[03] Exit"
	print " "
	
def install():
	os.system("pkg update -y")
	os.system("cd $HOME && git clone https://github.com/Hax4us/Metasploit_termux")
	os.system("cd $HOME/Metasploit_termux && cp * $HOME")
	os.system("cd $HOME && chmod +x metasploit.sh")
	os.system("cd $HOME && bash metasploit.sh")
	os.system("cd $HOME && bundle init > hdh.txt && rm -rf hdh.txt")
	os.system("cd $HOME && gem install bundler -v 1.16.1")
	os.system("cd $HOME && bundle install -j5")
	os.system("cd $HOME && bash metasploit.sh ")
	os.system("cd $HOME && rm -rf README.md apk.rb database.yml metasploit.sh Metasploit_termux")
	

def main():
	os.system("clear")
	logo()
	fff = raw_input("msfter > ")
	if fff == "1" or fff == "01":
		print "\n======================================"
		print "[+] Jesus, it will take a lot of time!"
		print "======================================"
		install()
		print "====================================="
		print "[+] Metasploit installed"
		print "[+] Type 'msfconsole' to start."
		print "====================================="

	elif fff == "2" or fff == "02":
		print (R+'____________________________')
		print (R+'||========================||')
		print (R+'||    Created By'+G+'otx2s'+R+'||')
		print (R+'||    ----------------    ||')
		print (R+'||From podval with love :3||')
		print (R+'||========================||')
		print (R+'||                        ||')
		print (R+'~~                        ~~'+W)
		raw_input("(Press ENTER) ")
		os.system("clear")
		main()

	elif fff == "3" or fff == "03":
		print "\nGoodbye..."
		sl(1)
		
	else:
		print "\nERROR: Check your command!"
		sl(1)
		os.system("clear")
		main()

if __name__ == '__main__':
	main()

#####################
# PRIVET FROM OTX2S #
#####################
