# Patching Firefox to enable JS injection (userchromeJS)
The files here are a fork of the work of [xiaoxiaoflood](https://github.com/xiaoxiaoflood/firefox-scripts), fixed to work with FF69+, and only loading the necessary things to load external JS and CSS files.

## Installation
You can patch your Firefox using the installer in the [releases](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases) section. The patcher will choose the default profile folder, so if you have more than 1 profile you should go to `about:profiles` and make sure that the path the patcher selects is the same as the one of the profile that you are currently using.

If you are using **Firefox portable, you will need to change the default root and profile folders to the ones of portable Firefox**, so check the [firefox root folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#firefox-root-folder) and [chrome folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder) sections to locate them first.

Alternatively you can follow the explanations below for the manual installation.

### Manual installation
To patch firefox with this method, you will have to locate both [firefox root folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#firefox-root-folder), and your profile [chrome folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder).

If you are using **Firefox portable**, note that the [firefox root folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#firefox-portable-1) is *not* the install path (such as `C:\FirefoxPortable\Firefox`), but 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`{install path}` + `\App\Firefox` (Example: `C:\FirefoxPortable\Firefox\App\Firefox`) or

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`{install path}` + `\App\Firefox64` (Example: `C:\FirefoxPortable\Firefox\App\Firefox64`)


#### Step by step:
  1. Copy `defaults` folder and `config.js` files inside `root` to [firefox root folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#firefox-root-folder).
  2. Copy `utils` folder to your [chrome folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder).

Next time you start up firefox, changes should take effect.

If you did it right, the structure of firefox root folder should look like this:

| Root folder      |
| ---------------- |
| `\browser\`      |
| `\defaults\`     |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`\pref\` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`channel-prefs.js` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`config-prefs.js` |
| `\fonts\`        |
| `\gmp-clearkey\` |
| `\META-INF\`     |
| `\uninstall\`    |
| `config.js`      |
| `firefox.exe` or `firefox` |
| Many other files |

And the structure of the chrome folder should look like:

  * utils (folder)
  * Any other optional file like userChrome.css, userContent.css, MultiRowTabLiteforFx.uc.js, etc...

The files inside the "utils" folder will enable both `*.uc.js` and `*.as.css` files inside your chrome folder.

To override CSS styles that can't be changed in any other way (like for scrollbars, or certain tooltips), you must give the CSS files you want to use the extension `.as.css`, since they won't be read at all if you don't (unless you import them directly through `userChrome.css` with an **@import** rule, but they will be read with the same privileges as userChrome.css).

### Troubleshooting

If after following the above installation some function doesn't seem to be working, you should try [the basic troubleshooting steps](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Troubleshooting) to see what's the problem.