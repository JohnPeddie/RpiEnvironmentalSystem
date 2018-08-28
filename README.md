This is a project done by Max Chernotsky, James de Villiers and John Peddie

Code Structure:

Master: main.py

Technical Branch ->inherits main.py from master
	- initialise Pins
	- set defaults

Sensor Branch ->inherits main.py from master
	- temperature sensor
	- voltage sensor
	- light sensor

Display Branch ->inherits main.py from master
	- nice output
	- reset output
	- switches
	
All branches contain all necessary code. The idea is to get main and init working together on the init branch
						            main and sensors working together on sensor branch
							    main and display working together on display

Do not edit code other than the specific .py on each branch as those wont be merged to master
                                                              
Once each branch works perfectly, mains will be merged and init, sensors and display will overwrite what is in master.


Max - testing from Pi
