  <h1>Internet Access Scheduler</h1>

  <p>This repository contains scripts designed to manage internet access for the Edge and Chrome browsers on a Windows system. The application uses batch files and a Python script to enable or disable internet access based on the time of day. Task Scheduler is used to automate the execution of the Python script at startup.</p>

  <h2>Files</h2>

  <h3><code>DisFirewallRule.bat</code></h3>
  <p>Disables firewall rules for Chrome and Edge, effectively blocking their internet access.</p>
  <pre><code>netsh advfirewall firewall set rule name="chromeOu" new enable=no
netsh advfirewall firewall set rule name="edgeOu" new enable=no</code></pre>

  <h3><code>EnaFirewallRule.bat</code></h3>
  <p>Enables firewall rules for Chrome and Edge, allowing them to access the internet.</p>
  <pre><code>netsh advfirewall firewall set rule name="chromeOu" new enable=yes
netsh advfirewall firewall set rule name="edgeOu" new enable=yes</code></pre>

  <h3><code>main.py</code></h3>
  <p>A Python script that checks the current time and runs the appropriate batch file to enable or disable internet access for Chrome and Edge.</p>
  <pre><code>import subprocess
from datetime import datetime

def disable_rule():
    subprocess.run(["C:\\Users\\Mohammad\\Desktop\\InternetAccessScheduler\\DisFirewallRule.bat"])

def enable_rule():
    subprocess.run(["C:\\Users\\Mohammad\\Desktop\\InternetAccessScheduler\\EnaFirewallRule.bat"])


current_time = datetime.now().time()
if current_time >= datetime.strptime("04:59:00", "%H:%M:%S").time() and current_time <= datetime.strptime("11:59:00", "%H:%M:%S").time():
    disable_rule()
else:
    enable_rule()</code></pre>

  <h3><code>runner.bat</code></h3>
  <p>A batch file that runs the Python script <code>main.py</code> using the Python interpreter.</p>
  <pre><code>@echo off
python "C:\Users\Mohammad\Desktop\InternetAccessScheduler\main.py"</code></pre>

  <h2>Setup and Usage</h2>

  <ol>
      <li><strong>Setup:</strong>
          <ul>
              <li>Place the batch files and the Python script in the specified paths or adjust the paths in the scripts as needed.</li>
              <li>Ensure Python is installed on your system and is accessible from the command line.</li>
          </ul>
      </li>
      <li><strong>Creating Firewall Rules:</strong>
          <ul>
              <li>Open Windows Defender Firewall with Advanced Security.</li>
              <li>Click on “Outbound Rules” on the left pane.</li>
              <li>Click on “New Rule…” on the right pane.</li>
              <li>Select “Program” and click “Next”.</li>
              <li>Choose “This program path” and browse to the executable for Chrome (usually <code>C:\Program Files\Google\Chrome\Application\chrome.exe</code>) and Edge (usually <code>C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe</code>).</li>
              <li>Select “Block the connection” and click “Next”.</li>
              <li>Name the rule as “chromeOu” for Chrome and “edgeOu” for Edge, and click “Finish”.</li>
          </ul>
        </li>
        <li><strong>Task Scheduler Configuration:</strong>
            <ul>
                <li>Open Task Scheduler.</li>
                <li>Click on “Create Basic Task…” in the right pane.</li>
                <li>Name the task (e.g., “Run Firewall Rule Manager”) and click “Next”.</li>
                <li>Choose “When the computer starts” and click “Next”.</li>
                <li>Choose “Start a program” and click “Next”.</li>
                <li>Browse and select <code>runner.bat</code> and click “Next”.</li>
                <li>Click “Finish” to create the task.</li>
            </ul>
        </li>
        <li><strong>Running the Automation:</strong>
            <ul>
                <li>The <code>runner.bat</code> file will execute the <code>main.py</code> script at system startup, which will check the time and adjust the firewall rules accordingly.</li>
            </ul>
        </li>
    </ol>

  <h2>Requirements</h2>
  <ul>
      <li>Windows operating system with administrative privileges.</li>
      <li>Python installed and properly configured on the system.</li>
  </ul>
