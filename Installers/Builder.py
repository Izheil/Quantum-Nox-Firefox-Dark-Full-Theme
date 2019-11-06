import os
import re
import sys
import ctypes
import shutil
import tkinter
import elevate
import webbrowser
import distutils.core
from pathlib import Path
from tkinter import LabelFrame, Checkbutton, Frame, Label, Entry, filedialog, Button, Listbox, Radiobutton, Spinbox, Scrollbar, messagebox, PhotoImage

elevate.elevate()

def SystemOS():
    "Identifies the OS"

    if sys.platform.startswith('win') or sys.platform.endswith('win'):
        SystemOS = "Windows"
    elif sys.platform.startswith('linux'):
        SystemOS = "Linux"
    elif sys.platform.startswith('darwin'):
        SystemOS = "Mac"
    else: SystemOS = "Unknown"
    return SystemOS

# We get the user folders here
if SystemOS() == "Windows":
    home = os.environ['APPDATA']
    MozPFolder = home + r"\Mozilla\Firefox\Profiles"
    Profiles = os.listdir(MozPFolder)
    SFolder = home + r'\Quantum Nox'
elif SystemOS() == "Linux":
    home = str(Path.home())
    MozPFolder = home + r"/.mozilla/firefox"
    Profiles = os.listdir(MozPFolder)
    SFolder = home + r"/.Quantum Nox"
elif SystemOS() == "Mac":
    home = str(Path.home())
    MozPFolder = home + r"/Application Support/Firefox/Profiles"
    Profiles = os.listdir(MozPFolder)
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

# We get the user folders here
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
            if os.access(root, os.F_OK) == False:
                rootN = "Not found"
elif SystemOS() == "Linux" or SystemOS() == "Unknown":
    root = r"/usr/lib/firefox/browser"
    rootN = r"/usr/lib/firefoxnightly/browser"
    if os.access(root, os.F_OK) == False:
        root = r"/usr/lib64/firefox/browser"
        if os.access(root, os.F_OK) == False:
            rootN = "Not found"
    if os.access(rootN, os.F_OK) == False:
        root = r"/usr/lib64/firefoxnightly/browser"
        if os.access(root, os.F_OK) == False:
            rootN = "Not found"
elif SystemOS() == "Mac":
    root = r"/Applications/Firefox.app/content/resources"
    rootN = r"/Applications/FirefoxNightly.app/content/resources"

PrFols = []
for x in Profiles:
    PrFols.append(os.path.normpath(MozPFolder + "/" + x))

# We get the default folders for each installation here
if root != "Not found" or rootN != "Not found":
    NProfile = "Not found"
    RProfile = "Not found"
    for x in PrFols:
        if x[-8:] == "-nightly":
            NProfile = x
        elif x[-8:] == ".default":
            RProfile = x

