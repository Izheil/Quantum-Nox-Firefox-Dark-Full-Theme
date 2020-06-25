#!/usr/bin/python3
import os
import re
import sys
import shutil
import requests
import subprocess
import webbrowser
import distutils.core
from pathlib import Path

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
    tmp_file = os.getcwd() + '\\tempData.txt'
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
    home = "/home/" + os.getenv("USER")
    MozPFolder = home + r"/.mozilla/firefox"
elif OSinUse == "Mac":
    home = str(Path.home())
    MozPFolder = home + r"/Library/Application Support/Firefox"

# We get the profiles here
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
# as the default to open.
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

# Function to get the UUIDs of the installed extensions
def parseUUIDS(selectedProfile):
    # We get the string with the extension UUIDs here
    PrefsFile = os.path.join(selectedProfile, "prefs.js")

    with open(PrefsFile, 'r') as f:
        for line in f.readlines():
            PrefString = re.search('"extensions.webextensions.uuids", "{(.*)}"\);', line, re.M|re.I)
            if PrefString != None:
                UUIDString = PrefString.group(1)
                break
            else:
                continue

    # We parse the UUIDs string here
    UUIDString = UUIDString.replace("\\", "")
    UUIDString = UUIDString.replace('"', '')
    UUIDArray = UUIDString.split(",")

    UUIDDict = {}

    idArrays = ["anttoolbar@ant.com", "CookieAutoDelete@kennydo.com",
            "{7e79d10d-9667-4d38-838d-471281c568c3}",
            "s3download@statusbar", "forget-me-not@lusito.info",
            "https-everywhere@eff.org", "{73a6fe31-595d-460b-a920-fcc0f8843232}",
            "jid0-GjwrPchS3Ugt7xydvqVK4DQk8Ls@jetpack", "@testpilot-containers",
            "extension@one-tab.com", "jid1-MnnxcxisBPnSXQ@jetpack",
            "Tab-Session-Manager@sienori", "{c607c8df-14a7-4f28-894f-29e8722976af}",
            "uBlock0@raymondhill.net", "uMatrix@raymondhill.net",
            "{b9db16a4-6edc-47ec-a1f4-b86292ed211d}",
            "{00000c4c-fcfd-49bc-9f0d-78db44456c9c}"]

    for x in range(len(UUIDArray)):
        keyPair = UUIDArray[x].split(":")
        for x in range(len(idArrays)):
            if keyPair[0] == idArrays[x]:
                UUIDDict[keyPair[0]] = keyPair[1]

    return UUIDDict

