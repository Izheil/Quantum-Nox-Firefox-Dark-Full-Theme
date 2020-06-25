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

On Windows you can run it double clicking the file when having python installed, or through the console (asuming you opened the console where the .py file is):

```
python3 Quantum-Nox-Installer.py
```

### Linux

On Linux, you can run it in the same way as Windows (asuming you opened the console where the .py file is):

```
python3 ./Quantum-Nox-Installer.py
```

### Mac

On Mac you only need to run the file with elevated privileges (asuming you opened the console where the .py file is):

```
python3 Quantum-Nox-Installer.py
```

### To create an executable:

To create an executable you only need to use **pyinstaller** with one of the `.spec` files provided here for each major operative system.

To do this first install pyinstaller module if you don't have it yet:

```
pip3 install pyinstaller
```

After that you will be able to use it to create an executable with the correct `.spec` file that applies. 
For example, for windows, you'll have to use `Windows.spec` file to create the installer:

```
pyinstaller Windows.spec
```

Note that the process for Mac requires an extra step, which is bundling the created executable from pyinstaller using the `Platypus-bundling.zsh` as the script to input on [platypus](https://sveinbjorn.org/platypus).

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