def fullPatcher(FFversion, FFprofile):
    "This method patches both the root and profile folders"
    try:
        if FFversion != "None":
            # We patch the root folder here
            if os.access(os.path.normpath(FFversion + "/config.js"), os.F_OK) and \
            os.access(os.path.normpath(FFversion + "/defaults/pref/config-prefs.js"), os.F_OK):

                distutils.file_util.copy_file(os.path.normpath(sys._MEIPASS + "/root/defaults/pref/config-prefs.js"), 
                                              os.path.normpath(FFversion + "/defaults/pref/"), update=True)
                distutils.file_util.copy_file(os.path.normpath(sys._MEIPASS + "/root/config.js"), FFversion, update=True)

            elif os.access(os.path.normpath(FFversion + "/config.js"), os.F_OK) or \
            os.access(os.path.normpath(FFversion + "/defaults/pref/config-prefs.js"), os.F_OK):

                if os.access(os.path.normpath(FFversion + "/config.js"), os.F_OK):
                    shutil.copy2(os.path.normpath(sys._MEIPASS + "/root/defaults/pref/config-prefs.js"), os.path.normpath(FFversion + "/defaults/pref/"))

                else: shutil.copy2(os.path.normpath(sys._MEIPASS + "/root/config.js"), FFversion)

            else: 
                shutil.copy2(os.path.normpath(sys._MEIPASS + "/root/config.js"), FFversion)
                shutil.copy2(os.path.normpath(sys._MEIPASS + "/root/defaults/pref/config-prefs.js"), os.path.normpath(FFversion + "/defaults/pref/"))

        if FFprofile != "None":

            # We patch the profile folder here
            if os.access(os.path.normpath(FFprofile + "/chrome/utils"), os.F_OK):
                utilFiles = []
                for r, d, f in os.walk(os.path.normpath(os.getcwd() + "/utils")):
                    for file in f:
                            utilFiles.append(os.path.join(r, file))
                for file in utilFiles:
                    distutils.file_util.copy_file(file, os.path.normpath(FFprofile + "/chrome/utils"), update=True)

            else: 
                shutil.copytree(os.path.normpath(sys._MEIPASS + "/utils"), os.path.normpath(FFprofile + "/chrome/utils"))
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

                os.remove(os.path.normpath(FFprofile + "/chrome/utils/boot.jsm"))
                os.remove(os.path.normpath(FFprofile + "/chrome/utils/chrome.manifest"))
                os.remove(os.path.normpath(FFprofile + "/chrome/utils/RDFDataSource.jsm"))
                os.remove(os.path.normpath(FFprofile + "/chrome/utils/RDFManifestConverter.jsm"))
                os.remove(os.path.normpath(FFprofile + "/chrome/utils/userChrome.jsm"))
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
    webbrowser.open_new(r"https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions")

