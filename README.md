# Project 4: Brevet time calculator with Ajax

Reimplementation of the RUSA ACP controle time calculator with flask and ajax.

Credits to Michal Young for the initial version of this code.

## ACP controle times

That's "controle" with an 'e', because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.   

The algorithm for calculating controle times is described here (https://rusa.org/pages/acp-brevet-control-times-calculator). 

Additional background information is given here (https://rusa.org/pages/rulesForRiders).  

This is a replacement of the calculator here (https://rusa.org/octime_acp.html).

## AJAX and Flask implementation

This code fills in times as the input fields are filled using Ajax and Flask. Currently the miles to km (and vice versa) is implemented with Ajax.

Each time a distance is filled in, the corresponding open and close times are filled in with Ajax.

## Testing

To run the server, change to the brevets directory and type:

- $ sudo make start

To exit the server type:

- $ sudo make stop

If you are running the server, type this to enter the docker container:

- $ sudo docker exec -it yeet-default /bin/bash

Once in the container, you can run nosetests like this ( -v for verbose mode ):

- $ nosetests -v

## Authors

Initial version by M Young; Docker version added by R Durairajan; to be revised by CIS 322 students.

Latest updated version by Samuel Lundquist.