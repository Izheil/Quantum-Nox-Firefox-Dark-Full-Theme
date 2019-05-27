@echo off

setlocal enableextensions

echo *******************************************************************************************************************
echo * WARNING: THIS WILL DELETE EVERYTHING INSIDE YOUR FIREFOX CHROME FOLDER, LIKE ANY CUSTOM USERCHROME YOU MAY HAVE *
echo *******************************************************************************************************************

set _TARGET_USER=%USERNAME%
set _FIREFOX_PROFILES_PATH="C:\Users\%_TARGET_USER%\AppData\Roaming\Mozilla\Firefox\Profiles"

:PROMPT
SET /P AREYOUSURE=Are you sure (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

for /f %%f in ('dir /b "%_FIREFOX_PROFILES_PATH:"=%\*.default*"') do (
    echo Deleting all files inside "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\addons.css"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\checkboxes.as.css"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\scrollbars.as.css"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\Sync-tabs-sidebar.as.css"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\tooltips.as.css"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\userChrome.css"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\userContent.css"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\MultiRowTabLiteforFx.uc.js"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\MultiRowTab-scrollable.uc.js"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\MultiRowTabLiteforFx-TabsBelow.uc.js"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\MultiRowTab-scrollable-TabsBelow.uc.js"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\userChrome.xml"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\setAttribute_unread.uc.js"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\Tabs-below-Menu-onTop.as.css"
)

:END
endlocal