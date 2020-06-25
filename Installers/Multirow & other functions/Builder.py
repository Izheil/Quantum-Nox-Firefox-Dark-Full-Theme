import os
import re
import sys
import glob
import ctypes
import shutil
import tkinter
import argparse
import subprocess
import webbrowser
import distutils.core
from pathlib import Path
from tkinter import (LabelFrame, Checkbutton, Frame, Label, Entry, 
                    filedialog, Button, Listbox, Radiobutton, Spinbox, 
                    Scrollbar, messagebox, PhotoImage)

def SystemOS():
    "Identifies the OS"

    if sys.platform.startswith('win'):
        SystemOS = "Windows"
    elif sys.platform.startswith('linux'):
        SystemOS = "Linux"
    elif sys.platform.startswith('darwin'):
        SystemOS = "Mac"
    else: SystemOS = "Unknown"
    return SystemOS

OSinUse = SystemOS()

if OSinUse != "Windows":
    if os.geteuid() != 0:
        os.execvp("sudo", ["sudo"] + sys.argv)
elif ctypes.windll.shell32.IsUserAnAdmin() == 0:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

def readProfiles(profile):
    "Fetches the profile folders"

    ProfilesINI = os.path.normpath(profile + "/profiles.ini")
    Paths = []
    if not os.access(ProfilesINI, os.F_OK):
        if OSinUse == "Windows" or OSinUse == "Mac":
            profile = os.path.normpath(profile + "/Profiles")

        profilenames = os.listdir(profile)
        for x in profilenames:
            Paths.append(os.path.normpath(profile + "/" + x))
    else:
        with open(ProfilesINI, 'r') as f:
            for line in f.readlines():
                profilepath = re.match("Path=(.*)", line, re.M|re.I)
                if profilepath != None:
                    rotationpath = profilepath.group(1)
                    if (((OSinUse == "Windows" or OSinUse == "Mac") and
                        rotationpath[0:9] == "Profiles/") or
                        OSinUse == "Linux" and rotationpath[0] != "/"):
                        Paths.append(os.path.normpath(profile + "/" + profilepath.group(1)))
                    else:
                        Paths.append(os.path.normpath(profilepath.group(1)))

    return Paths

def readDefaults(profile):
    "Fetches the default profile folders"

    installsINI = os.path.normpath(profile + "/installs.ini")
    Paths = []
    if not os.access(installsINI, os.F_OK):
        return None
    else:
        with open(installsINI, 'r') as f:
            for line in f.readlines():
                defaultspath = re.match("Default=(.*)", line, re.M|re.I)
                if defaultspath != None:
                    defaultrotation = defaultspath.group(1)
                    if (((OSinUse == "Windows" or OSinUse == "Mac") and
                        defaultrotation[0:9] == "Profiles/") or
                        OSinUse == "Linux" and defaultrotation[0] != "/"):
                        Paths.append(os.path.normpath(profile + "/" + defaultspath.group(1)))
                    else:
                        Paths.append(os.path.normpath(defaultspath.group(1)))
        return Paths

# We get the user folders here
if OSinUse == "Windows":
    # This is a workaround to find the current logged in user
    # in case they are not using an administrator account,
    # since otherwise it's not possible to find it on Windows
    tmp_file = sys._MEIPASS + '\\tempData.txt'
    try:
        with open(tmp_file, 'w+') as w:
            args = ['C:\\Windows\\Sysnative\\query.exe', 'user']
            findCurrentUser = subprocess.Popen(args, stdout=w, stderr=subprocess.STDOUT,
                            stdin=subprocess.PIPE,
                            universal_newlines=True,
                            shell=False)
            findCurrentUser.wait()

        with open(tmp_file, 'r') as r:
            output = r.readlines()

        users = []
        for line in output:
            if line == output[0]:
                continue
            else:
                userRead = re.match(">(.*?) console *", line, re.M | re.I)
                if userRead is not None:
                    users.append(str(userRead.group(1)).rstrip())

    except Exception as err:
        print("Couldn't locate login user, backing to default profile path.")
        users = [os.getenv('USERNAME')]

    if os.access(tmp_file, os.F_OK):
        os.remove(tmp_file)

    adminProfile = os.getenv('USERPROFILE')
    adminName = os.getenv('USERNAME')

    appdataPath = (adminProfile[0:-(len(adminName))] 
                  + users[0].capitalize() 
                  + "\\AppData\\Roaming")

    altPath = os.path.join("C:\\Users\\", users[0].capitalize() 
                           + "\\AppData\\Roaming")

    if os.access(appdataPath, os.F_OK):
        home = appdataPath
    elif os.access(altPath, os.F_OK):
        home = altPath
    else:
        home = os.getenv('APPDATA')
    MozPFolder = home + r"\Mozilla\Firefox"
elif OSinUse == "Linux":
    home = "/home/" + os.getenv("SUDO_USER")
    MozPFolder = home + r"/.mozilla/firefox"
elif OSinUse == "Mac":
    home = str(Path.home())
    MozPFolder = home + r"/Library/Application Support/Firefox"

Profiles = readProfiles(MozPFolder)
defaultProf = readDefaults(MozPFolder)

# We get the default folder where programs are installed here
if OSinUse == "Windows":
    PFolder = r"C:\Program Files"
    if os.access(PFolder, os.F_OK) == False:
        PFolder = ""
elif OSinUse == "Linux" or OSinUse == "Unknown":
    PFolder = r"/usr/lib"
    if os.access(PFolder, os.F_OK) == False:
        PFolder = ""
elif OSinUse == "Mac":
    PFolder = r"/Applications/"
    if os.access(PFolder, os.F_OK) == False:
        PFolder = ""

# We get the default folders for each installation here
if OSinUse == "Windows":
    root = r"C:\Program Files (x86)\Mozilla Firefox"
    rootN = r"C:\Program Files (x86)\Firefox Nightly"
    rootD = r"C:\Program Files (x86)\Firefox Developer Edition"
    if not os.access(root, os.F_OK):
        root = r"C:\Program Files\Mozilla Firefox"
        if not os.access(root, os.F_OK):
            root = "Not found"
    if not os.access(rootN, os.F_OK):
        rootN = r"C:\Program Files (x86)\Firefox Nightly"
        if not os.access(rootN, os.F_OK):
            rootN = r"C:\Program Files\Firefox Nightly"
            if not os.access(rootN, os.F_OK):
                rootN = "Not found"
    if not os.access(rootD, os.F_OK):
        rootD = r"C:\Program Files (x86)\Firefox Developer Edition"
        if not os.access(rootD, os.F_OK):
            rootD = r"C:\Program Files\Firefox Developer Edition"
            if not os.access(rootD, os.F_OK):
                rootD = "Not found"
elif OSinUse == "Linux" or OSinUse == "Unknown":
    root = r"/usr/lib/firefox/"
    rootN = r"/opt/nightly"
    rootD = r"/opt/developer"
    if not os.access(root, os.F_OK):
        root = r"/usr/lib64/firefox/"
        if not os.access(root, os.F_OK):
            root = "Not found"
    if not os.access(rootN, os.F_OK):
        rootN = r"/opt/firefox"
        if not os.access(rootN, os.F_OK):
            rootN = "Not found"
    if not os.access(rootD, os.F_OK):
        rootD = r"/opt/firefox"
        if not os.access(rootD, os.F_OK):
            rootD = "Not found"
elif OSinUse == "Mac":
    root = r"/Applications/Firefox.app/Contents/Resources"
    rootN = r"/Applications/Firefox Nightly.app/Contents/Resources"
    rootD = r"/Applications/Firefox Developer Edition.app/Contents/Resources"
    if not os.access(root, os.F_OK):
        root = "Not found"
    if not os.access(rootN, os.F_OK):
        rootN = "Not found"
    if not os.access(rootD, os.F_OK):
        rootD = "Not found"

# We get the default folders here
def RPFinder():
    for x in defaultProf:
        splitter = x.split(".")
        ProfileName = splitter[-1]
        if ProfileName == "default-release":
            return x
        elif ProfileName == "default":
            return x
        else:
            continue
    for x in Profiles:
        splitter = x.split(".")
        ProfileName = splitter[-1]
        if ProfileName == "default-release":
            return x
        elif ProfileName == "default":
            return x
        else:
            continue
    return "Not found"


def NPFinder():
    for y in defaultProf:
        Nsplitter = y.split(".")
        ProfileName = Nsplitter[-1]
        if ProfileName == "default-nightly":
            return y
        elif ProfileName[0:15] == "default-nightly":
            return y
        else:
            continue
    for y in Profiles:
        Nsplitter = y.split(".")
        ProfileName = Nsplitter[-1]
        if ProfileName == "default-nightly":
            return y
        elif ProfileName[0:15] == "default-nightly":
            return y
        else:
            continue
    return "Not found"


def DPFinder():
    for y in defaultProf:
        Dsplitter = y.split(".")
        ProfileName = Dsplitter[-1]
        if ProfileName == "dev-edition-default":
            return y
        elif ProfileName[0:19] == "dev-edition-default":
            return y
        else:
            continue
    for y in Profiles:
        Dsplitter = y.split(".")
        ProfileName = Dsplitter[-1]
        if ProfileName == "dev-edition-default":
            return y
        elif ProfileName[0:19] == "dev-edition-default":
            return y
        else:
            continue
    return "Not found"

