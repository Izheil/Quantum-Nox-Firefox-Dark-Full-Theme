# Only functionability CSS tweaks

The files contained here contain fixes that will let you alter the default behaviour of Firefox. You can use them as standalone files after patching firefox with [the patcher](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/releases) to use elevated CSS and JS, or you can add them to your own custom `userChrome.css` for them to apply.

If you prefer to go the userChrome way, a base empty `userChrome.css` is included here in case you don't have one already, so that you can use any of the tweaks included here without the need to know much CSS (you will just need to copy the things you want, which have a comment above them with a description of what each does and how to modify them to suit your needs).

If you are using the `userChrome.css` from the dark theme of this repository, add the fixes from the files here in that one instead.

To make it work, it's as simple as copying the function you want to apply at the bottom of `userChrome.css`, place it inside [the chrome folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder) if you hadn't yet, and restart Firefox.

**You can also keep some tweak inside your `userChrome.css` without it being enabled by encasing the lines you don't want to apply between `/*` and `*/`.**

You can find an explanation of what each files does in each folder.

## Installation

All you need to do is paste the tweaks you want to apply inside userChrome.css, and then place this file inside [the chrome folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder) of your Firefox profile.

### Step by step:

* Create an empty userchrome.css file, or right click and "save link as..." [this](https://raw.githubusercontent.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/master/CSS%20tweaks/userChrome.css), naming it `userChrome.css`.
* Type `about:support` in your URL bar, then go to that page.
* Click the "open folder" button inside the "profile folder" section.
* Create a folder named "chrome" in your profile folder if it doesn't exist yet.
* Place "userChrome.css" inside [the chrome folder](https://github.com/Izheil/Quantum-Nox-Firefox-Dark-Full-Theme/wiki/Chrome-and-Root-folders#the-chrome-folder).
* Edit userChrome.css with notepad or any code editor to add the rules that are you interested from any of the files inside these folders.
