# Weather app

Учебное приложение с использованием api сайта https://openweathermap.org/api , для вывода прогноза погоды в выбранном городе. 

## Quickstart

Run the following commands to bootstrap your environment:

    sudo apt-get install -y git python-venv python-pip
    git clone 
    cd weather-app

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    cp .env

Run the app locally:
    
    python manage.py runserver

Run the app docker:

    git clone 
    cd weather-app
    docker build . --tag docker-weather-app
    docker images
    docker run -p 8004:8001 image_id/image_tag