import os
import re
import sys
import glob
import ctypes
import shutil
import tkinter
import elevate
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

if SystemOS() == "Linux":
    if os.geteuid() != 0:
        os.execvp("sudo", ["sudo"] + sys.argv)
else: elevate.elevate()

def readProfiles(profile):
    "Fetches the profile folders"

    ProfilesINI = os.path.normpath(profile + "/profiles.ini")
    Paths = []
    if not os.access(ProfilesINI, os.F_OK):
        if SystemOS() == "Windows" or SystemOS() == "Mac":
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
                    if (((SystemOS() == "Windows" or SystemOS() == "Mac") and
                        rotationpath[0:9] == "Profiles/") or
                        SystemOS() == "Linux" and rotationpath[0] != "/"):
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
                defaultspath = re.match("default=(.*)", line, re.M|re.I)
                if defaultspath != None:
                    defaultrotation = defaultspath.group(1)
                    if (((SystemOS() == "Windows" or SystemOS() == "Mac") and
                        defaultrotation[0:9] == "Profiles/") or
                        SystemOS() == "Linux" and defaultrotation[0] != "/"):
                        Paths.append(os.path.normpath(profile + "/" + defaultspath.group(1)))
                    else:
                        Paths.append(os.path.normpath(defaultspath.group(1)))
        return Paths

# We get the user folders here
if SystemOS() == "Windows":
    nonRootUser = os.path.join(os.getenv('PUBLIC') + "\\QNUsername.txt")
    if os.access(nonRootUser, os.F_OK):
        with open(nonRootUser, "r") as f:
            logUsername = f.read()
        logUsername = logUsername.rstrip(" \n")
        home = logUsername
        os.remove(nonRootUser)
    else:
        home = os.getenv('APPDATA')
    MozPFolder = home + r"\Mozilla\Firefox"
    Profiles = readProfiles(MozPFolder)
    SFolder = home + r'\Quantum Nox'
elif SystemOS() == "Linux":
    home = "/home/" + os.getenv("SUDO_USER")
    MozPFolder = home + r"/.mozilla/firefox"
    Profiles = readProfiles(MozPFolder)
    SFolder = home + r"/.Quantum Nox"
elif SystemOS() == "Mac":
    home = str(Path.home())
    MozPFolder = home + r"/Library/Application Support/Firefox"
    Profiles = readProfiles(MozPFolder)
    SFolder = home + r"/Quantum Nox"

# We get the default folder where programs are installed here
if SystemOS() == "Windows":
    PFolder = r"C:\Program Files"
    if os.access(PFolder, os.F_OK) == False:
        PFolder = ""
elif SystemOS() == "Linux" or SystemOS() == "Unknown":
    PFolder = r"/usr/lib"
    if os.access(PFolder, os.F_OK) == False:
        PFolder = ""
elif SystemOS() == "Mac":
    PFolder = r"/Applications/"
    if os.access(PFolder, os.F_OK) == False:
        PFolder = ""

# We get the default folders for each installation here
if SystemOS() == "Windows":
    root = r"C:\Program Files (x86)\Mozilla Firefox"
    rootN = r"C:\Program Files (x86)\Firefox Nightly"
    if os.access(root, os.F_OK) == False:
        root = r"C:\Program Files\Mozilla Firefox"
        if os.access(root, os.F_OK) == False:
            root = "Not found"
    if os.access(rootN, os.F_OK) == False:
        rootN = r"C:\Program Files (x86)\Firefox Nightly"
        if os.access(rootN, os.F_OK) == False:
            rootN = r"C:\Program Files\Firefox Nightly"
            if os.access(rootN, os.F_OK) == False:
                rootN = "Not found"
elif SystemOS() == "Linux" or SystemOS() == "Unknown":
    root = r"/usr/lib/firefox/"
    rootN = r"/usr/lib/firefoxnightly/"
    if os.access(root, os.F_OK) == False:
        root = r"/usr/lib64/firefox/"
        if os.access(root, os.F_OK) == False:
            rootN = "Not found"
    if os.access(rootN, os.F_OK) == False:
        rootN = r"/usr/lib64/firefoxnightly/"
        if os.access(rootN, os.F_OK) == False:
            rootN = "Not found"
elif SystemOS() == "Mac":
    root = r"/Applications/Firefox.app/contents/resources"
    rootN = r"/Applications/FirefoxNightly.app/contents/resources"
    if os.access(root, os.F_OK) == False:
            root = "Not found"
    if os.access(rootN, os.F_OK) == False:
            rootN = "Not found"

# We get the default user folders here
NProfile = "Not found"
RProfile = "Not found"
DefProfiles = readDefaults(MozPFolder)

def RPFinder():
    for x in DefProfiles:
        splitter = x.split(".")
        ProfileName = splitter[-1]
        if ProfileName == "default-release":
            return x
        elif ProfileName == "default":
            return x
        elif ProfileName[0:7] == "default":
            return x
        else:
            continue
    return "Not found"

def NPFinder():
    for y in DefProfiles:
        Nsplitter = y.split(".")
        ProfileName = Nsplitter[-1]
        if ProfileName == "default-nightly":
            return y
        elif ProfileName[0:15] == "default-nightly":
            return y
        else:
            continue
    return "Not found"

RProfile = RPFinder()
NProfile = NPFinder()

if DefProfiles == None:
    if root != "Not found" or rootN != "Not found":
        for x in Profiles:
            splitter = x.split(".")
            ProfileName = splitter[-1]
            if ProfileName == "default-nightly":
                NProfile = x
            elif ProfileName == "default-release":
                RProfile = x
            elif ProfileName == "default":
                RProfile = x
            elif ProfileName[0:15] == "default-nightly":
                NProfile = x
            elif ProfileName[0:7] == "default":
                RProfile = x

        if RProfile == "Not found":
            if len(Profiles) == 1 and root != "Not found" and rootN == "Not found":
                RProfile = Profiles[0]

        if NProfile == "Not found":
            if len(Profiles) == 1 and rootN != "Not found" and root == "Not found":
                NProfile = Profiles[0]

