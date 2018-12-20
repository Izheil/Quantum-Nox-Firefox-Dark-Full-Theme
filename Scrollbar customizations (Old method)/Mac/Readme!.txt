SCROLLBAR PATCHERS
-------------------

Which one to use and how:

If using for the first time, make sure that the "scrollbars.css" file is in the same folder as the .bat files, and then apply the "First time patch".

After this, you should only need to apply the re-patcher after each firefox update (No need to have the scrollbars.css file to re-patch).


What each one does:

The "Scrollbars first time patch" adds the line override chrome://global/skin/scrollbars.css scrollbars.css to the chrome.manifest file. It also moves the scrollbars.css file from the folder the shell script file is to your firefox root folder (which is why it should only be used the first time only).

The "Scrollbars re-patcher" only edits the chrome.manifest file (just like the first time patch). 
