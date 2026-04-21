Set shell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Run the batch launcher hidden so the user can open the app by double-clicking.
appFolder = fso.GetParentFolderName(WScript.ScriptFullName)
batchFile = appFolder & "\Open_Traffic_Detection_App.bat"

shell.Run "cmd /c """ & batchFile & """", 0, False
