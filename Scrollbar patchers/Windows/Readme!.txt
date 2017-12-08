SCROLLBAR PATCHERS
-------------------

Which one to use and how:

If using for the first time, make sure that the "scrollbars.css" file is in the same folder as the .bat files, and then apply the "First time patch".

After this, you should only need to apply the re-patcher after each firefox update (No need to have the scrollbars.css file to re-patch).

 - Use Scrollbars re-patcher (32-bits) if you have a 64-bits Windows and you are using a 32-bits Firefox.
 - Use Scrollbars re-patcher (64-bits) if you have a 32-bits Windows, or a 64-bits Windows and you are using a 64-bits Firefox.

If you have a program files (x86) on your C: drive, you have a 64-bits Windows

If for some reason you installed firefox in some other drive other than C:, you will have to change the .bat files paths yourself (using notepad or any other code editor).



What each one does:

The "Scrollbars first time patch.bat" adds the line override chrome://global/skin/scrollbars.css scrollbars.css to the chrome.manifest file. It also moves the scrollbars.css file from the folder the batch file is to your firefox root folder (which is why it should only be used the first time only).

The "Scrollbars re-patcher.bat" only edits the chrome.manifest file (just like the first time patch). 
