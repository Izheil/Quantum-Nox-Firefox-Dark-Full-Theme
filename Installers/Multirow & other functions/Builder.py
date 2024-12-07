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
import configparser
import distutils.core
from pathlib import Path
from tkinter import (LabelFrame, Checkbutton, Frame, Label, Entry, 
                    filedialog, Button, Listbox, Radiobutton, Spinbox, 
                    Scrollbar, messagebox, PhotoImage)

def get_system_os():
    """Identifies the OS"""

    if sys.platform.startswith('win'):
        system_os = "Windows"
    elif sys.platform.startswith('darwin'):
        system_os = "Mac"
    else: 
        system_os = "Linux"
    return system_os


# General constants
OS_IN_USE = get_system_os()
ENCODINGS = ('utf-8', 'utf-16le', 'utf-16be', 'utf-16', 'cp1252')
NONE_VALUE = "None"
NOT_FOUND_MESSAGE = "Not found"
FF_STABLE = "stable"
FF_NIGHTLY = "nightly"
FF_DEV = "developer"
DEFAULTS_PREF_FOLDER = "/defaults/pref"
ROOT_FOLDER = "/root"
CONFIG_PREFS_FILE = DEFAULTS_PREF_FOLDER + "/config-prefs.js"
CONFIG_JS_ROOT_FILE = "/config.js"
CHROME_FOLDER = "/chrome"
UTILS_FOLDER = "/utils"
CURRENT_WORKING_DIR = sys._MEIPASS
LINUX_ROOT_ARGS = ["sudo"] + sys.argv

# Patcher function file constants
FFCMR71 = "/chrome/MultiRowTab-scrollableFF71.uc.js"
FFCMRL71 = "/chrome/MultiRowTabLiteforFF71.uc.js"
FFCMRA71 = "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js"
FFCMR = "/chrome/MultiRowTab-scrollable.uc.js"
FFCMRL = "/chrome/MultiRowTabLiteforFx.uc.js"
FFCMRA = "/chrome/MultiRowTab-scrollable-autohide.uc.js"
FFTBAA = "/chrome/Tabs-below-Menu-onTop.as.css"
FFTBOT = "/chrome/Tabs-below-Menu-overTabs.as.css"
FFTB = "/chrome/Tabs-below.as.css"
FFMB = "/chrome/Megabar-disabled-until-focus.as.css"
FFMBAR = "/chrome/Megabar-disabled-all-resizing.as.css"
FFFTOH = "/chrome/Focus-tab-on-hover.uc.js"
FFSAU = "/chrome/setAttribute_unread.uc.js"


if OS_IN_USE == "Linux":
    # We import the modules that are UNIX-only
    import grp
    import pwd

    # We check for root
    if os.geteuid() != 0:
        os.execvp("sudo", LINUX_ROOT_ARGS)

    # We get the non-root username and group here
    root_user = os.getenv("SUDO_USER")

    # If the non-root username exists, we assume a regular user
    # with root privileges is using it, otherwise a pure root user is.
    if root_user:
        acc_root = False
        gid = pwd.getpwnam(root_user).pw_gid
        root_group = grp.getgrgid(gid).gr_name
    else:
        acc_root = True

