# Project 4: Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax.

Credits to Michal Young for the initial version of this code.

## ACP controle times

That's "controle" with an 'e', because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.   

The algorithm for calculating controle times is described here (https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here (https://rusa.org/pages/rulesForRiders). The description is ambiguous, but the examples help. Part of finishing this project is clarifying anything that is not clear about the requirements, and documenting it clearly.  

We are essentially replacing the calculator here (https://rusa.org/octime_acp.html). We can also use that calculator to clarify requirements and develop test data.  

## AJAX and Flask reimplementation

The RUSA controle time calculator is a Perl script that takes an HTML form and emits a text page in the above link. 

The implementation that you will do will fill in times as the input fields are filled using Ajax and Flask. Currently the miles to km (and vice versa) is implemented with Ajax. You'll extend that functionality as follows:

* Each time a distance is filled in, the corresponding open and close times should be filled in with Ajax.   

* You'll also implement the logic in acp_times.py based on the algorithm given above. I will leave much of the design to you. You'll turn the implementation that you do. See below for more information.

## Testing

A suite of nose test cases is a requirement of this project. Design the test cases based on an interpretation of rules here (https://rusa.org/pages/acp-brevet-control-times-calculator). Be sure to test your test cases: You can use the current brevet time calculator (https://rusa.org/octime_acp.html) to check that your expected test outputs are correct. While checking these values once is a manual operation, re-running your test cases should be automated in the usual manner as a Nose test suite.

To make automated testing more practical, your open and close time calculations should be in a separate module. Because I want to be able to use my test suite as well as yours, I will require that module be named acp_times.py and contain the two functions I have included in the skeleton code (though revised, of course, to return correct results).

We should be able to run your test suite by changing to the "brevets" directory and typinng "nosetests". All tests should pass. You should have at least 5 test cases, and more importantly, your test cases should be chosen to distinguish between an implementation that correctly interprets the ACP rules and one that does not.

## Replace this README

This README is currently written primarily as instructions to CIS 322 students. Replace it with a proper README for an ACP time calculator. Think about what should be included for users and for developers. If it is growing too long, factor details into one or more separate documents, with references from the README. At the end, add your details.

## Tasks

The code under "brevets" can serve as a starting point. It illustrates a very simple Ajax transaction between the Flask server and javascript on the web page. At present the server does not calculate times. It just returns double the number of miles. Other things may be missing; add them as needed. As before, you should fork and then clone the git repository, make your changes, and turn in the URL of your repository.

You'll turn in your credentials.ini using which we will get the following:

* The working application.

* A README.md file that includes not only identifying information (your name, the path to your application on ix) but but also a revised, clear specification of the brevet controle time calculation rules.

* An automated 'nose' test suite.

* Dockerfile

## Grading Rubric

* If your code works as expected: 100 points. This includes:
	* AJAX in the frontend. That is, open and close times are automatically populated, 
	* Logic in the backend (acp_times.py), and 
	* Frontend to backend interaction (with correct requests/responses).

* If the AJAX logic is not working, 30 points will be docked off. 

* If the acp_times.py file is wrong or is missing in the appropriate location, 30 points will be docked off.

* If none of the functionalities work, 40 points will be given assuming 
    * The credentials.ini is submitted with the correct URL of your repo, and
    * The Dockerfile builds without any errors
    
* If the Dockerfile doesn't build or is missing, 20 points will be docked off.

* If credentials.ini is missing, 0 will be assigned.