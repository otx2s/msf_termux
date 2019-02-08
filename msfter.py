import os

print("""
             _____         
  __ _  ___ / _/ /____ ____
 /  ' \(_-</ _/ __/ -_) __/
/_/_/_/___/_/ \__/\__/_/
                             
---
Created By otx2s
Ver: 1.0
---

""")

fff = input("[???] Do you want to install metasploit? (y/n): ")
if fff == "y":
	print("======================================")
	print("[+] Jesus, it will take a lot of time!")
	print("======================================")
	os.system ("pkg update -y")
	os.system ("cd $HOME && git clone https://github.com/Hax4us/Metasploit_termux")
	os.system ("cd $HOME/Metasploit_termux && chmod +x metasploit.sh")
	os.system ("cd $HOME/Metasploit_termux && bash metasploit.sh")
	os.system ("cd $HOME && bundle init > hdh.txt && rm -rf hdh.txt")
	os.system ("cd $HOME && gem install bundler -v 1.16.1")
	os.system ("cd $HOME && bundle install -j5")
	os.system ("cd $HOME/Metasploit_termux && bash metasploit.sh")
	print("=====================================")
	print("[+] Metasploit installed successfully")
	print("[+] Type 'msfconsole' to start.")
	print("=====================================")

elif fff == "n":
	print("\nGoodbye...")
	
else:
	print("\nSomething wrond!")
	print("Restart script!")
