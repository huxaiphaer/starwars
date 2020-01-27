[![Build Status](https://travis-ci.org/huxaiphaer/starwars.svg?branch=master)](https://travis-ci.org/huxaiphaer/starwars)
[![codecov](https://codecov.io/gh/huxaiphaer/starwars/branch/master/graph/badge.svg)](https://codecov.io/gh/huxaiphaer/starwars)

# Star Wars Challenge 

This is an application which lists down star wars and their respective
hyperdrives sorted in an ascending order.


### Requirements for setting up the project.
1. Python3. 
2. Flask
3. Virtualenv. 
4. Redis. 
You need to install redis on your machine, then afterwards you activate it.
This is the command you run on mac ``` brew services start redis```
5. Celery. This is also needed to perform some background processes, for this project, 
celery is already in the `requirements.txt` file.
6. Docker. For easy deployment, you have to download `Docker` for containerizing our application.


### Installation on Mac

 First clone this repository 

```
git clone https://github.com/huxaiphaer/starwars.git
```

Create a `.env` file in the root directory and add the following :

```buildoutcfg
REDIS_CONFIG=redis://redis:6379/0
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=1
REDIS_CHAR_SET=utf-8
REDIS_DECODE_RESPONSE=True
SECRET_KEY=anyname
```


 Then, create a virtual environment and install in on Mac :

```buildoutcfg
virtualenv venv
source venv/bin/activate
```

  After activating the `virtualenv`, then install the necessary dependencies :

```buildoutcfg
pip3 install -r requirements.txt
```

Run docker :
```buildoutcfg
docker-compose up --build
```

Viola , then we can see our application routing to the api endpoint :-)


### Running Tests

Running tests of the project :

```buildoutcfg
nosetests
```

Running tests with coverage :

```buildoutcfg
nosetests --with-coverage
```


### Contributors 

* Lutaaya Huzaifah Idris



