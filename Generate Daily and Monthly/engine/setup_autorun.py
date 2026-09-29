import os
import sys

def enable_startup(mode="menu"):
    startup_folder = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
    os.makedirs(startup_folder, exist_ok=True)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    run_bat = os.path.join(root_dir, "run.bat")
    
    args = "--silent" if mode == "silent" else ""
    desc = "EFS Daily Health Report AutoRun"
    
    vbs_content = f'''Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "{startup_folder}\\EFS Daily Report.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{run_bat}"
oLink.Arguments = "{args}"
oLink.WorkingDirectory = "{root_dir}"
oLink.Description = "{desc}"
oLink.Save
'''
    vbs_path = os.path.join(root_dir, ".cache", "temp", "make_shortcut.vbs")
    os.makedirs(os.path.dirname(vbs_path), exist_ok=True)
    with open(vbs_path, "w", encoding="utf-8") as f:
        f.write(vbs_content)
        
    os.system(f'cscript //nologo "{vbs_path}"')
    lnk_file = os.path.join(startup_folder, "EFS Daily Report.lnk")
    return os.path.exists(lnk_file)

def disable_startup():
    startup_folder = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
    lnk_file = os.path.join(startup_folder, "EFS Daily Report.lnk")
    if os.path.exists(lnk_file):
        try:
            os.remove(lnk_file)
            return True
        except Exception:
            return False
    return True

def is_startup_enabled():
    startup_folder = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
    return os.path.exists(os.path.join(startup_folder, "EFS Daily Report.lnk"))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "disable":
        print("Disabled:", disable_startup())
    elif len(sys.argv) > 1 and sys.argv[1] == "silent":
        print("Enabled silent:", enable_startup("silent"))
    else:
        print("Enabled menu:", enable_startup("menu"))
