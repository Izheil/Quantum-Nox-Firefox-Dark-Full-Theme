@echo off

setlocal enableextensions

echo *****************************************************************************************************
echo * WARNING: THIS WILL OVERWRITE ANY CUSTOM USERCHROME AND USERCONTENT YOU MAY HAVE INSTALLED ALREADY *
echo *****************************************************************************************************

set _SOURCE_FILE="%~dp0Inst_files\*.*"

set _TARGET_USER=%USERNAME%
set _FIREFOX_PROFILES_PATH="C:\Users\%_TARGET_USER%\AppData\Roaming\Mozilla\Firefox\Profiles"

for /f %%f in ('dir /b "%_FIREFOX_PROFILES_PATH:"=%\*.default*"') do (
    echo Copying %_SOURCE_FILE% to "%_FIREFOX_PROFILES_PATH:"=%\%%f"
    xcopy /w /e %_SOURCE_FILE% "%_FIREFOX_PROFILES_PATH:"=%\%%f"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\MultiRowTabLiteforFx.uc.js"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\MultiRowTab-scrollable.uc.js"
    del "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\checkboxes.as.css"
)