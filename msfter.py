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
	os.system ("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Metasploit_termux")
	os.system ("cd /data/data/com.termux/files/home && cd Metasploit_termux")
	os.system ("cd /data/data/com.termux/files/home && chmod +x metasploit.sh")
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
