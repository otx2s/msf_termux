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
  r = "\033[31m"
	
  rand = (B,Y,G,R,C)
  P = random.choice(rand)

def logo():
  print(W+'            .            O                            +   ')
  print(W+' X                               +                        ')
  print(P+'    dMMMMMMMMb .dMMMb  dMMMMMP dMMMMMMP dMMMMMP dMMMMb    ')
  print(P+'   dMP"dMP"dMPdMP" VP dMP        dMP   dMP     dMP.dMP    ') 
  print(P+'  dMP dMP dMP VMMMb  dMMMP      dMP   dMMMP   dMMMMK"     ')  
  print(P+' dMP dMP dMPdP .dMP dMP        dMP   dMP     dMP"AMF      ')   
  print(P+'dMP dMP dMP VMMMP" dMP        dMP   dMMMMMP dMP dMP       ')
  print(W+'     x                   .                         .      ')
  print(W+'                 +                      o               '+W)
  print " "
  print (W+'   '+r+'[01]'+W+' Install Metasploit')
  print (W+'   '+r+'[02]'+W+' Remove Metasploit')
  print (W+'   '+r+'[03]'+W+' Info')
  print (W+'   '+r+'[00]'+W+' Exit')
  print " "
	
	
def install():
	os.system("cd $HOME && pkg install unstable-repo -y")
	os.system("cd $HOME && pkg update -y")
	os.system("cd $HOME && wget https://Auxilus.github.io/metasploit.sh")
	os.system("cd $HOME && bash metasploit.sh")
	os.system("cd $HOME && wget https://github.com/termux/termux-packages/files/2912002/fix-ruby-bigdecimal.sh.txt")
	os.system("cd $HOME && bash fix-ruby-bigdecimal.sh.txt")
	os.system("cd $HOME && patchelf --print-needed $PREFIX/lib/ruby/2.6.0/aarch64-linux-android/bigdecimal/util.so")
	os.system("cd $HOME && export LD_PRELOAD=$LD_PRELOAD:$PREFIX/lib/ruby/gems/2.6.0/gems/bigdecimal-1.4.3/ext/bigdecimal/bigdecimal.so")

def remove():
	os.system("cd $HOME")
	os.system("msfpath='/data/data/com.termux/files/home'")
	os.system("gem uninstall -aIx")
	os.system("apt remove -y bison coreutils findutils apr apr-util libsqlite-dev libtool ncurses-dev ruby ruby-dev libgrpc-dev postgresql libgmp-dev libpcap-dev readline-dev postgresql-dev")
	os.system("rm $PREFIX/bin/msfconsole $PREFIX/bin/msfvenom")
	os.system("cd $msfpath/metasploit-framework/")
	os.system("rm -rf $msfpath/metasploit-framework")

os.system("clear")
print(B+'\n[*]'+W+' Starting msfter\n')
sl(1)

def main():
  os.system("clear")
  logo()
  fff = raw_input("msfter > ")
  if fff == "1" or fff == "01":
    print (W+'\n======================================')
    print (G+'[+]'+W+' Jesus, it will take a lot of time!')
    print (W+'======================================\n')
    install()
    print (W+'=====================================')
    print (G+'[+]'+W+' Metasploit installed')
    print (G+'[+]'+W+' Type "'+G+'msfconsole'+W+'" to start.')
    print (W+'=====================================\n')
  
  elif fff == "2" or fff == "02":
    yas = raw_input("\nYou sure? (y/n): ")
    if yas == "y":
      os.system("clear")
      print (W+'\n=====================================')
      print (G+'[+]'+W+' Removing Metasploit')
      print (W+'=====================================')
      remove()
      print (W+'\n=====================================')
      print (G+'[+]'+W+' Metasploit removed')
      print (W+'=====================================')
      os.system("clear")
      main()
    elif yas == "n":
      os.system("clear")
      main()
    else:
      print (R+'\nERROR'+W+': Wrong command => '+ yas)
      sl(1)
      os.system("clear")
      main()

  elif fff == "3" or fff == "03":
    print (W+'\n____________________________')
    print (W+'||========================||')
    print (W+'||    Created By '+B+'otx2s'+W+'    ||')
    print (W+'||    ----------------    ||')
    print (W+'||From podval with love :3||')
    print (W+'||========================||')
    print (W+'||                        ||')
    print (W+'~~                        ~~\n'+W)
    raw_input("(Press ENTER) ")
    os.system("clear")
    main()
  elif fff == "0" or fff == "00":
		print "\nGoodbye..."
		sl(1)
		
  else:
		print (R+'\nERROR'+W+': Wrong command => '+ fff)
		sl(1)
		os.system("clear")
		main()

if __name__ == '__main__':
	main()

#####################
# PRIVET FROM OTX2S #
#####################
