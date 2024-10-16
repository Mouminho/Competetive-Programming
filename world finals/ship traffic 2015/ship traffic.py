import sys
"""Import the 'sys' module to read input from the command line and the typing module for type hints"""
def input_processing():
    """function 'input_processing' to convert the provided data in stdin into necessary values for the next calculations"""
    input_data = []
    """define list 'input_data' to store several data in it, which will be a part of the input for fuction 'largest_gap_finder' later"""
    for line in sys.stdin:
        """iterat over all lines of the input in stdin"""
        Lanes_number, Width, shipspeed, ferryspeed, T1, T2 = map(float, line.split())
        """define and dive values from first input line for the following variables:
        'Lanes_number', 'Width', 'shipspeed', 'ferryspeed', 'T1', 'T2'"""
        Timings = [(T1, 0), (T2, 0)]
        """list 'Timings' : includes tuples, the first value of the tuple represent a time point to be analised later,
        the second value represents an indicator for events, where:
        - if a ship is about to touch the crossing line then there is a ship crossing event -> indicator = 1
        - if a ship is about to cross and leave the line then there is a ship leaving event -> indicator = -1
        this means whern the sum is zero then the ferry will be able to cross safely"""
        for i in range(int(Lanes_number)):
            """iterate over all Lanes representations in input"""
            info = sys.stdin.readline().split()
            """each input line includes the following infos"""
            direction = info[0]
            """first info in the lane's direction"""
            ships_number = int(info[1])
            """second oone is the number of ships in this lane"""
            for l in range(2, 2 * ships_number + 2, 2):
                for p in range(l + 1, l + 2):
                    """read pairs of inputs"""
                    ship_length, position = float(info[l]), float(info[p])
                    """for each ship in the lane we get its length and position relatively to the ferry's crossing line"""
                    direction_factor = -1 if direction == 'E' else 1
                    """we want to consider that there is only one direction"""
                    position *= direction_factor
                    """we multiply all positions in every eastbound lane by -1 to get all positive values"""
                    ship_arriving_time = position / shipspeed
                    """using the formula : t = d/timings where t:time, d:distance, timings:speed
                    this indicate the time needed until the ship touches the ferry's crossing line(vertical line)"""
                    ship_leaving_time = (position + ship_length) / shipspeed
                    """this indicate the time needed until the ship crosses the ferry's crossing line(vertical line)"""
                    ferry_leaving_time = Width * (i + 1) / ferryspeed
                    """this indicate time needed til the ferry crosses the current horizontal lane"""
                    ferry_arriving_time = Width * i / ferryspeed
                    """this indicates time needed til ferry arrives to current lane"""
                    Timings.append((ship_arriving_time - ferry_leaving_time, 1))
                    """from this point on, the ferry is not allowed to start crossing"""
                    Timings.append((ship_leaving_time - ferry_arriving_time, -1))
                    """from this point on, the ferry might start crossing"""
        input_data.append((Timings, T1, T2, Width, ferryspeed, shipspeed))
        """insert all the following values as elements in the list 'input_data' as processed"""
    return input_data
def largest_gap_finder(Timings, T1, T2):
    """fuction 'largest_gap_finder' to find the largest gap between the timings"""
    Timings.sort()
    """sort all the timings in ascendant oreder"""
    largest_gap = 0.0
    """initialise 'largest_gape' with zero"""
    traffic_light = 0
    """when 'traffic_light' is equal to zero, then it means the ferrry has a green light and it could cross. when it is equal to a positive number, then it means the ferry should wait,
        until it has a possibility to start crossing safely"""
    for i in range(len(Timings)):
        traffic_light += Timings[i][1]
        """update the traffic_light by adding its indicator"""
        if traffic_light == 0 and Timings[i][0] >= T1 and Timings[i][0] < T2:
            """check if the traffic_light, which is the sum of indicators, is equal to zero, which means the leaving event has ended and the ferry has a time gap to start crossing safely"""
            largest_gap = max(largest_gap, Timings[i + 1][0] - Timings[i][0])
            """find the largest gap between all timings in list 'Timings'"""
    return largest_gap
def solver():
    input_data = input_processing()
    """call fuction 'input_processing' to prepare the data from the input, its return will be the data to work with"""
    for data in input_data:
        Timings, T1, T2, Width, ferryspeed, shipspeed = data
        """give values to the list 'Timings'  and the other variables"""
        result = largest_gap_finder(Timings, T1, T2)
        """call function 'largest_gap_finder' to find largest gap in 'Timings'"""
        print("{:.3f}".format(result))
solver()