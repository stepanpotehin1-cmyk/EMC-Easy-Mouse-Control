[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=0
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=Do you want to install EMC (Easy Mouse Control)?
DisplayLicense=None
FinishMessage=EMC has been installed successfully!
TargetName=EMC-Installer.exe
FriendlyName=EMC - Easy Mouse Control
AppLaunched=cmd /c install.bat
PostInstallCmd=<None>
AdminQuietInstCmd=
UserQuietInstCmd=
SourceFiles=SourceFiles
[SourceFiles]
SourceFiles0=.\
[SourceFiles0]
%FILE0%=EMC.exe
%FILE1%=install.bat
