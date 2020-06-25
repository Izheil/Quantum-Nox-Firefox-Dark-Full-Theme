# Addon UUID replacer
If you don't want to manually change every UUID of the addon files, you should use this installer.
**Make sure your addons are up to date, since addons.css file assume you have the lastest versions.**
This is the python version of the installer, for the executables [Full dark theme](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/tree/master/Full%20dark%20theme) folder.

#### Pre-requisites 
You need [Python 3.6+](https://www.python.org/downloads/release/python-375/) installed to use the python version, along with the **requests** module.

In **linux** you might need to install pip (to install the requests module) after installing Python 3.6+, which you can do with this command:

```
sudo apt install python3-pip

```

You will also need to install the required module after installing Python and pip **(on any OS)** using:

```
pip3 install requests
```

After that you can run `Addons-UUID-replacer.py` to start the patcher.

### Windows

On Windows you can run it double clicking the file when having python installed, or through the console (asuming you opened the console where the .py file is):

```
python3 Addons-UUID-replacer.py
```

### Linux

On Linux, you can run it in the same way as Windows (asuming you opened the console where the .py file is):

```
python3 ./Addons-UUID-replacer.py
```

### Mac

On Mac you only need to run the file with elevated privileges (asuming you opened the console where the .py file is):

```
python3 Addons-UUID-replacer.py
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