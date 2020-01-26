[![Build Status](https://travis-ci.org/huxaiphaer/starwars.svg?branch=master)](https://travis-ci.org/huxaiphaer/starwars)
[![codecov](https://codecov.io/gh/huxaiphaer/starwars/branch/master/graph/badge.svg)](https://codecov.io/gh/huxaiphaer/starwars)

# Star Wars Challenge 

This is an application which lists down star wars and their respective
hyperdrives sorted in an ascending order.


### Requirements.
1. Python3
2. Flask
3. Virtualenv
4. Redis
5. Celery
6. Docker


### Installation on Mac

 First clone this repository 

```
git clone https://github.com/huxaiphaer/starwars.git
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
 Then build your docker :

```buildoutcfg
docker build -t doc-flask:v1
```

when the building is successful, then run the container :

```buildoutcfg
docker run -p 5000:5000 doc-flask:v1
```
Then finally, route to this endpoint 

```buildoutcfg
http://localhost:5000/api/v1/starwars
```

Viola , then we can see our application routing to the api endpoint :-)



### Contributors 

* Lutaaya Huzaifah Idris



