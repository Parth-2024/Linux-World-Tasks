# pip install pywhatkit
import pywhatkit as wa
info=input("Enter the number of the person, text you want to send, hr of the time, min of the time:")
info1=info.split(",")
wa.sendwhatmsg(info1[0],info1[1],int(info1[2]),int(info1[3]))