# This function handles the addons placeholders replacement
def addonsPatcher(FFprofile, UUIDDict):
    "This method patches both the root and profile folders"

    # This one replaces the UUID strings
    def writeSettings(addonsFile, UUIDDict):
        with open(addonsFile, "r+") as f:
            s = f.read()
            isAddonInstalled = list(UUIDDict.keys())
            # Ant video downloader
            for x in range(len(isAddonInstalled)):
                if isAddonInstalled[x] == "anttoolbar@ant.com":
                    s = s.replace("TYPE-UUID-OF-ANT-VIDEO-DOWNLOADER-ADDON-HERE", 
                                  UUIDDict['anttoolbar@ant.com'])
                # History autodelete
                if isAddonInstalled[x] == "{7e79d10d-9667-4d38-838d-471281c568c3}":
                   s = s.replace("TYPE-UUID-OF-HISTORY-AUTODELETE-ADDON-HERE", 
                                  UUIDDict['{7e79d10d-9667-4d38-838d-471281c568c3}'])
                # Cookie autodelete
                if isAddonInstalled[x] == "CookieAutoDelete@kennydo.com":
                   s = s.replace("TYPE-UUID-OF-COOKIE-AUTODELETE-ADDON-HERE", 
                                  UUIDDict['CookieAutoDelete@kennydo.com'])
                # Download Manager (S3)
                if isAddonInstalled[x] == "s3download@statusbar":
                   s = s.replace("TYPE-UUID-OF-DOWNLOAD-MANAGER-(S3)-ADDON-HERE", 
                                  UUIDDict['s3download@statusbar'])
                # Forget me not
                if isAddonInstalled[x] == "forget-me-not@lusito.info":
                   s = s.replace("TYPE-UUID-OF-FORGET-ME-NOT-ADDON-HERE", 
                                  UUIDDict['forget-me-not@lusito.info'])
                # HTTPS everywhere
                if isAddonInstalled[x] == "https-everywhere@eff.org":
                   s = s.replace("TYPE-THE-UUID-OF-HTTPS-EVERYWHERE-ADDON-HERE", 
                                  UUIDDict['https-everywhere@eff.org'])
                # Noscript
                if isAddonInstalled[x] == "{73a6fe31-595d-460b-a920-fcc0f8843232}":
                   s = s.replace("TYPE-UUID-OF-NOSCRIPT-ADDON-HERE", 
                                  UUIDDict['{73a6fe31-595d-460b-a920-fcc0f8843232}'])
                # Notifier for Gmail (restartless)
                if isAddonInstalled[x] == "jid0-GjwrPchS3Ugt7xydvqVK4DQk8Ls@jetpack":
                   s = s.replace("TYPE-THE-UUID-OF-NOTIFIER-FOR-GMAIL-ADDON-HERE", 
                                  UUIDDict['jid0-GjwrPchS3Ugt7xydvqVK4DQk8Ls@jetpack'])
                # Multi-accounts container
                if isAddonInstalled[x] == "@testpilot-containers":
                   s = s.replace("TYPE-THE-UUID-OF-MULTI-ACCOUNTS-CONTAINER-ADDON-HERE", 
                                  UUIDDict['@testpilot-containers'])
                # Onetab
                if isAddonInstalled[x] == "extension@one-tab.com":
                   s = s.replace("TYPE-THE-UUID-OF-ONETAB-ADDON-HERE", 
                                  UUIDDict['extension@one-tab.com'])
                # Privacy Badger
                if isAddonInstalled[x] == "jid1-MnnxcxisBPnSXQ@jetpack":
                   s = s.replace("TYPE-UUID-OF-PRIVACY-BADGER-ADDON-HERE", 
                                  UUIDDict['jid1-MnnxcxisBPnSXQ@jetpack'])
                # Tab Session Manager
                if isAddonInstalled[x] == "Tab-Session-Manager@sienori":
                   s = s.replace("TYPE-UUID-OF-TAB-SESSION-MANAGER-ADDON-HERE", 
                                  UUIDDict['Tab-Session-Manager@sienori'])
                # Temporary Containers
                if isAddonInstalled[x] == "{c607c8df-14a7-4f28-894f-29e8722976af}":
                   s = s.replace("TYPE-THE-UUID-OF-TEMPORARY-CONTAINERS-ADDON-HERE", 
                                  UUIDDict['{c607c8df-14a7-4f28-894f-29e8722976af}'])
                # uBlock Origin
                if isAddonInstalled[x] == "uBlock0@raymondhill.net":
                   s = s.replace("TYPE-UUID-OF-UBLOCK-ORIGIN-ADDON-HERE", 
                                  UUIDDict['uBlock0@raymondhill.net'])
                # uMatrix
                if isAddonInstalled[x] == "uMatrix@raymondhill.net":
                   s = s.replace("TYPE-UUID-OF-UMATRIX-ADDON-HERE", 
                                  UUIDDict['uMatrix@raymondhill.net'])

                # Video Download Helper
                if isAddonInstalled[x] == "{b9db16a4-6edc-47ec-a1f4-b86292ed211d}":
                   s = s.replace("TYPE-UUID-OF-VIDEO-DOWNLOAD-HELPER-ADDON-HERE", 
                                  UUIDDict['{b9db16a4-6edc-47ec-a1f4-b86292ed211d}'])

                # Viewhance
                if isAddonInstalled[x] == "{00000c4c-fcfd-49bc-9f0d-78db44456c9c}":
                   s = s.replace("TYPE-THE-UUID-OF-VIEWHANCE-ADDON-HERE", 
                                  UUIDDict['{00000c4c-fcfd-49bc-9f0d-78db44456c9c}'])

            f.seek(0, 0)
            f.write(s)
            f.truncate()

    try:
        if FFprofile != None:
            addonFile = os.path.normpath(FFprofile + "/chrome/addons.css")

            # We patch the addons.css file here
            if os.access(addonFile, os.F_OK):

                # We do the placeholder update here
                writeSettings(addonFile, UUIDDict)

            elif os.access("addons.css", os.F_OK):
                shutil.copy2("addons.css", os.path.normpath(FFprofile + "/chrome/"))
                writeSettings(addonFile, UUIDDict)

            else:
                print("Addons.css file not found, fetching from repository...")
                getAddons = requests.get(r'https://raw.githubusercontent.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/master/Full%20dark%20theme/addons.css')
                if getAddons.status_code == 200:
                    print("File fetched successfully.\n")
                    with open(addonFile, "w") as f:
                        f.write(getAddons.text)
                    print("File finished downloading to " + addonFile)
                    writeSettings(addonFile, UUIDDict)
                else:
                    print("There was an error while trying to download the file.\n")

    except IOError:
        print("There was a problem while trying to write to addons.css file.")
        return 1

    return 0

