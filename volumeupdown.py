from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume)) 
    volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)

user_volume = int(input("Enter volume level (0 to 100): "))
set_volume(user_volume)