def fullPatcher(FFversion, FFprofile):
    "This method patches both the root and profile folders"
    try:
        if FFversion != "None":
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

            if SystemOS() == "Linux":
                rootUser = os.getenv("SUDO_USER")
                shutil.chown(ConfPref, user=rootUser, group=rootUser)
                shutil.chown(ConfJS, user=rootUser, group=rootUser)

        if FFprofile != "None":

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

            if SystemOS() == "Linux":
                chrome = FFprofile + "/chrome"
                utils = chrome + "/utils"
                rootUser = os.getenv("SUDO_USER")
                utilFiles = glob.glob(utils + "/*.*")
                shutil.chown(chrome, user=rootUser, group=rootUser)
                shutil.chown(utils, user=rootUser, group=rootUser)
                for file in utilFiles:
                    shutil.chown(file, user=rootUser, group=rootUser)

    except IOError:
        messagebox.showerror("Error", "You need higher privileges to apply the patch.")

def erasePatch(FFversion, FFprofile):
    "This method removes the patch from both the root and profile folders"
    try:
        if FFversion != "None":
            # We patch the root folder here
            if os.access(os.path.normpath(FFversion + "/config.js"), os.F_OK) and \
            os.access(os.path.normpath(FFversion + "/defaults/pref/config-prefs.js"), os.F_OK):

                os.remove(os.path.normpath(FFversion + "/defaults/pref/config-prefs.js"))
                os.remove(os.path.normpath(FFversion + "/config.js"))

            elif os.access(os.path.normpath(FFversion + "/config.js"), os.F_OK) or \
            os.access(os.path.normpath(FFversion + "/defaults/pref/config-prefs.js"), os.F_OK):

                if os.access(os.path.normpath(FFversion + "/config.js"), os.F_OK):
                    os.remove(os.path.normpath(FFversion + "/config.js"))

                else: os.remove(os.path.normpath(FFversion + "/defaults/pref/config-prefs.js"))

        if FFprofile != "None":

            # We patch the profile folder here
            if os.access(os.path.normpath(FFprofile + "/chrome/utils"), os.F_OK):
                if os.access(os.path.normpath(FFprofile + "/chrome/utils/boot.jsm"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile + "/chrome/utils/boot.jsm"))
                if os.access(os.path.normpath(FFprofile + "/chrome/utils/chrome.manifest"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile + "/chrome/utils/chrome.manifest"))
                if os.access(os.path.normpath(FFprofile + "/chrome/utils/RDFDataSource.jsm"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile + "/chrome/utils/RDFDataSource.jsm"))
                if os.access(os.path.normpath(FFprofile + "/chrome/utils/RDFManifestConverter.jsm"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile + "/chrome/utils/RDFManifestConverter.jsm"))
                if os.access(os.path.normpath(FFprofile + "/chrome/utils/userChrome.jsm"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile + "/chrome/utils/userChrome.jsm"))
                if os.access(os.path.normpath(FFprofile + "/chrome/utils/xPref.jsm"), os.F_OK):
                    os.remove(os.path.normpath(FFprofile + "/chrome/utils/xPref.jsm"))

                utilChromeFiles = []
                for r, d, f in os.walk(os.path.normpath(FFprofile + "/chrome/utils")):
                    for file in f:
                            utilChromeFiles.append(os.path.join(r, file))
                if utilChromeFiles == []:
                    os.rmdir(os.path.normpath(FFprofile + "/chrome/utils"))

    except IOError:
        messagebox.showerror("Error", "You need higher privileges to remove the patch.")

def callhome():
    "This method opens the repository page"
    webbrowser.open_new(r"https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Other%20features")

def openProfile(profileFolder):
    if os.access(profileFolder, os.F_OK) == True:
        chromeFolder = os.path.normpath(profileFolder + "/chrome")
        if os.access(chromeFolder, os.F_OK) == True:
            webbrowser.open(chromeFolder)
        else: 
            messagebox.showerror("Error", 
            "Couldn't locate the profile chrome folder.\nSelect a valid one and try again.")
    else: 
        messagebox.showerror("Error", 
        "Couldn't locate the profile folder.\nSelect a valid one and try again.")