elif OS_IN_USE == "Windows" and ctypes.windll.shell32.IsUserAnAdmin() == 0:
    print("Not running as admin, restarting as admin...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, subprocess.list2cmdline(sys.argv), None, 1)
    sys.exit()


def read_profiles(profile):
    """Fetches the profile folders"""

    profiles_ini = os.path.normpath(profile + "/profiles.ini")
    paths_found = []
    if not os.access(profiles_ini, os.F_OK):
        # Add folder names from profiles folder
        find_profile_folders(profile, paths_found)
    else:
        # Try different encodings
        for e in ENCODINGS:
            try:
                paths_found = read_paths_ini(profiles_ini, profile, paths_found, e)
                break
            except UnicodeDecodeError:
                print(f"Error reading profiles.ini using {e} encoding, trying a different one...")
    return paths_found


def read_paths_ini(ini_file, profile, paths_found, encoding_value):
    """Reads the ini file and appends the paths found"""

    if ini_file.endswith("profiles.ini"):
        path_regex = "Path=(.*)"
    else:
        path_regex = "Default=(.*)"

    with open(ini_file, 'r', encoding=encoding_value) as f:
        for line in f.readlines():
            ini_path = re.match(path_regex, line, re.M | re.I)
            if ini_path is not None:
                rotation_path = ini_path.group(1)
                if ((OS_IN_USE != "Linux" and rotation_path[0:9] == "Profiles/") or
                        OS_IN_USE == "Linux" and rotation_path[0] != "/"):
                    paths_found.append(os.path.normpath(profile + "/" + ini_path.group(1)))
                else:
                    paths_found.append(os.path.normpath(ini_path.group(1)))
    return paths_found


def find_profile_folders(profile, paths_found):
    """Finds the profile folders and appends them to the paths found"""

    if OS_IN_USE == "Windows" or OS_IN_USE == "Mac":
        profile = os.path.normpath(profile + "/profiles")
    if os.access(profile, os.F_OK):
        profile_names = os.listdir(profile)
        for x in profile_names:
            paths_found.append(os.path.normpath(profile + "/" + x))
    else:
        paths_found.append(NONE_VALUE)


def read_defaults(profile):
    """Fetches the default profile folders"""

    installs_ini = os.path.normpath(profile + "/installs.ini")
    paths_found = []
    if not os.access(installs_ini, os.F_OK):
        paths_found.append(NONE_VALUE)
    else:
        # Try different encodings
        for e in ENCODINGS:
            try:
                read_paths_ini(installs_ini, profile, paths_found, e)
                break
            except UnicodeDecodeError:
                print(f"Error reading installs.ini using {e} encoding, trying a different one...")
    return paths_found


# We get the user folders here
if OS_IN_USE == "Windows":
    # This is a workaround to find the current logged in user
    # in case they are not using an administrator account,
    # since otherwise it's not possible to find it on Windows
    tmp_file = CURRENT_WORKING_DIR + '\\tempData.txt'
    users = []
    try:
        with open(tmp_file, 'w+') as w:
            args = ['C:\\Windows\\Sysnative\\query.exe', 'user']
            user_proc_query = subprocess.Popen(args, stdout=w, stderr=subprocess.STDOUT,
                                               stdin=subprocess.PIPE,
                                               universal_newlines=True,
                                               shell=False)
            user_proc_query.wait()

        with open(tmp_file, 'r') as r:
            output = r.readlines()

        users = []
        for line in output:
            if line == output[0]:
                continue
            else:
                user_match = re.match(">(.*?) console *", line, re.M | re.I)
                if user_match is not None:
                    users.append(str(user_match.group(1)).rstrip())

    except Exception:
        print("Couldn't locate login user, backing to default profile path.")

    # Make sure the user array isn't empty
    if not users:
        users = [os.getenv('USERNAME')]

    # Remove traces of the temporary file to fetch non-root user
    if os.access(tmp_file, os.F_OK):
        os.remove(tmp_file)

    # Create default Firefox profile installations folder
    admin_profile = os.getenv('USERPROFILE')
    admin_name = os.getenv('USERNAME')

    appdata_path = (admin_profile[0:-(len(admin_name))]
                    + users[0].capitalize()
                    + "\\AppData\\Roaming")

    alt_appdata_path = os.path.join("C:\\Users\\", users[0].capitalize()
                                    + "\\AppData\\Roaming")

    if os.access(appdata_path, os.F_OK):
        home = appdata_path
    elif os.access(alt_appdata_path, os.F_OK):
        home = alt_appdata_path
    else:
        home = os.getenv('APPDATA')
    moz_profile_folder = home + r"\Mozilla\Firefox"
elif OS_IN_USE == "Linux":
    if acc_root:
        home = "/root"
        moz_profile_folder = home + r"/.mozilla/firefox"
    else:
        home = "/home/" + os.getenv("SUDO_USER")
        moz_profile_folder = home + r"/.mozilla/firefox"
elif OS_IN_USE == "Mac":
    home = str(Path.home())
    moz_profile_folder = home + r"/Library/Application Support/Firefox"

# Get the path of last saved installation paths if they exist
if OS_IN_USE == "Windows":
    qn_folder = home + r"\Quantum Nox"

elif OS_IN_USE == "Linux":
    qn_folder = home + r"/.Quantum Nox"

elif OS_IN_USE == "Mac":
    qn_folder = home + r"/Library/Application Support/Quantum Nox"

ff_paths_ini = os.path.normpath(qn_folder + '/FFPaths.ini')

# Get the location keys for later usage
if os.path.isfile(ff_paths_ini):
    config = configparser.ConfigParser()
    config.read(ff_paths_ini)
    ff_root_path = config['FIREFOX_ROOT_PATH']
    ff_profile_path = config['FIREFOX_PROFILE_PATH']

# Make sure that th_p default Firefox folder exists or that it's correctly fetched
if os.access(moz_profile_folder, os.F_OK):
    profiles = read_profiles(moz_profile_folder)
    default_profile = read_defaults(moz_profile_folder)
    if not profiles:
        profiles = [NONE_VALUE]
    if not default_profile:
        default_profile = [NONE_VALUE]
else:
    profiles = [NONE_VALUE]
    default_profile = [NONE_VALUE]

if (profiles == [NONE_VALUE] or default_profile == [NONE_VALUE]) and os.path.isfile(ff_paths_ini):

    if profiles == [NONE_VALUE]:
        for profile_path in ff_profile_path:
            if os.path.exists(ff_profile_path.get(profile_path)):
                profiles = [ff_profile_path.get(profile_path)]
    if default_profile == [NONE_VALUE]:
        for profile_path in ff_profile_path:
            if os.path.exists(ff_profile_path.get(profile_path)):
                default_profile = [ff_profile_path.get(profile_path)]
                break

# We get the default folder where programs are installed here
if OS_IN_USE == "Windows":
    prog_folder = r"C:\Program Files"
    if os.access(prog_folder, os.F_OK) is False:
        prog_folder = ""
elif OS_IN_USE == "Linux":
    prog_folder = r"/usr/lib"
    if os.access(prog_folder, os.F_OK) is False:
        prog_folder = ""
elif OS_IN_USE == "Mac":
    prog_folder = r"/Applications/"
    if os.access(prog_folder, os.F_OK) is False:
        prog_folder = ""


def resolve_root_folder(root_folder, alt_folder, ff_version):
    root_dir = root_folder
    if not os.access(root_folder, os.F_OK) and alt_folder is not None:
        root_dir = alt_folder

    if not os.access(root_dir, os.F_OK):
        root_dir = NOT_FOUND_MESSAGE
        if os.path.isfile(ff_paths_ini):
            if ff_root_path.get(ff_version) is not None:
                root_dir = ff_root_path.get(ff_version)
                if not os.path.exists(root_dir):
                    root_dir = NOT_FOUND_MESSAGE
    return root_dir


# We get the default folders for each installation here
if OS_IN_USE == "Windows":
    root = resolve_root_folder(r"C:\Program Files (x86)\Mozilla Firefox",
                               r"C:\Program Files\Mozilla Firefox", FF_STABLE)
    root_nightly = resolve_root_folder(r"C:\Program Files (x86)\Firefox Nightly",
                                       r"C:\Program Files\Firefox Nightly", FF_NIGHTLY)
    root_dev = resolve_root_folder(r"C:\Program Files (x86)\Firefox Developer Edition",
                                   r"C:\Program Files\Firefox Developer Edition", FF_DEV)

elif OS_IN_USE == "Linux":
    root = resolve_root_folder(r"/usr/lib/firefox/", r"/usr/lib64/firefox/", FF_STABLE)
    root_nightly = resolve_root_folder(r"/opt/nightly", r"/opt/firefox", FF_NIGHTLY)
    root_dev = resolve_root_folder(r"/opt/developer", r"/opt/firefox", FF_DEV)

elif OS_IN_USE == "Mac":
    root = resolve_root_folder(r"/Applications/Firefox.app/Contents/Resources", None, FF_STABLE)
    root_nightly = resolve_root_folder(r"/Applications/Firefox Nightly.app/Contents/Resources", None, FF_NIGHTLY)
    root_dev = resolve_root_folder(r"/Applications/Firefox Developer Edition.app/Contents/Resources", None, FF_DEV)


# We get the default folders here
def find_stable_default_profile():
    """Finds the default profile for stable release"""

    if default_profile != [NONE_VALUE] and len(default_profile) >= 1:
        parsed_default = parse_stable_default_profile(default_profile)
        if parsed_default != NOT_FOUND_MESSAGE:
            return parsed_default
    if profiles != [NONE_VALUE] and len(profiles) >= 1:
        parsed_default = parse_stable_default_profile(profiles)
        if parsed_default != NOT_FOUND_MESSAGE:
            return parsed_default
    return NOT_FOUND_MESSAGE


def parse_stable_default_profile(profile_to_parse):
    """Parses the default profiles of stable release"""

    for p in profile_to_parse:
        splitter = p.split(".")
        profile_name = splitter[-1]
        if profile_name == "default-release":
            return p
        elif profile_name == "default":
            return p
        else:
            continue
    return NOT_FOUND_MESSAGE


def find_nightly_default_profile():
    """Finds the default profile of the nightly release"""

    NIGHTLY_PROFILE_SUFFIX = "default-nightly"
    if default_profile != [NONE_VALUE] and len(default_profile) >= 1:
        parsed_default = parse_nightly_or_dev_def_profile(default_profile, NIGHTLY_PROFILE_SUFFIX, 15)
        if parsed_default != NOT_FOUND_MESSAGE:
            return parsed_default
    if profiles != [NONE_VALUE] and len(profiles) >= 1:
        parsed_default = parse_nightly_or_dev_def_profile(default_profile, NIGHTLY_PROFILE_SUFFIX, 15)
        if parsed_default != NOT_FOUND_MESSAGE:
            return parsed_default
    return NOT_FOUND_MESSAGE


def parse_nightly_or_dev_def_profile(profile_to_parse, profile_suffix, name_limit):
    for p in profile_to_parse:
        splitter = p.split(".")
        profile_name = splitter[-1]
        if profile_name == profile_suffix:
            return p
        elif profile_name[0:name_limit] == profile_suffix:
            return p
        else:
            continue
    return NOT_FOUND_MESSAGE


def find_dev_default_profile():
    """Finds the default profile of the developer release"""

    DEV_PROFILE_SUFFIX = "dev-edition-default"
    if default_profile != [NONE_VALUE] and len(default_profile) >= 1:
        parsed_default = parse_nightly_or_dev_def_profile(default_profile, DEV_PROFILE_SUFFIX, 19)
        if parsed_default != NOT_FOUND_MESSAGE:
            return parsed_default
    if profiles != [NONE_VALUE] and len(profiles) >= 1:
        parsed_default = parse_nightly_or_dev_def_profile(default_profile, DEV_PROFILE_SUFFIX, 19)
        if parsed_default != NOT_FOUND_MESSAGE:
            return parsed_default
    return NOT_FOUND_MESSAGE


# We call the default profile finders
stable_profile = find_stable_default_profile()
nightly_profile = find_nightly_default_profile()
dev_profile = find_dev_default_profile()

# If any of the profile values is NOT_FOUND_MESSAGE and there is a value stored, we restore it
if os.path.isfile(ff_paths_ini):
    if stable_profile == NOT_FOUND_MESSAGE:
        if ff_profile_path.get(FF_STABLE) is not None:
            stable_profile = ff_profile_path.get(FF_STABLE)
            if not os.path.exists(stable_profile):
                stable_profile = NOT_FOUND_MESSAGE
    if nightly_profile == NOT_FOUND_MESSAGE:
        if ff_profile_path.get(FF_NIGHTLY) is not None:
            nightly_profile = ff_profile_path.get(FF_NIGHTLY)
            if not os.path.exists(nightly_profile):
                nightly_profile = NOT_FOUND_MESSAGE
    if dev_profile == NOT_FOUND_MESSAGE:
        if ff_profile_path.get(FF_DEV) is not None:
            dev_profile = ff_profile_path.get(FF_DEV)
            if not os.path.exists(dev_profile):
                dev_profile = NOT_FOUND_MESSAGE

# Check if only 1 profile exists and only 1 installation exists
# so that if not using the default profile names, it will get
# selected.
if profiles is not None:
    # First we check if only 1 firefox is installed
    only_stable = (root != NOT_FOUND_MESSAGE
                   and root_nightly == NOT_FOUND_MESSAGE
                   and root_dev == NOT_FOUND_MESSAGE)
    only_dev = (root_dev != NOT_FOUND_MESSAGE
                and root == NOT_FOUND_MESSAGE
                and root_nightly == NOT_FOUND_MESSAGE)
    only_nightly = (root_nightly != NOT_FOUND_MESSAGE
                    and root == NOT_FOUND_MESSAGE
                    and root_dev == NOT_FOUND_MESSAGE)

    if stable_profile == NOT_FOUND_MESSAGE and only_stable:
        stable_profile = profiles[0]

    if dev_profile == NOT_FOUND_MESSAGE and only_dev:
        dev_profile = profiles[0]

    if nightly_profile == NOT_FOUND_MESSAGE and only_nightly:
        nightly_profile = profiles[0]

# We try to get the folder where profiles are located to show
# as the default to open in the "select profile" buttons.
# If it doesn't exist we go back to the default mozilla folder.
def_profile_location = os.path.join(moz_profile_folder, "profiles")

if not os.access(def_profile_location, os.F_OK):
    if profiles is not None:
        if OS_IN_USE == "Windows":
            profilesplitter = profiles[0].split("\\")
        else:
            profilesplitter = profiles[0].split("/")
        removeLast = len(profilesplitter[-1])
        def_profile_location = profiles[0][0:-removeLast]
        del removeLast
        del profilesplitter
    else:
        def_profile_location = moz_profile_folder


def remove_non_standard_config_files(firefox_version):
    """Removes non-standard config files from firefox profile"""

    config_files = []
    for r, d, f in os.walk(os.path.normpath(firefox_version + DEFAULTS_PREF_FOLDER)):
        for file in f:
            config_files.append(os.path.join(r, file))

    # Removes non-standard configuration files if required
    for conf_file in config_files:
        if (conf_file != os.path.normpath(firefox_version + "/defaults/pref/channel-prefs.js") and
                conf_file != os.path.normpath(firefox_version + CONFIG_PREFS_FILE)):
            if args_in_use:
                print("The file " + conf_file + " might prevent the functions from working as they should.\n" +
                      "If you added this file, remove it or merge it with 'config-prefs.js' in the same location.")
                return

            conf_error = ("A non-standard configuration file was detected on Firefox root folder " +
                          "which might prevent the functions to work properly.\n" +
                          "\nWould you like to remove the following configuration file " +
                          "to fix the issue?\n\n" + conf_file)
            should_remove_alt_conf = messagebox.askyesno("Alternative configuration detected", conf_error)
            if should_remove_alt_conf:
                os.remove(conf_file)
            else:
                messagebox.showwarning("Possible compatibility problem",
                                       "It is possible that the installed functions won't work until " +
                                       "you remove the non-standard configuration files inside this path:\n" +
                                       os.path.normpath(firefox_version + DEFAULTS_PREF_FOLDER))


def patch_root_folder(firefox_version):
    """Patches firefox root folder"""

    # We first define the location of the files
    conf_pref = os.path.normpath(firefox_version + CONFIG_PREFS_FILE)
    conf_js = os.path.normpath(firefox_version + CONFIG_JS_ROOT_FILE)

    # We patch the root folder here
    if os.access(conf_js, os.F_OK) and os.access(conf_pref, os.F_OK):

        distutils.file_util.copy_file(
            os.path.normpath(CURRENT_WORKING_DIR + ROOT_FOLDER + CONFIG_PREFS_FILE),
            os.path.normpath(firefox_version + DEFAULTS_PREF_FOLDER + "/"), update=True)
        distutils.file_util.copy_file(os.path.normpath(CURRENT_WORKING_DIR + ROOT_FOLDER + CONFIG_JS_ROOT_FILE),
                                      firefox_version, update=True)

    elif os.access(os.path.normpath(firefox_version + CONFIG_JS_ROOT_FILE), os.F_OK) or \
            os.access(os.path.normpath(firefox_version + CONFIG_PREFS_FILE), os.F_OK):

        if os.access(conf_js, os.F_OK):
            shutil.copy2(os.path.normpath(CURRENT_WORKING_DIR + ROOT_FOLDER + CONFIG_PREFS_FILE),
                         os.path.normpath(firefox_version + DEFAULTS_PREF_FOLDER))

        else:
            shutil.copy2(os.path.normpath(CURRENT_WORKING_DIR + ROOT_FOLDER + CONFIG_JS_ROOT_FILE), firefox_version)

    else:
        shutil.copy2(os.path.normpath(CURRENT_WORKING_DIR + ROOT_FOLDER + CONFIG_JS_ROOT_FILE), firefox_version)
        shutil.copy2(os.path.normpath(CURRENT_WORKING_DIR + ROOT_FOLDER + CONFIG_PREFS_FILE),
                     os.path.normpath(firefox_version + DEFAULTS_PREF_FOLDER))

    if OS_IN_USE == "Linux":
        shutil.chown(conf_pref, root_user, root_group)
        os.chmod(conf_pref, 0o775)
        shutil.chown(conf_js, root_user, root_group)
        os.chmod(conf_js, 0o775)


def patch_profile_folder(firefox_profile):
    """Patches the profile folder"""

    # We patch the profile folder here
    if os.access(os.path.normpath(firefox_profile + CHROME_FOLDER + UTILS_FOLDER), os.F_OK):
        util_files = []
        for r, d, f in os.walk(os.path.normpath(CURRENT_WORKING_DIR + UTILS_FOLDER)):
            for file in f:
                util_files.append(os.path.join(r, file))
        for file in util_files:
            distutils.file_util.copy_file(file,
                                          os.path.normpath(firefox_profile + CHROME_FOLDER + UTILS_FOLDER), update=True)

    else:
        shutil.copytree(os.path.normpath(CURRENT_WORKING_DIR + UTILS_FOLDER),
                        os.path.normpath(firefox_profile + CHROME_FOLDER + UTILS_FOLDER))

    if OS_IN_USE == "Linux":
        chrome = firefox_profile + CHROME_FOLDER
        utils = chrome + UTILS_FOLDER
        util_files = glob.glob(utils + "/*.*")
        shutil.chown(chrome, root_user, root_group)
        os.chmod(chrome, 0o775)
        shutil.chown(utils, root_user, root_group)
        os.chmod(utils, 0o775)
        for file in util_files:
            shutil.chown(file, root_user, root_group)
            os.chmod(file, 0o775)


# This applies the basic patch for the functions to work
def apply_base_patch(firefox_version, firefox_profile):
    """This method patches both the root and profile folders"""
    
    try:
        # Check that the provided Firefox path is not empty
        if firefox_version is not None:
            remove_non_standard_config_files(firefox_version)
            patch_root_folder(firefox_version)

        # Check that the provided profile path is not empty
        if firefox_profile is not None:
            patch_profile_folder(firefox_profile)

    except IOError as err:
        error_msg = "You need higher privileges to apply the patch.\n\n" + str(err)
        if not args_in_use:
            messagebox.showerror("Error", error_msg)
        else:
            print(error_msg)
        return 1

    return 0


# These write the settings to the files
def write_function_settings(installer_function, function_to_install, function_settings):
    """Writes the settings we may have set of any function to the file"""

    with open(installer_function, "r+", encoding='utf-8') as f:
        s = f.read()
        if function_to_install.startswith("Multirow"):
            s = s.replace("TABROWS", function_settings)
        elif function_to_install.startswith("Focus-tab"):
            s = s.replace("DELAYTIME", function_settings)
        f.seek(0, 0)
        f.write(s)
        f.truncate()


# These remove the duplicated functions
def remove_duplicate_multirow(function_to_install, firefox_profile):
    """Removes duplicated multirow function files"""

    FULL_FFCMR71 = os.path.normpath(firefox_profile + FFCMR71)
    FULL_FFCMRL71 = os.path.normpath(firefox_profile + FFCMRL71)
    FULL_FFCMRA71 = os.path.normpath(firefox_profile + FFCMRA71)
    FULL_FFCMR = os.path.normpath(firefox_profile + FFCMR)
    FULL_FFCMRL = os.path.normpath(firefox_profile + FFCMRL)
    FULL_FFCMRA = os.path.normpath(firefox_profile + FFCMRA)

    if os.access(FULL_FFCMRA, os.F_OK) and function_to_install != "Multirow-autohide":
        os.remove(FULL_FFCMRA)
    if os.access(FULL_FFCMR, os.F_OK) and function_to_install != "Multirow-scrollable":
        os.remove(FULL_FFCMR)
    if os.access(FULL_FFCMRL, os.F_OK) and function_to_install != "Multirow-unlimited":
        os.remove(FULL_FFCMRL)

    if os.access(FULL_FFCMRA71, os.F_OK):
        os.remove(FULL_FFCMRA71)
    if os.access(FULL_FFCMR71, os.F_OK):
        os.remove(FULL_FFCMR71)
    if os.access(FULL_FFCMRL71, os.F_OK):
        os.remove(FULL_FFCMRL71)


def remove_duplicate_tabs_below(function_to_install, firefox_profile):
    """Removes duplicated tabs below function files"""

    FULL_FFTBAA = os.path.normpath(firefox_profile + FFTBAA)
    FULL_FFTBOT = os.path.normpath(firefox_profile + FFTBOT)
    FULL_FFTB = os.path.normpath(firefox_profile + FFTB)

    if os.access(FULL_FFTB, os.F_OK) and function_to_install != "Tabs-below":
        os.remove(FULL_FFTB)
    if os.access(FULL_FFTBOT, os.F_OK) and function_to_install != "Tabs-below-menu-over-tabs":
        os.remove(FULL_FFTBOT)

    if os.access(FULL_FFTBAA, os.F_OK):
        os.remove(FULL_FFTBAA)


def remove_duplicate_megabar(function_to_install, firefox_profile):
    """Removes duplicated megabar function files"""

    FULL_FFMB = os.path.normpath(firefox_profile + FFMB)
    FULL_FFMBAR = os.path.normpath(firefox_profile + FFMBAR)

    if os.access(FULL_FFMB, os.F_OK) and function_to_install != "Megabar-until-focus":
        os.remove(FULL_FFMB)
    if os.access(FULL_FFMBAR, os.F_OK) and function_to_install != "Megabar-all-resizing":
        os.remove(FULL_FFMBAR)


def change_file_ownership(profile_installed_file):
    """Changes file ownership on linux"""

    shutil.chown(profile_installed_file, root_user, root_group)
    os.chmod(profile_installed_file, 0o775)


# We copy the function files to the profile folder with this method
def install_function(firefox_profile, function_to_install, function_settings="0"):
    """Installs the css and js functions"""

    # We first get the chrome folder
    profile_chrome_folder = os.path.normpath(firefox_profile + CHROME_FOLDER)

    # Functions installation here
    function_map = {
        "Multirow-scrollable": (os.path.normpath(CURRENT_WORKING_DIR
                                                 + "/functions/MultiRowTab-scrollable.uc.js"),
                                os.path.normpath(firefox_profile
                                                 + FFCMR)),
        "Multirow-autohide": (os.path.normpath(CURRENT_WORKING_DIR
                                               + "/functions/MultiRowTab-scrollable-autohide.uc.js"),
                              os.path.normpath(firefox_profile
                                               + FFCMRA)),
        "Multirow-unlimited": (os.path.normpath(CURRENT_WORKING_DIR
                                                + "/functions/MultiRowTabLiteforFx.uc.js"),
                               os.path.normpath(firefox_profile
                                                + FFCMRL)),
        "Tabs-below": (os.path.normpath(CURRENT_WORKING_DIR
                                        + "/functions/Tabs-below.as.css"),
                       os.path.normpath(firefox_profile
                                        + FFTB)),
        "Tabs-below-menu-over-tabs": (os.path.normpath(CURRENT_WORKING_DIR
                                                       + "/functions/Tabs-below-Menu-overTabs.as.css"),
                                      os.path.normpath(firefox_profile
                                                       + FFTBOT)),
        "Megabar-until-focus": (os.path.normpath(CURRENT_WORKING_DIR
                                                 + "/functions/Megabar-disabled-until-focus.as.css"),
                                os.path.normpath(firefox_profile
                                                 + FFMB)),
        "Megabar-all-resizing": (os.path.normpath(CURRENT_WORKING_DIR
                                                  + "/functions/Megabar-disabled-all-resizing.as.css"),
                                 os.path.normpath(firefox_profile
                                                  + FFMBAR)),
        "Focus-tab": (os.path.normpath(CURRENT_WORKING_DIR
                                       + "/functions/Focus-tab-on-hover.uc.js"),
                      os.path.normpath(firefox_profile
                                       + FFFTOH)),
        "Unread-state": (os.path.normpath(CURRENT_WORKING_DIR
                                          + "/functions/setAttribute_unread.uc.js"),
                         os.path.normpath(firefox_profile
                                          + FFSAU))
    }

    ff_function = function_map[function_to_install][0]
    installer_function = function_map[function_to_install][1]

    try:
        shutil.copy2(ff_function, profile_chrome_folder)

        if function_to_install.startswith("Multirow") or function_to_install == "Focus-tab":
            write_function_settings(installer_function, function_to_install, function_settings)

        if OS_IN_USE == "Linux":
            change_file_ownership(installer_function)

        # We remove the alternative versions on those functions
        # that have it
        if function_to_install.startswith("Multirow"):
            remove_duplicate_multirow(function_to_install, firefox_profile)
        elif function_to_install.startswith("Tabs-below"):
            remove_duplicate_tabs_below(function_to_install, firefox_profile)
        elif function_to_install.startswith("Megabar"):
            remove_duplicate_megabar(function_to_install, firefox_profile)
        return 0

    except IOError:
        error_msg = "There was a problem while trying to install "
        error_map = {
            "Multirow-scrollable": "Multirow scrollable.",
            "Multirow-autohide": "Multirow autohide.",
            "Multirow-unlimited": "Multirow unlimited.",
            "Tabs-below": "Tabs Below.",
            "Tabs-below-menu-over-tabs": "Tabs Below menu over tabs.",
            "Megabar-until-focus": "Megabar resizing disabler until focus.",
            "Megabar-all-resizing": "Megabar resizing disabler.",
            "Focus-tab": "Focus tabs on hover.",
            "Unread-state": "Tabs unread state."
        }

        error_msg += error_map[function_to_install]

        if not args_in_use:
            messagebox.showwarning("Write access error", error_msg)
        else:
            print(error_msg)
        if os.access(installer_function, os.F_OK):
            os.remove(installer_function)
        return 1


def remove_root_patch(firefox_version):
    """Removes the patch from the root folder"""

    if os.access(os.path.normpath(firefox_version + CONFIG_JS_ROOT_FILE), os.F_OK) and \
            os.access(os.path.normpath(firefox_version + CONFIG_PREFS_FILE), os.F_OK):

        os.remove(os.path.normpath(firefox_version + CONFIG_PREFS_FILE))
        os.remove(os.path.normpath(firefox_version + CONFIG_JS_ROOT_FILE))

    elif os.access(os.path.normpath(firefox_version + CONFIG_JS_ROOT_FILE), os.F_OK) or \
            os.access(os.path.normpath(firefox_version + CONFIG_PREFS_FILE), os.F_OK):
        if os.access(os.path.normpath(firefox_version + CONFIG_JS_ROOT_FILE), os.F_OK):
            os.remove(os.path.normpath(firefox_version + CONFIG_JS_ROOT_FILE))

        else:
            os.remove(os.path.normpath(firefox_version + CONFIG_PREFS_FILE))


def remove_file_if_exists(file_to_remove):
    """Removes profile patch files"""

    if os.access(file_to_remove, os.F_OK):
        os.remove(file_to_remove)


def remove_profile_patch(firefox_profile):
    """Removes the profile patch files"""

    if os.access(os.path.normpath(firefox_profile + CHROME_FOLDER + UTILS_FOLDER), os.F_OK):
        remove_file_if_exists(os.path.normpath(firefox_profile + "/chrome/utils/boot.jsm"))
        remove_file_if_exists(os.path.normpath(firefox_profile + "/chrome/utils/chrome.manifest"))
        remove_file_if_exists(os.path.normpath(firefox_profile + "/chrome/utils/RDFDataSource.jsm"))
        remove_file_if_exists(os.path.normpath(firefox_profile + "/chrome/utils/RDFManifestConverter.jsm"))
        remove_file_if_exists(os.path.normpath(firefox_profile + "/chrome/utils/userChrome.jsm"))
        remove_file_if_exists(os.path.normpath(firefox_profile + "/chrome/utils/xPref.jsm"))

        util_chrome_files = []
        for r, d, f in os.walk(os.path.normpath(firefox_profile + CHROME_FOLDER + UTILS_FOLDER)):
            for file in f:
                util_chrome_files.append(os.path.join(r, file))
        if not util_chrome_files:
            os.rmdir(os.path.normpath(firefox_profile + CHROME_FOLDER + UTILS_FOLDER))


def erase_patch(firefox_version, firefox_profile):
    """This method removes the patch from both the root and profile folders"""

    try:
        if firefox_version is not None:
            # We remove the patch from the root folder here
            remove_root_patch(firefox_version)

        if firefox_profile is not None:
            # We remove the patch from the profile folder here
            remove_profile_patch(firefox_profile)

    except IOError:
        if not args_in_use:
            messagebox.showerror("Error",
                                 "You need higher privileges to remove the patch.")
        else:
            print("You need higher privileges to remove the patch.")
        return 1

    return 0


# This displays the error messages on write access failure
def display_error(err_msg):
    """Displays errors to the user"""

    if not args_in_use:
        messagebox.showwarning("Write access error", err_msg)
    else:
        print(err_msg)


def remove_function(firefox_profile, func_to_remove):
    """This function removes the functions from the selected profile folder."""

    error_msg = "There was a problem while removing "

    # We remove the files here
    if func_to_remove == "Multirow":
        MRS = os.path.normpath(firefox_profile
                               + "/chrome/MultiRowTab-scrollable.uc.js")
        MRS71 = os.path.normpath(firefox_profile
                                 + "/chrome/MultiRowTab-scrollableFF71.uc.js")
        MRL = os.path.normpath(firefox_profile
                               + "/chrome/MultiRowTabLiteforFx.uc.js")
        MRL71 = os.path.normpath(firefox_profile
                                 + "/chrome/MultiRowTabLiteforFF71.uc.js")
        MRSA = os.path.normpath(firefox_profile
                                + "/chrome/MultiRowTab-scrollable-autohide.uc.js")
        MRSA71 = os.path.normpath(firefox_profile
                                  + "/chrome/MultiRowTab-scrollable-autohideFF71.uc.js")
        try:
            remove_file_if_exists(MRS)
            remove_file_if_exists(MRS71)
            remove_file_if_exists(MRL)
            remove_file_if_exists(MRL71)
            remove_file_if_exists(MRSA)
            remove_file_if_exists(MRSA71)

        except IOError:
            error_msg += "Multirow."
            display_error(error_msg)
            return 1

    elif func_to_remove == "Tabs-below":
        TB = os.path.normpath(firefox_profile + "/chrome/Tabs-below.as.css")
        TBOT = os.path.normpath(firefox_profile
                                + "/chrome/Tabs-below-Menu-overTabs.as.css")
        TBAA = os.path.normpath(firefox_profile
                                + "/chrome/Tabs-below-Menu-onTop.as.css")
        try:
            remove_file_if_exists(TB)
            remove_file_if_exists(TBOT)
            remove_file_if_exists(TBAA)

        except IOError:
            error_msg += "Tabs below."
            display_error(error_msg)
            return 1

    elif func_to_remove == "Megabar":
        MB = os.path.normpath(firefox_profile + "/chrome/Megabar-disabled-until-focus.as.css")
        MBAR = os.path.normpath(firefox_profile
                                + "/chrome/Megabar-disabled-all-resizing.as.css")
        try:
            remove_file_if_exists(MB)
            remove_file_if_exists(MBAR)

        except IOError:
            error_msg += "Megabar resizing disabler."
            display_error(error_msg)
            return 1

    elif func_to_remove == "Focus-tab":
        FT = os.path.normpath(firefox_profile + "/chrome/Focus-tab-on-hover.uc.js")
        try:
            remove_file_if_exists(FT)

        except IOError:
            error_msg += "Focus tab on hover."
            display_error(error_msg)
            return 1

    elif func_to_remove == "Unread-state":
        US = os.path.normpath(firefox_profile + "/chrome/setAttribute_unread.uc.js")

        try:
            remove_file_if_exists(US)

        except IOError:
            error_msg += "Unread state on tabs."
            display_error(error_msg)
            return 1
    return 0


def call_home():
    """This method opens the repository page"""
    webbrowser.open_new(
        r"https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions/Other%20features")


def open_chrome_folder(firefox_profile):
    if os.access(firefox_profile, os.F_OK):
        chrome_folder = os.path.normpath(firefox_profile + CHROME_FOLDER)
        if os.access(chrome_folder, os.F_OK):
            webbrowser.open(chrome_folder)
        else:
            messagebox.showerror("Error",
                                 "Couldn't locate the profile chrome folder.\nSelect a valid one and try again.")
    else:
        messagebox.showerror("Error",
                             "Couldn't locate the profile folder.\nSelect a valid one and try again.")


class PatcherUI(Frame):
    """This class creates the UI of the patcher"""

    NOT_INSTALLED_LABEL = "Not installed"
    NOT_PATCHED_LABEL = "Not patched"
    ROOT_LABEL = "Root: "
    PROFILE_LABEL = "Profile: "
    EMPTY_SPACE_LABEL = "        "
    OPEN_PROFILE_LABEL = "Open profile"
    PROFILE_NOT_PATCHED_LABEL = "Profile not patched"
    ROOT_NOT_PATCHED_LABEL = "Root not patched"
    PATCHED_LABEL = "Patched"
    RED_COLOR = "#cc0000"
    GREEN_COLOR = "#339900"

    def __init__(self):
        super().__init__()

        self.rpDetail = None
        self.ff_nightly_patch_status = None
        self.ff_dev_patch_status = None
        self.ff_stable_patch_status = None
        self.fpCkUTD = None
        self.fpCkUT = None
        self.CkUT = None
        self.fpCkFTDE = None
        self.fpCkFTD = None
        self.fpCkFT = None
        self.CkFTDE = None
        self.CkFT = None
        self.fpCkMB1 = None
        self.fpCkMB = None
        self.CkMB1 = None
        self.CkMB = None
        self.fpCkTB1 = None
        self.fpCkTB = None
        self.CkTB1 = None
        self.CkTB = None
        self.fpCkMR2 = None
        self.fpCkMR1C = None
        self.fpCkMR1E = None
        self.fpCkMR1 = None
        self.fpCkMR = None
        self.RdMR = None
        self.CkMR1C = None
        self.CkMR1E = None
        self.CkMR = None
        self.rpCkFFP1 = None
        self.rpCkFFP = None
        self.CkFFP = None
        self.rpCkFF1 = None
        self.rpCkFFN23 = None
        self.rpCkFFN22 = None
        self.rpCkFFN13 = None
        self.rpCkFFN12 = None
        self.rpCkFFN1 = None
        self.rpCkFFN = None
        self.rpCkFFD23 = None
        self.rpCkFFD22 = None
        self.rpCkFFD2 = None
        self.rpCkFFD13 = None
        self.rpCkFFD12 = None
        self.rpCkFFD1 = None
        self.check_ff = None
        self.check_ff_dev = None
        self.check_ff_nightly = None
        self.rpCkFF23 = None
        self.rpCkFF22 = None
        self.rpCkFF2 = None
        self.rpCkFF13 = None
        self.rpCkFF12 = None
        self.rpCkFF = None
        self.rpCkFFN2 = None
        self.rpCkFFD = None
        self.init_ui()

    def init_ui(self):
        """Creates the user interface"""

        self.pack(expand=True, fill="both")

        # These are the outer frames of each section
        root_patch = Frame(self, padx=30, pady=20)
        feature_patch = Frame(self, pady=20)

        # This part covers the root_patch frame
        Label(root_patch, text="Choose what do you want to patch or unpatch:\n",
              font=("", 10, "bold")).grid(column=0, row=0, columnspan=4, sticky="W")

        self.check_ff = tkinter.IntVar()
        self.rpCkFF = Checkbutton(root_patch, text="Firefox", variable=self.check_ff,
                                  command=self.update_ff_children)
        self.rpCkFF.grid(column=0, row=1, columnspan=3, sticky="W")

        Label(root_patch, text=self.EMPTY_SPACE_LABEL).grid(column=0, row=2, sticky="w")
        self.rpCkFF1 = Label(root_patch, text=self.ROOT_LABEL, state="disabled")
        self.rpCkFF1.grid(column=1, row=2, sticky="E")
        self.rpCkFF12 = Entry(root_patch, width=60)
        self.rpCkFF12.insert(0, root)
        self.rpCkFF12.config(state="disabled")
        self.rpCkFF12.grid(column=2, row=2, sticky="W")
        self.rpCkFF13 = Button(root_patch, text="Select", width=7,
                               command=lambda: self.update_entry("1"), state="disabled")
        self.rpCkFF13.grid(column=3, row=2, sticky="W", padx=3)

        Label(root_patch, text=self.EMPTY_SPACE_LABEL).grid(column=0, row=3, sticky="w")
        self.rpCkFF2 = Label(root_patch, text=self.PROFILE_LABEL, state="disabled")
        self.rpCkFF2.grid(column=1, row=3, sticky="E")
        self.rpCkFF22 = Entry(root_patch)
        self.rpCkFF22.insert(0, stable_profile)
        self.rpCkFF22.config(state="disabled")
        self.rpCkFF22.grid(column=2, row=3, sticky="WE")
        self.rpCkFF23 = Button(root_patch, text="Select",
                               command=lambda: self.update_entry("2"), state="disabled")
        self.rpCkFF23.grid(column=3, row=3, sticky="WE", padx=3)
        Label(root_patch, text=" ").grid(column=4, row=4)

        self.check_ff_dev = tkinter.IntVar()
        self.rpCkFFD = Checkbutton(root_patch, text="Firefox Developer",
                                   variable=self.check_ff_dev, command=self.update_ff_dev_children)
        self.rpCkFFD.grid(column=0, row=5, columnspan=3, sticky="W")

        Label(root_patch, text=self.EMPTY_SPACE_LABEL).grid(column=0, row=6, sticky="w")
        self.rpCkFFD1 = Label(root_patch, text=self.ROOT_LABEL, state="disabled")
        self.rpCkFFD1.grid(column=1, row=6, sticky="E")
        self.rpCkFFD12 = Entry(root_patch, width=60)
        self.rpCkFFD12.insert(0, root_dev)
        self.rpCkFFD12.config(state="disabled")
        self.rpCkFFD12.grid(column=2, row=6, sticky="W")
        self.rpCkFFD13 = Button(root_patch, text="Select", width=7,
                                command=lambda: self.update_entry("3"), state="disabled")
        self.rpCkFFD13.grid(column=3, row=6, sticky="W", padx=3)

        Label(root_patch, text=self.EMPTY_SPACE_LABEL).grid(column=0, row=7, sticky="w")
        self.rpCkFFD2 = Label(root_patch, text=self.PROFILE_LABEL, state="disabled")
        self.rpCkFFD2.grid(column=1, row=7, sticky="E")
        self.rpCkFFD22 = Entry(root_patch)
        self.rpCkFFD22.insert(0, dev_profile)
        self.rpCkFFD22.config(state="disabled")
        self.rpCkFFD22.grid(column=2, row=7, sticky="WE")
        self.rpCkFFD23 = Button(root_patch, text="Select",
                                command=lambda: self.update_entry("4"), state="disabled")
        self.rpCkFFD23.grid(column=3, row=7, sticky="WE", padx=3)
        Label(root_patch, text=" ").grid(column=4, row=8)

        self.check_ff_nightly = tkinter.IntVar()
        self.rpCkFFN = Checkbutton(root_patch, text="Firefox Nightly",
                                   variable=self.check_ff_nightly, command=self.update_ff_nightly_children)
        self.rpCkFFN.grid(column=0, row=9, columnspan=3, sticky="W")

        Label(root_patch, text=self.EMPTY_SPACE_LABEL).grid(column=0, row=10, sticky="w")
        self.rpCkFFN1 = Label(root_patch, text=self.ROOT_LABEL, state="disabled")
        self.rpCkFFN1.grid(column=1, row=10, sticky="E")
        self.rpCkFFN12 = Entry(root_patch)
        self.rpCkFFN12.insert(0, root_nightly)
        self.rpCkFFN12.config(state="disabled")
        self.rpCkFFN12.grid(column=2, row=10, sticky="WE")
        self.rpCkFFN13 = Button(root_patch, text="Select",
                                command=lambda: self.update_entry("5"), state="disabled")
        self.rpCkFFN13.grid(column=3, row=10, sticky="WE", padx=3)

        Label(root_patch, text=self.EMPTY_SPACE_LABEL).grid(column=0, row=11, sticky="w")
        self.rpCkFFN2 = Label(root_patch, text=self.PROFILE_LABEL, state="disabled")
        self.rpCkFFN2.grid(column=1, row=11, sticky="E")
        self.rpCkFFN22 = Entry(root_patch)
        self.rpCkFFN22.insert(0, nightly_profile)
        self.rpCkFFN22.config(state="disabled")
        self.rpCkFFN22.grid(column=2, row=11, sticky="WE")
        self.rpCkFFN23 = Button(root_patch, text="Select",
                                command=lambda: self.update_entry("6"), state="disabled")
        self.rpCkFFN23.grid(column=3, row=11, sticky="WE", padx=3)
        Label(root_patch, text=" ").grid(column=4, row=12)

        if root != NOT_FOUND_MESSAGE:
            self.rpCkFF.select()
            self.rpCkFF1.config(state="normal")
            self.rpCkFF12.config(state="normal")
            self.rpCkFF13.config(state="normal")
            self.rpCkFF2.config(state="normal")
            self.rpCkFF22.config(state="normal")
            self.rpCkFF23.config(state="normal")
        if root_dev != NOT_FOUND_MESSAGE:
            self.rpCkFFD.select()
            self.rpCkFFD1.config(state="normal")
            self.rpCkFFD12.config(state="normal")
            self.rpCkFFD13.config(state="normal")
            self.rpCkFFD2.config(state="normal")
            self.rpCkFFD22.config(state="normal")
            self.rpCkFFD23.config(state="normal")
        if root_nightly != NOT_FOUND_MESSAGE:
            self.rpCkFFN.select()
            self.rpCkFFN1.config(state="normal")
            self.rpCkFFN12.config(state="normal")
            self.rpCkFFN13.config(state="normal")
            self.rpCkFFN2.config(state="normal")
            self.rpCkFFN22.config(state="normal")
            self.rpCkFFN23.config(state="normal")

        self.CkFFP = tkinter.IntVar()
        self.rpCkFFP = Checkbutton(root_patch, text="profiles only* "
                                                    + "(Hold Ctrl or Shift to select more than one)",
                                   variable=self.CkFFP, command=self.update_ff_profile_children)
        self.rpCkFFP.grid(column=0, row=13, columnspan=3, sticky="W")

        self.rpCkFFP1 = Listbox(root_patch, selectmode="extended")

        for y in range(len(profiles)):
            self.rpCkFFP1.insert("end", profiles[y])

        profiles_scrollbar = Scrollbar(root_patch, orient="vertical",
                                       command=self.rpCkFFP1.yview)
        self.rpCkFFP1.config(yscrollcommand=profiles_scrollbar.set, state="disabled")
        profiles_scrollbar.grid(column=4, row=14, sticky="NSW")

        self.rpCkFFP1.grid(column=1, row=14, columnspan=3, sticky="WE")

        # Note for profiles box
        self.rpDetail = Label(root_patch,
                              text="* You need to have patched Firefox root folder first "
                                   + "with the 'Firefox', 'Firefox Developer' or\n'Firefox nightly' sections. "
                                   + "These only patch the profile folders.",
                              justify="left", state="disabled")
        self.rpDetail.grid(column=1, row=15, columnspan=4, sticky="W")
        Label(root_patch, text=" ").grid(column=0, row=16)

        # Reset button
        Button(root_patch, text="Reset folders", padx=10, pady=5,
               command=self.reset_entry).grid(column=0, row=17, sticky="W", columnspan=2)

        # This other part covers the feature_patch frame
        fplf = LabelFrame(feature_patch, padx=20, pady=20,
                          text="Choose what functions you want to "
                               + "install/remove:",
                          font=("", 10, "bold"))
        fplf.grid(column=0, row=0, columnspan=4)

        # Label above functions
        Label(fplf, text="You need to patch the Firefox version you "
                         + "have installed\nfor these changes to take effect."
                         + "\n('profiles only' just copies the functions)\n").grid(column=0,
                                                                                   row=0, columnspan=4, sticky="WE")

        self.CkMR = tkinter.IntVar()
        self.CkMR1E = tkinter.IntVar()
        self.CkMR1C = tkinter.IntVar()
        self.RdMR = tkinter.IntVar()
        self.fpCkMR = Checkbutton(fplf, text="Multi-row Tabs", variable=self.CkMR,
                                  command=self.update_multirow_children)
        self.fpCkMR.grid(column=0, row=1, columnspan=4, sticky="W")
        self.fpCkMR1 = Radiobutton(fplf, text="Scrollable rows", value=0,
                                   variable=self.RdMR, command=self.update_multirow_spinbox,
                                   state="disabled")
        self.fpCkMR1.grid(column=1, row=2, sticky="W")
        self.fpCkMR1E = Spinbox(fplf, from_=2, to=10, textvariable=self.CkMR1E)
        self.fpCkMR1E.delete(0, "end")
        self.fpCkMR1E.insert(0, "3")
        self.fpCkMR1E.config(state="disabled")
        self.fpCkMR1E.grid(column=2, row=2, columnspan=1, sticky="WE")
        self.fpCkMR1C = Checkbutton(fplf, text="Autohide scrollbars",
                                    variable=self.CkMR1C, state="disabled")
        self.fpCkMR1C.grid(column=1, row=3, columnspan=2, padx=20, sticky="W")
        self.fpCkMR2 = Radiobutton(fplf, text="All rows visible", value=1,
                                   variable=self.RdMR, command=self.update_multirow_spinbox,
                                   state="disabled")
        self.fpCkMR2.grid(column=1, row=4, sticky="W")

        self.CkTB = tkinter.IntVar()
        self.CkTB1 = tkinter.IntVar()
        self.fpCkTB = Checkbutton(fplf, text="Tabs below URL bar",
                                  variable=self.CkTB, command=self.update_tabs_below_check)
        self.fpCkTB.grid(column=0, row=5, columnspan=3, sticky="W")
        self.fpCkTB1 = Checkbutton(fplf, text="Menu right above tabs",
                                   variable=self.CkTB1, state="disabled")
        self.fpCkTB1.grid(column=0, row=6, columnspan=3, padx=20, sticky="W")

        self.CkMB = tkinter.IntVar()
        self.CkMB1 = tkinter.IntVar()
        self.fpCkMB = Checkbutton(fplf, text="Disable Megabar resize until focus",
                                  variable=self.CkMB, command=self.update_megabar_check)
        self.fpCkMB.grid(column=0, row=7, columnspan=3, sticky="W")
        self.fpCkMB1 = Checkbutton(fplf, text="Disable Megabar resize completelly",
                                   variable=self.CkMB1, state="disabled")
        self.fpCkMB1.grid(column=0, row=8, columnspan=3, padx=20, sticky="W")

        self.CkFT = tkinter.IntVar()
        self.CkFTDE = tkinter.IntVar()
        self.fpCkFT = Checkbutton(fplf, text="Focus Tab on hover",
                                  variable=self.CkFT, command=self.update_focus_tab_children)
        self.fpCkFT.grid(column=0, row=9, columnspan=4, sticky="W")
        self.fpCkFTD = Label(fplf, text="    Specify Delay (in ms)",
                             state="disabled")
        self.fpCkFTD.grid(column=0, row=10, columnspan=2, sticky="E", padx=10)
        self.fpCkFTDE = Spinbox(fplf, from_=0, to=2000, textvariable=self.CkFTDE)
        self.fpCkFTDE.delete(0, "end")
        self.fpCkFTDE.insert(0, "200")
        self.fpCkFTDE.config(state="disabled")
        self.fpCkFTDE.grid(column=2, row=10, columnspan=2, sticky="W")

        self.CkUT = tkinter.IntVar()
        self.fpCkUT = Checkbutton(fplf, text="Enable unread state on tabs*",
                                  variable=self.CkUT)
        self.fpCkUT.grid(column=0, row=11, columnspan=4, sticky="W")
        self.fpCkUTD = Label(fplf, text="* Allows you to customize unread tabs"
                                        + " with userChrome.css\n"
                                        + "using the [unread] attribute",
                             state="disabled")
        self.fpCkUTD.grid(column=0, row=12, columnspan=4, rowspan=2,
                          sticky="E", padx=10)
        Label(fplf, text="").grid(column=0, row=14,
                                  sticky="w")

        Label(fplf, text="For other functions:").grid(column=0, row=15, columnspan=4, sticky="w")

        # Home button
        Button(fplf, text="Visit repository", cursor="hand2",
               command=call_home).grid(column=0, row=16, columnspan=5, sticky="WE")

        patch_status_lb_frame = LabelFrame(feature_patch, text="Patch status", padx=20)
        patch_status_lb_frame.grid(column=0, row=1, pady=10, columnspan=4, sticky="WE")

        ff_patch_stats_frame = Frame(patch_status_lb_frame)
        ff_patch_stats_frame.pack(side="top", fill="x", pady=6)

        # Stable chrome folder open button
        Button(ff_patch_stats_frame, text=self.OPEN_PROFILE_LABEL,
               cursor="hand2",
               command=lambda: open_chrome_folder(self.rpCkFF22.get())).pack(side="right")

        Label(ff_patch_stats_frame, text="Firefox:  ").pack(side="left")
        self.ff_stable_patch_status = Label(ff_patch_stats_frame)
        self.check_ff_stable_patch()
        self.ff_stable_patch_status.pack(side="left")

        ff_patch_stats_frame_dev = Frame(patch_status_lb_frame)
        ff_patch_stats_frame_dev.pack(side="top", fill="x", pady=6)

        # Dev chrome folder open button
        Button(ff_patch_stats_frame_dev, text=self.OPEN_PROFILE_LABEL, cursor="hand2",
               command=lambda: open_chrome_folder(self.rpCkFFD22.get())).pack(side="right")

        Label(ff_patch_stats_frame_dev, text="Developer:  ").pack(side="left")
        self.ff_dev_patch_status = Label(ff_patch_stats_frame_dev)
        self.check_ff_dev_patch()
        self.ff_dev_patch_status.pack(side="left")

        ff_patch_stats_frame_nightly = Frame(patch_status_lb_frame)
        ff_patch_stats_frame_nightly.pack(side="bottom", fill="x", pady=10)

        # Nightly chrome folder open button
        Button(ff_patch_stats_frame_nightly, text=self.OPEN_PROFILE_LABEL,
               cursor="hand2",
               command=lambda: open_chrome_folder(self.rpCkFFN22.get())).pack(side="right")
        Label(ff_patch_stats_frame_nightly, text="Nightly: ").pack(side="left")
        self.ff_nightly_patch_status = Label(ff_patch_stats_frame_nightly)
        self.check_ff_nightly_patch()
        self.ff_nightly_patch_status.pack(side="left")

        # Patch button and unpatch buttons
        Button(feature_patch, text="Patch", cursor="hand2", pady=5, padx=5,
               command=self.install_patch).grid(column=0, row=2, pady=10, columnspan=2, padx=5, sticky="WE")
        Button(feature_patch, text="Remove Patch", cursor="hand2", pady=5, padx=5,
               command=self.unpatch).grid(column=2, row=2, columnspan=2, padx=5, sticky="WE")

        root_patch.grid(column=0, row=0)
        feature_patch.grid(column=1, row=0, padx=30, sticky="W")

    # These methods update the entries when looking for a
    # root/profile folder
    def update_entry(self, selected_btn):
        selected_dir = ""
        if selected_btn == "1" or selected_btn == "3" or selected_btn == "5":
            selected_dir = os.path.normpath(
                filedialog.askdirectory(initialdir=prog_folder))

        elif selected_btn == "2" or selected_btn == "4" or selected_btn == "6":
            selected_dir = os.path.normpath(
                filedialog.askdirectory(initialdir=def_profile_location))

        if selected_dir != "" and selected_dir != ".":
            if selected_btn == "1":
                self.rpCkFF12.delete(0, "end")
                self.rpCkFF12.insert(0, selected_dir)

            elif selected_btn == "2":
                self.rpCkFF22.delete(0, "end")
                self.rpCkFF22.insert(0, selected_dir)

            elif selected_btn == "3":
                self.rpCkFFD12.delete(0, "end")
                self.rpCkFFD12.insert(0, selected_dir)

            elif selected_btn == "4":
                self.rpCkFFD22.delete(0, "end")
                self.rpCkFFD22.insert(0, selected_dir)

            elif selected_btn == "5":
                self.rpCkFFN12.delete(0, "end")
                self.rpCkFFN12.insert(0, selected_dir)

            elif selected_btn == "6":
                self.rpCkFFN22.delete(0, "end")
                self.rpCkFFN22.insert(0, selected_dir)

            self.check_ff_stable_patch()
            self.check_ff_dev_patch()
            self.check_ff_nightly_patch()

    def reset_entry(self):
        disabled_state = False
        if self.rpCkFF12["state"] == "disabled":
            self.rpCkFF12.config(state="normal")
            disabled_state = True

        self.rpCkFF12.delete(0, "end")
        self.rpCkFF12.insert(0, root)

        if disabled_state:
            self.rpCkFF12.config(state="disabled")
            disabled_state = False

        if self.rpCkFF22["state"] == "disabled":
            self.rpCkFF22.config(state="normal")
            disabled_state = True

        self.rpCkFF22.delete(0, "end")
        self.rpCkFF22.insert(0, stable_profile)

        if disabled_state:
            self.rpCkFFD22.config(state="disabled")
            disabled_state = False

        if self.rpCkFFD12["state"] == "disabled":
            self.rpCkFFD12.config(state="normal")
            disabled_state = True

        self.rpCkFFD12.delete(0, "end")
        self.rpCkFFD12.insert(0, root_dev)

        if disabled_state:
            self.rpCkFFD12.config(state="disabled")
            disabled_state = False

        if self.rpCkFFD22["state"] == "disabled":
            self.rpCkFFD22.config(state="normal")
            disabled_state = True

        self.rpCkFFD22.delete(0, "end")
        self.rpCkFFD22.insert(0, dev_profile)

        if disabled_state:
            self.rpCkFFD22.config(state="disabled")
            disabled_state = False

        if self.rpCkFFN12["state"] == "disabled":
            self.rpCkFFN12.config(state="normal")
            disabled_state = True

        self.rpCkFFN12.delete(0, "end")
        self.rpCkFFN12.insert(0, root_nightly)

        if disabled_state:
            self.rpCkFFN12.config(state="disabled")
            disabled_state = False

        if self.rpCkFFN22["state"] == "disabled":
            self.rpCkFFN22.config(state="normal")
            disabled_state = True

        self.rpCkFFN22.delete(0, "end")
        self.rpCkFFN22.insert(0, nightly_profile)

        if disabled_state:
            self.rpCkFFN22.config(state="disabled")

        self.check_ff_stable_patch()
        self.check_ff_dev_patch()
        self.check_ff_nightly_patch()

    # We disable the children of the checkboxes that aren't selected here
    def update_ff_children(self):
        if self.check_ff.get() == 0:
            self.rpCkFF1.config(state="disabled")
            self.rpCkFF12.config(state="disabled")
            self.rpCkFF13.config(state="disabled")
            self.rpCkFF2.config(state="disabled")
            self.rpCkFF22.config(state="disabled")
            self.rpCkFF23.config(state="disabled")
        elif self.check_ff.get() == 1:
            self.rpCkFF1.config(state="normal")
            self.rpCkFF12.config(state="normal")
            self.rpCkFF13.config(state="normal")
            self.rpCkFF2.config(state="normal")
            self.rpCkFF22.config(state="normal")
            self.rpCkFF23.config(state="normal")

    def update_ff_dev_children(self):
        if self.check_ff_dev.get() == 0:
            self.rpCkFFD1.config(state="disabled")
            self.rpCkFFD12.config(state="disabled")
            self.rpCkFFD13.config(state="disabled")
            self.rpCkFFD2.config(state="disabled")
            self.rpCkFFD22.config(state="disabled")
            self.rpCkFFD23.config(state="disabled")
        elif self.check_ff_dev.get() == 1:
            self.rpCkFFD1.config(state="normal")
            self.rpCkFFD12.config(state="normal")
            self.rpCkFFD13.config(state="normal")
            self.rpCkFFD2.config(state="normal")
            self.rpCkFFD22.config(state="normal")
            self.rpCkFFD23.config(state="normal")

    def update_ff_nightly_children(self):
        if self.check_ff_nightly.get() == 0:
            self.rpCkFFN1.config(state="disabled")
            self.rpCkFFN12.config(state="disabled")
            self.rpCkFFN13.config(state="disabled")
            self.rpCkFFN2.config(state="disabled")
            self.rpCkFFN22.config(state="disabled")
            self.rpCkFFN23.config(state="disabled")
        elif self.check_ff_nightly.get() == 1:
            self.rpCkFFN1.config(state="normal")
            self.rpCkFFN12.config(state="normal")
            self.rpCkFFN13.config(state="normal")
            self.rpCkFFN2.config(state="normal")
            self.rpCkFFN22.config(state="normal")
            self.rpCkFFN23.config(state="normal")

    def update_ff_profile_children(self):
        if self.CkFFP.get() == 0:
            self.rpCkFFP1.config(state="disabled")
            self.rpDetail.config(state="disabled")
        elif self.CkFFP.get() == 1:
            self.rpCkFFP1.config(state="normal")
            self.rpDetail.config(state="normal")

    def update_multirow_children(self):
        if self.CkMR.get() == 0:
            self.fpCkMR1.config(state="disabled")
            self.fpCkMR2.config(state="disabled")
            self.fpCkMR1E.config(state="disabled")
            self.fpCkMR1C.config(state="disabled")
        elif self.CkMR.get() == 1:
            self.fpCkMR1.config(state="normal")
            self.fpCkMR2.config(state="normal")
            if self.RdMR.get() == 1:
                self.fpCkMR1E.config(state="disabled")
                self.fpCkMR1C.config(state="disabled")
            elif self.RdMR.get() == 0:
                self.fpCkMR1E.config(state="normal")
                self.fpCkMR1C.config(state="normal")

    def update_multirow_spinbox(self):
        if self.RdMR.get() == 1:
            self.fpCkMR1E.config(state="disabled")
            self.fpCkMR1C.config(state="disabled")
        elif self.RdMR.get() == 0:
            self.fpCkMR1E.config(state="normal")
            self.fpCkMR1C.config(state="normal")

    def update_focus_tab_children(self):
        if self.CkFT.get() == 0:
            self.fpCkFTD.config(state="disabled")
            self.fpCkFTDE.config(state="disabled")
        elif self.CkFT.get() == 1:
            self.fpCkFTD.config(state="normal")
            self.fpCkFTDE.config(state="normal")

    def update_megabar_check(self):
        if self.CkMB.get() == 0:
            self.fpCkMB1.config(state="disabled")
        elif self.CkMB.get() == 1:
            self.fpCkMB1.config(state="normal")

    def update_tabs_below_check(self):
        if self.CkTB.get() == 0:
            self.fpCkTB1.config(state="disabled")
        elif self.CkTB.get() == 1:
            self.fpCkTB1.config(state="normal")

    # This method will call the required functions to patch the root and profile folders
    def install_patch(self):
        errors_found = 0

        # We handle the choices below
        # v v v v v v v v v v v v v v v v v v v

        # Create the config element to store the installed paths
        config_file = configparser.ConfigParser()
        config_file['FIREFOX_ROOT_PATH'] = {}
        config_file['FIREFOX_PROFILE_PATH'] = {}

        # This is the call for Firefox Stable functions
        if self.check_ff.get() == 1:
            firefox_version = "Firefox"
            firefox_root = self.rpCkFF12.get()
            firefox_profile = self.rpCkFF22.get()
            firefox_error = 0
            firefox_error += self.copy_root_files(firefox_root, firefox_version)
            firefox_error += self.copy_profile_files(firefox_profile, firefox_version)
            if firefox_error == 0:
                config_file['FIREFOX_ROOT_PATH'][FF_STABLE] = firefox_root
                config_file['FIREFOX_PROFILE_PATH'][FF_STABLE] = firefox_profile
            errors_found += firefox_error

        # This is the call for Firefox Nightly functions
        if self.check_ff_dev.get() == 1:
            firefox_dev_version = "Firefox Developer"
            firefox_dev_root = self.rpCkFFD12.get()
            firefox_dev_profile = self.rpCkFFD22.get()
            firefox_error = 0
            firefox_error += self.copy_root_files(firefox_dev_root, firefox_dev_version)
            firefox_error += self.copy_profile_files(firefox_dev_profile, firefox_dev_version)
            if firefox_error == 0:
                config_file['FIREFOX_ROOT_PATH'][FF_DEV] = firefox_dev_root
                config_file['FIREFOX_PROFILE_PATH'][FF_DEV] = firefox_dev_profile
            errors_found += firefox_error

        # This is the call for Firefox Nightly functions
        if self.check_ff_nightly.get() == 1:
            firefox_nightly_version = "Firefox Nightly"
            firefox_nightly_root = self.rpCkFFN12.get()
            firefox_nightly_profile = self.rpCkFFN22.get()
            firefox_error = 0
            firefox_error += self.copy_root_files(firefox_nightly_root, firefox_nightly_version)
            firefox_error += self.copy_profile_files(firefox_nightly_profile, firefox_nightly_version)
            if firefox_error == 0:
                config_file['FIREFOX_ROOT_PATH'][FF_NIGHTLY] = firefox_nightly_root
                config_file['FIREFOX_PROFILE_PATH'][FF_NIGHTLY] = firefox_nightly_profile
            errors_found += firefox_error

        # Make sure that folder exists and create/update the file
        try:
            if not os.path.exists(qn_folder):
                os.mkdir(qn_folder)
            with open(ff_paths_ini, 'w', encoding='utf-8') as configfile:
                config_file.write(configfile)
        except OSError:
            messagebox.showerror("Error saving last used paths",
                                 "There was an error while storing the last "
                                 + "used paths for the next patching.")

        # This installs functions for each of the selected Profile folders
        errors_found += self.install_profile_files()

        if errors_found == 0:
            messagebox.showinfo("Patching complete",
                                "The patching is complete."
                                + "\nRestart Firefox for changes "
                                + "to take effect.")
        elif errors_found < 0:
            return

        self.check_ff_stable_patch()
        self.check_ff_dev_patch()
        self.check_ff_nightly_patch()

    def install_profile_files(self):
        values = []
        errors_found = 0
        if self.CkFFP.get() == 1:
            for y in self.rpCkFFP1.curselection():
                values.append(self.rpCkFFP1.get(y))

            if self.CkMR.get() == 0 and self.CkTB.get() == 0 and self.CkMB.get() == 0 \
                    and self.CkFT.get() == 0 and self.CkUT.get() == 0:
                messagebox.showerror("Nothing happened",
                                     "You need to select at least "
                                     + "one function to install.")
                return -1

            for x in values:
                ff_sel_profile = x
                # We get the name of the profile here
                splitter = x.split("/")

                if OS_IN_USE == "Windows":
                    splitter = x.split("\\")

                ff_sel_version = splitter[-1].split(".")[-1]

                errors_found += self.copy_profile_files(ff_sel_profile, ff_sel_version)

        if (self.CkFFP.get() == 0 and self.check_ff_dev.get() == 0 and self.check_ff_nightly.get() == 0
            and self.check_ff.get() == 0) or \
                (self.CkFFP.get() == 1 and self.check_ff_nightly.get() == 0 and self.check_ff.get() == 0
                 and self.check_ff_dev.get() == 0 and values == []):
            messagebox.showerror("No profile selected",
                                 "You need to select at least "
                                 + "one profile to patch.")
            return -1
        return errors_found


    def prompt_what_to_unpatch(self):
        """Prompts for what to unpatch"""
        should_remove_all = False
        abort_unpatch = False
        if (self.check_ff.get() + self.check_ff_dev.get() + self.check_ff_nightly.get() == 1):
            should_remove_all = messagebox.askyesno("Remove all?",
                                                    "Do you want to remove all files installed "
                                                    + "(both the patch and the functions)?")
            abort_unpatch = self.prompt_for_unpatch_abort(should_remove_all)
        elif self.check_ff.get() == 1 and (self.check_ff_nightly.get() + self.check_ff_dev.get() == 1):
            should_remove_all = messagebox.askyesno("Remove all",
                                                    "This will remove all the patch files from the selected "
                                                    + "Firefox installations.\nIs that okay?")
            abort_unpatch = self.prompt_for_unpatch_abort(should_remove_all)
        elif self.CkFFP.get() == 1 and self.check_ff.get() + self.check_ff_nightly.get() \
                + self.check_ff_dev.get() == 0:
            should_remove_all = False
        elif self.CkFFP.get() == 0 and not self.rpCkFFP1.curselection():
            messagebox.showerror("No option selected",
                                 "You need to select at least one Firefox installation"
                                 + "\nor profile folder to remove it's installed patch.")
            abort_unpatch = True
        return abort_unpatch, should_remove_all

    def prompt_for_unpatch_abort(self, should_remove_all):
        """Prompts for aborting the unpatch process if they don't want to patch the functions"""

        if should_remove_all is False:
            should_remove_funcs = messagebox.askyesno("Function removal",
                                                        "Do you only want to remove the selected functions?")
            if should_remove_funcs is False:
                return True

    def check_elements_to_unpatch(self):
        """Returns the root elements and profiles to remove the patch from"""

        roots_to_remove = []
        profiles_to_remove = []
        if self.check_ff.get() == 1:
            roots_to_remove.append(self.rpCkFF12.get())
            profiles_to_remove.append(self.rpCkFF22.get())

        if self.check_ff_dev.get() == 1:
            roots_to_remove.append(self.rpCkFFD12.get())
            profiles_to_remove.append(self.rpCkFFD22.get())

        if self.check_ff_nightly.get() == 1:
            roots_to_remove.append(self.rpCkFFN12.get())
            profiles_to_remove.append(self.rpCkFFN22.get())

        if self.CkFFP.get() == 1:
            for y in self.rpCkFFP1.curselection():
                profiles_to_remove.append(self.rpCkFFP1.get(y))
        return roots_to_remove, profiles_to_remove


    def show_unpatch_result(self, profiles_to_remove):
        """Shows information about the unpatch process to the user"""

        if self.CkFFP.get() == 1 and self.check_ff_nightly.get() \
                + self.check_ff.get() + self.check_ff_dev.get() == 0:
            if profiles_to_remove:
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


    def remove_functions_from_profile(self, profile, func_dict, remove_all):
        """Remove functions from a dictionary from the profile folder"""

        for key in func_dict:
            if remove_all or func_dict[key]:
                remove_function(profile, key)


    # This method will call the required functions to remove the patch
    def unpatch(self):
        abort_unpatch, should_remove_all = self.prompt_what_to_unpatch()

        if abort_unpatch:
            return

        # Get elements to be removed
        roots_to_remove, profiles_to_remove = self.check_elements_to_unpatch()
        func_dict = {
                "Multirow": self.CkMR.get() == 1,
                "Tabs-below": self.CkTB.get() == 1,
                "Megabar": self.CkMB.get() == 1,
                "Focus-tab": self.CkFT.get() == 1,
                "Unread-state": self.CkUT.get() == 1
            }

        if should_remove_all:
            for x in roots_to_remove:
                erase_patch(x, None)

            for z in profiles_to_remove:
                erase_patch(None, z)
                self.remove_functions_from_profile(z, func_dict, True)
        else:
            # Remove functions if they were ticked for the selected profiles
            for z in profiles_to_remove:
                self.remove_functions_from_profile(z, func_dict, False)

        self.show_unpatch_result(profiles_to_remove)

        self.check_ff_stable_patch()
        self.check_ff_dev_patch()
        self.check_ff_nightly_patch()

    # We check the patch status with these methods
    def check_ff_stable_patch(self):
        if root == NOT_FOUND_MESSAGE:
            self.ff_stable_patch_status.config(text=self.NOT_INSTALLED_LABEL)
        else:
            self.ff_stable_patch_status.config(text=self.NOT_PATCHED_LABEL, fg=self.RED_COLOR)
        if os.access(os.path.normpath(self.rpCkFF12.get() + CONFIG_JS_ROOT_FILE), os.F_OK) and \
                os.access(os.path.normpath(self.rpCkFF12.get() + CONFIG_PREFS_FILE), os.F_OK):
            if os.access(os.path.normpath(self.rpCkFF22.get() + CHROME_FOLDER + UTILS_FOLDER), os.F_OK):
                self.ff_stable_patch_status.config(text=self.PATCHED_LABEL, fg=self.GREEN_COLOR)
            else:
                self.ff_stable_patch_status.config(text=self.PROFILE_NOT_PATCHED_LABEL, fg=self.RED_COLOR)
        elif os.access(os.path.normpath(self.rpCkFF22.get() + CHROME_FOLDER + UTILS_FOLDER), os.F_OK):
            self.ff_stable_patch_status.config(text=self.ROOT_NOT_PATCHED_LABEL, fg=self.RED_COLOR)

    def check_ff_dev_patch(self):
        if root_dev == NOT_FOUND_MESSAGE:
            self.ff_dev_patch_status.config(text=self.NOT_INSTALLED_LABEL)
        else:
            self.ff_dev_patch_status.config(text=self.NOT_PATCHED_LABEL, fg=self.RED_COLOR)
        if os.access(os.path.normpath(self.rpCkFFD12.get() + CONFIG_JS_ROOT_FILE), os.F_OK) and \
                os.access(os.path.normpath(self.rpCkFFD12.get() + CONFIG_PREFS_FILE), os.F_OK):
            if os.access(os.path.normpath(self.rpCkFFD22.get() + CHROME_FOLDER + UTILS_FOLDER), os.F_OK):
                self.ff_dev_patch_status.config(text=self.PATCHED_LABEL, fg=self.GREEN_COLOR)
            else:
                self.ff_dev_patch_status.config(text=self.PROFILE_NOT_PATCHED_LABEL, fg=self.RED_COLOR)
        elif os.access(os.path.normpath(self.rpCkFFD22.get() + CHROME_FOLDER + UTILS_FOLDER), os.F_OK):
            self.ff_dev_patch_status.config(text=self.ROOT_NOT_PATCHED_LABEL, fg=self.RED_COLOR)

    def check_ff_nightly_patch(self):
        if root_nightly == NOT_FOUND_MESSAGE:
            self.ff_nightly_patch_status.config(text=self.NOT_INSTALLED_LABEL)
        else:
            self.ff_nightly_patch_status.config(text=self.NOT_PATCHED_LABEL, fg=self.RED_COLOR)
        if os.access(os.path.normpath(self.rpCkFFN12.get() + CONFIG_JS_ROOT_FILE), os.F_OK) and \
                os.access(os.path.normpath(self.rpCkFFN12.get() + CONFIG_PREFS_FILE), os.F_OK):
            if os.access(os.path.normpath(self.rpCkFFN22.get() + CHROME_FOLDER + UTILS_FOLDER), os.F_OK):
                self.ff_nightly_patch_status.config(text=self.PATCHED_LABEL, fg=self.GREEN_COLOR)
            else:
                self.ff_nightly_patch_status.config(text=self.PROFILE_NOT_PATCHED_LABEL, fg=self.RED_COLOR)
        elif os.access(os.path.normpath(self.rpCkFFN22.get() + CHROME_FOLDER + UTILS_FOLDER), os.F_OK):
            self.ff_nightly_patch_status.config(text=self.ROOT_NOT_PATCHED_LABEL, fg=self.RED_COLOR)

    # This is the root patcher invoker
    def copy_root_files(self, firefox_root, firefox_version):
        errors_found = 0
        # We check for the root folder structure to exist
        if os.access(firefox_root, os.F_OK) and \
                os.access(os.path.normpath(firefox_root
                                           + DEFAULTS_PREF_FOLDER), os.F_OK):
            apply_base_patch(firefox_root, None)
        else:
            errors_found = 1
            error_msg = firefox_version \
                        + "root folder location is wrong." \
                        + "\nSelect a valid one and try again."
            messagebox.showerror("Error", error_msg)
        return errors_found


    def install_multirow_function(self, firefox_profile):
        """Installs multirow functions on the selected profile folder"""

        # Multirow scrollable
        errors_found = 0
        if self.RdMR.get() == 0:
            if self.CkMR1C.get() == 0:
                errors_found += install_function(firefox_profile,
                                                    "Multirow-scrollable",
                                                    str(self.CkMR1E.get()))
            # Multirow autohide
            else:
                errors_found += install_function(firefox_profile,
                                                    "Multirow-autohide",
                                                    str(self.CkMR1E.get()))
        # If not scrollable, then unlimited
        else:
            errors_found += install_function(firefox_profile,
                                                "Multirow-unlimited")
        return errors_found


    def install_tabs_below_function(self, firefox_profile):
        """Installs the tabs below function on the selected profile folder"""

        errors_found = 0
        if self.CkTB1.get() == 1:
            errors_found += install_function(firefox_profile,
                                                    "Tabs-below-menu-over-tabs")
        else:
            errors_found += install_function(firefox_profile,
                                                "Tabs-below")
        return errors_found


    def install_megabar_function(self, firefox_profile):
        """Installs megabar functions on the selected profile folder"""

        errors_found = 0
        if self.CkMB1.get() == 1:
            errors_found += install_function(firefox_profile,
                                                "Megabar-all-resizing")
        else:
            errors_found += install_function(firefox_profile,
                                                "Megabar-until-focus")
        return errors_found


    def install_profile_functions(self, firefox_profile): 
        # Multirow check
        errors_found = 0
        if self.CkMR.get() == 1:
            errors_found += self.install_multirow_function(firefox_profile)

        # Tabs below
        if self.CkTB.get() == 1:
            errors_found += self.install_tabs_below_function(firefox_profile)

        # Disable megabar resizing
        if self.CkMB.get() == 1:
            errors_found += self.install_megabar_function(firefox_profile)

        # Focus tabs on hover
        if self.CkFT.get() == 1:
            errors_found += install_function(firefox_profile,
                                                "Focus-tab",
                                                str(self.CkFTDE.get()))

        # Set unread state on tabs
        if self.CkUT.get() == 1:
            errors_found += install_function(firefox_profile,
                                                "Unread-state")
        return errors_found

    # This is the profile functions copying invoker
    def copy_profile_files(self, firefox_profile, firefox_version):
        errors_found = 0
        # We check for the profile folder to exist
        if os.access(firefox_profile, os.F_OK):
            apply_base_patch(None, firefox_profile)

            # We then check for function selections

            # Multirow check
            errors_found += self.install_profile_functions(firefox_profile)
        else:
            errors_found = 1
            error_msg = firefox_version \
                        + "profile folder location is wrong." \
                        + "\nSelect a valid one and try again."
            messagebox.showerror("Error", error_msg)
        return errors_found


def start_ui():
    """Starts the window interface"""

    quantum_nox_window = tkinter.Tk()
    quantum_nox_window.resizable(False, False)
    if OS_IN_USE == "Windows":
        quantum_nox_window.iconbitmap(os.path.normpath(CURRENT_WORKING_DIR + '/icon.ico'))
    else:
        logo = PhotoImage(file=os.path.normpath(CURRENT_WORKING_DIR + '/icon.gif'))
        quantum_nox_window.call('wm', 'iconphoto', quantum_nox_window._w, logo)
    PatcherUI()
    quantum_nox_window.title("Quantum Nox - Firefox Patcher")
    quantum_nox_window.mainloop()


# We add command line arguments support here
parser = argparse.ArgumentParser()

# We define some default variables here
developerIsDefault = (os.access(root_dev, os.F_OK) and
                      not os.access(root_nightly, os.F_OK) and
                      not os.access(root, os.F_OK))
devOverNightly = (os.access(root_dev, os.F_OK) and
                  os.access(root_nightly, os.F_OK) and
                  not os.access(root, os.F_OK))
nightlyIsDefault = (os.access(root_nightly, os.F_OK) and
                    not os.access(root, os.F_OK) and
                    not os.access(root_dev, os.F_OK))

if developerIsDefault or devOverNightly:
    defaultCLRoot = root_dev
    defaultCLProfile = dev_profile
elif nightlyIsDefault:
    defaultCLRoot = root_nightly
    defaultCLProfile = nightly_profile
else:
    defaultCLRoot = root
    defaultCLProfile = stable_profile

ACCEPTABLE_VALUES = "Acceptable values: "

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
                         + ACCEPTABLE_VALUES
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
                         + ACCEPTABLE_VALUES
                         + "1 (titlebar on top), 2 (titlebar above tabs).",
                    type=int, choices=[1, 2], default=1)

