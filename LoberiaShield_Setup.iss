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
; Corregido: skipifsilent para que no dé error de flag
Filename: "{app}\LoberiaShield_XDR.exe"; Description: "Lanzar Loberia Shield"; Flags: nowait postinstall skipifsilent

[Registry]
; Iniciar con Windows para el usuario actual
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "LoberiaShield"; ValueData: """{app}\LoberiaShield_XDR.exe"""; Flags: uninsdeletevalue

; Nota: Eliminamos la entrada de HKLM por ahora para evitar problemas de permisos en Windows X Lite
; Registrar como Servicio de Recuperación en el sistema
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Services\LoberiaShield"; ValueType: dword; ValueName: "Start"; ValueData: 2; Flags: uninsdeletekey
