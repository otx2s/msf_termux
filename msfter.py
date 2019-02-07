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

fff = input("[???] Do you want install metasploit? (y/n): ")
if fff == "y":
	print("======================================")
	print("[+] Jesus, it will take a lot of time!")
	print("======================================")
	os.system ("pkg update -y")
	os.system ("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Metasploit_termux")
	os.system ("cd /data/data/com.termux/files/home/Metasploit_termux && chmod +x metasploit.sh")
	os.system ("cd /data/data/com.termux/files/home/Metasploit_termux && bash metasploit.sh")
	os.system ("cd /data/data/com.termux/files/home && bundle init")
	os.system ("cd /data/data/com.termux/files/home && gem install bundler -v 1.16.1")
	os.system ("cd /data/data/com.termux/files/home && bundle install -j5")
	os.system ("cd /data/data/com.termux/files/home/Metasploit_termux && bash metasploit.sh")
	print("=====================================")
	print("[+] Metasploit installed successfully")
	print("[+] Type 'msfconsole' to start.")
	print("=====================================")

elif fff == "n":
	print("\nGoodbye...")
	
else:
	print("\nSomething wrond!")
	print("Restart script!")
