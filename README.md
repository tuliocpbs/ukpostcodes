# United Kingdom API Postcodes Validation - [Wikipedia Link](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom)

### Requirements

##### Docker Compose - [Link for instructions](https://docs.docker.com/compose/install/)

### How to Run

###### Execute the commands bellow in sequence:

`$ git clone https://github.com/tuliocpbs/ukpostcodes.git`

`$ cd ukpostcodes`

`$ sudo sysctl -w vm.max_map_count=262144` # Necessary for Elasticsearch stay up

`$ docker-compose up -d`

### How to interact with API

###### Access `API Swagger Endpoint` : <http://localhost:8080/api/docs/>

### Monitoring with Elastic APM

> Wait for Kibana be up

###### Access `APM app on Kibana ` : <http://localhost:5601/app/apm>

### How to run the tests

###### Execute the commands bellow:

`$ pyenv virtualenv 3.7.0 uk-postcode` # Create virtualenv with pyenv tool

`$ pyenv activate uk-postcode` # Active virtualenv

`$ pip install -r requirements/requirements-dev.txt`

`$ python -m pytest postcode`