# Function to open a profile folder
def openProfile(profileFolder):
    if os.access(profileFolder, os.F_OK):
        chromeFolder = os.path.normpath(profileFolder + "/chrome")
        if os.access(chromeFolder, os.F_OK):
            webbrowser.open(chromeFolder)
        else:
            print("Couldn't locate the profile chrome folder."
            + "\nSelect a valid one and try again.")
    else: 
        print("Couldn't locate the profile folder."
        + "\nSelect a valid one and try again.")

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

# Here we give the shorthand names for the default profiles
if OSinUse == "Windows":
    char2Esc = "\\"
else:
    char2Esc = "/"

if developerIsDefault or devOverNightly:
    defaultCLProfile = DProfile.split(char2Esc)[-1]
elif nightlyIsDefault:
    defaultCLProfile = NProfile.split(char2Esc)[-1]
else:
    defaultCLProfile = RProfile.split(char2Esc)[-1]

# We start the CLI here
print("This program will replace all the UUID placeholder strings in 'addons.css' file for their corresponding identifiers.")
print("First choose the profile folder where the file will be installed:\n")

print("The current default profile is " + defaultCLProfile + ".\n")

for x in range(len(Profiles)):
    profName = Profiles[x].split(char2Esc)
    Str2Print = "{}. {}".format(x + 1, profName[-1])
    print(Str2Print)

SelChoice = int(input("Choice: "))

SelProfile = Profiles[SelChoice - 1]

print("\nSelect the addons you want to theme:\n")

SelChoice2 = None
themeArray = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]

