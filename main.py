import subprocess
from datetime import datetime

def disable_rule():
    subprocess.run(["C:\\Users\\Mohammad\\Desktop\\DisFirewallRule.bat"])

def enabel_rule():
    subprocess.run(["C:\\Users\\Mohammad\\Desktop\\EnaFirewallRule.bat"])

# Check if the current time is between 5:00 AM and 12:00 PM
current_time = datetime.now().time()
if current_time >= datetime.strptime("04:59:00", "%H:%M:%S").time() and current_time <= datetime.strptime("11:59:00", "%H:%M:%S").time():
    disable_rule()
else :
    enabel_rule()