def openProfile(profileFolder):
    if os.access(profileFolder, os.F_OK) == True:
        chromeFolder = os.path.normpath(profileFolder + "/chrome")
        if os.access(chromeFolder, os.F_OK) == True:
            webbrowser.open(chromeFolder)
        else: messagebox.showerror("Error", "Couldn't locate the profile chrome folder.\nSelect a valid one and try again.")
    else: messagebox.showerror("Error", "Couldn't locate the profile folder.\nSelect a valid one and try again.")

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
            elif CkFFP.get() == 1:
                rpCkFFP1.config(state="normal")

        def updateMRChildren():
            if CkMR.get() == 0:
                fpCkMR1.config(state="disabled")
                fpCkMR2.config(state="disabled")
                fpCkMR1E.config(state="disabled")
            elif CkMR.get() == 1:
                fpCkMR1.config(state="normal")
                fpCkMR2.config(state="normal")
                fpCkMR1E.config(state="normal")

        def updateMRSpinbox():
            if RdMR.get() == 1:
                fpCkMR1E.config(state="disabled")
            elif RdMR.get() == 0:
                fpCkMR1E.config(state="normal")

        def updateFTChildren():
            if CkFT.get() == 0:
                fpCkFTD.config(state="disabled")
                fpCkFTDE.config(state="disabled")
            elif CkFT.get() == 1:
                fpCkFTD.config(state="normal")
                fpCkFTDE.config(state="normal")

        # We check the patch status with these methods
        def checkPatchFF():
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

            FFChrome = os.path.normpath(rpCkFF22.get() + "/chrome")
            FFNChrome = os.path.normpath(rpCkFFN22.get() + "/chrome")

            Fire71MR = os.path.normpath(sys._MEIPASS + "/functions/MultiRowTab-scrollableFF71.uc.js")
            FireMR = os.path.normpath(sys._MEIPASS + "/functions/MultiRowTab-scrollable.uc.js")
            FireTB = os.path.normpath(sys._MEIPASS + "/functions/Tabs-below.as.css")
            FireFT = os.path.normpath(sys._MEIPASS + "/functions/Focus-tab-on-hover.uc.js")

            FFCMR = os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollable.uc.js")
            FFCMR71 = os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTab-scrollableFF71.uc.js")

            FFCMRL = os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTabLiteforFx.uc.js")
            FFCMRL71 = os.path.normpath(rpCkFF22.get() + "/chrome/MultiRowTabLiteforFF71.uc.js")

            FFNCMR = os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollable.uc.js")
            FFNCMR71 = os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTab-scrollableFF71.uc.js")

            FFNCMRL = os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTabLiteforFx.uc.js")
            FFNCMRL71 = os.path.normpath(rpCkFFN22.get() + "/chrome/MultiRowTabLiteforFF71.uc.js")

            if CkFF.get() == 1:
                if os.access(rpCkFF12.get(), os.F_OK) == True and \
                   os.access(os.path.normpath(rpCkFF12.get() + "/defaults/pref"), os.F_OK) == True:
                   fullPatcher(rpCkFF12.get(), "None")
                else: 
                    messagebox.showerror("Error", "Firefox root folder location is wrong.\nSelect a valid one and try again.")
                    return

                if os.access(rpCkFF22.get(), os.F_OK) == True:
                    fullPatcher("None", rpCkFF22.get())

                    if CkMR.get() == 1:
                        FF71 = messagebox.askyesno("Firefox 71 prompt", "Is your current Firefox version 71 or above?")
                        try:
                            if FF71 == True:
                                distutils.file_util.copy_file(Fire71MR, FFChrome)

                                if os.access(FFCMR, os.F_OK) == True:
                                    os.remove(FFCMR)

                                writeMR(FFCMR71)

                            else:
                                distutils.file_util.copy_file(FireMR, FFChrome)

                                if os.access(FFCMR71, os.F_OK) == True:
                                    os.remove(FFCMR71)

                                writeMR(FFCMR)

                            if os.access(FFCMRL, os.F_OK) == True:
                                os.remove(FFCMRL)

                            if os.access(FFCMRL71, os.F_OK) == True:
                                os.remove(FFCMRL71)

                        except IOError:
                            messagebox.showwarning("Warning", "Couldn't manage to install Multi-row Tabs function.")

                    if CkTB.get() == 1:
                        try:
                            distutils.file_util.copy_file(FireTB, FFChrome, update=True)

                        except IOError:
                            messagebox.showwarning("Warning", "Couldn't manage to install Tabs Below function.")

                    if CkFT.get() == 1:
                        try:
                            distutils.file_util.copy_file(FireFT, FFChrome, update=True)

                            FireFile = os.path.normpath(rpCkFF22.get() + "/chrome/Focus-tab-on-hover.uc.js")
                            writeFT(FireFile)
                        except IOError:
                            messagebox.showwarning("Warning", "Couldn't manage to install Focus Tab on hover function.")

                else: 
                    messagebox.showerror("Error", "Firefox profile folder location is wrong.\nSelect a valid one and try again.")
                    return

            if CkFFN.get() == 1:
                if os.access(rpCkFFN12.get(), os.F_OK) == True and \
                   os.access(os.path.normpath(rpCkFFN12.get() + "/defaults/pref"), os.F_OK) == True:
                   fullPatcher(rpCkFFN12.get(), "None")
                else: 
                    messagebox.showerror("Error", "Nightly root folder location is wrong.\nSelect a valid one and try again.")
                    return

                if os.access(rpCkFFN22.get(), os.F_OK) == True:
                    fullPatcher("None", rpCkFFN22.get())

                    if CkMR.get() == 1:
                        try:
                            distutils.file_util.copy_file(Fire71MR, FFNChrome)

                            writeMR(FFNCMR71)

                            if os.access(FFNCMRL71, os.F_OK) == True:
                                os.remove(FFNCMRL71)

                        except IOError:
                            messagebox.showwarning("Warning", "Couldn't manage to install Multi-row Tabs function.")

                    if CkTB.get() == 1:
                        try:
                            distutils.file_util.copy_file(FireTB, FFNChrome, update=True)

                        except IOError:
                            messagebox.showwarning("Warning", "Couldn't manage to install Tabs Below function.")

                    if CkFT.get() == 1:
                        try:
                            FireFile = os.path.normpath(rpCkFFN22.get() + "/chrome/Focus-tab-on-hover.uc.js")
                            writeFT(FireFile)
                        except IOError:
                            messagebox.showwarning("Warning", "Couldn't manage to install Focus Tab on hover function.")
                else: 
                    messagebox.showerror("Error", "Firefox profile folder location is wrong.\nSelect a valid one and try again.")
                    return

            if CkFFP.get() == 1:
                values = []
                for y in rpCkFFP1.curselection():
                    values.append(rpCkFFP1.get(y))
                
                for x in values:
                    FFChrome = os.path.normpath(x + "/chrome")

                    FFCMR = os.path.normpath(x + "/chrome/MultiRowTab-scrollable.uc.js")
                    FFCMR71 = os.path.normpath(x + "/chrome/MultiRowTab-scrollableFF71.uc.js")

                    FFCMRL = os.path.normpath(x + "/chrome/MultiRowTabLiteforFx.uc.js")
                    FFCMRL71 = os.path.normpath(x + "/chrome/MultiRowTabLiteforFF71.uc.js")

                    if SystemOS() == "Windows":
                        splitter = x.split("\\")
                        selectedProfile = splitter[-1]

                    else: 
                        splitter = x.split("/")
                        selectedProfile = splitter[-1]

                    if os.access(x, os.F_OK) == True:
                        fullPatcher("None", x)

                        if CkMR.get() == 1:
                            FF71 = messagebox.askyesno("Firefox 71 prompt", 
                                "Does the following profile belong to a Firefox version of 71 or above?\n{0}".format(selectedProfile))
                            try:
                                if FF71 == True:
                                    distutils.file_util.copy_file(Fire71MR, FFChrome)

                                    if os.access(FFCMR, os.F_OK) == True:
                                        os.remove(FFCMR)

                                    writeMR(FFCMR71)

                                else:
                                    distutils.file_util.copy_file(FireMR, FFChrome)

                                    if os.access(FFCMR71, os.F_OK) == True:
                                        os.remove(FFCMR71)

                                    writeMR(FFCMR)

                                if os.access(FFCMRL, os.F_OK) == True:
                                    os.remove(FFCMRL)

                                if os.access(FFCMRL71, os.F_OK) == True:
                                    os.remove(FFCMRL71)

                            except IOError:
                                messagebox.showwarning("Warning", "Couldn't manage to install Multi-row Tabs function.")

                        if CkTB.get() == 1:
                            try:
                                distutils.file_util.copy_file(FireTB, FFChrome, update=True)

                            except IOError:
                                messagebox.showwarning("Warning", "Couldn't manage to install Tabs Below function.")

                        if CkFT.get() == 1:
                            try:
                                distutils.file_util.copy_file(FireFT, FFChrome, update=True)

                                FireFile = os.path.normpath(x + "/chrome/Focus-tab-on-hover.uc.js")
                                writeFT(FireFile)
                            except IOError:
                                messagebox.showwarning("Warning", "Couldn't manage to install Focus Tab on hover function.")

                    else: 
                        messagebox.showerror("Error", "Couldn't access the selected profile.\nIt was either deleted or moved.")
            
            if (CkFFP.get() == 0 and CkFFN.get() == 0 and CkFF.get() == 0) or \
               (CkFFP.get() == 1 and CkFFN.get() == 0 and CkFF.get() == 0 and values == []):
                messagebox.showerror("Nothing happened", "You need to select at least one profile to patch.")
            else:
                messagebox.showinfo("Patching complete", "The patching is complete.\nRestart Firefox for changes to take effect.")

            checkPatchFF()
            checkPatchFFN()

        # This method will call the required functions to remove the patch
        def patchRemove():
            if (CkFF.get() == 1 and CkFFN.get() == 0) or (CkFF.get() == 0 and CkFFN.get() == 1):
                removeAll = messagebox.askyesno("Remove all", 
                    "This will remove all the patch files from the selected Firefox installation.\nIs that okay?")
                if removeAll == False:
                    messagebox.showwarning("Function removal", 
                    "Only the selected functions will be removed from the selected Firefox installation.")
            elif CkFF.get() == 1 and CkFFN.get() == 1:
                removeAll = messagebox.askyesno("Remove all", 
                    "This will remove all the patch files from the selected Firefox installations.\nIs that okay?")
                if removeAll == False:
                    messagebox.showwarning("Function removal", 
                    "Only the selected functions will be removed from the selected Firefox installations.")
            elif CkFFP.get() == 0:
                messagebox.showerror("No option selected", 
                    "You need to select at least one Firefox installation\nor profile folder to remove it's installed patch.")
                return

            if CkFF.get() == 1:
                if removeAll == True:
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

                if CkTB.get() == 1:
                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below.as.css"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/Tabs-below.as.css"))

                if CkFT.get() == 1:
                    if os.access(os.path.normpath(rpCkFF22.get() + "/chrome/Focus-tab-on-hover.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFF22.get() + "/chrome/Focus-tab-on-hover.uc.js"))

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

                if CkTB.get() == 1:
                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/Tabs-below.as.css"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/Tabs-below.as.css"))

                if CkFT.get() == 1:
                    if os.access(os.path.normpath(rpCkFFN22.get() + "/chrome/Focus-tab-on-hover.uc.js"), os.F_OK) == True:
                        os.remove(os.path.normpath(rpCkFFN22.get() + "/chrome/Focus-tab-on-hover.uc.js"))

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

                    if CkTB.get() == 1:
                        if os.access(os.path.normpath(x + "/chrome/Tabs-below.as.css"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/Tabs-below.as.css"))

                    if CkFT.get() == 1:
                        if os.access(os.path.normpath(x + "/chrome/Focus-tab-on-hover.uc.js"), os.F_OK) == True:
                            os.remove(os.path.normpath(x + "/chrome/Focus-tab-on-hover.uc.js"))

            if CkFFP.get() == 1 and CkFFN.get() == 0 and CkFF.get() == 0:
                if values != []:
                    messagebox.showinfo("Unpatch complete", "Functions removed successfully.\nRestart firefox for changes to take effect.")
                else: messagebox.showwarning("No profile selected", "You need to select at least one profile folder.")
            else: messagebox.showinfo("Unpatch complete", "Patch files removed succesfully.\nRestart firefox for changes to take effect.")

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
        rpCkFF.select()
        rpCkFF.grid(column=0, row=1, columnspan=3, sticky="W")

        rpCkFF01 = Label(rootPatch, text="        ").grid(column=0, row=2, sticky="w")
        rpCkFF1 = Label(rootPatch, text="Root: ")
        rpCkFF1.grid(column=1, row=2, sticky="E")
        rpCkFF12 = Entry(rootPatch, width=60)
        rpCkFF12.insert(0, root)
        rpCkFF12.grid(column=2, row=2, sticky="W")
        rpCkFF13 = Button(rootPatch, text="Select", width=7, command=lambda:EntryUpdate("1"))
        rpCkFF13.grid(column=3, row=2, sticky="W", padx=3)

        rpCkFF02 = Label(rootPatch, text="        ").grid(column=0, row=3, sticky="w")
        rpCkFF2 = Label(rootPatch, text="Profile: ")
        rpCkFF2.grid(column=1, row=3, sticky="E")
        rpCkFF22 = Entry(rootPatch)
        rpCkFF22.insert(0, RProfile)
        rpCkFF22.grid(column=2, row=3, sticky="WE")
        rpCkFF23 = Button(rootPatch, text="Select", command=lambda:EntryUpdate("2"))
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

        CkFFP = tkinter.IntVar()
        rpCkFFP = Checkbutton(rootPatch, text="Profiles only", variable=CkFFP, command=updateFFPChildren)
        rpCkFFP.grid(column=0, row=9, columnspan=3, sticky="W")

        rpCkFFP1 = Listbox(rootPatch, selectmode="extended")

        for y in range(len(PrFols)):
            rpCkFFP1.insert("end", PrFols[y])

        LBScrollbar = Scrollbar(rootPatch, orient="vertical", command=rpCkFFP1.yview)
        rpCkFFP1.config(yscrollcommand=LBScrollbar.set, state="disabled")
        LBScrollbar.grid(column=4, row=10, sticky="NSW")

        rpCkFFP1.grid(column=1, row=10, columnspan=3, sticky="WE")
        rpSpacer3 = Label(rootPatch, text=" ").grid(column=0, row=11)

        rpReset = Button(rootPatch, text="Reset folders", padx=10, pady=5, command=EntryReset)
        rpReset.grid(column=0, row=12, sticky="W", columnspan=2)

        # This other part covers the featurePatch frame
        FPLF = LabelFrame(featurePatch, padx=20, pady=20, text="Choose what functions you want to install/uninstall:", font=("", 10, "bold"))
        FPLF.grid(column=0, row=0, columnspan=4)

        fpLb = Label(FPLF, text="You need to patch the Firefox version you are using for\nthese changes to take effect.\n")
        fpLb.grid(column=0, row=0, columnspan=4, sticky="W")

        CkMR = tkinter.IntVar()
        CkMR1E = tkinter.IntVar()
        RdMR = tkinter.IntVar()
        fpCkMR = Checkbutton(FPLF, text="Multi-row Tabs", variable=CkMR, command=updateMRChildren)
        fpCkMR.select()
        fpCkMR.grid(column=0, row=1, columnspan=4, sticky="W")
        fpCkMR1 = Radiobutton(FPLF, text="Scrollable rows", value=0, variable=RdMR, command=updateMRSpinbox)
        fpCkMR1.grid(column=1, row=2, sticky="W")
        fpCkMR1E = Spinbox(FPLF, from_=2, to=10, textvariable=CkMR1E)
        fpCkMR1E.delete(0,"end")
        fpCkMR1E.insert(0, 3)
        fpCkMR1E.grid(column=2, row=2, columnspan=2, sticky="WE")
        fpCkMR2 = Radiobutton(FPLF, text="All rows visible", value=1, variable=RdMR, command=updateMRSpinbox)
        fpCkMR2.grid(column=1, row=3, sticky="W")

        CkTB = tkinter.IntVar()
        fpCkTB = Checkbutton(FPLF, text="Tabs below URL bar", variable=CkTB)
        fpCkTB.grid(column=0, row=4, columnspan=4, sticky="W")

        CkFT = tkinter.IntVar()
        CkFTDE = tkinter.IntVar()
        fpCkFT = Checkbutton(FPLF, text="Focus Tab on hover", variable=CkFT, command=updateFTChildren)
        fpCkFT.grid(column=0, row=5, columnspan=4, sticky="W")
        fpCkFTD = Label(FPLF, text="Specify Delay (in ms)", state="disabled")
        fpCkFTD.grid(column=0, row=6, columnspan=2, sticky="E")
        fpCkFTDE = Spinbox(FPLF, from_=0, to=2000, textvariable=CkFTDE)
        fpCkFTDE.delete(0,"end")
        fpCkFTDE.insert(0, 200)
        fpCkFTDE.config(state="disabled")
        fpCkFTDE.grid(column=3, row=6, columnspan=2, sticky="W")
        fpspacer3 = Label(FPLF, text="").grid(column=0, row=8, sticky="w")

        fpfooter = Label(FPLF, text="For other functions:").grid(column=0, row=9, columnspan=4, sticky="w")
        fpfooterL = Button(FPLF, text="Visit repository", cursor="hand2", command=callhome)
        fpfooterL.grid(column=0, row=10, columnspan=4, sticky="we")

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
        featurePatch.grid(column=1, row=0)

def UIStart():

    QNWindow = tkinter.Tk()
    QNWindow.geometry("965x536")
    QNWindow.iconbitmap(os.path.normpath(sys._MEIPASS + '/icon.ico'))
    QNWindow.resizable(False, False)
    app = patcherUI()
    QNWindow.title("Quantum Nox - Firefox Patcher")
    QNWindow.mainloop()

if __name__ == '__main__':
    UIStart()