## Guessing Game using ChatGPT 3.5

This is a guide on how to deploy the a5-group3-game project on Ubuntu.

## Prerequisites

Before you start, make sure you have the following installed on your system:

- Python 3
- pip3
- nginx

## Installation

To install the necessary dependencies, run the following commands in your terminal:

```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3
sudo pip3 install flask
sudo pip3 install openai
sudo apt install git 
```

## Cloning the Repository

Generate a token (https://github.com/settings/tokens) and clone the a5-group3-game repository using the following command:

```
git clone https://oauth-key-goes-here@github.com/gimgim2326/a5-group3-game.git
```

Confirm if you copied it correctly:

```
ls | grep a5-group3-game
```
Output: a5-group3-game

## Configure the API KEY

Insert your OpenAI API key to the code:

```
cd a5-group3-game && sudo nano app.py
```
Edit the following line/s:
```
        #openai.api_key= "INSERT  API KEY" #<---CHANGE THIS TO YOUR API KEY and Remove # at the beginning
        openai.api_key_path = "api_key.txt" #<---Comment this by adding # at the beginning if you are using the line above
```

## Configuring Apache2

Make sure you are using root folder:

```
cd ~
```

Link the app to Apache root folder:

```
sudo ln -sT ~/a5-group3-game /var/www/html/flaskapp
```

Edit configuration file:

```
sudo nano /etc/apache2/sites-enabled/000-default.conf
```

After the line DocumentRoot /var/www/html add the following code:

```
 WSGIDaemonProcess flaskapp threads=5
        WSGIScriptAlias / /var/www/html/flaskapp/flaskapp.wsgi
        WSGIApplicationGroup %{GLOBAL}
        <Directory flaskapp>
             WSGIProcessGroup flaskapp
             WSGIApplicationGroup %{GLOBAL}
             Order deny,allow
             Allow from all 
        </Directory>
```

## Restarting Apache2

Enable Apache2 at system start up:

```
sudo service apache2 enable
```

Restart Apache2:
```
sudo service apache2 restart
```

## Test the Application

Your application should now be running and accessible at `http://<server-ip>` or `http://<domain-name>`.