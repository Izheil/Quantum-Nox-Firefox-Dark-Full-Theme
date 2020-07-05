# Context menu fixes

### Context-menu-commands.css

This file contains selectors that target most commands contained in context menus (like send image, reload tab, etc..), so that you can hide them to make your context menus look less cluttered with commands that you may never or rarely use.

**This file is NOT intended to use as-is. You are suposed to delete or comment out the commands that you don't want to hide.**

To comment them out, encase any of the selectors between `/*` and `*/` so that they don't get read, making sure that the last active selector doesn't have any comma (`,`) after it:
```CSS
/* This is a CSS comment */
#This-is-a-selector,
.this-is-a-selector-too
/* #this-is-a-commented-out-selector, */
{display: none}
```

You can hide the following commands from context menus:

* Tab context menu
  * Reload tab.
  * Mute tab.
  * Mute selected tabs.
  * Select all tabs (only the active tab context menu, not the title context menu one).
  * Pin tab.
  * Pin selected tabs.
  * Duplicate tab.
  * Open tab in new window.
  * Send tab to device.
  * Separators left by send tab to device on tabs context menu.
  * Reload selected tabs (only the active tab context menu, not the title context menu one).
  * Bookmark tab.
  * Bookmark selected tabs.
  * Reopen tab in container.
  * Move tab.
  * Close multiple tabs.
  * Close all tabs to the right.
  * Close all other tabs.
  * Close tab.
* Bookmark items context menu
  * Open bookmarked page in a new window.
  * Open bookmarked page in a new private window.
  * Open all bookmarked pages in the bookmark folder.
* Web area context menu
  * Navigation buttons (Back, forward and reload buttons) & it's separator (since you can do the same with the keyboard or other buttons).
  * Send image... (misclicking this when saving an image can happen easily, and waiting for outlook to open to close it gets annoying).
  * Set image as desktop background...
  * Bookmark this page (you can do the same with the star icon on the URL bar, or creating the bookmark manually with more control of where it's going to be placed).
  * Send page...(same as with send image, if you wanted to send something, you'd open your prefered mail yourself).
  * Send video... (same as with send page).
  * Save video capture.
  * Frame selector separator (You can hide it to avoid double separators).
  * Bookmark this link (same as bookmark this page).
  * Send link... (same as send image).
  * Search highlighted word on your default search engine.
  * Open link in new tab (You can do the same middle mouse clicking, or holding ctrl while clicking a link).
  * Open link in a new window.
  * Open link in a private window.
  * Take a screenshot and its separator.
  * Send tab to device and its separators.
  * Send page to device and its separator.
  * Send link to device and its separator.