import os
import time

sl = time.sleep

msfter_logo = """
    dMMMMMMMMb .dMMMb  dMMMMMP dMMMMMMP dMMMMMP dMMMMb 
   dMP"dMP"dMPdMP" VP dMP        dMP   dMP     dMP.dMP 
  dMP dMP dMP VMMMb  dMMMP      dMP   dMMMP   dMMMMK"  
 dMP dMP dMPdP .dMP dMP        dMP   dMP     dMP"AMF   
dMP dMP dMP VMMMP" dMP        dMP   dMMMMMP dMP dMP    

 [01] Install Metasploit
 [02] Info
 [03] Exit

"""

def logo():
	print msfter_logo

def main():
	logo()
	fff = raw_input("msfter > ")
	if fff == "1" or fff == "01":
		print "======================================"
		print "[+] Jesus, it will take a lot of time!"
		print "======================================"
		os.system ("pkg update -y")
		os.system ("cd $HOME && git clone https://github.com/Hax4us/Metasploit_termux")
		os.system ("cd $HOME/Metasploit_termux && chmod +x metasploit.sh")
		os.system ("cd $HOME/Metasploit_termux && bash metasploit.sh")
		os.system ("cd $HOME && bundle init > hdh.txt && rm -rf hdh.txt")
		os.system ("cd $HOME && gem install bundler -v 1.16.1")
		os.system ("cd $HOME && bundle install -j5")
		os.system ("cd $HOME/Metasploit_termux && bash metasploit.sh")
		print "====================================="
		print "[+] Metasploit installed"
		print "[+] Type 'msfconsole' to start."
		print "====================================="

	elif fff == "2":
		print """
		____________________________
		||========================||
		||    Created By otx2s    ||
		||From podval with love :3||
		||========================||
		||                        ||
		~~                        ~~ 
		"""
		raw_input("(Press ENTER) ")
		os.system("clear")
		main()

	elif fff == "3":
		print "\nGoodbye..."
		sl(1)
		
	else:
		print "\nSomething wrong"
		sl(1)
		os.system("clear")
		main()

if __name__ == '__main__':
	main()
