Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "C:\Users\901191\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\EFS Daily Report.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly\run.bat"
oLink.Arguments = ""
oLink.WorkingDirectory = "C:\Users\901191\Music\Automasi EFS\Generate Daily and Monthly"
oLink.Description = "EFS Daily Health Report AutoRun"
oLink.Save