# Megabar resize disabler arguments
parser.add_argument("-mb", "--megabar",
                    help="Installs the megabar resize disabler function "
                         + "(Disables the resizing until focusing the megabar by default).",
                    action="store_true")
parser.add_argument("-mbv", "--megabar-version",
                    help="Changes the options of megabar resize disabler. "
                         + ACCEPTABLE_VALUES
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
args_in_use = (CLArgs.multirow or CLArgs.unread_state
               or CLArgs.focus_tab or CLArgs.tabs_below
               or CLArgs.megabar or CLArgs.remove
               or CLArgs.remove_all)

# We set the actions for command line arguments here
if CLArgs.root:
    if CLArgs.root.capitalize() == "Stable":
        CLArgs.root = root
    elif CLArgs.root.capitalize() == "Developer":
        CLArgs.root = root_dev
    elif CLArgs.root.capitalize() == "Nightly":
        CLArgs.root = root_nightly
    if not os.access(CLArgs.root, os.F_OK) and args_in_use:
        print("The root path " + CLArgs.root + " was incorrect.")
        sys.exit()
    if not CLArgs.silent and args_in_use:
        print("Using " + CLArgs.root + " as root path.")
if CLArgs.profile:
    if CLArgs.root.capitalize() == "Stable":
        CLArgs.profile = stable_profile
    elif CLArgs.root.capitalize() == "Developer":
        CLArgs.root = dev_profile
    elif CLArgs.root.capitalize() == "Nightly":
        CLArgs.profile = nightly_profile
    if not os.access(CLArgs.profile, os.F_OK) and args_in_use:
        print("The profile path " + CLArgs.profile + " was incorrect.")
        sys.exit()
    if not CLArgs.silent and args_in_use:
        print("Using " + CLArgs.profile + " as profile path.")

# Errors control variable
CLError = 0

# First we check for remove modes
if CLArgs.remove_all:
    CLError += erase_patch(CLArgs.root, CLArgs.profile)
    CLError += remove_function(CLArgs.profile, "Multirow")
    CLError += remove_function(CLArgs.profile, "Tabs-below")
    CLError += remove_function(CLArgs.profile, "Megabar")
    CLError += remove_function(CLArgs.profile, "Focus-tab")
    CLError += remove_function(CLArgs.profile, "Unread-state")
    if not CLArgs.silent and CLError == 0:
        print("All patch files were removed")
elif CLArgs.remove:
    if CLArgs.multirow:
        CLError += remove_function(CLArgs.profile, "Multirow")
        if not CLArgs.silent and CLError == 0:
            print("Multirow uninstalled.")
    if CLArgs.tabs_below:
        CLError += remove_function(CLArgs.profile, "Tabs-below")
        if not CLArgs.silent and CLError == 0:
            print("Tabs below uninstalled.")
    if CLArgs.megabar:
        CLError += remove_function(CLArgs.profile, "Megabar")
        if not CLArgs.silent and CLError == 0:
            print("Megabar resize disabler uninstalled.")
    if CLArgs.focus_tab:
        CLError += remove_function(CLArgs.profile, "Focus-tab")
        if not CLArgs.silent and CLError == 0:
            print("Focus tab on hover uninstalled.")
    if CLArgs.unread_state:
        CLError += remove_function(CLArgs.profile, "Unread-state")
        if not CLArgs.silent and CLError == 0:
            print("Unread state tagging uninstalled.")

# If none of the remove modes are specified, we enter
# install mode
else:
    # We first make sure that the profile and root
    # folders are patched
    if args_in_use:
        apply_base_patch(CLArgs.root, CLArgs.profile)

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
        CLError += install_function(CLArgs.profile,
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
        CLError += install_function(CLArgs.profile,
                                    CLTBVersion)
        if not CLArgs.silent and CLError == 0:
            print("Tabs below installed.")

    if CLArgs.megabar:
        CLError = 0
        if CLArgs.megabar_version == 1:
            CLTBVersion = "Megabar-until-focus"
        else:
            CLTBVersion = "Megabar-all-resizing"
        CLError += install_function(CLArgs.profile,
                                    CLTBVersion)
        if not CLArgs.silent and CLError == 0:
            print("Megabar resize disabler installed.")

    if CLArgs.focus_tab:
        CLError = 0
        CLFTDelay = str(CLArgs.focus_tab_options)
        CLError += install_function(CLArgs.profile,
                                    "Focus-tab",
                                    CLFTDelay)
        if not CLArgs.silent and CLError == 0:
            print("Focus tab on hover installed.")

    if CLArgs.unread_state:
        CLError = 0
        CLError += install_function(CLArgs.profile,
                                    "Unread-state")
        if not CLArgs.silent and CLError == 0:
            print("Unread state tagging installed.")

# For debugging purposes
if CLArgs.print_defaults:
    ROOT_LOG = " - Root: "
    PROFILE_LOG = " - Profile: "
    print("Firefox stable:")
    print(ROOT_LOG + root)
    print(PROFILE_LOG + stable_profile)
    print("\nFirefox developer:")
    print(ROOT_LOG + root_dev)
    print(PROFILE_LOG + dev_profile)
    print("\nFirefox Nightly:")
    print(ROOT_LOG + root_nightly)
    print(PROFILE_LOG + nightly_profile)
    input("Press enter to exit.")
    sys.exit()

# GUI initializator
if __name__ == '__main__' and not args_in_use:
    start_ui()
