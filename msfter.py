import os
import sys
import time

sl = time.sleep

if sys.platform == "linux" or sys.platform == "linux2":
	B = "\033[34m"
	W = "\033[0m"

def logo():
	print " "
	print(B+'    dMMMMMMMMb .dMMMb  dMMMMMP dMMMMMMP dMMMMMP dMMMMb')
	print(B+'   dMP"dMP"dMPdMP" VP dMP        dMP   dMP     dMP.dMP') 
	print(B+'  dMP dMP dMP VMMMb  dMMMP      dMP   dMMMP   dMMMMK"')  
	print(B+' dMP dMP dMPdP .dMP dMP        dMP   dMP     dMP"AMF')   
	print(B+'dMP dMP dMP VMMMP" dMP        dMP   dMMMMMP dMP dMP'+W)    
	print " "
 	print " [01] Install Metasploit"
 	print " [02] Info"
 	print " [03] Exit"
	print " "
	
def install():
	os.system("pkg update -y")
	os.system("cd $HOME && git clone https://github.com/Hax4us/Metasploit_termux")
	os.system("cd $HOME/Metasploit_termux && chmod +x metasploit.sh")
	os.system("cd $HOME/Metasploit_termux && bash metasploit.sh")
	os.system("cd $HOME && bundle init > hdh.txt && rm -rf hdh.txt")
	os.system("cd $HOME && gem install bundler -v 1.16.1")
	os.system("cd $HOME && bundle install -j5")
	os.system("cd $HOME/Metasploit_termux && bash metasploit.sh ")

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
		os.system("clear")

	elif fff == "2" or fff == "02":
		print """
		____________________________
		||========================||
		||    Created By otx2s    ||
		||    ----------------    ||
		||From podval with love :3||
		||========================||
		||                        ||
		~~                        ~~ 
		"""
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

####################
# Privet, kak dela?#
####################
