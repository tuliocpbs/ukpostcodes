# United Kingdom API Postcodes Validation

### Requirements

##### Docker Compose - [Link for instructions](https://docs.docker.com/compose/install/)

### How to Run

###### Execute the commands bellow in sequence:

`$ git clone https://github.com/tuliocpbs/ukpostcodes.git`

`$ cd ukpostcodes`

`$ sudo sysctl -w vm.max_map_count=262144` # Necessary for Elasticsearch be up

`$ docker-compose up -d`

### How to interact with API

###### Access `API Swagger Endpoint` : <http://localhost:8080/api/docs/>

### How to run the tests

###### Execute the commands bellow:

`$ python -m pytest postcode`
