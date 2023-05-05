
import os
import datetime as dt
import webbrowser
import cv2
import time
import subprocess
import re
import sys

# Keene's stuff
import platform, warnings
# Mac OS
if (platform.system() == "Darwin"):
    import osascript
# Windows
if (platform.system() == "Windows"):
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# Linux
if (platform.system() == "Linux"):
    from subprocess import call
# Input
from pynput.keyboard import Key
from pynput.mouse import Button

from pynput.keyboard import Controller as Key_Controller
from pynput.mouse import Controller as Mouse_Controller

# Keene's stuff
import platform, warnings
# Mac OS
if (platform.system() == "Darwin"):
    import osascript
# Windows
if (platform.system() == "Windows"):
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# Linux
if (platform.system() == "Linux"):
    from subprocess import call
# Input
from pynput.keyboard import Key
from pynput.mouse import Button

from pynput.keyboard import Controller as Key_Controller
from pynput.mouse import Controller as Mouse_Controller



# bird, no, yes, help, book, movie, quiet, restaurant, medicine, newspaper, shop, music, train, weather, email, alarm, airplane, calendar, hotel, theater, camera, grocery, store, emergency, bank

# no, yes, restaurant, medicine, newspaper, shop, music, train, weather, email, alarm, airplane, calendar, hotel, theater, camera, grocery, store, emergency, bank

def movie():
    webbrowser.open_new("https://www.netflix.com/browse/genre/34399")

def book():
    webbrowser.open_new("https://read.amazon.com/landing")

def help():
    webbrowser.open_new("https://docs.google.com/document/d/1RFXxQReQgHmkk0qMInJ5DZc2wxQEcU95MnX2F63UzSM/edit")

def open_twitter():
    """Opens twitter in default browser"""

    url = 'https://twitter.com/home?lang=en'
    webbrowser.open_new(url)

def open_browser():
    """Opens google in default browser"""

    url = 'https://www.google.com/'
    webbrowser.open_new(url)

def open_netflix():
    """Opens google in default browser"""

    url = 'https://www.netflix.com/browse/genre/34399'
    webbrowser.open_new(url)

def open_booking():
    """Opens youtube in default browser"""

    url = 'https://www.booking.com/'
    webbrowser.open_new(url)

def open_email():
    """Opens youtube in default browser"""

    url = 'https://www.gmail.com/'
    webbrowser.open_new(url)

def open_youtube():
    """Opens youtube in default browser"""

    url = 'https://www.youtube.com/'
    webbrowser.open_new(url)

def check_weather():
    """
    Opens up google weather 
    TODO: pretty sure this just goes to berkeley weather no matter where you are, add location based lookup
    """

    url = "https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57j0i67l2j46i20i199i263i433i465i512j69i60l2j69i61j69i60.5279j1j7&sourceid=chrome&ie=UTF-8"
    webbrowser.open_new(url)

def sleep():
    "makes the computer go to sleep"

    if (platform.system() == 'Darwin'):
        os.system("pmset sleepnow")

    elif (platform.system() == 'Windows'):
        print("Command not implemented for Windows")
        raise NotImplementedError
        
    elif (platform.system() == 'Linux'):
        os.system("systemctl suspend")
    else:
        warnings.warn("ERROR: OS cannot be determined")

def volume(direction="UP"):
   
    # TODO might have to adjust for OS sensitivity
    if (platform.system() == 'Darwin'):
        # Mac OS

        curr_volume = get_speaker_output_volume()

        if direction == "UP":
            curr_volume += 8 # how much to increment volume by 
        elif direction == "DOWN":
            curr_volume -= 8
        else:
            raise Exception("Specify 'UP' or 'DOWN' direction in logic handler function call")

        osascript.osascript("set volume output volume " + str(curr_volume))

    elif (platform.system() == 'Linux'):
        print("Command not implemented for Linux")
        raise NotImplementedError

    elif (platform.system() == 'Windows'):
        # print("Command not implemented for Windows")
        # raise NotImplementedError
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        curr_volume = volume.GetMasterVolumeLevel()
        if direction == "UP":
            if curr_volume < -34:
                curr_volume = -34
            elif curr_volume <= -30:
                curr_volume += 8
            elif curr_volume <= -18:
                curr_volume += 4
            elif curr_volume <= -8:
                curr_volume += 2
            else:
                curr_volume += 1
        elif direction == "DOWN":
            if curr_volume >= -6:
                curr_volume -= 1
            elif curr_volume >= -14:
                curr_volume -= 2
            elif curr_volume >= -22:
                curr_volume -= 4
            elif curr_volume >= -34:
                curr_volume -= 8
            else:
                curr_volume = -65
        else:
            raise Exception("Specify 'UP' or 'DOWN' direction in logic handler function call")
        volume.SetMasterVolumeLevel(curr_volume, None)
    else:
        warnings.warn("ERROR: OS cannot be determined")

def get_speaker_output_volume():
    """

    HELPER FUNCTION FOR volume()

    Get the current speaker output volume from 0 to 100.

    Note that the speakers can have a non-zero volume but be muted, in which
    case we return 0 for simplicity.

    Note: Only runs on macOS.
    """
    cmd = "osascript -e 'get volume settings'"
    process = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    output = process.stdout.strip().decode('ascii')

    pattern = re.compile(r"output volume:(\d+), input volume:(\d+), "
                         r"alert volume:(\d+), output muted:(true|false)")
    volume, _, _, muted = pattern.match(output).groups()

    volume = int(volume)
    muted = (muted == 'true')

    return 0 if muted else volume

