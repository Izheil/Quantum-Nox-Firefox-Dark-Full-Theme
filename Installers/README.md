# JS function installers
If you don't want to copy the files manually to install multirow, tabs below, or focus tab on hover, you can do it with this installer.
**Make sure your Firefox is up to date, since the userscripts installed with this assume you have the lastest firefox version.**
This is the python version of the installer, which requires all files and folders in here to work. For the single file installer go to the [releases](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases) page.

#### Pre-requisites 
You need [Python 3.6+](https://www.python.org/downloads/release/python-375/) installed to use these, along with the **elevate** module.

In **linux** you might need to install pip (to install the elevate module) and tkinter after installing Python 3.6+, which you can do with these commands respectively:

```
sudo apt install python3-pip
sudo apt-get install python3-tk
```

You will also need to install the required module after installing Python and pip **(on any OS)** using:

```
pip3 install elevate
```

After that you can run `Quantum-Nox-Installer.py` to start the patcher.

### Windows

**To use**:

On Windows you will only have to type (asuming you opened the console where the .py file is):

```
python3 Quantum-Nox-Installer.py
```

**To create an executable** you will need to do 2 steps for windows:

First, you need to create the base patcher:

```
pyinstaller windows.spec
```

After that, if you want to enable support for users that are not using an administrator account when patching (You could just run the created executable with the previous command if you don't need this), you need to bundle `FindNonRootID.bat` along with the `Firefox-patcher.exe`file that will have been created in `dist` folder with the previous command.

To do this, you can use **iexpress**, which is a bat-to-exe conversor that comes built-in into Windows.
By default it's located in `C:\Windows\System32\iexpress.exe`.

Run iexpress as admin, and bundle the bat and the exe into an installer. **Do NOT use the `.sed` file inside the repo when it asks you to use one, unless you change the paths to wherever you placed the repository files**

For the installer to be created properly you will need to **enable long filenames**, and you will need to **add some commands before each file** when it asks you to select them.
So when it asks for the files, select each file and type "cmd /c " before the name of each:

```
cmd /c FindNonRootID.bat
```

```
cmd /c Firefox-patcher.exe
```

### Linux

**To use**:

On Linux, you can run it in the same way as Windows (asuming you opened the console where the .py file is):

```
python3 ./Quantum-Nox-Installer.py
```

**To create an executable**:

```
pyinstaller "Linux.spec"
```

### Mac

**To use**:

On Mac you only need to run the file with elevated privileges (asuming you opened the console where the .py file is):

```
sudo python3 Quantum-Nox-Installer.py
```

**To create an executable** you would use this, but pyinstaller doesn't bundle tkinter correctly with the executable, so you will need to wait for the rewrite of the installer to use this:

```
pyinstaller "Mac.spec"
```

## The functions
You can find more explanations in the folders inside [Multirow and other functions](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Multirow%20and%20other%20functions) folder in this repository.

### Multi-row Tabs

#### Scrollable rows
This version shows all tabs you currently have open splitting them on rows up to a max of 3 rows by default (can be changed using the variable inside the file). After the max number of rows has been reached, a scrollbar will be shown to be able to scroll around the extra tabs.
![Scrollable rows preview](https://i.imgur.com/qqQn4Ky.png)

#### Autohide Scrollable rows
Same as scrollable multirow tabs, but it will autohide the scrollbar when not hovering over the tabs.

#### All rows visible
This version of multirow tabs shows all tabs you currently have open splitting them on rows, without any limit to the amount of rows to show. Choose this option if you want to always see all the tabs you have open without limits to the number of rows.
![Unlimited rows preview](https://i.imgur.com/GWSgqD9.png)

### Tabs below URL bar
These will swap the tab bar position under the URL bar, while keeping the menu bar on top.
![Tabs below preview](https://i.imgur.com/5vbG6mh.png)

### Focus tab on hover
This will activate the tab you hover over with your mouse after the delay you specify.