## Project Name
F-Farm
## Description
Empowering Livelihoods in Africa through affordable and sustainable Agri Business, through Milq Greenhouse , Net house and Drip irrigation system.

## Setup and installations
Fork the data onto your own personal repository. Clone Project to your machine Activate a virtual environment on terminal:<code> source virtual/bin/activate </code>Install all the requirements found in requirements file. On your terminal run <code>python3.7 manage.py runserver</code> Access the live site using the local host provided.


## Getting started
# Prerequisites

<code>python3.7 virtual environment pip</code>

## Clone the Repo and rename it to suit your needs.
https://github.com/Fridah-Alwanga/Farm

## Initialize git and add the remote repository

git init

git remote add origin <code>your-repository-url</code>

## Create and activate the virtual environment
python3.7 -m virtualenv virtual<code>

source virtual/bin/activate</code>

## Setting up environment variables
<pre><code>
DEBUG=True
DB_NAME='farm'
DB_USER=''
DB_PASSWORD=''
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
</code></pre>

## Install dependancies
Install dependancies that will create an environment for the app to run<code> pip install -r requirements.txt</code>

## Make and run migrations
<pre><code>
python3.7 manage.py check
python manage.py makemigrations news
python3.7 manage.py sqlmigrate news 0001
python3.7 manage.py migrate

</code></pre>

## Run the app
<code>python3.7 manage.py runserver
</code>

## Built With
1. Python3.7
2. Django 2.2.8
3. Postgresql
4. Boostrap
5. HTML
6. CSS

## License
LICENSED UNDER License: MIT
