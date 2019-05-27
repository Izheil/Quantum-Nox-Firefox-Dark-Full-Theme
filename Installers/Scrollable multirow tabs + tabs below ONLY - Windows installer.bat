@echo off

setlocal enableextensions

echo ***************************************************************************************************************
echo * WARNING: THIS WILL OVERWRITE ANY CUSTOM USERCHROME YOU MAY HAVE INSTALLED ALREADY - MORE INFO ON THE README *
echo ***************************************************************************************************************

set _SOURCE_FILE="%~dp0Inst_files\chrome\MultiRowTab-scrollable.uc.js"
set _SOURCE_FILE2="%~dp0Inst_files\chrome\Tabs-below-Menu-onTop.as.css"
set _SOURCE_FILE3="%~dp0Inst_files\chrome\Userchrome.xml"
set _SOURCE_FILE4="%~dp0Patch_files\Userchrome.css"

set _TARGET_USER=%USERNAME%
set _FIREFOX_PROFILES_PATH="C:\Users\%_TARGET_USER%\AppData\Roaming\Mozilla\Firefox\Profiles"

for /f %%f in ('dir /b "%_FIREFOX_PROFILES_PATH:"=%\*.default*"') do (
    echo Copying %_SOURCE_FILE% to "%_FIREFOX_PROFILES_PATH:"=%\%%f"
    xcopy /w /e %_SOURCE_FILE% "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\"
    xcopy /e %_SOURCE_FILE2% "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\"
echo **************************************************************************************************************
echo * THE PATCHED USERCHROME WILL BE COPIED NEXT, EXIT IF YOU DONT WANT YOUR CUSTOM USERCHROME TO BE OVERWRITTEN *
echo **************************************************************************************************************
    xcopy /w /e %_SOURCE_FILE3% "%_FIREFOX_PROFILES_PATH:"=%\%%f\chrome\"
)

