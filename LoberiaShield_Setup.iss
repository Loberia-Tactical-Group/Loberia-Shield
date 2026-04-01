[Setup]
AppName=Loberia Shield XDR
AppVersion=1.0
DefaultDirName={pf}\LoberiaTactical\Shield
DefaultGroupName=Loberia Tactical Group
UninstallDisplayIcon={app}\LoberiaShield.exe
Compression=lzma
SolidCompression=yes
OutputDir=userdocs:Loberia_Output

[Files]
; Aquí va tu ejecutable compilado por PyInstaller
Source: "dist\LoberiaShield_XDR.exe"; DestDir: "{app}"; Flags: ignoreversion
; Aquí creamos la base de datos de cuarentena
Source: "shield\core\*"; DestDir: "{app}\core"; Flags: ignoreversion recursesubdirs

[Dirs]
Name: "C:\Loberia_Shield\Quarantine"; Permissions: authusers-modify

[Icons]
Name: "{group}\Loberia Shield"; Filename: "{app}\LoberiaShield_XDR.exe"
Name: "{commondesktop}\Loberia Shield"; Filename: "{app}\LoberiaShield_XDR.exe"

[Run]
; Esto hace que el antivirus se inicie solo al terminar la instalación
Filename: "{app}\LoberiaShield_XDR.exe"; Description: "Lanzar Loberia Shield"; Flags: nowait postinstall skipfs

[Registry]
; Iniciar con Windows (HKEY_CURRENT_USER)
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "LoberiaShield"; ValueData: "{app}\LoberiaShield_XDR.exe"; Flags: uninsdeletevalue

; Registrar como Servicio de Recuperación en el sistema
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Services\LoberiaShield"; ValueType: dword; ValueName: "Start"; ValueData: 2; Flags: uninsdeletekey
