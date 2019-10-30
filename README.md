# UBUNTU_alarm
battery low alarm for ubuntu
For many users UBUNTU fast running out of battery is a problem
TLP and other softwares are also there but when when battery is getting low laptops might shutdown unexpectedly
hence this file might add some alarm to the laptop
'''
(1) first download the given python file in a folder '''



  open terminal and type "sudo cp -i /path_of_your_file /bin"  
  ---
  then type "sudo crontab -e"
  ----
  after all the hashes type:  "@reboot python /bin/battery_alarm.py &" 
  -
  restart
'''
