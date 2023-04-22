## Guessing Game using ChatGPT 3.5

This is a guide on how to deploy the a5-group3-game project on Ubuntu.

## Prerequisites

Before you start, make sure you have the following installed on your system:

- Python 3
- pip3
- nginx
- gunicorn3

## Installation

To install the necessary dependencies, run the following commands in your terminal:

```
sudo su
sudo apt-get update
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
sudo pip3 install flask
sudo pip3 install openai
sudo apt-get install -y nginx
sudo apt-get install -y gunicorn3
```

## Cloning the Repository

Generate a token (https://github.com/settings/tokens) and clone the a5-group3-game repository using the following command:

```
git clone https://oauth-key-goes-here@github.com/gimgim2326/a5-group3-game.git
```

## Configuring the Environment Variables

Create a `.env` file and insert your OpenAI API key:

```
cd a5-group3-game && sudo nano api_key.txt
```
```
api_key="INSERT_API_KEY_HERE"
```

## Configuring Nginx

Create a new Nginx configuration file:

```
sudo nano /etc/nginx/sites-available/a5-group3-game
```

Add the following configuration to the file:

```
server {
    listen 80;
    server_name <server-ip or domain-name>; # Replace with your server's IP address or domain name
    access_log  /var/log/nginx/example.log;
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Save and exit the file.

## Restarting Nginx

Restart Nginx to apply the new configuration:

```
sudo service nginx restart
```

## Test the Application

Run the following command to test the application using gunicorn3:

```
gunicorn -w 4 --bind 0.0.0.0:8000 wsgi:app
```

Your application should now be running and accessible at `http://<server-ip>/8000` or `http://<domain-name>`.