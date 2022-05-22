# MaskProgect

<h1>Getting Started</h1>
<p>These instructions will get you a copy of the project up and running on your local machine.</p>

<h2>Prerequisites</h2>
<code>python==3.7 or 3.8</code>

<h2>Installation</h2>
<h3>1. Clone the Repo</h3>
<p>Clone repo using git:</p>

    git clone https://github.com/rondi201/MaskProgect.git
<p>or simply download using the url below:</p>
<code>https://github.com/rondi201/MaskProgect.git</code>
<p>and go to the project directory.</p>
<h3>2. Setup pipenv & Install Requirements</h3>

    pip install pipenv 
    pipenv install -r requirements.txt
    pipenv shell

<h3>3. Open server directory</h3>
<p>Go to server directory:</p>
<code>MaskProgect/src</code>
<h3>4. Migrate Database</h3>

    python manage.py makemigrations
    python manage.py migrate

<h3>5. Make admin</h3>
<p>To use admin panel you need to create superuser using this command:</p>

    python manage.py createsuperuser

<h2>Usage</h2>
<p>Start server in src directory using this command:</p>

    python manage.py runserver
<p>In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/</p>
