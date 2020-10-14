# CKAN-Auto_Assign_Users_RCIIMS

## Steps to set up process
<b>1)</b> Active your CKAN virtual environment by running ". /usr/lib/ckan/default/bin/activate" on the command prompt.<br><br>
<b>2)</b> Install CKAN API Python package if not already your CKAN virtual environment by running "pip install ckanapi" on command prompt.<br><br>
<b>3)</b> Run "git clone https://github.com/tyryrich/CKAN-Auto_Assign_Users_RCIIMS.git" on command prompt in appropriate directory.<br>
<b>4)</b> Set up a new cron job by running "crontab -e" on command prompt. Copy/paste "* * * * * /usr/bin/python3 /full/path/to/UserAutoAssign.py" onto crontab file to execute this process once every minute (of course change the path to match the directory that UserAutoAssign.py is in.