class patcherUI(Frame):
    "This class creates the UI of the patcher"

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.pack(expand=True, fill="both")

        # These methods update the entries when looking for a root/profile folder
        def EntryUpdate(SelButton):
            if SelButton == "1" or SelButton == "3":
                SelDir = os.path.normpath(filedialog.askdirectory(initialdir=PFolder))

            elif SelButton == "2" or SelButton == "4":
                SelDir = os.path.normpath(filedialog.askdirectory(initialdir=MozPFolder))
            
            if SelDir != "" and SelDir != ".":
                if SelButton == "1":
                    rpCkFF12.delete(0, "end")
                    rpCkFF12.insert(0, SelDir)

                elif SelButton == "2":
                    rpCkFF22.delete(0, "end")
                    rpCkFF22.insert(0, SelDir)

                elif SelButton == "3":
                    rpCkFFN12.delete(0, "end")
                    rpCkFFN12.insert(0, SelDir)

                elif SelButton == "4":
                    rpCkFFN22.delete(0, "end")
                    rpCkFFN22.insert(0, SelDir)

                checkPatchFF()
                checkPatchFFN()

        def EntryReset():
            disState=False
            if rpCkFF12["state"] == "disabled":
                rpCkFF12.config(state="normal")
                disState=True

            rpCkFF12.delete(0, "end")
            rpCkFF12.insert(0, root)

            if disState == True:
                rpCkFF12.config(state="disabled")
                disState=False

            if rpCkFF22["state"] == "disabled":
                rpCkFF22.config(state="normal")
                disState=True

            rpCkFF22.delete(0, "end")
            rpCkFF22.insert(0, RProfile)

            if disState == True:
                rpCkFF22.config(state="disabled")
                disState=False

            if rpCkFFN12["state"] == "disabled":
                rpCkFFN12.config(state="normal")
                disState=True

            rpCkFFN12.delete(0, "end")
            rpCkFFN12.insert(0, rootN)

            if disState == True:
                rpCkFFN12.config(state="disabled")
                disState=False

            if rpCkFFN22["state"] == "disabled":
                rpCkFFN22.config(state="normal")
                disState=True

            rpCkFFN22.delete(0, "end")
            rpCkFFN22.insert(0, NProfile)

            if disState == True:
                rpCkFFN22.config(state="disabled")
                disState=False

            checkPatchFF()
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
            if os.access(os.path.normpath(rpCkFF12.get() + "/config.js"), os.F_OK) == True and \
               os.access(os.path.normpath(rpCkFF12.get() + "/defaults/pref/config-prefs.js"), os.F_OK):
                if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/utils"), os.F_OK) == True:
                    PatchStatusFFr.config(text="Patched", fg="#339900")
                else: 
                    PatchStatusFFr.config(text="Profile not patched", fg="#cc0000")
            elif os.access(os.path.normpath(rpCkFF22.get() + "/chrome/utils"), os.F_OK) == True:
                PatchStatusFFr.config(text="Root not patched", fg="#cc0000")

        def checkPatchFFN():
            if rootN == "Not found":
               PatchStatusFFNr.config(text="Not installed")
            else:
                PatchStatusFFNr.config(text="Not Patched", fg="#cc0000")
            if os.access(os.path.normpath(rpCkFFN12.get() + "/config.js"), os.F_OK) == True and \
               os.access(os.path.normpath(rpCkFFN12.get() + "/defaults/pref/config-prefs.js"), os.F_OK):
                if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/utils"), os.F_OK) == True:
                    PatchStatusFFNr.config(text="Patched", fg="#339900")
                else: 
                    PatchStatusFFNr.config(text="Profile not patched", fg="#cc0000")
            elif os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/utils"), os.F_OK) == True:
                PatchStatusFFNr.config(text="Root not patched", fg="#cc0000")

        def writeMR(FireFile):
            with open(FireFile, "r+") as f:
                s = f.read()
                s = s.replace("TABROWS", str(CkMR1E.get()))
                f.seek(0,0)
                f.write(s)
                f.truncate()

        def writeFT(FireFile):
            with open(FireFile, "r+") as f:
                s = f.read()
                s = s.replace("DELAYTIME", str(CkFTDE.get()))
                f.seek(0,0)
                f.write(s)
                f.truncate()

        # This method will call the required functions to patch the root and profile folders
        def patchInstall():
            Error = 0
            FFChrome = os.path.normpath(rpCkFF22.get() + "/chrome")
            FFNChrome = os.path.normpath(rpCkFFN22.get() + "/chrome")

            FireMR = os.path.normpath(sys._MEIPASS + "/functions/MultiRowTab-scrollable.uc.js")
            FireMRL = os.path.normpath(sys._MEIPASS + "/functions/MultiRowTabLiteforFx.uc.js")
            FireMRA = os.path.normpath(sys._MEIPASS + "/functions/MultiRowTab-scrollable-autohide.uc.js")
            FireTB = os.path.normpath(sys._MEIPASS + "/functions/Tabs-below.as.css")
            FireTBoT = os.path.normpath(sys._MEIPASS + "/functions/Tabs-below-Menu-overTabs.as.css")
            FireFT = os.path.normpath(sys._MEIPASS + "/functions/Focus-tab-on-hover.uc.js")
            FireUT = os.path.normpath(sys._MEIPASS + "/functions/setAttribute_unread.uc.js")

            FFUT = os.path.normpath(rpCkFF22.get() + "/chrome/setAttribute_unread.uc.js")
            FFTB = os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below.as.css")
            FFFT = os.path.normpath(rpCkFF22.get() + "/chrome/Focus-tab-on-hover.uc.js")
            FFTBoT = os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below-Menu-overTabs.as.css")
            FFTBaA = os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below-Menu-onTop.as.css")

            FFNUT = os.path.normpath(rpCkFFN22.get() + "/chrome/setAttribute_unread.uc.js")
            FFNTB = os.path.normpath(rpCkFFN22.get() + "/chrome/Tabs-below.as.css")
            FFNFT = os.path.normpath(rpCkFFN22.get() + "/chrome/Focus-tab-on-hover.uc.js")
            FFNTBoT = os.path.normpath(rpCkFFN22.get() + "/chrome/Tabs-below-Menu-overTabs.as.css")
            FFNTBaA = os.path.normpath(rpCkFFN22.get() + "/chrome/Tabs-below-Menu-onTop.as.css")

            if SystemOS() == "Linux":
                rootUser = os.getenv("SUDO_USER")
                functionFiles = glob.glob(FFChrome + "/*.*")
                functionFilesN = glob.glob(FFNChrome + "/*.*")

            # We define the common multi-row choice patching here
            def MRpatch(FFversion):
                Error = 0
                try:
                    if FFversion == "Stable":
                        FFChrome = os.path.normpath(rpCkFF22.get() + "/chrome")
                        FFCMR = os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollable.uc.js")
                        FFCMRL = os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTabLiteforFx.uc.js")
                        FFCMRA = os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollable-autohide.uc.js")

                        FFCMR71 = os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollableFF71.uc.js")
                        FFCMRL71 = os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTabLiteforFF71.uc.js")
                        FFCMRA71 = os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js")

                    elif FFversion == "Nightly":
                        FFChrome = os.path.normpath(rpCkFFN22.get() + "/chrome")
                        FFCMR = os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollable.uc.js")
                        FFCMRL = os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTabLiteforFx.uc.js")
                        FFCMRA = os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollable-autohide.uc.js")

                        FFCMR71 = os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollableFF71.uc.js")
                        FFCMRL71 = os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTabLiteforFF71.uc.js")
                        FFCMRA71 = os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js")

                    elif FFversion == "Profiles":
                        FFChrome = os.path.normpath(x + "/chrome")
                        FFCMR = os.path.normpath(x + "/chrome/MultiRowTab-scrollable.uc.js")
                        FFCMRL = os.path.normpath(x + "/chrome/MultiRowTabLiteforFx.uc.js")
                        FFCMRA = os.path.normpath(x + "/chrome/MultiRowTab-scrollable-autohide.uc.js")

                        FFCMR71 = os.path.normpath(x + "/chrome/MultiRowTab-scrollableFF71.uc.js")
                        FFCMRL71 = os.path.normpath(x + "/chrome/MultiRowTabLiteforFF71.uc.js")
                        FFCMRA71 = os.path.normpath(x + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js")

                    if RdMR.get() == 0:

                        if CkMR1C.get() == 0:
                            distutils.file_util.copy_file(FireMR, FFChrome)

                            if os.access(FFCMRA, os.F_OK) == True:
                                os.remove(FFCMRA)
                            try:
                                writeMR(FFCMR)
                                if SystemOS() == "Linux":
                                    shutil.chown(FFCMR, user=rootUser, group=rootUser)

                            except IOError:
                                Error = 1
                                messagebox.showwarning("Write access error", 
                                    "There was a problem while trying to write Multi-row scrollable.")
                                if os.access(FFCMR, os.F_OK) == True:
                                    os.remove(FFCMR)

                        if CkMR1C.get() == 1:
                            distutils.file_util.copy_file(FireMRA, FFChrome)

                            if os.access(FFCMR, os.F_OK) == True:
                                os.remove(FFCMR)
                            try:
                                writeMR(FFCMRA)
                                if SystemOS() == "Linux":
                                    shutil.chown(FFCMRA, user=rootUser, group=rootUser)

                            except IOError:
                                Error = 1
                                messagebox.showwarning("Write access error", 
                                    "There was a problem while trying to write Multi-row autohide.")
                                if os.access(FFCMRA, os.F_OK) == True:
                                    os.remove(FFCMRA)

                        if os.access(FFCMR71, os.F_OK) == True:
                                os.remove(FFCMR71)

                        if os.access(FFCMRA71, os.F_OK) == True:
                                os.remove(FFCMRA71)

                        if os.access(FFCMRL, os.F_OK) == True:
                            os.remove(FFCMRL)

                        if os.access(FFCMRL71, os.F_OK) == True:
                            os.remove(FFCMRL71)

                    else:
                        distutils.file_util.copy_file(FireMRL, FFChrome)

                        if os.access(FFCMRL71, os.F_OK) == True:
                            os.remove(FFCMRL71)

                        try:
                            writeMR(FFCMRL)
                            if SystemOS() == "Linux":
                                    shutil.chown(FFCMRL, user=rootUser, group=rootUser)

                        except IOError:
                            Error = 1
                            messagebox.showwarning("Write access error", 
                                "There was a problem while trying to write Multi-row unlimited.")
                            if os.access(FFCMRL, os.F_OK) == True:
                                os.remove(FFCMRL)

                        if os.access(FFCMR, os.F_OK) == True:
                            os.remove(FFCMR)

                        if os.access(FFCMR71, os.F_OK) == True:
                            os.remove(FFCMR71)

                        if os.access(FFCMRA, os.F_OK) == True:
                            os.remove(FFCMRA)

                        if os.access(FFCMRA71, os.F_OK) == True:
                            os.remove(FFCMRA71)

                except IOError:
                    Error = 1
                    messagebox.showwarning("Warning", 
                        "Couldn't manage to install Multi-row Tabs function.")

            # We handle the rest of choices here
            if CkFF.get() == 1:
                if os.access(rpCkFF12.get(), os.F_OK) == True and \
                   os.access(os.path.normpath(rpCkFF12.get() + "/defaults/pref"), os.F_OK) == True:
                   fullPatcher(rpCkFF12.get(), "None")
                else: 
                    Error = 1
                    messagebox.showerror("Error", 
                        "Firefox root folder location is wrong.\nSelect a valid one and try again.")
                    return

                if os.access(rpCkFF22.get(), os.F_OK) == True:
                    fullPatcher("None", rpCkFF22.get())

                    if CkMR.get() == 1:

                        MRpatch("Stable")

                    if CkTB.get() == 1:
                        try: 
                            if CkTB1.get() == 1:
                                distutils.file_util.copy_file(FireTBoT, FFChrome, update=True)
                                if SystemOS() == "Linux":
                                    shutil.chown(FFTBoT, user=rootUser, group=rootUser)

                                if os.access(FFTB, os.F_OK):
                                    os.remove(FFTB)

                            else:
                                distutils.file_util.copy_file(FireTB, FFChrome, update=True)
                                if SystemOS() == "Linux":
                                    shutil.chown(FFTB, user=rootUser, group=rootUser)

                                if os.access(FFTBoT, os.F_OK):
                                    os.remove(FFTBoT)

                            if os.access(FFTBaA, os.F_OK):
                                os.remove(FFTBaA)
                        except IOError:
                            Error = 1
                            messagebox.showwarning("Warning", 
                                "Couldn't manage to install Tabs Below function.")

                    if CkFT.get() == 1:
                        try:
                            distutils.file_util.copy_file(FireFT, FFChrome, update=True)

                            writeFT(FFFT)

                            if SystemOS() == "Linux":
                                    shutil.chown(FFFT, user=rootUser, group=rootUser)

                        except IOError:
                            Error = 1
                            messagebox.showwarning("Warning", 
                                "Couldn't manage to install Focus Tab on hover function.")

                    if CkUT.get() == 1:
                        try:
                            distutils.file_util.copy_file(FireUT, FFChrome, update=True)
                            if SystemOS() == "Linux":
                                    shutil.chown(FFUT, user=rootUser, group=rootUser)

                        except IOError:
                            Error = 1
                            messagebox.showwarning("Warning", 
                                "Couldn't manage to enable unread state on tabs.")

                else: 
                    Error = 1
                    messagebox.showerror("Error", 
                        "Firefox profile folder location is wrong.\nSelect a valid one and try again.")
                    return


            if CkFFN.get() == 1:
                if os.access(rpCkFFN12.get(), os.F_OK) == True and \
                   os.access(os.path.normpath(rpCkFFN12.get() + "/defaults/pref"), os.F_OK) == True:
                   fullPatcher(rpCkFFN12.get(), "None")
                else: 
                    Error = 1
                    messagebox.showerror("Error", 
                        "Nightly root folder location is wrong.\nSelect a valid one and try again.")
                    return

                if os.access(rpCkFFN22.get(), os.F_OK) == True:
                    fullPatcher("None", rpCkFFN22.get())

                    if CkMR.get() == 1:
                        MRpatch("Nightly")

                    if CkTB.get() == 1:
                        try: 
                            if CkTB1.get() == 1:
                                distutils.file_util.copy_file(FireTBoT, FFNChrome, update=True)

                                if SystemOS() == "Linux":
                                    shutil.chown(FFNTBoT, user=rootUser, group=rootUser)

                                if os.access(FFNTB, os.F_OK):
                                    os.remove(FFNTB)

                            else:
                                distutils.file_util.copy_file(FireTB, FFNChrome, update=True)

                                if SystemOS() == "Linux":
                                    shutil.chown(FFNTB, user=rootUser, group=rootUser)

                                if os.access(FFNTBoT, os.F_OK):
                                    os.remove(FFNTBoT)

                            if os.access(FFNTBaA, os.F_OK):
                                os.remove(FFNTBaA)
                        except IOError:
                            Error = 1
                            messagebox.showwarning("Warning", 
                                "Couldn't manage to install Tabs Below function.")

                    if CkFT.get() == 1:
                        try:
                            distutils.file_util.copy_file(FireFT, FFNChrome, update=True)

                            writeFT(FFNFT)

                            if SystemOS() == "Linux":
                                    shutil.chown(FFNFT, user=rootUser, group=rootUser)

                        except IOError:
                            Error = 1
                            messagebox.showwarning("Warning", 
                                "Couldn't manage to install Focus Tab on hover function.")

                    if CkUT.get() == 1:
                        try:
                            distutils.file_util.copy_file(FireUT, FFNChrome, update=True)

                            if SystemOS() == "Linux":
                                    shutil.chown(FFNUT, user=rootUser, group=rootUser)

                        except IOError:
                            Error = 1
                            messagebox.showwarning("Warning", 
                                "Couldn't manage to enable unread state on tabs.")
                else: 
                    Error = 1
                    messagebox.showerror("Error", 
                        "Firefox profile folder location is wrong.\nSelect a valid one and try again.")
                    return

            if CkFFP.get() == 1:
                values = []
                for y in rpCkFFP1.curselection():
                    values.append(rpCkFFP1.get(y))
                
                for x in values:
                    FFChrome = os.path.normpath(x + "/chrome")

                    FFUT = os.path.normpath(x + "/chrome/setAttribute_unread.uc.css")
                    FFTB = os.path.normpath(x + "/chrome/Tabs-below.as.css")
                    FFFT = os.path.normpath(x + "/chrome/Focus-tab-on-hover.uc.js")
                    FFTBoT = os.path.normpath(x + "/chrome/Tabs-below-Menu-overTabs.as.css")
                    FFTBaA = os.path.normpath(x + "/chrome/Tabs-below-Menu-onTop.as.css")

                    if SystemOS() == "Windows":
                        splitter = x.split("\\")
                        selectedProfile = splitter[-1]

                    else: 
                        splitter = x.split("/")
                        selectedProfile = splitter[-1]

                    if os.access(x, os.F_OK) == True:
                        fullPatcher("None", x)

                        if CkMR.get() == 1:
                            MRpatch("Profiles")

                        if CkTB.get() == 1:
                            try: 
                                if CkTB1.get() == 1:
                                    distutils.file_util.copy_file(FireTBoT, FFChrome, update=True)

                                    if SystemOS() == "Linux":
                                            shutil.chown(FFTBoT, user=rootUser, group=rootUser)

                                    if os.access(FFTB, os.F_OK):
                                        os.remove(FFTB)

                                else:
                                    distutils.file_util.copy_file(FireTB, FFChrome, update=True)

                                    if SystemOS() == "Linux":
                                            shutil.chown(FFTB, user=rootUser, group=rootUser)

                                    if os.access(FFTBoT, os.F_OK):
                                        os.remove(FFTBoT)

                                if os.access(FFTBaA, os.F_OK):
                                        os.remove(FFTBaA)
                            except IOError:
                                Error = 1
                                messagebox.showwarning("Warning", 
                                    "Couldn't manage to install Tabs Below function.")

                        if CkFT.get() == 1:
                            try:
                                distutils.file_util.copy_file(FireFT, FFChrome, update=True)

                                writeFT(FFFT)

                                if SystemOS() == "Linux":
                                            shutil.chown(FFFT, user=rootUser, group=rootUser)

                            except IOError:
                                Error = 1
                                messagebox.showwarning("Warning", 
                                    "Couldn't manage to install Focus Tab on hover function.")

                        if CkUT.get() == 1:
                            try:
                                distutils.file_util.copy_file(FireUT, FFChrome, update=True)

                                if SystemOS() == "Linux":
                                            shutil.chown(FFUT, user=rootUser, group=rootUser)

                            except IOError:
                                Error = 1
                                messagebox.showwarning("Warning", 
                                    "Couldn't manage to enable unread state on tabs.")

                    else: 
                        Error = 1
                        messagebox.showerror("Error", 
                            "Couldn't access the selected profile.\nIt was either deleted or moved.")
            
            if (CkFFP.get() == 0 and CkFFN.get() == 0 and CkFF.get() == 0) or \
               (CkFFP.get() == 1 and CkFFN.get() == 0 and CkFF.get() == 0 and values == []):
                messagebox.showerror("Nothing happened", 
                    "You need to select at least one profile to patch.")
            elif Error != 1:
                messagebox.showinfo("Patching complete", 
                    "The patching is complete.\nRestart Firefox for changes to take effect.")

            checkPatchFF()
            checkPatchFFN()

        # This method will call the required functions to remove the patch
        def patchRemove():
            if (CkFF.get() == 1 and CkFFN.get() == 0) or (CkFF.get() == 0 and CkFFN.get() == 1):
                removeAll = messagebox.askyesno("Remove all?", 
                    "Do you want to remove all files installed (both the patch and the functions)?")
                if removeAll == False:
                    removeFunctions = messagebox.askyesno("Function removal", 
                    "Do you want to remove only the functions?.")
                    if removeFunctions == False:
                        return
            elif CkFF.get() == 1 and CkFFN.get() == 1:
                removeAll = messagebox.askyesno("Remove all", 
                    "This will remove all the patch files from the selected Firefox installations.\nIs that okay?")
                if removeAll == False:
                    removeFunctions = messagebox.askyesno("Function removal", 
                    "Do you want to remove only the functions?.")
                    if removeFunctions == False:
                        return
            elif CkFFP.get() == 0 and not rpCkFFP1.curselection():
                messagebox.showerror("No option selected", 
                    "You need to select at least one Firefox installation\nor profile folder to remove it's installed patch.")
                return

            if CkFF.get() == 1:
                if removeAll:
                    erasePatch(rpCkFF12.get(), rpCkFF22.get())

                if CkMR.get() == 1:
                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollable.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollable.uc.js"))

                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollableFF71.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollableFF71.uc.js"))

                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTabLiteforFx.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTabLiteforFx.uc.js"))

                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTabLiteforFF71.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTabLiteforFF71.uc.js"))

                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollable-autohide.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollable-autohide.uc.js"))

                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js"))

                if CkTB.get() == 1:
                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below.as.css"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below.as.css"))
                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below-Menu-onTop.as.css"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below-Menu-onTop.as.css"))
                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below-Menu-overTabs.as.css"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below-Menu-overTabs.as.css"))

                if CkFT.get() == 1:
                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/Focus-tab-on-hover.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/Focus-tab-on-hover.uc.js"))

                if CkUT.get() == 1:
                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/setAttribute_unread.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/setAttribute_unread.uc.js"))

            if CkFFN.get() == 1:
                if removeAll == True:
                    erasePatch(rpCkFFN12.get(), rpCkFFN22.get())

                if CkMR.get() == 1:
                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollable.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollable.uc.js"))

                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollableFF71.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollableFF71.uc.js"))

                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTabLiteforFx.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTabLiteforFx.uc.js"))

                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTabLiteforFF71.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTabLiteforFF71.uc.js"))

                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollable-autohide.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollable-autohide.uc.js"))

                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js"))

                if CkTB.get() == 1:
                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/Tabs-below.as.css"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/Tabs-below.as.css"))

                if CkFT.get() == 1:
                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/Focus-tab-on-hover.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/Focus-tab-on-hover.uc.js"))

                if CkUT.get() == 1:
                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/setAttribute_unread.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/setAttribute_unread.uc.js"))

            if CkFFP.get() == 1:
                values = []
                for y in rpCkFFP1.curselection():
                    values.append(rpCkFFP1.get(y))
                
                for x in values:
                    if CkMR.get() == 1:
                        if os.access(os.path.normpath(x + "/chrome/MultiRowTab-scrollable.uc.js"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/MultiRowTab-scrollable.uc.js"))

                        if os.access(os.path.normpath(x + "/chrome/MultiRowTab-scrollableFF71.uc.js"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/MultiRowTab-scrollableFF71.uc.js"))

                        if os.access(os.path.normpath(x + "/chrome/MultiRowTabLiteforFx.uc.js"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/MultiRowTabLiteforFx.uc.js"))

                        if os.access(os.path.normpath(x + "/chrome/MultiRowTabLiteforFF71.uc.js"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/MultiRowTabLiteforFF71.uc.js"))

                        if os.access(os.path.normpath(x + "/chrome/MultiRowTab-scrollable-autohide.uc.js"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/MultiRowTab-scrollable-autohide.uc.js"))

                        if os.access(os.path.normpath(x + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js"))

                    if CkTB.get() == 1:
                        if os.access(os.path.normpath(x + "/chrome/Tabs-below.as.css"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/Tabs-below.as.css"))
                        if os.access(os.path.normpath(x + "/chrome/Tabs-below-Menu-onTop.as.css"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/Tabs-below-Menu-onTop.as.css"))
                        if os.access(os.path.normpath(x + "/chrome/Tabs-below-Menu-overTabs.as.css"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/Tabs-below-Menu-overTabs.as.css"))

                    if CkFT.get() == 1:
                        if os.access(os.path.normpath(x + "/chrome/Focus-tab-on-hover.uc.js"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/Focus-tab-on-hover.uc.js"))

                    if CkUT.get() == 1:
                        if os.access(os.path.normpath(x + "/chrome/setAttribute_unread.uc.js"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/setAttribute_unread.uc.js"))

            if CkFFP.get() == 1 and CkFFN.get() == 0 and CkFF.get() == 0:
                if values != []:
                    messagebox.showinfo("Unpatch complete", 
                        "Functions removed successfully.\nRestart firefox for changes to take effect.")
                else: 
                    messagebox.showwarning("No profile selected", 
                    "You need to select at least one profile folder.")
            else: 
                messagebox.showinfo("Unpatch complete", 
                "Patch files removed succesfully.\nRestart firefox for changes to take effect.")

            checkPatchFF()
            checkPatchFFN()

        # ------- UI drawing starts here -------

        # These are the outter frames of each section
        rootPatch = Frame(self, padx=30, pady=20)
        featurePatch = Frame(self, pady=20)

        # This part covers the rootPatch frame
        rpLb = Label(rootPatch, text="Choose what do you want to patch or unpatch:\n", font=("", 10, "bold"))
        rpLb.grid(column=0, row=0, columnspan=4, sticky="W")

        CkFF = tkinter.IntVar()
        rpCkFF = Checkbutton(rootPatch, text="Firefox", variable=CkFF, command=updateFFChildren)
        rpCkFF.grid(column=0, row=1, columnspan=3, sticky="W")

        rpCkFF01 = Label(rootPatch, text="        ").grid(column=0, row=2, sticky="w")
        rpCkFF1 = Label(rootPatch, text="Root: ", state="disabled")
        rpCkFF1.grid(column=1, row=2, sticky="E")
        rpCkFF12 = Entry(rootPatch, width=60)
        rpCkFF12.insert(0, root)
        rpCkFF12.config(state="disabled")
        rpCkFF12.grid(column=2, row=2, sticky="W")
        rpCkFF13 = Button(rootPatch, text="Select", width=7, command=lambda:EntryUpdate("1"), state="disabled")
        rpCkFF13.grid(column=3, row=2, sticky="W", padx=3)

        rpCkFF02 = Label(rootPatch, text="        ").grid(column=0, row=3, sticky="w")
        rpCkFF2 = Label(rootPatch, text="Profile: ", state="disabled")
        rpCkFF2.grid(column=1, row=3, sticky="E")
        rpCkFF22 = Entry(rootPatch)
        rpCkFF22.insert(0, RProfile)
        rpCkFF22.config(state="disabled")
        rpCkFF22.grid(column=2, row=3, sticky="WE")
        rpCkFF23 = Button(rootPatch, text="Select", command=lambda:EntryUpdate("2"), state="disabled")
        rpCkFF23.grid(column=3, row=3, sticky="WE", padx=3)
        rpSpacer = Label(rootPatch, text=" ").grid(column=4, row=4)

        CkFFN = tkinter.IntVar()
        rpCkFFN = Checkbutton(rootPatch, text="Firefox Nightly", variable=CkFFN, command=updateFFNChildren)
        rpCkFFN.grid(column=0, row=5, columnspan=3, sticky="W")

        rpCkFF03 = Label(rootPatch, text="        ").grid(column=0, row=6, sticky="w")
        rpCkFFN1 = Label(rootPatch, text="Root: ", state="disabled")
        rpCkFFN1.grid(column=1, row=6, sticky="E")
        rpCkFFN12 = Entry(rootPatch)
        rpCkFFN12.insert(0, rootN)
        rpCkFFN12.config(state="disabled")
        rpCkFFN12.grid(column=2, row=6, sticky="WE")
        rpCkFFN13 = Button(rootPatch, text="Select", command=lambda:EntryUpdate("3"), state="disabled")
        rpCkFFN13.grid(column=3, row=6, sticky="WE", padx=3)

        rpCkFF04 = Label(rootPatch, text="        ").grid(column=0, row=7, sticky="w")
        rpCkFFN2 = Label(rootPatch, text="Profile: ", state="disabled")
        rpCkFFN2.grid(column=1, row=7, sticky="E")
        rpCkFFN22 = Entry(rootPatch)
        rpCkFFN22.insert(0, NProfile)
        rpCkFFN22.config(state="disabled")
        rpCkFFN22.grid(column=2, row=7, sticky="WE")
        rpCkFFN23 = Button(rootPatch, text="Select", command=lambda:EntryUpdate("4"), state="disabled")
        rpCkFFN23.grid(column=3, row=7, sticky="WE", padx=3)
        rpSpacer2 = Label(rootPatch, text=" ").grid(column=4, row=8)

        if root != "Not found":
            rpCkFF.select()
            rpCkFF1.config(state="normal")
            rpCkFF12.config(state="normal")
            rpCkFF13.config(state="normal")
            rpCkFF2.config(state="normal")
            rpCkFF22.config(state="normal")
            rpCkFF23.config(state="normal")
        if rootN != "Not found":
            rpCkFFN.select()
            rpCkFFN1.config(state="normal")
            rpCkFFN12.config(state="normal")
            rpCkFFN13.config(state="normal")
            rpCkFFN2.config(state="normal")
            rpCkFFN22.config(state="normal")
            rpCkFFN23.config(state="normal")

        CkFFP = tkinter.IntVar()
        rpCkFFP = Checkbutton(rootPatch, text="Profiles only* (Hold Ctrl or Shift to select more than one)", variable=CkFFP, command=updateFFPChildren)
        rpCkFFP.grid(column=0, row=9, columnspan=3, sticky="W")

        rpCkFFP1 = Listbox(rootPatch, selectmode="extended")

        for y in range(len(Profiles)):
            rpCkFFP1.insert("end", Profiles[y])

        LBScrollbar = Scrollbar(rootPatch, orient="vertical", command=rpCkFFP1.yview)
        rpCkFFP1.config(yscrollcommand=LBScrollbar.set, state="disabled")
        LBScrollbar.grid(column=4, row=10, sticky="NSW")

        rpCkFFP1.grid(column=1, row=10, columnspan=3, sticky="WE")
        rpDetail = Label(rootPatch, 
            text="* You need to have patched Firefox root folder first with the 'Firefox' or 'Firefox nightly'\nsections. These only patch the profile folders.", 
            justify="left", state="disabled")
        rpDetail.grid(column=1, row=11, columnspan=4, sticky="W")
        rpSpacer3 = Label(rootPatch, text=" ").grid(column=0, row=12)

        rpReset = Button(rootPatch, text="Reset folders", padx=10, pady=5, command=EntryReset)
        rpReset.grid(column=0, row=13, sticky="W", columnspan=2)

        # This other part covers the featurePatch frame
        FPLF = LabelFrame(featurePatch, padx=20, pady=20, text="Choose what functions you want to install/remove:", font=("", 10, "bold"))
        FPLF.grid(column=0, row=0, columnspan=4)

        fpLb = Label(FPLF, text="You need to patch the Firefox version you have installed\nfor these changes to take effect.\n('Profiles only' just copies the functions)\n")
        fpLb.grid(column=0, row=0, columnspan=4, sticky="WE")

        CkMR = tkinter.IntVar()
        CkMR1E = tkinter.IntVar()
        CkMR1C = tkinter.IntVar()
        RdMR = tkinter.IntVar()
        fpCkMR = Checkbutton(FPLF, text="Multi-row Tabs", variable=CkMR, command=updateMRChildren)
        fpCkMR.grid(column=0, row=1, columnspan=4, sticky="W")
        fpCkMR1 = Radiobutton(FPLF, text="Scrollable rows", value=0, variable=RdMR, command=updateMRSpinbox, state="disabled")
        fpCkMR1.grid(column=1, row=2, sticky="W")
        fpCkMR1E = Spinbox(FPLF, from_=2, to=10, textvariable=CkMR1E)
        fpCkMR1E.delete(0,"end")
        fpCkMR1E.insert(0, 3)
        fpCkMR1E.config(state="disabled")
        fpCkMR1E.grid(column=2, row=2, columnspan=1, sticky="WE")
        fpCkMR1C = Checkbutton(FPLF, text="Autohide", variable=CkMR1C, state="disabled")
        fpCkMR1C.grid(column=1, row=3, columnspan=2, padx=20, sticky="W")
        fpCkMR2 = Radiobutton(FPLF, text="All rows visible", value=1, variable=RdMR, command=updateMRSpinbox, state="disabled")
        fpCkMR2.grid(column=1, row=4, sticky="W")

        CkTB = tkinter.IntVar()
        CkTB1 = tkinter.IntVar()
        fpCkTB = Checkbutton(FPLF, text="Tabs below URL bar", variable=CkTB, command=updateTBCheck)
        fpCkTB.grid(column=0, row=5, columnspan=3, sticky="W")
        fpCkTB1 = Checkbutton(FPLF, text="Menu right above tabs", variable=CkTB1, state="disabled")
        fpCkTB1.grid(column=0, row=6, columnspan=3, padx=20, sticky="W")

        CkFT = tkinter.IntVar()
        CkFTDE = tkinter.IntVar()
        fpCkFT = Checkbutton(FPLF, text="Focus Tab on hover", variable=CkFT, command=updateFTChildren)
        fpCkFT.grid(column=0, row=7, columnspan=4, sticky="W")
        fpCkFTD = Label(FPLF, text="    Specify Delay (in ms)", state="disabled")
        fpCkFTD.grid(column=0, row=8, columnspan=2, sticky="E", padx=10)
        fpCkFTDE = Spinbox(FPLF, from_=0, to=2000, textvariable=CkFTDE)
        fpCkFTDE.delete(0,"end")
        fpCkFTDE.insert(0, 200)
        fpCkFTDE.config(state="disabled")
        fpCkFTDE.grid(column=2, row=8, columnspan=2, sticky="W")

        CkUT = tkinter.IntVar()
        fpCkUT = Checkbutton(FPLF, text="Enable unread state on tabs*", variable=CkUT)
        fpCkUT.grid(column=0, row=10, columnspan=4, sticky="W")
        fpCkUTD = Label(FPLF, text="* Allows you to customize unread tabs with userChrome.css\n using the [unread] attribute", state="disabled")
        fpCkUTD.grid(column=0, row=11, columnspan=4, rowspan=2, sticky="E", padx=10)
        fpspacer3 = Label(FPLF, text="").grid(column=0, row=13, sticky="w")

        fpfooter = Label(FPLF, text="For other functions:").grid(column=0, row=14, columnspan=4, sticky="w")
        fpfooterL = Button(FPLF, text="Visit repository", cursor="hand2", command=callhome)
        fpfooterL.grid(column=0, row=15, columnspan=5, sticky="WE")

        PatchStats = LabelFrame(featurePatch, text="Patch status", padx=20)
        PatchStats.grid(column=0, row=1, pady=10, columnspan=4, sticky="WE")

        PatchStatusFF = Frame(PatchStats)
        PatchStatusFF.pack(side="top", fill="x", pady=6)
        FFChromeFolder = Button(PatchStatusFF, text="Open profile", cursor="hand2", command=lambda:openProfile(rpCkFF22.get()))
        FFChromeFolder.pack(side="right")
        PatchStatusFFl = Label(PatchStatusFF, text="Firefox:  ")
        PatchStatusFFl.pack(side="left")
        PatchStatusFFr = Label(PatchStatusFF)
        checkPatchFF()
        PatchStatusFFr.pack(side="left")
        
        PatchStatusFFN = Frame(PatchStats)
        PatchStatusFFN.pack(side="bottom", fill="x", pady=10)
        FFNChromeFolder = Button(PatchStatusFFN, text="Open profile", cursor="hand2", command=lambda:openProfile(rpCkFFN22.get()))
        FFNChromeFolder.pack(side="right")
        PatchStatusFFNl = Label(PatchStatusFFN, text="Nightly: ")
        PatchStatusFFNl.pack(side="left")
        PatchStatusFFNr = Label(PatchStatusFFN)
        checkPatchFFN()
        PatchStatusFFNr.pack(side="left")

        PatchButton = Button(featurePatch, text="Patch", cursor="hand2", pady=5, padx=5, command=patchInstall)
        PatchButton.grid(column=0, row=2, pady=10, columnspan=2, padx=5, sticky="WE")
        unPatchButton = Button(featurePatch, text="Remove Patch", cursor="hand2", pady=5, padx=5, command=patchRemove)
        unPatchButton.grid(column=2, row=2, columnspan=2, padx=5, sticky="WE")

        rootPatch.grid(column=0, row=0)
        featurePatch.grid(column=1, row=0, padx=30, sticky="W")

def UIStart():

    QNWindow = tkinter.Tk()
    QNWindow.resizable(False, False)
    if SystemOS() == "Windows":
        QNWindow.iconbitmap(os.path.normpath(sys._MEIPASS + '/icon.ico'))
    else:
        logo = PhotoImage(file=os.path.normpath(sys._MEIPASS + '/icon.gif'))
        QNWindow.call('wm', 'iconphoto', QNWindow._w, logo)
    app = patcherUI()
    QNWindow.title("Quantum Nox - Firefox Patcher")
    QNWindow.mainloop()

if __name__ == '__main__':
    UIStart()