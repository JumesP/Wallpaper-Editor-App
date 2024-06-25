def CreatePattern1(pattern1):
    for x in range(0, 4):  # looping across
        x *= 50
        for y in range(0, 10):  # looping down
            y *= 20
            pattern1.create_polygon(2 + x, 24 + y, 12 + x, 4 + y, 42 + x, 4 + y, 52 + x, 24 + y,
                                    fill='#7B48DD', outline='black', width=2)

def CreatePattern2(pattern2):
    pattern2_xLocations = [14, 2, 10, 2, 14, 22, 30, 42, 34, 42, 30, 22]
    pattern2_yLocations = [75, 75, 50, 25, 25, 0, 25, 25, 50, 75, 75, 100]

    for x in range(0, 10):  # looping across
        pattern2_Locations = []  # resetting position
        if x > 4:  # loop for bottem row
            x = x - 5  # second rows x coordinates move back to the left of the screen
            y = 100  # moving it down
        else:
            y = 0
        x1 = x * 40  # shifting the shape right

        for alpha in range(0, 12):  # creating the shape
            pattern2_Locations.append(pattern2_xLocations[alpha] + x1)
            pattern2_Locations.append(pattern2_yLocations[alpha] + y)

            pattern2.create_polygon(pattern2_Locations, fill='#7B48DD')  # Creating pattern

