import os

from os.path import expanduser
home = expanduser("~") + "/"
# os.system("python3 {}catkin_ws/src/robot_face/src/headturn.py {}".format(home,str(5)))

print("talking now")
# os.system("python3 /home/gal/catkin_ws/src/robot_voice/src/ohbot_say_function.py %s" %("Hello my new "))
os.system("python3 {}catkin_ws/src/robot_voice/src/ohbot_say_function.py {}".format(home,str(101)))
                    # os.system("python3 /home/gal/catkin_ws/src/robot_face/src/headturn.py %s" %(str(5)))
