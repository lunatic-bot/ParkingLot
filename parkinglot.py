## Two lavels - A and B, each level can accomodate 20 vehicles 1-20, 21-40

## 1. Autometically assign parking lot to a new vehicle
## 2. Retrieve parking spot number output should return level and parking spot number 
# eg - {'level' : A, 'spot' : 19}




## import random to generate random spots
import random
import sqlite3 as sl
import argparse
 

## create a database
connection = sl.connect('parking-slot.db')


## create a table with 3 colums to store vechile number, level and lot number

# with connection:
#     connection.execute("""CREATE TABLE ALLOTEDLOTS (
#             RegNo INTEGER NOT NULL PRIMARY KEY,
#             Level TEXT,
#             LotNo INTEGER
#         );
#     """)


## method to assign random spot to a vehicle
def assign_spot(vehicle_number):
    ''' 
    takes a number as vehicle number and assignes a parking spot from 
    one of the floors from A and B
    '''
    ## get a random spot from all spots between 1-40
    spot = random.randrange(1,41)
    ## if spot is less than 21, assign level 1 otherwise level 2
    if spot < 21:
        level = "A"
    else:
        level = "B"

    ## create a databse entry for this vehicle and parking lot assigned
    sql = 'INSERT OR IGNORE INTO ALLOTEDLOTS (RegNo, Level, LotNo) values(?, ?, ?)'
    with connection:
        connection.execute(sql, (vehicle_number, level, spot))

        


## method to get a random spot for a vehicle
def get_spot(vehicle_number):
    ''' 
    takes a number as vehicle number and returns a parking spot from 
    one of the floors from A and B
    '''

    with connection:
        ## execute query for the given vehicle number
        data = connection.execute(f"SELECT * FROM ALLOTEDLOTS WHERE RegNo =={vehicle_number}")

        ## get one recored from cursor object
        row = data.fetchone()
        if not row:
            print("No slot alloted for this vehicle. Please allot a slot first.")
        else:
            vehicle, floor, lot = row 
            print(f'Paking lot for vehicle - {vehicle} : ',{"level" : floor, "spot" : lot})




if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-i", "--Input", help = "Takes one input as registration number and allots a slot")
    # Adding optional argument
    parser.add_argument("-o", "--Output", help = "Takes one input as registration Number and returns alloted slot")
    args = parser.parse_args()
    
    if args.Input:
        # print("Displaying Input as: % s" % args.Input)
        ## assign a slot to vehicle
        assign_spot(args.Input)


    if args.Output:
        # print("Displaying Output as: % s" % args.Output)
        ## get previously alloted slot of vehicle
        get_spot(args.Output)
    