# We call the default profile finders
RProfile = RPFinder()
NProfile = NPFinder()
DProfile = DPFinder()

# Check if only 1 profile exists and only 1 installation exists
# so that if not using the default profile names, it will get
# selected.
if Profiles is not None:
    # First we check if only 1 firefox is installed
    onlyStable = (root != "Not found"
        and rootN == "Not found"
        and rootD == "Not found")
    onlyDev = (rootD != "Not found"
        and root == "Not found"
        and rootN == "Not found")
    onlyNightly = (rootN != "Not found"
        and root == "Not found"
        and rootD == "Not found")

    if RProfile == "Not found" and onlyStable:
        RProfile = Profiles[0]

    if DProfile == "Not found" and onlyDev:
        DProfile = Profiles[0]

    if NProfile == "Not found" and onlyNightly:
        NProfile = Profiles[0]

# We try to get the folder where profiles are located to show
# as the default to open in the "select profile" buttons.
# If it doesn't exist we go back to the default mozilla folder.
defPLocation = os.path.join(MozPFolder, "Profiles")

if not os.access(defPLocation, os.F_OK):
    if Profiles is not None:
        if OSinUse == "Windows":
            profileSplitter = Profiles[0].split("\\")
        else:
            profileSplitter = Profiles[0].split("/")
        removeLast = len(profileSplitter[-1])
        defPLocation = Profiles[0][0:-removeLast]
        del removeLast
        del profileSplitter
    else:
        defPLocation = MozPFolder

# This applies the basic patch for the functions to work
def fullPatcher(FFversion, FFprofile):
    "This method patches both the root and profile folders"
    try:
        if FFversion != None:
            # We first define the location of the files
            ConfPref = os.path.normpath(FFversion + "/defaults/pref/config-prefs.js")
            ConfJS = os.path.normpath(FFversion + "/config.js")

            # We patch the root folder here
            if os.access(ConfJS, os.F_OK) and os.access(ConfPref, os.F_OK):

                distutils.file_util.copy_file(os.path.normpath(sys._MEIPASS + "/root/defaults/pref/config-prefs.js"), 
                                              os.path.normpath(FFversion + "/defaults/pref/"), update=True)
                distutils.file_util.copy_file(os.path.normpath(sys._MEIPASS + "/root/config.js"), 
                                              FFversion, update=True)

            elif os.access(os.path.normpath(FFversion + "/config.js"), os.F_OK) or \
            os.access(os.path.normpath(FFversion + "/defaults/pref/config-prefs.js"), os.F_OK):

                if os.access(ConfJS, os.F_OK):
                    shutil.copy2(os.path.normpath(sys._MEIPASS + "/root/defaults/pref/config-prefs.js"), 
                                 os.path.normpath(FFversion + "/defaults/pref/"))

                else: shutil.copy2(os.path.normpath(sys._MEIPASS + "/root/config.js"), FFversion)

            else: 
                shutil.copy2(os.path.normpath(sys._MEIPASS + "/root/config.js"), FFversion)
                shutil.copy2(os.path.normpath(sys._MEIPASS + "/root/defaults/pref/config-prefs.js"), 
                             os.path.normpath(FFversion + "/defaults/pref/"))

            if OSinUse == "Linux":
                rootUser = os.getenv("SUDO_USER")
                shutil.chown(ConfPref, user=rootUser, group=rootUser)
                os.chmod(ConfPref, 0o775)
                shutil.chown(ConfJS, user=rootUser, group=rootUser)
                os.chmod(ConfJS, 0o775)

        if FFprofile != None:

            # We patch the profile folder here
            if os.access(os.path.normpath(FFprofile + "/chrome/utils"), os.F_OK):
                utilFiles = []
                for r, d, f in os.walk(os.path.normpath(sys._MEIPASS + "/utils")):
                    for file in f:
                            utilFiles.append(os.path.join(r, file))
                for file in utilFiles:
                    distutils.file_util.copy_file(file, 
                        os.path.normpath(FFprofile + "/chrome/utils"), update=True)

            else: 
                shutil.copytree(os.path.normpath(sys._MEIPASS + "/utils"), 
                                os.path.normpath(FFprofile + "/chrome/utils"))

            if OSinUse == "Linux":
                chrome = FFprofile + "/chrome"
                utils = chrome + "/utils"
                rootUser = os.getenv("SUDO_USER")
                utilFiles = glob.glob(utils + "/*.*")
                shutil.chown(chrome, user=rootUser, group=rootUser)
                os.chmod(chrome, 0o775)
                shutil.chown(utils, user=rootUser, group=rootUser)
                os.chmod(utils, 0o775)
                for file in utilFiles:
                    shutil.chown(file, user=rootUser, group=rootUser)
                    os.chmod(file, 0o775)

    except IOError:
        errorMessage = "You need higher privileges to apply the patch."
        if not argumentsInUse:
            messagebox.showerror("Error", errorMessage)
        else:
            print(errorMessage)
        return 1

    return 0