while SelChoice2 != 0:
    print("1. [" + themeArray[0] + "] All")
    print("2. ["  + themeArray[1] + "] Ant video downloader")
    print("3. ["  + themeArray[2] + "] Cookie autodelete")
    print("4. ["  + themeArray[3] + "] History autodelete")
    print("5. ["  + themeArray[4] + "] Download Manager (s3)")
    print("6. ["  + themeArray[5] + "] Forget me not")
    print("7. ["  + themeArray[6] + "] HTTPS everywhere")
    print("8. ["  + themeArray[7] + "] Noscript")
    print("9. ["  + themeArray[8] + "] Notifier for Gmail (restartless)")
    print("10. ["  + themeArray[9] + "] Multi-accounts container")
    print("11. ["  + themeArray[10] + "] Onetab")
    print("12. ["  + themeArray[11] + "] Privacy Badger")
    print("13. ["  + themeArray[12] + "] Tab Session Manager")
    print("14. ["  + themeArray[13] + "] Temporary Containers")
    print("15. ["  + themeArray[14] + "] Ublock Origin")
    print("16. ["  + themeArray[15] + "] Umatrix")
    print("17. ["  + themeArray[16] + "] Viewhance")
    print("0. Continue\n")

    SelChoice2 = int(input("Choice: "))

    if SelChoice2 != 0 and SelChoice2 > 1 and SelChoice2 < 18:
        SelChoice2 = SelChoice2 - 1
        if themeArray[SelChoice2] == "x":
            themeArray[SelChoice2] = " "
            themeArray[0] = "o"
        else:
            themeArray[SelChoice2] = "x"
            if themeArray[0] == " ":
                themeArray[0] = "o"
            else:
                numSel = 0
                for x in range(len(themeArray)):
                    if themeArray[x] == "x":
                        numSel += 1
                if numSel == 16:
                    themeArray[0] = "x"
    elif SelChoice2 == 1:
        if themeArray[0] == "x":
            for x in range(len(themeArray)):
                themeArray[x] = " "
        else:
            for x in range(len(themeArray)):
                themeArray[x] = "x"
    
UUIDDict = parseUUIDS(SelProfile)

if themeArray[0] != "x":
    idArrays = ["All", "anttoolbar@ant.com", "CookieAutoDelete@kennydo.com",
                "{7e79d10d-9667-4d38-838d-471281c568c3}",
                "s3download@statusbar", "forget-me-not@lusito.info",
                "https-everywhere@eff.org", "{73a6fe31-595d-460b-a920-fcc0f8843232}",
                "jid0-GjwrPchS3Ugt7xydvqVK4DQk8Ls@jetpack", "@testpilot-containers",
                "extension@one-tab.com", "jid1-MnnxcxisBPnSXQ@jetpack",
                "Tab-Session-Manager@sienori", "{c607c8df-14a7-4f28-894f-29e8722976af}",
                "uBlock0@raymondhill.net", "uMatrix@raymondhill.net",
                "{b9db16a4-6edc-47ec-a1f4-b86292ed211d}",
                "{00000c4c-fcfd-49bc-9f0d-78db44456c9c}"]

    for y in range(len(themeArray)):
        if y == 0:
            continue
        elif themeArray[y] != "x":
            if UUIDDict[idArrays[y]]:
                del UUIDDict[idArrays[y]]

addonFile = os.path.normpath(SelProfile + "/chrome/addons.css")

# We patch the addons.css file here
if os.access(addonFile, os.F_OK):
    print("Would you like to overwrite your current addons.css version with the lastest from the repository?")
    print("1. Yes")
    print("2. No\n")

    ovrwAdd = int(input("Choice: "))

    if ovrwAdd == 1:
        print("\nFetching addons.css from repo...")
        getAddons = requests.get(r'https://raw.githubusercontent.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/master/Full%20dark%20theme/addons.css')
        if getAddons.status_code == 200:
            print("File fetched successfully.\n")
            with open(addonFile, "w") as f:
                f.write(getAddons.text)
                f.truncate()
            print("File finished downloading to " + addonFile)
        else:
            print("There was an error while trying to download the file.\n")

# We call the replacement function for the addons file here
errorCatch = addonsPatcher(SelProfile, UUIDDict)

if errorCatch == 0:
    print("\nUUID's replaced successfully.\n\nRemember to place the \"@import 'addons.css'\" rule at the top of your userContent.css file if you created your own userContent.css,\nor aren't using the one provided in the repository.")
else:
    print("The UUIDs couldn't be replaced correctly. Try again when you are connected to the internet, or when you have a local copy of addons.css file.")
input("\nPress enter to exit.")