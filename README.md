This is a project I made while following this tutorial
https://www.youtube.com/watch?v=ERMRVORGvZM

There's just one modification I made where I added a second button to execute a different python script. 

To setup local dev environment:
<ol>
  <li>Download latest version of Python</li>
  Get the latest version from here: https://www.python.org/downloads/. <br>
  <b>Note: (I think this is for Windows users only) <br>
  Make sure to add Python to PATH. <br>
  This will add Python as an environment variable so your machine recognizes <code>python</code> or <code>py</code> as a command</b>. <br><br>
  
  <li>Activate the virtual environment</li>
  In a command prompt or git bash, run <code>django_tutorial/Scripts/activate.bat</code> <br><br>
  
  <li>Install Django (and a Python module called 'requests')</li>
  Ensure that virtual environment is active before proceeding. <br>
  Installing Python will also install a package manager called pip. <br>
  Do <code>py -m pip install django</code> <br>
  Do <code>py -m pip install requests</code> <br><br>
  
  <li>Run local server</li>
  <code>cd</code> into directory <code>django_tutorial/buttonpython</code> and run <code>py manage.py runserver</code> <br>
  Your terminal should display the text: <code>Watching for file changes with StatReloader</code> <br>
  
  The web application should now run on localhost:8000 in any browser.
  <img src="https://user-images.githubusercontent.com/67928223/131170174-ef370fe3-a327-4eb9-b476-4e85fc147b55.png" width=50%> <br><br>
  
  <b>Note: If using VSCode IDE, running <code>py manage.py runserver</code> in built-in terminal might not work. <br>
    Run command in an external command prompt or git bash instead.</b>
</ol>
