# pip install pywhatkit
import pywhatkit as wa
info=input("Enter the following info\n 1.the number of the person along with the country code(e.g.+91 for India)\n 2.text you want to send\n 3.hr of the time, min of the time(in 24hrs time):")
#this info store the information that has been asked in the sentence and provided by the user
info1=info.split(",")
wa.sendwhatmsg(info1[0],info1[1],int(info1[2]),int(info1[3]))
