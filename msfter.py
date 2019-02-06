import os
import time
sl = time.sleep

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
	print("=======================================")
	print("[+] Jesus, it will take a lot of time!")
	print("=======================================")
	os.system ("pkg update -y")
	os.system ("pkg install -y curl")
	os.system ("cd /data/data/com.termux/files/home && curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh")
	os.system ("cd /data/data/com.termux/files/home && chmod +x metasploit.sh")
	os.system ("cd /data/data/com.termux/files/home && bash metasplot.sh")
	os.system ("cd /data/data/com.termux/files/home && bundle init")
	os.system ("cd /data/data/com.termux/files/home && gem install bundler -v 1.16.1")
	os.system ("cd /data/data/com.termux/files/home && bundle install -j5")
	os.system ("cd /data/data/com.termux/files/home && bash metasplot.sh")
	print("=====================================")
	print("[+] Metasploit installed successfully")
	print("Type 'msfconsole' to start.")
	print("=====================================")

elif fff == "n":
	print("\nGoodbye...")
	sl(1)
	
else:
	print("\nSomething wrond!")
	print("Restart script!")
	sl(1)
