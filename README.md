# ParkingLot
## Allots parking slots to vehicles randomly.

This is a python script takes vehicle number as input from command line and allotes a parking lot to vehicle if not alloted. 
For vehicles alloted a parking slot it returnes the previously alloted slot number along with level of the slot.

Here I used sqlite3 for storing and fetching the parking lot. Sqlite3 is an in-memory database which gives almost same performance as in memory data structures.

Script takes one input and one output as registration number of vehicle. 
For eg - 
if tou want to assign a parking slot to a vehicle : parkinglot.py -i 9854
if tou want to get the assigned parking slot for a vehicle : parkinglot.py -o 9854
for help : parkingslot.py -h


