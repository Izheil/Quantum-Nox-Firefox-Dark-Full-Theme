#!/bin/bash
sudo mv ./scrollbars.css /usr/lib/firefox/browser
sudo sh -c 'echo "override chrome://global/skin/scrollbars.css scrollbars.css" > /usr/lib/firefox/browser/chrome.manifest'
