[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=1
HideExtractAnimation=1
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles
[Strings]
InstallPrompt=
DisplayLicense=
FinishMessage=
TargetName=D:\Documentos\GitHub\Quantum-Nox-Firefox-Dark-Full-Theme\Installers\dist\Quantum-Nox-Installer.exe
FriendlyName=Quantum Nox Installer
AppLaunched=cmd /c FindNonRootID.bat
PostInstallCmd=cmd /c Firefox-Patcher.exe
AdminQuietInstCmd=
UserQuietInstCmd=
FILE0="FindNonRootID.bat"
FILE1="Firefox-Patcher.exe"
[SourceFiles]
SourceFiles0=D:\Documentos\GitHub\Quantum-Nox-Firefox-Dark-Full-Theme\Installers\
SourceFiles1=D:\Documentos\GitHub\Quantum-Nox-Firefox-Dark-Full-Theme\Installers\dist\
[SourceFiles0]
%FILE0%=
[SourceFiles1]
%FILE1%=