# We copy the function files to the profile folder with this method
def functionInstall(FFprofile, Func2Inst, FuncSettings="0"):
    "This function installs the functions"

    # We first get the chrome folder
    FFChrome = os.path.normpath(FFprofile + "/chrome")

    # We define the common variables used for each function next
    if Func2Inst.startswith('Multirow'):
        FFCMR = os.path.normpath(FFprofile 
                    + "/chrome/MultiRowTab-scrollable.uc.js")
        FFCMRL = os.path.normpath(FFprofile 
                    + "/chrome/MultiRowTabLiteforFx.uc.js")
        FFCMRA = os.path.normpath(FFprofile 
                    + "/chrome/MultiRowTab-scrollable-autohide.uc.js")
        FFCMR71 = os.path.normpath(FFprofile 
                    + "/chrome/MultiRowTab-scrollableFF71.uc.js")
        FFCMRL71 = os.path.normpath(FFprofile 
                    + "/chrome/MultiRowTabLiteforFF71.uc.js")
        FFCMRA71 = os.path.normpath(FFprofile 
                    + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js")

    elif Func2Inst.startswith('Tabs-below'):
        FFTBoT = os.path.normpath(FFprofile 
                    + "/chrome/Tabs-below-Menu-overTabs.as.css")
        FFTBaA = os.path.normpath(FFprofile 
                    + "/chrome/Tabs-below-Menu-onTop.as.css")
        FFTB = os.path.normpath(FFprofile 
                    + "/chrome/Tabs-below.as.css")

    elif Func2Inst.startswith('Megabar'):
        FFMB = os.path.normpath(FFprofile 
                    + "/chrome/Megabar-disabled-until-focus.as.css")
        FFMBAR = os.path.normpath(FFprofile 
                    + "/chrome/Megabar-disabled-all-resizing.as.css")

    # These write the settings to the files
    def writeSettings(InstFunct):
        with open(InstFunct, "r+") as f:
            s = f.read()
            if Func2Inst.startswith("Multirow"):
                s = s.replace("TABROWS", FuncSettings)
            elif Func2Inst.startswith("Focus-tab"):
                s = s.replace("DELAYTIME", FuncSettings)
            f.seek(0, 0)
            f.write(s)
            f.truncate()

    # These remove the duplicated functions
    def remDupMR(Func2Inst):
        if os.access(FFCMRA, os.F_OK) \
                and Func2Inst != "Multirow-autohide":
            os.remove(FFCMRA)
        if os.access(FFCMR, os.F_OK) \
                and Func2Inst != "Multirow-scrollable":
            os.remove(FFCMR)
        if os.access(FFCMRL, os.F_OK) \
                and Func2Inst != "Multirow-unlimited":
            os.remove(FFCMRL)

        if os.access(FFCMRA71, os.F_OK):
            os.remove(FFCMRA71)    
        if os.access(FFCMR71, os.F_OK):
            os.remove(FFCMR71)
        if os.access(FFCMRL71, os.F_OK):
            os.remove(FFCMRL71)

    def remDupTB(Func2Inst):
        if os.access(FFTB, os.F_OK) \
                and Func2Inst != "Tabs-below":
            os.remove(FFTB)
        if os.access(FFTBoT, os.F_OK) \
                and Func2Inst != "Tabs-below-menu-over-tabs":
            os.remove(FFTBoT)

        if os.access(FFTBaA, os.F_OK):
            os.remove(FFTBaA)

    def remDupMB(Func2Inst):
        if os.access(FFMB, os.F_OK) \
                and Func2Inst != "Megabar-until-focus":
            os.remove(FFMB)
        if os.access(FFMBAR, os.F_OK) \
                and Func2Inst != "Megabar-all-resizing":
            os.remove(FFMBAR)

    # This is the function to change ownership on Linux
    def fileOwn(profInstFile):
        rootUser = os.getenv('SUDO_USER')
        shutil.chown(profInstFile, user=rootUser, group=rootUser)
        os.chmod(profInstFile, 0o775)

    # Functions installation here
    def instFunct():
        if Func2Inst == "Multirow-scrollable":
            FireFunct = os.path.normpath(sys._MEIPASS
                        + "/functions/MultiRowTab-scrollable.uc.js")
            InstFunct = FFCMR
        elif Func2Inst == "Multirow-autohide":
            FireFunct = os.path.normpath(sys._MEIPASS
                        + "/functions/MultiRowTab-scrollable-autohide.uc.js")
            InstFunct = FFCMRA
        elif Func2Inst == "Multirow-unlimited":
            FireFunct = os.path.normpath(sys._MEIPASS
                        + "/functions/MultiRowTabLiteforFx.uc.js")
            InstFunct = FFCMRL
        elif Func2Inst == "Tabs-below":
            FireFunct = os.path.normpath(sys._MEIPASS
                        + "/functions/Tabs-below.as.css")
            InstFunct = FFTB
        elif Func2Inst == "Tabs-below-menu-over-tabs":
            FireFunct = os.path.normpath(sys._MEIPASS
                        + "/functions/Tabs-below-Menu-overTabs.as.css")
            InstFunct = FFTBoT
        elif Func2Inst == "Megabar-until-focus":
            FireFunct = os.path.normpath(sys._MEIPASS
                        + "/functions/Megabar-disabled-until-focus.as.css")
            InstFunct = FFMB
        elif Func2Inst == "Megabar-all-resizing":
            FireFunct = os.path.normpath(sys._MEIPASS
                        + "/functions/Megabar-disabled-all-resizing.as.css")
            InstFunct = FFMBAR
        elif Func2Inst == "Focus-tab":
            FireFunct = os.path.normpath(sys._MEIPASS
                        + "/functions/Focus-tab-on-hover.uc.js")
            InstFunct = os.path.normpath(FFprofile 
                        + "/chrome/Focus-tab-on-hover.uc.js")
        elif Func2Inst == "Unread-state":
            FireFunct = os.path.normpath(sys._MEIPASS
                        + "/functions/setAttribute_unread.uc.js")
            InstFunct = os.path.normpath(FFprofile 
                        + "/chrome/setAttribute_unread.uc.js")

        try:
            shutil.copy2(FireFunct, FFChrome)

            if Func2Inst.startswith("Multirow") or Func2Inst == "Focus-tab":
                writeSettings(InstFunct)

            if OSinUse == "Linux":
                fileOwn(InstFunct)

            # We remove the alternative versions on those functions
            # that have it
            if Func2Inst.startswith("Multirow"):
                remDupMR(Func2Inst)
            elif Func2Inst.startswith("Tabs-below"):
                remDupTB(Func2Inst)
            elif Func2Inst.startswith("Megabar"):
                remDupMB(Func2Inst)
            return 0

        except IOError:
            errorMessage = "There was a problem while trying to install "
            if Func2Inst.startswith("Multirow"):
                errorMessage += "Multirow."
            elif Func2Inst.startswith("Tabs-below"):
                errorMessage += "Tabs Below."
            elif Func2Inst.startswith("Megabar"):
                errorMessage += "Megabar resizing disabler."
            elif Func2Inst == "Focus-tab":
                errorMessage = "Focus tabs on hover."
            elif Func2Inst == "Unread-state":
                errorMessage = "Tabs unread state."

            if not argumentsInUse:
                messagebox.showwarning("Write access error", errorMessage)
            else:
                print(errorMessage)
            if os.access(InstFunct, os.F_OK):
                os.remove(InstFunct)
            return 1

    return instFunct()


def erasePatch(FFversion, FFprofile):
    "This method removes the patch from both the root and profile folders"
    try:
        if FFversion is not None:
            # We remove the patch from the root folder here
            if os.access(os.path.normpath(FFversion + "/config.js"), os.F_OK) and \
            os.access(os.path.normpath(FFversion + "/defaults/pref/config-prefs.js"), os.F_OK):

                os.remove(os.path.normpath(FFversion + "/defaults/pref/config-prefs.js"))
                os.remove(os.path.normpath(FFversion + "/config.js"))

            elif os.access(os.path.normpath(FFversion + "/config.js"), os.F_OK) or \
                 os.access(os.path.normpath(FFversion + "/defaults/pref/config-prefs.js"), os.F_OK):
                if os.access(os.path.normpath(FFversion + "/config.js"), os.F_OK):
                    os.remove(os.path.normpath(FFversion + "/config.js"))

                else: os.remove(os.path.normpath(FFversion 
                                + "/defaults/pref/config-prefs.js"))

        if FFprofile is not None:

            # We remove the patch from the profile folder here
            if os.access(os.path.normpath(FFprofile
                         + "/chrome/utils"), os.F_OK):
                if os.access(os.path.normpath(FFprofile
                             + "/chrome/utils/boot.jsm"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile
                              + "/chrome/utils/boot.jsm"))
                if os.access(os.path.normpath(FFprofile
                             + "/chrome/utils/chrome.manifest"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile
                              + "/chrome/utils/chrome.manifest"))
                if os.access(os.path.normpath(FFprofile
                             + "/chrome/utils/RDFDataSource.jsm"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile
                              + "/chrome/utils/RDFDataSource.jsm"))
                if os.access(os.path.normpath(FFprofile
                             + "/chrome/utils/RDFManifestConverter.jsm"),
                             os.F_OK):
                    os.remove(os.path.normpath(FFprofile
                              + "/chrome/utils/RDFManifestConverter.jsm"))
                if os.access(os.path.normpath(FFprofile
                             + "/chrome/utils/userChrome.jsm"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile
                              + "/chrome/utils/userChrome.jsm"))
                if os.access(os.path.normpath(FFprofile
                             + "/chrome/utils/xPref.jsm"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile
                              + "/chrome/utils/xPref.jsm"))

                utilChromeFiles = []
                for r, d, f in os.walk(os.path.normpath(FFprofile + "/chrome/utils")):
                    for file in f:
                            utilChromeFiles.append(os.path.join(r, file))
                if utilChromeFiles == []:
                    os.rmdir(os.path.normpath(FFprofile + "/chrome/utils"))

    except IOError:
        if not argumentsInUse:
            messagebox.showerror("Error",
                        "You need higher privileges to remove the patch.")
        else:
            print("You need higher privileges to remove the patch.")
        return 1

    return 0


def functionRemove(FFprofile, Func2Remove):
    "This function removes the functions from the selected profile folder."

    errorMessage = "There was a problem while removing "

    # This displays the error messages on write access failure
    def displayError(Err):
        if not argumentsInUse:
            messagebox.showwarning("Write access error", errorMessage)
        else:
            print(errorMessage)

    # We remove the files here
    if Func2Remove == "Multirow":
        MRS = os.path.normpath(FFprofile
                               + "/chrome/MultiRowTab-scrollable.uc.js")
        MRS71 = os.path.normpath(FFprofile
                               + "/chrome/MultiRowTab-scrollableFF71.uc.js")
        MRL = os.path.normpath(FFprofile
                               + "/chrome/MultiRowTabLiteforFx.uc.js")
        MRL71 = os.path.normpath(FFprofile
                               + "/chrome/MultiRowTabLiteforFF71.uc.js")
        MRSA = os.path.normpath(FFprofile
                               + "/chrome/MultiRowTab-scrollable-autohide.uc.js")
        MRSA71 = os.path.normpath(FFprofile
                               + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js")
        try:
            if os.access(MRS, os.F_OK):
                os.remove(MRS)
            if os.access(MRS71, os.F_OK):
                os.remove(MRS71)
            if os.access(MRL, os.F_OK):
                os.remove(MRL)
            if os.access(MRL71, os.F_OK):
                os.remove(MRL71)
            if os.access(MRSA, os.F_OK):
                os.remove(MRSA)
            if os.access(MRSA71, os.F_OK):
                os.remove(MRSA71)

        except IOError:
            errorMessage += "Multirow."
            displayError(errorMessage)
            return 1

    elif Func2Remove == "Tabs-below":
        TB = os.path.normpath(FFprofile + "/chrome/Tabs-below.as.css")
        TBoT = os.path.normpath(FFprofile
                                + "/chrome/Tabs-below-Menu-overTabs.as.css")
        TBaA = os.path.normpath(FFprofile
                                + "/chrome/Tabs-below-Menu-onTop.as.css")
        try:
            if os.access(TB, os.F_OK):
                os.remove(TB)
            if os.access(TBoT, os.F_OK):
                os.remove(TBoT)
            if os.access(TBaA, os.F_OK):
                os.remove(TBaA)

        except IOError:
            errorMessage += "Tabs below."
            displayError(errorMessage)
            return 1

    elif Func2Remove == "Megabar":
        MB = os.path.normpath(FFprofile + "/chrome/Megabar-disabled-until-focus.as.css")
        MBAR = os.path.normpath(FFprofile
                                + "/chrome/Megabar-disabled-all-resizing.as.css")
        try:
            if os.access(MB, os.F_OK):
                os.remove(MB)
            if os.access(MBAR, os.F_OK):
                os.remove(MBAR)

        except IOError:
            errorMessage += "Megabar resizing disabler."
            displayError(errorMessage)
            return 1

    elif Func2Remove == "Focus-tab":
        FT = os.path.normpath(FFprofile + "/chrome/Focus-tab-on-hover.uc.js")
        try:
            if os.access(FT, os.F_OK):
                os.remove(FT)

        except IOError:
            errorMessage += "Focus tab on hover."
            displayError(errorMessage)
            return 1

    elif Func2Remove == "Unread-state":
        US = os.path.normpath(FFprofile + "/chrome/setAttribute_unread.uc.js")

        try:
            if os.access(US, os.F_OK):
                os.remove(US)

        except IOError:
            errorMessage += "Unread state on tabs."
            displayError(errorMessage)
            return 1
    return 0


def callhome():
    "This method opens the repository page"
    webbrowser.open_new(r"https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Other%20features")


def openProfile(profileFolder):
    if os.access(profileFolder, os.F_OK):
        chromeFolder = os.path.normpath(profileFolder + "/chrome")
        if os.access(chromeFolder, os.F_OK):
            webbrowser.open(chromeFolder)
        else:
            messagebox.showerror("Error",
            "Couldn't locate the profile chrome folder."
            + "\nSelect a valid one and try again.")
    else: 
        messagebox.showerror("Error",
        "Couldn't locate the profile folder."
        + "\nSelect a valid one and try again.")


class patcherUI(Frame):
    "This class creates the UI of the patcher"

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.pack(expand=True, fill="both")

        # These methods update the entries when looking for a
        # root/profile folder
        def EntryUpdate(SelButton):
            if SelButton == "1" or SelButton == "3" or SelButton == "5":
                SelDir = os.path.normpath(
                         filedialog.askdirectory(initialdir=PFolder))

            elif SelButton == "2" or SelButton == "4" or SelButton == "6":
                SelDir = os.path.normpath(
                         filedialog.askdirectory(initialdir=defPLocation))

            if SelDir != "" and SelDir != ".":
                if SelButton == "1":
                    rpCkFF12.delete(0, "end")
                    rpCkFF12.insert(0, SelDir)

                elif SelButton == "2":
                    rpCkFF22.delete(0, "end")
                    rpCkFF22.insert(0, SelDir)

                elif SelButton == "3":
                    rpCkFFD12.delete(0, "end")
                    rpCkFFD12.insert(0, SelDir)

                elif SelButton == "4":
                    rpCkFFD22.delete(0, "end")
                    rpCkFFD22.insert(0, SelDir)

                elif SelButton == "5":
                    rpCkFFN12.delete(0, "end")
                    rpCkFFN12.insert(0, SelDir)

                elif SelButton == "6":
                    rpCkFFN22.delete(0, "end")
                    rpCkFFN22.insert(0, SelDir)

                checkPatchFF()
                checkPatchFFD()
                checkPatchFFN()

        def EntryReset():
            disState = False
            if rpCkFF12["state"] == "disabled":
                rpCkFF12.config(state="normal")
                disState = True

            rpCkFF12.delete(0, "end")
            rpCkFF12.insert(0, root)

            if disState:
                rpCkFF12.config(state="disabled")
                disState = False

            if rpCkFF22["state"] == "disabled":
                rpCkFF22.config(state="normal")
                disState = True

            rpCkFF22.delete(0, "end")
            rpCkFF22.insert(0, RProfile)

            if disState:
                rpCkFFD22.config(state="disabled")
                disState = False

            if rpCkFFD12["state"] == "disabled":
                rpCkFFD12.config(state="normal")
                disState = True

            rpCkFFD12.delete(0, "end")
            rpCkFFD12.insert(0, rootD)

            if disState:
                rpCkFFD12.config(state="disabled")
                disState = False

            if rpCkFFD22["state"] == "disabled":
                rpCkFFD22.config(state="normal")
                disState = True

            rpCkFFD22.delete(0, "end")
            rpCkFFD22.insert(0, DProfile)

            if disState:
                rpCkFFD22.config(state="disabled")
                disState = False

            if rpCkFFN12["state"] == "disabled":
                rpCkFFN12.config(state="normal")
                disState = True

            rpCkFFN12.delete(0, "end")
            rpCkFFN12.insert(0, rootN)

            if disState:
                rpCkFFN12.config(state="disabled")
                disState = False

            if rpCkFFN22["state"] == "disabled":
                rpCkFFN22.config(state="normal")
                disState = True

            rpCkFFN22.delete(0, "end")
            rpCkFFN22.insert(0, NProfile)

            if disState:
                rpCkFFN22.config(state="disabled")
                disState = False

            checkPatchFF()
            checkPatchFFD()
            checkPatchFFN()

        # We disable the children of the checkboxes that aren't selected here
        def updateFFChildren():
            if CkFF.get() == 0:
                rpCkFF1.config(state="disabled")
                rpCkFF12.config(state="disabled")
                rpCkFF13.config(state="disabled")
                rpCkFF2.config(state="disabled")
                rpCkFF22.config(state="disabled")
                rpCkFF23.config(state="disabled")
            elif CkFF.get() == 1:
                rpCkFF1.config(state="normal")
                rpCkFF12.config(state="normal")
                rpCkFF13.config(state="normal")
                rpCkFF2.config(state="normal")
                rpCkFF22.config(state="normal")
                rpCkFF23.config(state="normal")

        def updateFFDChildren():
            if CkFFD.get() == 0:
                rpCkFFD1.config(state="disabled")
                rpCkFFD12.config(state="disabled")
                rpCkFFD13.config(state="disabled")
                rpCkFFD2.config(state="disabled")
                rpCkFFD22.config(state="disabled")
                rpCkFFD23.config(state="disabled")
            elif CkFF.get() == 1:
                rpCkFFD1.config(state="normal")
                rpCkFFD12.config(state="normal")
                rpCkFFD13.config(state="normal")
                rpCkFFD2.config(state="normal")
                rpCkFFD22.config(state="normal")
                rpCkFFD23.config(state="normal")

        def updateFFNChildren():
            if CkFFN.get() == 0:
                rpCkFFN1.config(state="disabled")
                rpCkFFN12.config(state="disabled")
                rpCkFFN13.config(state="disabled")
                rpCkFFN2.config(state="disabled")
                rpCkFFN22.config(state="disabled")
                rpCkFFN23.config(state="disabled")
            elif CkFFN.get() == 1:
                rpCkFFN1.config(state="normal")
                rpCkFFN12.config(state="normal")
                rpCkFFN13.config(state="normal")
                rpCkFFN2.config(state="normal")
                rpCkFFN22.config(state="normal")
                rpCkFFN23.config(state="normal")

        def updateFFPChildren():
            if CkFFP.get() == 0:
                rpCkFFP1.config(state="disabled")
                rpDetail.config(state="disabled")
            elif CkFFP.get() == 1:
                rpCkFFP1.config(state="normal")
                rpDetail.config(state="normal")

        def updateMRChildren():
            if CkMR.get() == 0:
                fpCkMR1.config(state="disabled")
                fpCkMR2.config(state="disabled")
                fpCkMR1E.config(state="disabled")
                fpCkMR1C.config(state="disabled")
            elif CkMR.get() == 1:
                fpCkMR1.config(state="normal")
                fpCkMR2.config(state="normal")
                if RdMR.get() == 1:
                    fpCkMR1E.config(state="disabled")
                    fpCkMR1C.config(state="disabled")
                elif RdMR.get() == 0:
                    fpCkMR1E.config(state="normal")
                    fpCkMR1C.config(state="normal")

        def updateMRSpinbox():
            if RdMR.get() == 1:
                fpCkMR1E.config(state="disabled")
                fpCkMR1C.config(state="disabled")
            elif RdMR.get() == 0:
                fpCkMR1E.config(state="normal")
                fpCkMR1C.config(state="normal")

        def updateFTChildren():
            if CkFT.get() == 0:
                fpCkFTD.config(state="disabled")
                fpCkFTDE.config(state="disabled")
            elif CkFT.get() == 1:
                fpCkFTD.config(state="normal")
                fpCkFTDE.config(state="normal")

        def updateMBCheck():
            if CkMB.get() == 0:
                fpCkMB1.config(state="disabled")
            elif CkMB.get() == 1:
                fpCkMB1.config(state="normal")

        def updateTBCheck():
            if CkTB.get() == 0:
                fpCkTB1.config(state="disabled")
            elif CkTB.get() == 1:
                fpCkTB1.config(state="normal")

        # We check the patch status with these methods
        def checkPatchFF():
            if root == "Not found":
                PatchStatusFFr.config(text="Not installed")
            else:
                PatchStatusFFr.config(text="Not Patched", fg="#cc0000")
            if os.access(os.path.normpath(rpCkFF12.get() + "/config.js"), os.F_OK) and \
               os.access(os.path.normpath(rpCkFF12.get() + "/defaults/pref/config-prefs.js"), os.F_OK):
                if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/utils"), os.F_OK):
                    PatchStatusFFr.config(text="Patched", fg="#339900")
                else: 
                    PatchStatusFFr.config(text="Profile not patched", fg="#cc0000")
            elif os.access(os.path.normpath(rpCkFF22.get() + "/chrome/utils"), os.F_OK):
                PatchStatusFFr.config(text="Root not patched", fg="#cc0000")

        def checkPatchFFD():
            if rootD == "Not found":
                PatchStatusFFDr.config(text="Not installed")
            else:
                PatchStatusFFDr.config(text="Not Patched", fg="#cc0000")
            if os.access(os.path.normpath(rpCkFFD12.get() + "/config.js"), os.F_OK) and \
               os.access(os.path.normpath(rpCkFFD12.get() + "/defaults/pref/config-prefs.js"), os.F_OK):
                if os.access(os.path.normpath(rpCkFFD22.get() + "/chrome/utils"), os.F_OK):
                    PatchStatusFFDr.config(text="Patched", fg="#339900")
                else: 
                    PatchStatusFFDr.config(text="Profile not patched", fg="#cc0000")
            elif os.access(os.path.normpath(rpCkFFD22.get() + "/chrome/utils"), os.F_OK):
                PatchStatusFFDr.config(text="Root not patched", fg="#cc0000")

        def checkPatchFFN():
            if rootN == "Not found":
               PatchStatusFFNr.config(text="Not installed")
            else:
                PatchStatusFFNr.config(text="Not Patched", fg="#cc0000")
            if os.access(os.path.normpath(rpCkFFN12.get() + "/config.js"), os.F_OK) and \
               os.access(os.path.normpath(rpCkFFN12.get() + "/defaults/pref/config-prefs.js"), os.F_OK):
                if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/utils"), os.F_OK):
                    PatchStatusFFNr.config(text="Patched", fg="#339900")
                else: 
                    PatchStatusFFNr.config(text="Profile not patched", fg="#cc0000")
            elif os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/utils"), os.F_OK):
                PatchStatusFFNr.config(text="Root not patched", fg="#cc0000")

        # This method will call the required functions to patch the root and profile folders
        def patchInstall():
            Error = 0
            MRSettings = str(CkMR1E.get())
            FTSettings = str(CkFTDE.get())

            # This is the root patcher invoker
            def copyRFunctions(FFroot, FFVersion):
                Error = 0
                # We check for the root folder structure to exist
                if os.access(FFroot, os.F_OK) and \
                   os.access(os.path.normpath(FFroot
                                              + "/defaults/pref"), os.F_OK):
                   fullPatcher(FFroot, None)
                else:
                    Error = 1
                    errorMessage = FFVersion \
                        + "root folder location is wrong." \
                        + "\nSelect a valid one and try again."
                    messagebox.showerror("Error", errorMessage)
                return Error

            # This is the profile functions copying invoker
            def copyPFunctions(FFprofile, FFVersion):
                Error = 0
                # We check for the profile folder to exist
                if os.access(FFprofile, os.F_OK):
                    fullPatcher(None, FFprofile)

                    # We then check for function selections

                    # Multirow check
                    if CkMR.get() == 1:
                        # Multirow scrollable
                        if RdMR.get() == 0:
                            if CkMR1C.get() == 0:
                                Error += functionInstall(FFprofile,
                                                         "Multirow-scrollable",
                                                         MRSettings)
                            # Multirow autohide
                            else:
                                Error += functionInstall(FFprofile,
                                                         "Multirow-autohide",
                                                         MRSettings)
                        # If not scrollable, then unlimited
                        else:
                            Error += functionInstall(FFprofile,
                                                     "Multirow-unlimited")

                    # Tabs below
                    if CkTB.get() == 1:
                        if CkTB1.get() == 1:
                            Error += functionInstall(FFprofile,
                                            "Tabs-below-menu-over-tabs")
                        else:
                            Error += functionInstall(FFprofile,
                                                     "Tabs-below")

                    # Disable megabar resizing
                    if CkMB.get() == 1:
                        if CkMB1.get() == 1:
                            Error += functionInstall(FFprofile,
                                            "Megabar-all-resizing")
                        else:
                            Error += functionInstall(FFprofile,
                                            "Megabar-until-focus")

                    # Focus tabs on hover
                    if CkFT.get() == 1:
                        Error += functionInstall(FFprofile,
                                                 "Focus-tab",
                                                 FTSettings)

                    # Set unread state on tabs
                    if CkUT.get() == 1:
                        Error += functionInstall(FFprofile,
                                                 "Unread-state")
                else:
                    Error = 1
                    errorMessage = FFVersion \
                        + "profile folder location is wrong." \
                        + "\nSelect a valid one and try again."
                    messagebox.showerror("Error", errorMessage)
                return Error

            # We handle the choices below
            # v v v v v v v v v v v v v v v v v v v

            # This is the call for Firefox Stable functions
            if CkFF.get() == 1:
                FFVersion = "Firefox"
                FFroot = rpCkFF12.get()
                FFprofile = rpCkFF22.get()
                Error += copyRFunctions(FFroot, FFVersion)
                Error += copyPFunctions(FFprofile, FFVersion)

            # This is the call for Firefox Nightly functions
            if CkFFD.get() == 1:
                FFDVersion = "Firefox Developer"
                FFDroot = rpCkFFD12.get()
                FFDprofile = rpCkFFD22.get()
                Error += copyRFunctions(FFDroot, FFDVersion)
                Error += copyPFunctions(FFDprofile, FFDVersion)

            # This is the call for Firefox Nightly functions
            if CkFFN.get() == 1:
                FFNVersion = "Firefox Nightly"
                FFNroot = rpCkFFN12.get()
                FFNprofile = rpCkFFN22.get()
                Error += copyRFunctions(FFNroot, FFNVersion)
                Error += copyPFunctions(FFNprofile, FFNVersion)

            # This installs functions for each of the selected Profile folders
            if CkFFP.get() == 1:
                values = []
                for y in rpCkFFP1.curselection():
                    values.append(rpCkFFP1.get(y))

                if CkMR.get() == 0 and CkTB.get() == 0 and CkMB.get() == 0 \
                and CkFT.get() == 0 and CkUT.get() == 0:
                    messagebox.showerror("Nothing happened",
                                     "You need to select at least "
                                     + "one function to install.")

                for x in values:
                    FFPprofile = x
                    # We get the name of the profile here
                    if OSinUse == "Windows":
                        splitter = x.split("\\")
                        FFPVersion = splitter[-1].split(".")[-1]

                    else:
                        splitter = x.split("/")
                        FFPVersion = splitter[-1].split(".")[-1]

                    Error += copyPFunctions(FFPprofile, FFPVersion)

            if (CkFFP.get() == 0 and CkFFD.get() == 0 and CkFFN.get() == 0
                and CkFF.get() == 0) or \
                (CkFFP.get() == 1 and CkFFN.get() == 0 and CkFF.get() == 0
                and CkFFD.get() == 0 and values == []):
                messagebox.showerror("No profile selected",
                                     "You need to select at least "
                                     + "one profile to patch.")
            elif Error == 0:
                messagebox.showinfo("Patching complete",
                                    "The patching is complete."
                                    + "\nRestart Firefox for changes "
                                    + "to take effect.")

            checkPatchFF()
            checkPatchFFD()
            checkPatchFFN()

        # This method will call the required functions to remove the patch
        def patchRemove():
            if (CkFF.get() == 1 and CkFFD.get() == 0 and CkFFN.get() == 0) \
            or (CkFF.get() == 0 and CkFFD.get() == 1 and CkFFN.get() == 0) \
            or (CkFF.get() == 0 and CkFFD.get() == 0 and CkFFN.get() == 1):
                removeAll = messagebox.askyesno("Remove all?", 
                    "Do you want to remove all files installed "
                    + "(both the patch and the functions)?")
                if removeAll == False:
                    removeFunctions = messagebox.askyesno("Function removal", 
                    "Do you want to remove only the functions?.")
                    if removeFunctions == False:
                        return
            elif CkFF.get() == 1 and (CkFFN.get() == 1 or CkFFD.get() == 1):
                removeAll = messagebox.askyesno("Remove all", 
                    "This will remove all the patch files from the selected "
                    + "Firefox installations.\nIs that okay?")
                if removeAll == False:
                    removeFunctions = messagebox.askyesno("Function removal", 
                    "Do you want to only remove the functions?.")
                    if removeFunctions == False:
                        return
            elif CkFFP.get() == 1 and CkFF.get() == 0 and CkFFN.get() == 0 \
            and CkFFD.get() == 0:
                removeAll = False
            elif CkFFP.get() == 0 and not rpCkFFP1.curselection():
                messagebox.showerror("No option selected", 
                    "You need to select at least one Firefox installation"
                    + "\nor profile folder to remove it's installed patch.")
                return

            # We define some arrays to specify which ones will be deleted
            remRoot = []
            remProf = []

            if CkFF.get() == 1:
                remRoot.append(rpCkFF12.get())
                remProf.append(rpCkFF22.get())

            if CkFFD.get() == 1:
                remRoot.append(rpCkFFD12.get())
                remProf.append(rpCkFFD22.get())

            if CkFFN.get() == 1:
                remRoot.append(rpCkFFN12.get())
                remProf.append(rpCkFFN22.get())

            if CkFFP.get() == 1:
                for y in rpCkFFP1.curselection():
                    remProf.append(rpCkFFP1.get(y))

            if removeAll:
                for x in remRoot:
                    erasePatch(x, None)

                for z in remProf:
                    erasePatch(None, z)
            else:
                for z in remProf:
                    if CkMR.get() == 1:
                        functionRemove(z, "Multirow")

                    if CkTB.get() == 1:
                        functionRemove(z, "Tabs-below")

                    if CkMB.get() == 1:
                        functionRemove(z, "Megabar")

                    if CkFT.get() == 1:
                        functionRemove(z, "Focus-tab")

                    if CkUT.get() == 1:
                        functionRemove(z, "Unread-state")

            if CkFFP.get() == 1 and CkFFN.get() == 0 \
            and CkFF.get() == 0 and CkFFD.get() == 0:
                if remProf != []:
                    messagebox.showinfo("Unpatch complete", 
                        "Functions removed successfully.\n"
                        + "Restart firefox for changes to take effect.")
                else: 
                    messagebox.showwarning("No profile selected", 
                    "You need to select at least one profile folder.")
            else: 
                messagebox.showinfo("Unpatch complete", 
                "Patch files removed succesfully.\n"
                + "Restart firefox for changes to take effect.")

            checkPatchFF()
            checkPatchFFD()
            checkPatchFFN()

        # ------- UI drawing starts here -------

        # These are the outter frames of each section
        rootPatch = Frame(self, padx=30, pady=20)
        featurePatch = Frame(self, pady=20)

        # This part covers the rootPatch frame
        rpLb = Label(rootPatch, text="Choose what do you want to patch or unpatch:\n", font=("", 10, "bold"))
        rpLb.grid(column=0, row=0, columnspan=4, sticky="W")

        CkFF = tkinter.IntVar()
        rpCkFF = Checkbutton(rootPatch, text="Firefox", variable=CkFF,
                             command=updateFFChildren)
        rpCkFF.grid(column=0, row=1, columnspan=3, sticky="W")

        Label(rootPatch, text="        ").grid(column=0, row=2, sticky="w")
        rpCkFF1 = Label(rootPatch, text="Root: ", state="disabled")
        rpCkFF1.grid(column=1, row=2, sticky="E")
        rpCkFF12 = Entry(rootPatch, width=60)
        rpCkFF12.insert(0, root)
        rpCkFF12.config(state="disabled")
        rpCkFF12.grid(column=2, row=2, sticky="W")
        rpCkFF13 = Button(rootPatch, text="Select", width=7,
                          command=lambda:EntryUpdate("1"), state="disabled")
        rpCkFF13.grid(column=3, row=2, sticky="W", padx=3)

        Label(rootPatch, text="        ").grid(column=0, row=3, sticky="w")
        rpCkFF2 = Label(rootPatch, text="Profile: ", state="disabled")
        rpCkFF2.grid(column=1, row=3, sticky="E")
        rpCkFF22 = Entry(rootPatch)
        rpCkFF22.insert(0, RProfile)
        rpCkFF22.config(state="disabled")
        rpCkFF22.grid(column=2, row=3, sticky="WE")
        rpCkFF23 = Button(rootPatch, text="Select",
                          command=lambda:EntryUpdate("2"), state="disabled")
        rpCkFF23.grid(column=3, row=3, sticky="WE", padx=3)
        Label(rootPatch, text=" ").grid(column=4, row=4)

        CkFFD = tkinter.IntVar()
        rpCkFFD = Checkbutton(rootPatch, text="Firefox Developer",
                              variable=CkFFD, command=updateFFDChildren)
        rpCkFFD.grid(column=0, row=5, columnspan=3, sticky="W")

        Label(rootPatch, text="        ").grid(column=0, row=6, sticky="w")
        rpCkFFD1 = Label(rootPatch, text="Root: ", state="disabled")
        rpCkFFD1.grid(column=1, row=6, sticky="E")
        rpCkFFD12 = Entry(rootPatch, width=60)
        rpCkFFD12.insert(0, rootD)
        rpCkFFD12.config(state="disabled")
        rpCkFFD12.grid(column=2, row=6, sticky="W")
        rpCkFFD13 = Button(rootPatch, text="Select", width=7,
                           command=lambda:EntryUpdate("3"), state="disabled")
        rpCkFFD13.grid(column=3, row=6, sticky="W", padx=3)

        Label(rootPatch, text="        ").grid(column=0, row=7, sticky="w")
        rpCkFFD2 = Label(rootPatch, text="Profile: ", state="disabled")
        rpCkFFD2.grid(column=1, row=7, sticky="E")
        rpCkFFD22 = Entry(rootPatch)
        rpCkFFD22.insert(0, DProfile)
        rpCkFFD22.config(state="disabled")
        rpCkFFD22.grid(column=2, row=7, sticky="WE")
        rpCkFFD23 = Button(rootPatch, text="Select",
                           command=lambda:EntryUpdate("4"), state="disabled")
        rpCkFFD23.grid(column=3, row=7, sticky="WE", padx=3)
        Label(rootPatch, text=" ").grid(column=4, row=8)

        CkFFN = tkinter.IntVar()
        rpCkFFN = Checkbutton(rootPatch, text="Firefox Nightly",
                              variable=CkFFN, command=updateFFNChildren)
        rpCkFFN.grid(column=0, row=9, columnspan=3, sticky="W")

        Label(rootPatch, text="        ").grid(column=0, row=10, sticky="w")
        rpCkFFN1 = Label(rootPatch, text="Root: ", state="disabled")
        rpCkFFN1.grid(column=1, row=10, sticky="E")
        rpCkFFN12 = Entry(rootPatch)
        rpCkFFN12.insert(0, rootN)
        rpCkFFN12.config(state="disabled")
        rpCkFFN12.grid(column=2, row=10, sticky="WE")
        rpCkFFN13 = Button(rootPatch, text="Select",
                           command=lambda:EntryUpdate("5"), state="disabled")
        rpCkFFN13.grid(column=3, row=10, sticky="WE", padx=3)

        Label(rootPatch, text="        ").grid(column=0, row=11, sticky="w")
        rpCkFFN2 = Label(rootPatch, text="Profile: ", state="disabled")
        rpCkFFN2.grid(column=1, row=11, sticky="E")
        rpCkFFN22 = Entry(rootPatch)
        rpCkFFN22.insert(0, NProfile)
        rpCkFFN22.config(state="disabled")
        rpCkFFN22.grid(column=2, row=11, sticky="WE")
        rpCkFFN23 = Button(rootPatch, text="Select",
                           command=lambda:EntryUpdate("6"), state="disabled")
        rpCkFFN23.grid(column=3, row=11, sticky="WE", padx=3)
        Label(rootPatch, text=" ").grid(column=4, row=12)

        if root != "Not found":
            rpCkFF.select()
            rpCkFF1.config(state="normal")
            rpCkFF12.config(state="normal")
            rpCkFF13.config(state="normal")
            rpCkFF2.config(state="normal")
            rpCkFF22.config(state="normal")
            rpCkFF23.config(state="normal")
        if rootD != "Not found":
            rpCkFFD.select()
            rpCkFFD1.config(state="normal")
            rpCkFFD12.config(state="normal")
            rpCkFFD13.config(state="normal")
            rpCkFFD2.config(state="normal")
            rpCkFFD22.config(state="normal")
            rpCkFFD23.config(state="normal")
        if rootN != "Not found":
            rpCkFFN.select()
            rpCkFFN1.config(state="normal")
            rpCkFFN12.config(state="normal")
            rpCkFFN13.config(state="normal")
            rpCkFFN2.config(state="normal")
            rpCkFFN22.config(state="normal")
            rpCkFFN23.config(state="normal")

        CkFFP = tkinter.IntVar()
        rpCkFFP = Checkbutton(rootPatch, text="Profiles only* "
                              + "(Hold Ctrl or Shift to select more than one)",
                              variable=CkFFP, command=updateFFPChildren)
        rpCkFFP.grid(column=0, row=13, columnspan=3, sticky="W")

        rpCkFFP1 = Listbox(rootPatch, selectmode="extended")

        for y in range(len(Profiles)):
            rpCkFFP1.insert("end", Profiles[y])

        LBScrollbar = Scrollbar(rootPatch, orient="vertical",
                                command=rpCkFFP1.yview)
        rpCkFFP1.config(yscrollcommand=LBScrollbar.set, state="disabled")
        LBScrollbar.grid(column=4, row=14, sticky="NSW")

        rpCkFFP1.grid(column=1, row=14, columnspan=3, sticky="WE")
        rpDetail = Label(rootPatch,
            text="* You need to have patched Firefox root folder first "
                 + "with the 'Firefox', 'Firefox Developer' or\n'Firefox nightly' sections. "
                 + "These only patch the profile folders.",
            justify="left", state="disabled")
        rpDetail.grid(column=1, row=15, columnspan=4, sticky="W")
        Label(rootPatch, text=" ").grid(column=0, row=16)

        rpReset = Button(rootPatch, text="Reset folders", padx=10, pady=5,
                         command=EntryReset)
        rpReset.grid(column=0, row=17, sticky="W", columnspan=2)

        # This other part covers the featurePatch frame
        FPLF = LabelFrame(featurePatch, padx=20, pady=20,
                          text="Choose what functions you want to "
                               + "install/remove:",
                               font=("", 10, "bold"))
        FPLF.grid(column=0, row=0, columnspan=4)

        fpLb = Label(FPLF, text="You need to patch the Firefox version you "
                                + "have installed\nfor these changes to take effect."
                                + "\n('Profiles only' just copies the functions)\n")
        fpLb.grid(column=0, row=0, columnspan=4, sticky="WE")

        CkMR = tkinter.IntVar()
        CkMR1E = tkinter.IntVar()
        CkMR1C = tkinter.IntVar()
        RdMR = tkinter.IntVar()
        fpCkMR = Checkbutton(FPLF, text="Multi-row Tabs", variable=CkMR,
                             command=updateMRChildren)
        fpCkMR.grid(column=0, row=1, columnspan=4, sticky="W")
        fpCkMR1 = Radiobutton(FPLF, text="Scrollable rows", value=0,
                              variable=RdMR, command=updateMRSpinbox, 
                              state="disabled")
        fpCkMR1.grid(column=1, row=2, sticky="W")
        fpCkMR1E = Spinbox(FPLF, from_=2, to=10, textvariable=CkMR1E)
        fpCkMR1E.delete(0,"end")
        fpCkMR1E.insert(0, 3)
        fpCkMR1E.config(state="disabled")
        fpCkMR1E.grid(column=2, row=2, columnspan=1, sticky="WE")
        fpCkMR1C = Checkbutton(FPLF, text="Autohide scrollbars",
                               variable=CkMR1C, state="disabled")
        fpCkMR1C.grid(column=1, row=3, columnspan=2, padx=20, sticky="W")
        fpCkMR2 = Radiobutton(FPLF, text="All rows visible", value=1,
                              variable=RdMR, command=updateMRSpinbox,
                              state="disabled")
        fpCkMR2.grid(column=1, row=4, sticky="W")

        CkTB = tkinter.IntVar()
        CkTB1 = tkinter.IntVar()
        fpCkTB = Checkbutton(FPLF, text="Tabs below URL bar",
                             variable=CkTB, command=updateTBCheck)
        fpCkTB.grid(column=0, row=5, columnspan=3, sticky="W")
        fpCkTB1 = Checkbutton(FPLF, text="Menu right above tabs",
                              variable=CkTB1, state="disabled")
        fpCkTB1.grid(column=0, row=6, columnspan=3, padx=20, sticky="W")

        CkMB = tkinter.IntVar()
        CkMB1 = tkinter.IntVar()
        fpCkMB = Checkbutton(FPLF, text="Disable Megabar resize until focus",
                             variable=CkMB, command=updateMBCheck)
        fpCkMB.grid(column=0, row=7, columnspan=3, sticky="W")
        fpCkMB1 = Checkbutton(FPLF, text="Disable Megabar resize completelly",
                              variable=CkMB1, state="disabled")
        fpCkMB1.grid(column=0, row=8, columnspan=3, padx=20, sticky="W")

        CkFT = tkinter.IntVar()
        CkFTDE = tkinter.IntVar()
        fpCkFT = Checkbutton(FPLF, text="Focus Tab on hover",
                             variable=CkFT, command=updateFTChildren)
        fpCkFT.grid(column=0, row=9, columnspan=4, sticky="W")
        fpCkFTD = Label(FPLF, text="    Specify Delay (in ms)",
                        state="disabled")
        fpCkFTD.grid(column=0, row=10, columnspan=2, sticky="E", padx=10)
        fpCkFTDE = Spinbox(FPLF, from_=0, to=2000, textvariable=CkFTDE)
        fpCkFTDE.delete(0,"end")
        fpCkFTDE.insert(0, 200)
        fpCkFTDE.config(state="disabled")
        fpCkFTDE.grid(column=2, row=10, columnspan=2, sticky="W")

        CkUT = tkinter.IntVar()
        fpCkUT = Checkbutton(FPLF, text="Enable unread state on tabs*", 
                             variable=CkUT)
        fpCkUT.grid(column=0, row=11, columnspan=4, sticky="W")
        fpCkUTD = Label(FPLF, text="* Allows you to customize unread tabs"
                                   + " with userChrome.css\n"
                                   + "using the [unread] attribute",
                                   state="disabled")
        fpCkUTD.grid(column=0, row=12, columnspan=4, rowspan=2, 
                     sticky="E", padx=10)
        fpspacer3 = Label(FPLF, text="").grid(column=0, row=14, 
                                              sticky="w")

        fpfooter = Label(FPLF, text="For other functions:").grid(column=0, 
                                                                 row=15,
                                                                 columnspan=4,
                                                                 sticky="w")
        fpfooterL = Button(FPLF, text="Visit repository", cursor="hand2", 
                           command=callhome)
        fpfooterL.grid(column=0, row=16, columnspan=5, sticky="WE")

        PatchStats = LabelFrame(featurePatch, text="Patch status", padx=20)
        PatchStats.grid(column=0, row=1, pady=10, columnspan=4, sticky="WE")

        PatchStatusFF = Frame(PatchStats)
        PatchStatusFF.pack(side="top", fill="x", pady=6)
        FFChromeFolder = Button(PatchStatusFF, text="Open profile",
                                cursor="hand2",
                                command=lambda:openProfile(rpCkFF22.get()))
        FFChromeFolder.pack(side="right")
        PatchStatusFFl = Label(PatchStatusFF, text="Firefox:  ")
        PatchStatusFFl.pack(side="left")
        PatchStatusFFr = Label(PatchStatusFF)
        checkPatchFF()
        PatchStatusFFr.pack(side="left")

        PatchStatusFFD = Frame(PatchStats)
        PatchStatusFFD.pack(side="top", fill="x", pady=6)
        FFDChromeFolder = Button(PatchStatusFFD, text="Open profile",
                                cursor="hand2",
                                command=lambda:openProfile(rpCkFFD22.get()))
        FFDChromeFolder.pack(side="right")
        PatchStatusFFDl = Label(PatchStatusFFD, text="Developer:  ")
        PatchStatusFFDl.pack(side="left")
        PatchStatusFFDr = Label(PatchStatusFFD)
        checkPatchFFD()
        PatchStatusFFDr.pack(side="left")

        PatchStatusFFN = Frame(PatchStats)
        PatchStatusFFN.pack(side="bottom", fill="x", pady=10)
        FFNChromeFolder = Button(PatchStatusFFN, text="Open profile", 
                                 cursor="hand2",
                                 command=lambda:openProfile(rpCkFFN22.get()))
        FFNChromeFolder.pack(side="right")
        PatchStatusFFNl = Label(PatchStatusFFN, text="Nightly: ")
        PatchStatusFFNl.pack(side="left")
        PatchStatusFFNr = Label(PatchStatusFFN)
        checkPatchFFN()
        PatchStatusFFNr.pack(side="left")

        PatchButton = Button(featurePatch, text="Patch", cursor="hand2",
                             pady=5, padx=5, command=patchInstall)
        PatchButton.grid(column=0, row=2, pady=10, columnspan=2, padx=5,
                         sticky="WE")
        unPatchButton = Button(featurePatch, text="Remove Patch",
                               cursor="hand2", pady=5, padx=5,
                               command=patchRemove)
        unPatchButton.grid(column=2, row=2, columnspan=2, padx=5,
                           sticky="WE")

        rootPatch.grid(column=0, row=0)
        featurePatch.grid(column=1, row=0, padx=30, sticky="W")


def UIStart():
    "Starts the window interface"

    QNWindow = tkinter.Tk()
    QNWindow.resizable(False, False)
    if OSinUse == "Windows":
        QNWindow.iconbitmap(os.path.normpath(sys._MEIPASS + '/icon.ico'))
    else:
        logo = PhotoImage(file=os.path.normpath(sys._MEIPASS + '/icon.gif'))
        QNWindow.call('wm', 'iconphoto', QNWindow._w, logo)
    app = patcherUI()
    QNWindow.title("Quantum Nox - Firefox Patcher")
    QNWindow.mainloop()


# We add command line arguments support here
parser = argparse.ArgumentParser()

# We define some default variables here
developerIsDefault = (os.access(rootD, os.F_OK) and
                      not os.access(rootN, os.F_OK) and
                      not os.access(root, os.F_OK))
devOverNightly = (os.access(rootD, os.F_OK) and
                  os.access(rootN, os.F_OK) and
                  not os.access(root, os.F_OK))
nightlyIsDefault = (os.access(rootN, os.F_OK) and
                    not os.access(root, os.F_OK) and
                    not os.access(rootD, os.F_OK))

if developerIsDefault or devOverNightly:
    defaultCLRoot = rootD
    defaultCLProfile = DProfile
elif nightlyIsDefault:
    defaultCLRoot = rootN
    defaultCLProfile = NProfile
else:
    defaultCLRoot = root
    defaultCLProfile = RProfile

# Firefox path arguments
parser.add_argument("-r", "--root",
                    help="Specify the root path of your Firefox installation."
                    + " Accepts 'stable', 'nightly', or a custom path.",
                    default=defaultCLRoot)
parser.add_argument("-p", "--profile",
                    help="Specify the Firefox profile path to patch."
                    + " Accepts 'stable', 'nightly', or a custom path.",
                    default=defaultCLProfile)

# Multirow arguments
parser.add_argument("-mr", "--multirow",
                    help="Installs scrollable multirow tabs "
                    + "(3 scrollable rows by default).",
                    action="store_true")

parser.add_argument("-mrv", "--multirow-version",
                    help="Changes the version to install of multirow tabs. "
                    + "Acceptable values: "
                    + "1 (Scrollable rows), 2 (Autohiding scrollbars),"
                    + " 3 (Unlimited rows). ",
                    type=int, choices=[1, 2, 3], default=1)

parser.add_argument("-mro", "--multirow-options",
                    help="Changes the number of rows to display in multirow. "
                    + "Acceptable values: any number (3 to 10 recommended)",
                    type=int, default=3)

# Tabs below arguments
parser.add_argument("-tb", "--tabs-below",
                    help="Installs tabs below function "
                    + "(Tabs below with titlebar on top by default).",
                    action="store_true")
parser.add_argument("-tbv", "--tabs-below-version",
                    help="Changes the options of tabs below. "
                    + "Acceptable values: "
                    + "1 (titlebar on top), 2 (titlebar above tabs).",
                    type=int, choices=[1, 2], default=1)

# Megabar resize disabler arguments
parser.add_argument("-mb", "--megabar",
                    help="Installs the megabar resize disabler function "
                    + "(Disables the resizing until focusing the megabar by default).",
                    action="store_true")
parser.add_argument("-mbv", "--megabar-version",
                    help="Changes the options of megabar resize disabler. "
                    + "Acceptable values: "
                    + "1 (Disable resize until focus), 2 (Disable resizing completelly).",
                    type=int, choices=[1, 2], default=1)

# Focus tab on hover arguments
parser.add_argument("-ft", "--focus-tab",
                    help="Enables focusing tabs on mouseover "
                    + "(200ms delay by default).",
                    action="store_true")

parser.add_argument("-fto", "--focus-tab-options",
                    help="Set the delay of the tab focus.",
                    type=int, default=200)

# Focus tab on hover arguments
parser.add_argument("-us", "--unread-state",
                    help="Enables 'unread' state of tabs to be able to "
                    + "customize unread but loaded tabs with userChrome.css.",
                    action="store_true")

# Remove arguments
parser.add_argument("-rm", "--remove",
                    help="Installer set on removal mode." +
                    " Any function specified will be deleted.",
                    action="store_true")
parser.add_argument("-rma", "--remove-all",
                    help="Both the patch and all functions installed in the "
                    + "specified root and profile folders will be deleted."
                    + " If no folders are specified, stable release paths "
                    + "will be selected by default",
                    action="store_true")

# Print paths argument
parser.add_argument("-pd", "--print-defaults",
                    help="Shows the default paths found by the patcher.",
                    action="store_true")

# Verbosity argument
parser.add_argument("-s", "--silent",
                    help="Prevents non-error messages to be printed.",
                    action="store_true")

CLArgs = parser.parse_args()

# We check if any installing or removal argument was given
argumentsInUse = (CLArgs.multirow or CLArgs.unread_state
                  or CLArgs.focus_tab or CLArgs.tabs_below
                  or CLArgs.megabar or CLArgs.remove
                  or CLArgs.remove_all)

# We set the actions for command line arguments here
if CLArgs.root:
    if CLArgs.root.capitalize() == "Stable":
        CLArgs.root = root
    elif CLArgs.root.capitalize() == "Developer":
        CLArgs.root = rootD
    elif CLArgs.root.capitalize() == "Nightly":
        CLArgs.root = rootN
    if not os.access(CLArgs.root, os.F_OK) and argumentsInUse:
        print("The root path " + CLArgs.root + " was incorrect.")
        sys.exit()
    if not CLArgs.silent and argumentsInUse:
        print("Using " + CLArgs.root + " as root path.")
if CLArgs.profile:
    if CLArgs.root.capitalize() == "Stable":
        CLArgs.profile = RProfile
    elif CLArgs.root.capitalize() == "Developer":
        CLArgs.root = DProfile
    elif CLArgs.root.capitalize() == "Nightly":
        CLArgs.profile = NProfile
    if not os.access(CLArgs.profile, os.F_OK) and argumentsInUse:
        print("The profile path " + CLArgs.profile + " was incorrect.")
        sys.exit()
    if not CLArgs.silent and argumentsInUse:
        print("Using " + CLArgs.profile + " as profile path.")

# Errors control variable
CLError = 0

# First we check for remove modes
if CLArgs.remove_all:
    CLError += erasePatch(CLArgs.root, CLArgs.profile)
    CLError += functionRemove(CLArgs.profile, "Multirow")
    CLError += functionRemove(CLArgs.profile, "Tabs-below")
    CLError += functionRemove(CLArgs.profile, "Megabar")
    CLError += functionRemove(CLArgs.profile, "Focus-tab")
    CLError += functionRemove(CLArgs.profile, "Unread-state")
    if not CLArgs.silent and CLError == 0:
        print("All patch files were removed")
elif CLArgs.remove:
    if CLArgs.multirow:
        CLError += functionRemove(CLArgs.profile, "Multirow")
        if not CLArgs.silent and CLError == 0:
            print("Multirow uninstalled.")
    if CLArgs.tabs_below:
        CLError += functionRemove(CLArgs.profile, "Tabs-below")
        if not CLArgs.silent and CLError == 0:
            print("Tabs below uninstalled.")
    if CLArgs.megabar:
        CLError += functionRemove(CLArgs.profile, "Megabar")
        if not CLArgs.silent and CLError == 0:
            print("Megabar resize disabler uninstalled.")
    if CLArgs.focus_tab:
        CLError += functionRemove(CLArgs.profile, "Focus-tab")
        if not CLArgs.silent and CLError == 0:
            print("Focus tab on hover uninstalled.")
    if CLArgs.unread_state:
        CLError += functionRemove(CLArgs.profile, "Unread-state")
        if not CLArgs.silent and CLError == 0:
            print("Unread state tagging uninstalled.")

# If none of the remove modes are specified, we enter
# install mode
else:
    # We first make sure that the profile and root
    # folders are patched
    if argumentsInUse:
        fullPatcher(CLArgs.root, CLArgs.profile)

    # Then we start installing the functions
    if CLArgs.multirow:
        CLError = 0
        CLMRRows = str(CLArgs.multirow_options)
        if CLArgs.multirow_version == 1:
            CLMRVersion = "Multirow-scrollable"
        elif CLArgs.multirow_version == 2:
            CLMRVersion = "Multirow-autohide"
        else:
            CLMRVersion = "Multirow-unlimited"
        CLError += functionInstall(CLArgs.profile,
                                   CLMRVersion,
                                   CLMRRows)
        if not CLArgs.silent and CLError == 0:
            print("Multirow installed.")

    if CLArgs.tabs_below:
        CLError = 0
        if CLArgs.tabs_below_version == 1:
            CLTBVersion = "Tabs-below"
        else:
            CLTBVersion = "Tabs-below-menu-over-tabs"
        CLError += functionInstall(CLArgs.profile,
                                   CLTBVersion)
        if not CLArgs.silent and CLError == 0:
            print("Tabs below installed.")

    if CLArgs.megabar:
        CLError = 0
        if CLArgs.megabar_version == 1:
            CLTBVersion = "Megabar-until-focus"
        else:
            CLTBVersion = "Megabar-all-resizing"
        CLError += functionInstall(CLArgs.profile,
                                   CLTBVersion)
        if not CLArgs.silent and CLError == 0:
            print("Megabar resize disabler installed.")

    if CLArgs.focus_tab:
        CLError = 0
        CLFTDelay = str(CLArgs.focus_tab_options)
        CLError += functionInstall(CLArgs.profile,
                                   "Focus-tab",
                                   CLFTDelay)
        if not CLArgs.silent and CLError == 0:
            print("Focus tab on hover installed.")

    if CLArgs.unread_state:
        CLError = 0
        CLError += functionInstall(CLArgs.profile,
                                   "Unread-state")
        if not CLArgs.silent and CLError == 0:
            print("Unread state tagging installed.")

# For debugging purposes
if CLArgs.print_defaults:
    print("Firefox stable:")
    print(" - Root: " + root)
    print(" - Profile: " + RProfile)
    print("\nFirefox developer:")
    print(" - Root: " + rootD)
    print(" - Profile: " + DProfile)
    print("\nFirefox Nightly:")
    print(" - Root: " + rootN)
    print(" - Profile: " + NProfile)
    sys.exit()

# GUI initializator
if __name__ == '__main__' and not argumentsInUse:
    UIStart()
