# CKAN-Auto_Assign_Users_RCIIMS
AutoAssignUsers.py automatically assigns new users to become members of Groups (Topics) and the RCIIMS organization. Setting up a cron job to automatically execute this process once a minute will allow new users to quickly start creating private datasets without requiring an admin the add the new users to Groups and RCIIMS organization themselves.

## Steps to set up process
<b>1)</b> Active your CKAN virtual environment by running ". /usr/lib/ckan/default/bin/activate" on the command prompt.<br><br>
<b>2)</b> Install CKAN API Python package if not already your CKAN virtual environment by running "pip install ckanapi" on the command prompt.<br><br>
<b>3)</b> Download the AutoAssignUsers.py from Github by running "git clone https://github.com/tyryrich/CKAN-Auto_Assign_Users_RCIIMS.git" on the command prompt in an appropriate directory.<br><br>
<b>4)</b> Automate this process (execute once every minute) by setting up a new cron job. To do this open crontab by running "crontab -e" on the command prompt. Copy/paste "* * * * * /usr/bin/python3 /full/path/to/UserAutoAssign.py" (of course change the path to match the directory that UserAutoAssign.py is in.
