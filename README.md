# UBUNTU_alarm
battery low alarm for ubuntu
For many users UBUNTU fast running out of battery is a problem
TLP and other softwares are also there but when when battery is getting low laptops might shutdown unexpectedly
hence this file might add some alarm to the laptop

first download the given python file in a folder 

steps:
1: go to "my computer"(as per ubuntu 18.04)(or where all the root files are kept)
2: go to "/etc/init.d/", right click the mouse and open terminal in the folder.
3: type the command "sudo gedit rc.local"
4: at the end of the file type "python path_to_your_file"
         for example:  python /home/Downloads/file.py
5: save the file and restart
6 engine will alert you at low battery
