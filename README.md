# PyNOGS

## Requirements
You will need to configure [SatNOGS Network API](https://satnogs.org/2014/10/30/api-on-satnogs-network/), which needs [docker](https://docs.docker.com/get-started/get-docker/#installation) and [docker-compose](https://docs.docker.com/compose/install/).

Then, clone source code from the [repository](https://gitlab.com/librespacefoundation/satnogs/satnogs-db):

    git clone https://gitlab.com/librespacefoundation/satnogs/satnogs-db.git
    cd satnogs-db

Configure settings by setting environmental variables

    cp env-dist .env

Install frontend dependencies with npm and test & copy the newly downloaded static asset

    npm install
    ./node_modules/.bin/gulp

Run satnogs-db

    docker-compose up -d --build