def mute():

    if (platform.system() == 'Darwin'):
        osascript.osascript("set volume output volume 0")

    elif (platform.system() == 'Windows'):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(1, None)

    elif (platform.system() == 'Linux'):
        print("Command not implemented for Linux")
        raise NotImplementedError
    else:
        warnings.warn("ERROR: OS cannot be determined")

def cancel():

    sys.exit()

# Developing 04/08/2023

def open_finder():
    osascript.osascript('tell app "Finder" to make new Finder window')

def open_app():
    osascript.osascript('tell app "Safari" to activate')

def close_app():
    osascript.osascript('quit app "safari.app"')

def dark_mode():
    osascript.osascript('tell application "System Events" to tell appearance preferences to set dark mode to not dark mode')

def clean_trash():
    osascript.osascript('tell application "Finder" to empty trash')

def display_text():
    osascript.osascript('tell app "System Events" to display dialog "Please give me the medicine!"')

def write_text():
    osascript.osascript('tell application "TextEdit" to activate')
    osascript.osascript('tell application "TextEdit" to make new document')
    osascript.osascript('tell application "System Events" to keystroke "I need support!"')


##########################################################################################################################################
########### FUNCTIONS THAT WE DO NOT YET HAVE A COMMAND MAPPED TO #######################################################################
##########################################################################################################################################

def mousepress(button, mode='tap'):
    """
    Mouse click control function
    modes = 
        tap, immediately click and release
        hold, simulate a mouse click
        release, simulate a mouse release
        scroll, simulate scrolling. use button param as (dx, dy)
        double, double click mouse button, buttom param as (key, how many times)
    """
    mouse = Mouse_Controller()
    
    if (mode == 'tap'):
        mouse.press(button)
        mouse.release(button)
    elif (mode == 'hold'):
        mouse.press(button)
    elif (mode == 'release'):
        mouse.release(button)
    elif (mode == 'scroll'):
        mouse.scroll(button[0], button[1])
    elif (mode == 'double'):
        mouse.click(button[0], button[1])
# Open Application... (Set up with parameter) 

def keypress(key, mode='tap'):
    """
    Key press control function
    modes = 
        tap, immediately press and release
        hold, simulate a key press
        release, simulate a key release
    """
    keyboard = Key_Controller()

    if (mode == 'tap'):
        keyboard.press(key)
        keyboard.release(key)
    elif (mode == 'hold'):
        keyboard.press(key)
    elif (mode == 'release'):
        keyboard.release(key)

def take_picture():
    """
    Opens webcam preview and takes a picture when you hit the spacebar. 
    TODO: set this to run on timer or 1 sign to load preview and one sign to take picture 
    """
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        cv2.imshow('Image Preview', rgb)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            out = cv2.imwrite('~/Desktop/capture.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()


def screenshot():
    """Takes a screenshot and saves to desktop"""

    time = str(dt.datetime.now().strftime("%Y-%m-%d_%h:%m"))
    os.system(f"screencapture -P ~/Desktop/screenshot{time}.jpeg")

def brightness(dir="up"):
    # TODO
    ...

def volume(value):
    # TODO might have to adjust for OS sensitivity
    if (platform.system() == 'Linux'):
        # Linux
        call(["amixer", "-D", "pulse", "sset", "Master", str(value) + "%"])
    elif (platform.system() == 'Darwin'):
        # Mac OS
        osascript.osascript("set volume output volume " + str(value))
    elif (platform.system() == 'Windows'):
        # Windows
        dev = AudioUtilities.GetSpeakers()
        interface = dev.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolume(value, None)
    else:
        warnings.warn("ERROR: OS cannot be determined")

def keypress(key, mode='tap'):
    """
    Key press control function
    modes = 
        tap, immediately press and release
        hold, simulate a key press
        release, simulate a key release
    """
    keyboard = Key_Controller()

    if (mode == 'tap'):
        keyboard.press(key)
        keyboard.release(key)
    elif (mode == 'hold'):
        keyboard.press(key)
    elif (mode == 'release'):
        keyboard.release(key)

def mousepress(button, mode='tap'):
    """
    Mouse click control function
    modes = 
        tap, immediately click and release
        hold, simulate a mouse click
        release, simulate a mouse release
        scroll, simulate scrolling. use button param as (dx, dy)
        double, double click mouse button, buttom param as (key, how many times)
    """
    mouse = Mouse_Controller()
    
    if (mode == 'tap'):
        mouse.press(button)
        mouse.release(button)
    elif (mode == 'hold'):
        mouse.press(button)
    elif (mode == 'release'):
        mouse.release(button)
    elif (mode == 'scroll'):
        mouse.scroll(button[0], button[1])
    elif (mode == 'double'):
        mouse.click(button[0], button[1])
# Open Application... (Set up with parameter) 

if __name__ == "__main__":
    # take_picture()
    # screenshot()
    # open_browser()
    check_weather()
