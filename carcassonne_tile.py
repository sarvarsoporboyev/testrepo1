'''

author: soporboyev sarvarbek
carcassonne_tile.py should be the project in which the tile information
is given in a class and it can be used for the carcassonne_map.py project
'''

N = 0
E = 1
S = 2
W = 3


class CarcassonneTile:
    '''
    the carcassonnetile class should store one tile at a time
    and carcassonnemap should get these information for every
    tile that is going through the carcassonnetile file


    '''
    def __init__(self, north, east, south, west, center):
        '''
        the array should store the values for the sides
        of the tile that we use for the carcassonne_map.py

        :param north: things located at north side of the tile
        :param east:things located at east side of the tile
        :param south:things located at south side of the tile
        :param west:things located at west side of the tile
        :param center:things located at center of the tile
        '''
        self._array = [[north.split('+'), east.split('+'), south.split('+'), west.split('+')], [center]]

    def city_list(self, side):
        '''

        :param side:side of the
        tile that the city is in
        :return: the sides that
        the city is connected to
        '''

        cities = []
        if side == 0:
            if self.city_connects(0, 1) == True:
                cities.append(1)
            if self.city_connects(0, 2) == True:
                cities.append(2)
            if self.city_connects(0, 3) == True:
                cities.append(3)
        if side == 1:
            if self.city_connects(0, 1) == True:
                cities.append(0)
            if self.city_connects(1, 2) == True:
                cities.append(2)
            if self.city_connects(1, 3) == True:
                cities.append(3)
        if side == 2:
            if self.city_connects(2, 0) == True:
                cities.append(0)
            if self.city_connects(2, 1) == True:
                cities.append(1)
            if self.city_connects(2, 3) == True:
                cities.append(3)
        if side == 3:
            if self.city_connects(3, 0) == True:
                cities.append(0)
            if self.city_connects(3, 1) == True:
                cities.append(1)
            if self.city_connects(3, 2) == True:
                cities.append(2)
        return cities

    def city_connects(self, from_side, to_side):
        '''
        from the two sides we should return the
        boolean expression of whether the two
        cities are connected or not
        :param from_side: the first side of the tile
        :param to_side: the second side of the tile
        :return: a boolean expression of whether
        the city in the given side of the
        tile is connected to another side of the tile
        '''
        if from_side == to_side:
            return True
        if from_side == 0 and to_side == 2 and self._array[1][0] == 'city':
            if 'uncovered' in self._array[0][from_side] and 'uncovered' in self._array[0][to_side]:
                return True
        if from_side == 2 and to_side == 0 and self._array[1][0] == 'city':
            if 'uncovered' in self._array[0][from_side] and 'uncovered' in self._array[0][to_side]:
                return True
        if from_side == 1 and to_side == 3 and self._array[1][0] == 'city':
            if 'uncovered' in self._array[0][from_side] and 'uncovered' in self._array[0][to_side]:
                return True
        if from_side == 3 and to_side == 1 and self._array[1][0] == 'city':
            if 'uncovered' in self._array[0][from_side] and 'uncovered' in self._array[0][to_side]:
                return True
        if 'uncovered' in self._array[0][from_side] and 'uncovered' in self._array[0][to_side]:
            return True
        return False

    def get_edge(self, value):
        '''

        :param value: the number value for
        the side of the tile
        :return: the edge number is given and the
        returning value should be the items
        located at that side of the tile
        '''
        if value == N:
            if self._array[0][0] == ['city', 'covered']:
                return 'city'
            if self._array[0][0] == ['city', 'uncovered']:
                return 'city'
            else:
                return '+'.join(self._array[0][0])
        elif value == E:
            if self._array[0][1] == ['city', 'covered']:
                return 'city'
            if self._array[0][1] == ['city', 'uncovered']:
                return 'city'
            else:
                return '+'.join(self._array[0][1])

        elif value == S:
            if self._array[0][2] == ['city', 'covered']:
                return 'city'
            if self._array[0][2] == ['city', 'uncovered']:
                return 'city'
            else:
                return '+'.join(self._array[0][2])
        elif value == W:
            if self._array[0][3] == ['city', 'covered']:
                return 'city'
            if self._array[0][3] == ['city', 'uncovered']:
                return 'city'
            else:
                return '+'.join(self._array[0][3])
    def rotate(self):
        '''

        :return:the new class object of the
        rotated form of the current tile object
        '''
        temp = []

        temp.append('+'.join(self._array[0][3]))
        temp.append('+'.join(self._array[0][0]))
        temp.append('+'.join(self._array[0][1]))
        temp.append('+'.join(self._array[0][2]))
        temp.append(self._array[1][0])
        tileneed = CarcassonneTile(temp[0], temp[1],
                                   temp[2], temp[3], temp[4])
        return tileneed
    def has_crossroads(self):
        '''

        :return: the returning value of the function
        should be the boolean expression of whether
        the current tile has a crossroad in the middle
        '''
        temporary = 0
        if 'road' in self._array[0][0]:
            temporary += 1
        if 'road' in self._array[0][1]:
            temporary += 1
        if 'road' in self._array[0][2]:
            temporary += 1
        if 'road' in self._array[0][3]:
            temporary += 1
        if temporary >= 3:
            return True
        else:
            return False

    def edge_has_road(self, val):
        '''

        :param val: the number value of the
        side of the tile as indicated
        :return: return value for the
         function should be the boolean
         expression of the whether the current
         parameter side of the tile has an item road or not
        '''
        if val == 0:
            if 'road' in self._array[0][0]:
                return True
        if val == 1:
            if 'road' in self._array[0][1]:
                return True
        if val == 2:
            if 'road' in self._array[0][2]:
                return True
        if val == 3:
            if 'road' in self._array[0][3]:
                return True
        return False
    def edge_has_city(self, cur):
        '''

        :param cur: the number value indicating the
        number value of the current side of the tile
        :return: the function should return the b
        boolean of whether the current parameter side has city or not
        '''
        val = cur
        if val == 0:
            if 'city' in self._array[0][0]:
                return True
        if val == 1:
            if 'city' in self._array[0][1]:
                return True
        if val == 2:
            if 'city' in self._array[0][2]:
                return True
        if val == 3:
            if 'city' in self._array[0][3]:
                return True
        return False
    def road_get_connection(self, edge):
        '''

        :param edge: it should think about
        the current edge of the tile
        :return: the return should think about
        the side of the town that the road is connected to
        if the center is a city, then the road ends here
        '''
        if edge == 0:
            if self._array[1][0] == 'city':
                return -1
            if 'road' in self._array[0][1]:
                return 1
            if 'road' in self._array[0][2]:
                return 2
            if 'road' in self._array[0][3]:
                return 3
        if edge == 1:
            if self._array[1][0] == 'city':
                return -1
            if 'road' in self._array[0][0]:
                return 0
            if 'road' in self._array[0][2]:
                return 2
            if 'road' in self._array[0][3]:
                return 3
        if edge == 2:
            if self._array[1][0] == 'city':
                return -1

            if 'road' in self._array[0][1]:
                return 1
            if 'road' in self._array[0][0]:
                return 0
            if 'road' in self._array[0][3]:
                return 3
        if edge == 3:
            if self._array[1][0] == 'city':
                return -1

            if 'road' in self._array[0][1]:
                return 1
            if 'road' in self._array[0][2]:
                return 2
            if 'road' in self._array[0][0]:
                return 0



