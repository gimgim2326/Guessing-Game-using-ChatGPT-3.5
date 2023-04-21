# a5-group3-game

Pre-requisites:
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install flask
sudo pip3 install openai
sudo pip3 install dotenv
sudo apt-get install nginx
sudo apt-get install gunicorn3

git clone https://github.com/gimgim2326/a5-group3-game.git
cd a5-group3-game

sudo nano /etc/nginx/sites-available/a5-group3-game
server {
        listen 80;
        server_name 18.207.88.68;

        location / {
                proxy_pass http://127.0.0.1:8000;
        }
}

sudo service nginx restart

gunicorn3 app:app