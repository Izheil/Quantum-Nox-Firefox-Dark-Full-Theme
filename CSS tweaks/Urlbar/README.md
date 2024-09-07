# Urlbar fixes

### Megabar-disabled-all-resizing.as.css
Since Firefox 76, the address bar now resizes when you open a new tab or when it's on focus. This will disable the resizing effect, along with the shadows that come with it.

### Megabar-disabled-until-focus.as.css
Since Firefox 76, the address bar now resizes when you open a new tab or when it's on focus. This will disable the resizing effect until you have focused the urlbar by clicking on it. This means that it won't resize when you for example open a new tab.

At some point they made not resize when the popup isn't open, so this might not be needed anymore.

### Remove-urlbar-icons.as
Since Firefox 89, you can't hide icons from the urlbar, so the only way to hide them is with CSS. The icons included are the bookmarks icon, multi-account containers, and reader mode (the file is intended just to show the rules to copy & paste on your `userChrome.css`, not to be used as-is).

### Urlbar-font.as.css
This changes the font of the urlbar so that it's easier for the user to detect url spoofing. Georgia font is used by default, but you can choose any other one that you want editing the value in the file.