tile01 = CarcassonneTile('city+covered',(f"grass+road"),'grass',(f"grass+road"), 'non-city')
tile02 = CarcassonneTile('city+uncovered','city+uncovered','grass','city+uncovered', 'city')
tile03 = CarcassonneTile((f"grass+road"),(f"grass+road"),(f"grass+road"),(f"grass+road"), 'city')
tile04 = CarcassonneTile('city+covered',(f"grass+road"),(f"grass+road"),'grass', 'non-city')
tile05 = CarcassonneTile('city+uncovered','city+uncovered','city+uncovered','city+uncovered', 'city')
tile06 = CarcassonneTile((f"grass+road"),'grass', (f"grass+road"), 'grass', 'non-city')
tile07 = CarcassonneTile('grass', 'city+covered', 'grass', 'city+covered', 'non-city')
tile08 = CarcassonneTile('grass', 'city+uncovered', 'grass', 'city+uncovered', 'city')
tile09 = CarcassonneTile('city+uncovered', 'city+uncovered', 'grass', 'grass', 'non-city')
tile10 = CarcassonneTile('grass', (f"grass+road"), (f"grass+road"), (f"grass+road"), 'city')
tile11 = CarcassonneTile('city+uncovered', (f"grass+road"), (f"grass+road"), 'city+uncovered', 'non-city')
tile12 = CarcassonneTile('city+covered', 'grass', (f"grass+road"), (f"grass+road"), 'non-city')
tile13 = CarcassonneTile('city+covered', (f"grass+road"), (f"grass+road"), (f"grass+road"), 'city')
tile14 = CarcassonneTile('city+covered', 'city+covered', 'grass', 'grass', 'non-city')
tile15 = CarcassonneTile('grass', 'grass', (f"grass+road"), (f"grass+road"), 'non-city')
tile16 = CarcassonneTile('city+covered', 'grass', 'grass', 'grass', 'non-city')