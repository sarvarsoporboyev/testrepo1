'''
author soporboyev sarvarbek
the program should provide
the tile information for
the carcassonnemap class
and especially carcassonne_map.py file

'''



import carcassonne_tile
tile01 = carcassonne_tile.CarcassonneTile('city+covered',(f"grass+road"),'grass',(f"grass+road"), 'non-city')
tile02 = carcassonne_tile.CarcassonneTile('city+uncovered','city+uncovered','grass','city+uncovered', 'city')
tile03 = carcassonne_tile.CarcassonneTile((f"grass+road"),(f"grass+road"),(f"grass+road"),(f"grass+road"), 'city')
tile04 = carcassonne_tile.CarcassonneTile('city+covered',(f"grass+road"),(f"grass+road"),'grass', 'non-city')
tile05 = carcassonne_tile.CarcassonneTile('city+uncovered','city+uncovered','city+uncovered','city+uncovered', 'city')
tile06 = carcassonne_tile.CarcassonneTile((f"grass+road"),'grass', (f"grass+road"), 'grass', 'non-city')
tile07 = carcassonne_tile.CarcassonneTile('grass', 'city+covered', 'grass', 'city+covered', 'non-city')
tile08 = carcassonne_tile.CarcassonneTile('grass', 'city+uncovered', 'grass', 'city+uncovered', 'city')
tile09 = carcassonne_tile.CarcassonneTile('city+uncovered', 'city+uncovered', 'grass', 'grass', 'non-city')
tile10 = carcassonne_tile.CarcassonneTile('grass', (f"grass+road"), (f"grass+road"), (f"grass+road"), 'city')
tile11 = carcassonne_tile.CarcassonneTile('city+uncovered', (f"grass+road"), (f"grass+road"), 'city+uncovered', 'non-city')
tile12 = carcassonne_tile.CarcassonneTile('city+covered', 'grass', (f"grass+road"), (f"grass+road"), 'non-city')
tile13 = carcassonne_tile.CarcassonneTile('city+covered', (f"grass+road"), (f"grass+road"), (f"grass+road"), 'city')
tile14 = carcassonne_tile.CarcassonneTile('city+covered', 'city+covered', 'grass', 'grass', 'non-city')
tile15 = carcassonne_tile.CarcassonneTile('grass', 'grass', (f"grass+road"), (f"grass+road"), 'non-city')
tile16 = carcassonne_tile.CarcassonneTile('city+covered', 'grass', 'grass', 'grass', 'non-city')
# the tile information that we need for
# doing some operations around
# the carcassonne_map.py file
N = 0
E = 1
S = 2
W = 3

# the side notations for the four
# sides that are east south west and north

class CarcassonneMap:
    '''
        the carcassonnemap should build a map of
        tiles from carcassonnetile class


    '''

    def __init__(self):
        '''
        the initializer should say that the starting
        map is the tile01 as the (0, 0) position in the map'''
        self._sides = [[0, 0]] + [tile01._array[0]] + [tile01._array[1]]
        self._road = set()
        self._coord = set()

    def get(self, x, y):
        '''

        :param x:the x component of the coordinate
        :param y: the y component of the coordinate
        :return: the part of the map that the map
        contains which should be a tile
        '''
        # the get() function should return the particular
        # tile in the map in a particular part of the map

        for i in range(0, len(self._sides), 3):
            if self._sides[i] == [x, y]:
                return carcassonne_tile.CarcassonneTile('+'.join(self._sides[i + 1][0]),
                                                        '+'.join(self._sides[i + 1][1]),
                                                        '+'.join(self._sides[i + 1][2]),
                                                        '+'.join(self._sides[i + 1][3]),
                                                        self._sides[i + 2][0])
        return None
    def get_all_coords(self):
        '''

        :return: the get_all_coords function should return
        the coordinate information about the map
        '''
        get_coords = set()

        for i in range(0, len(self._sides), 3):
            get_coords.add((self._sides[i][0], self._sides[i][1]))
        return get_coords
    def find_map_border(self):
        '''

        :return:
        the find_map_border function should
        return us the possible coordinates
        that can be the next adding
        tile to the map
        '''
        get_coords = self.get_all_coords()
        find = set()
        for i in range(0, len(self._sides), 3):
            if (self._sides[i][0], self._sides[i][1] + 1) not in get_coords:
                find.add((self._sides[i][0], self._sides[i][1] + 1))
            if (self._sides[i][0], self._sides[i][1] - 1) not in get_coords:
                find.add((self._sides[i][0], self._sides[i][1] - 1))
            if (self._sides[i][0] + 1, self._sides[i][1]) not in get_coords:
                find.add((self._sides[i][0] + 1, self._sides[i][1]))
            if (self._sides[i][0] - 1, self._sides[i][1]) not in get_coords:
                find.add((self._sides[i][0] - 1, self._sides[i][1]))
        return find
    def confirm_nottryonly(self, x, y, object):
        '''

        if confirm == True and tryOnly == False:
        :param x: x coordinate for the add function
        :param y: y coordinate for the add function
        :param object: the carcassonnetile object
        :return: the boolean of whether the tile
        is added to the carcassonnemap
        '''
        tempo = []
        for j in range(0, len(self._sides), 3):
            if self._sides[j] == [x, y - 1]:
                if self._sides[j + 1][0] == object._array[0][2] or \
                        ('city' in self._sides[j + 1][0] and 'city' in object._array[0][2]):
                    tempo.append(True)
                else:
                    tempo.append(False)
            # if the neighbouring coordinate item
            # is in get_all_coords function, then we keep up confirming
            if self._sides[j] == [x, y + 1]:
                if self._sides[j + 1][2] == object._array[0][0] or \
                        ('city' in self._sides[j + 1][2] and 'city' in object._array[0][0]):
                    tempo.append(True)
                else:
                    tempo.append(False)
            # if the neighbouring coordinate item
            # is in get_all_coords function, then we keep up confirming
            if self._sides[j] == [x + 1, y]:
                if self._sides[j + 1][3] == object._array[0][1] or \
                        ('city' in self._sides[j + 1][3] and 'city' in object._array[0][1]):
                    tempo.append(True)
                else:
                    tempo.append(False)
            # if the neighbouring coordinate item
            # is in get_all_coords function, then we keep up confirming
            if self._sides[j] == [x - 1, y]:
                if self._sides[j + 1][1] == object._array[0][3] or \
                        ('city' in self._sides[j + 1][1] and 'city' in object._array[0][3]):
                    tempo.append(True)
                else:
                    tempo.append(False)
        count = 0
        for p in tempo:
            if p == True:
                count += 1
        # if all the neighbouring tiles are confirming the
        # addition, then we can add the item to the map

        if len(tempo) == count and count != 0:
            self._sides.append([x, y])
            self._sides.append(object._array[0])
            self._sides.append(object._array[1])
            return True
        return False
    def notconfirm_nottryonly(self, x, y, object):
        '''

        if confirm == False and tryOnly == False:
        :param x: x coordinate of the map
        :param y: y coordinate of the map
        :param object: the carcassonnetile object
        :return:
        '''
        self._sides.append([x, y])
        self._sides.append(object._array[0])
        self._sides.append(object._array[1])
        return True
    def confirm_tryonly(self, x, y, object):
        '''

        if confirm == True and tryOnly == True:
        :param x: x coordinate of the carcassonnemap
        :param y: y coordinate of the carcassonne map
        :param object: the carcassonnetile object
        :return:
        '''
        tempe = []
        for j in range(0, len(self._sides), 3):
            if self._sides[j] == [x, y - 1]:
                if self._sides[j + 1][0] == object._array[0][2] or \
                        ('city' in self._sides[j + 1][0] and 'city' in object._array[0][2]):
                    tempe.append(True)
                else:
                    tempe.append(False)
            if self._sides[j] == [x, y + 1]:
                if self._sides[j + 1][2] == object._array[0][0] or \
                        ('city' in self._sides[j + 1][2] and 'city' in object._array[0][0]):
                    tempe.append(True)
                else:
                    tempe.append(False)
            if self._sides[j] == [x + 1, y]:
                if self._sides[j + 1][3] == object._array[0][1] or \
                        ('city' in self._sides[j + 1][3] and 'city' in object._array[0][1]):
                    tempe.append(True)
                else:
                    tempe.append(False)
            if self._sides[j] == [x - 1, y]:
                if self._sides[j + 1][1] == object._array[0][3] or \
                        ('city' in self._sides[j + 1][1] and 'city' in object._array[0][3]):
                    tempe.append(True)
                else:
                    tempe.append(False)
        count = 0
        for p in tempe:
            if p == True:
                count += 1

        if len(tempe) == count and count != 0:
            return True
        return False
    def add(self, x, y, object, confirm = True, tryOnly = False):
        '''

        :param x:x component of the map coordinate
        :param y: y component of the map coordinate
        :param object: the tile object for adding
        :param confirm: the default boolean
        :param tryOnly: the default boolean
        :return:the add function is not possible if
        the coordinate is in the get_all_coords set

        '''
        get_coords = self.get_all_coords()
        if (x, y) in get_coords:
            return False

        # if confirm  == True and tryOnly == False
        # then the tile is added if the conditions
        # are met in all the cases of rotation
        if confirm == True and tryOnly == False:
            return self.confirm_nottryonly(x, y, object)
        # if confirm == False and tryOnly == False
        # then we just add without any confirmation
        # of the whether it is meeting the
        # requirement of the map being created
        elif confirm == False and tryOnly == False:

            return self.notconfirm_nottryonly(x, y, object)
        # if confirm == True and tryOnly == True
        # then we just confirm whether or not it
        # is possible to add it, it just returns
        # the boolean expression of whether
        # or not it is meeting the requirement
        # but after the confirmation the tile
        # is not added overall
        elif confirm == True and tryOnly == True:
            return self.confirm_tryonly(x, y, object)
    # this add() function should return the True False
    # boolean expression for whether the next tile
    # indicated has been added to the map

    def trace_road_one_direction(self, x, y, side):
        '''

        :param x: x parameter for the coordinate
        that we should start our road tracing from
        :param y: y parameter for the coordinate
        that we should start our road tracing from
        :param side: the side should indicated the
        starting part of the road tracing and it
        should start in a particular part of the tile
        :return: the tuple of all the tracing from the
        starting part of the carcassonne_map.py to the
        end of the loop of the road throughout
        the possible parts of the map
        '''
        temp_trace = []
        from_side = side
        i = x
        j = y
        count = len(self._sides) // 3
        temp_coords = []
        sets = set()
        values = len(self._sides) - 3
        while count >= 0:
            for k in range(0, len(self._sides), 3):
                if from_side == 0:
                    if self._sides[k] == [i, j + 1]:
                        if self._sides[k + 2][0] == 'city':
                            temp_trace.append((i, j + 1, 2, -1))
                            return temp_trace

                        elif 'road' in self._sides[k + 1][0]:
                            if (i, j + 1) not in temp_coords:
                                temp_coords.append((i, j + 1))
                                temp_trace.append((i, j + 1, 2, 0))
                                j += 1
                                from_side = 0
                            else:
                                return temp_trace



                        elif 'road' in self._sides[k + 1][1]:
                            if (i, j + 1) not in temp_coords:
                                temp_coords.append((i, j + 1))
                                temp_trace.append((i, j + 1, 2, 1))
                                j += 1
                                from_side = 1
                            else:
                                return temp_trace


                        elif 'road' in self._sides[k + 1][3]:
                            if (i, j + 1) not in temp_coords:
                                temp_coords.append((i, j + 1))
                                temp_trace.append((i, j + 1, 2, 3))
                                j += 1
                                from_side = 3
                            else:
                                return temp_trace

                        count -= 1
                        break
                elif from_side == 1:
                    if self._sides[k] == [i + 1, j]:
                        if self._sides[k + 2][0] == 'city':
                            temp_trace.append((i + 1, j, 3, -1))
                            return temp_trace

                        elif 'road' in self._sides[k + 1][0]:
                            if (i + 1, j) not in temp_coords:
                                temp_coords.append((i + 1, j))
                                temp_trace.append((i + 1, j, 3, 0))
                                i += 1
                                from_side = 0
                            else:
                                return temp_trace


                        elif 'road' in self._sides[k + 1][1]:
                            if (i + 1, j) not in temp_coords:
                                temp_coords.append((i + 1, j))
                                temp_trace.append((i + 1, j, 3, 1))
                                i += 1
                                from_side = 1
                            else:
                                return temp_trace


                        elif 'road' in self._sides[k + 1][2]:
                            if (i + 1, j) not in temp_coords:
                                temp_coords.append((i + 1, j))
                                temp_trace.append((i + 1, j, 3, 2))
                                i += 1
                                from_side = 2
                            else:
                                return temp_trace


                        count -= 1
                        break
                elif from_side == 2:
                    if self._sides[k] == [i, j - 1]:
                        if self._sides[k + 2][0] == 'city':

                            temp_trace.append((i, j - 1, 0, -1))
                            return temp_trace

                        elif 'road' in self._sides[k + 1][3]:
                            if (i, j - 1) not in temp_coords:
                                temp_coords.append((i, j - 1))
                                temp_trace.append((i, j - 1, 0, 3))
                                j -= 1
                                from_side = 3
                            else:
                                return temp_trace


                        elif 'road' in self._sides[k + 1][1]:
                            if (i, j - 1) not in temp_coords:
                                temp_coords.append((i, j - 1))
                                temp_trace.append((i, j - 1, 0, 1))
                                j -= 1
                                from_side = 1
                            else:
                                return temp_trace


                        elif 'road' in self._sides[k + 1][2]:
                            if (i, j - 1) not in temp_coords:
                                temp_coords.append((i, j - 1))
                                temp_trace.append((i, j - 1, 0, 2))
                                j -= 1
                                from_side = 2
                            else:
                                return temp_trace


                        count -= 1
                        break
                elif from_side == 3:
                    if self._sides[k] == [i - 1, j]:
                        if self._sides[k + 2][0] == 'city':
                            temp_trace.append((i - 1, j, 1, -1))
                            return temp_trace

                        elif 'road' in self._sides[k + 1][0]:
                            if (i - 1, j) not in temp_coords:
                                temp_coords.append((i - 1, j))
                                temp_trace.append((i - 1, j, 1, 0))
                                i -= 1
                                from_side = 0
                            else:
                                return temp_trace


                        elif 'road' in self._sides[k + 1][2]:
                            if (i - 1, j) not in temp_coords:
                                temp_coords.append((i - 1, j))
                                temp_trace.append((i - 1, j, 1, 2))
                                i -= 1
                                from_side = 2
                            else:
                                return temp_trace


                        elif 'road' in self._sides[k + 1][3]:
                            if (i - 1, j) not in temp_coords:
                                temp_coords.append((i - 1, j))
                                temp_trace.append((i - 1, j, 1, 3))
                                i -= 1
                                from_side = 3
                            else:
                                return temp_trace


                        count -= 1
                        break
                if k == values:
                    if count in sets:
                        return temp_trace
                    else:
                        sets.add(count)

        if len(temp_trace) == 0:
            return []
        else:
            return temp_trace
    def trace_road(self, x , y, side):
        '''

        :param x: the x coordinate of the tile in the map
        :param y: the y coordinate of the tile in the map
        :param side: side that the tracing road
        throughout the map starts from
        :return:
        two direction of the trace_road_one_direction
        '''
        temp_need = []
        for i in range(0, len(self._sides), 3):
            if self._sides[i] == [x, y]:
                if 'road' in self._sides[i + 1][side]:
                    if self._sides[i + 2][0] == 'city':
                        temp_need = [(x, y, -1, side)]
                        temp_need += (self.trace_road_one_direction(x, y, side))


                    elif 'road' in self._sides[i + 1][side - 1]:
                        sided = side
                        if side - 1 < 0:
                            sided += 4
                        temp_need = (reverse(self.trace_road_one_direction(x, y ,sided - 1))) + \
                                    [(x, y, sided - 1, side)] + self.trace_road_one_direction(x, y, side)
                        if 2 * len(list(set(temp_need))) + 1 == len(temp_need):
                            temp_need = self.trace_road_one_direction(x, y, side)


                    elif 'road' in self._sides[i + 1][side - 2]:
                        sided = side
                        if side - 2 < 0:
                            sided += 4
                        temp_need = (reverse(self.trace_road_one_direction(x, y, sided - 2))) + \
                                    [(x, y, sided - 2, side)] + self.trace_road_one_direction(x, y, side)
                        if 2 * len(list(set(temp_need))) + 1 == len(temp_need):
                            temp_need = self.trace_road_one_direction(x, y, side)

                    elif 'road' in self._sides[i + 1][side - 3]:
                        sided = side

                        if side - 3 < 0:
                            sided += 4
                        temp_need = (reverse(self.trace_road_one_direction(x, y, sided - 3))) + \
                                    [(x, y, sided - 3, side)] + self.trace_road_one_direction(x, y, side)
                        if 2*len(list(set(temp_need))) + 1 == len(temp_need):
                            temp_need = self.trace_road_one_direction(x, y, side)


        return temp_need
    def neighbour(self, tuples):
        '''

        :param tuples: the current coordinate tile side tuple in the map
        :return: the neighbour side
        to the current coordinate tile in the map
        '''
        tuples = list(tuples)
        for ind in range(0, len(self._sides), 3):
            if tuples[2] == 0:
                if self._sides[ind] == [tuples[0], tuples[1] + 1]:
                    return (tuples[0], tuples[1] + 1, 2)
            elif tuples[2] == 1:
                if self._sides[ind] == [tuples[0] + 1, tuples[1]]:
                    return (tuples[0] + 1, tuples[1], 3)
            elif tuples[2] == 2:
                if self._sides[ind] == [tuples[0], tuples[1] - 1]:
                    return (tuples[0], tuples[1] - 1, 0)
            elif tuples[2] == 3:
                if self._sides[ind] == [tuples[0] - 1, tuples[1]]:
                    return (tuples[0] - 1, tuples[1], 1)
        return []


    def trace_city(self, x, y, side):
        '''

        :param x: x coordinate of the tile
        in the map of tiles
        :param y: y coordinate of the tile
        in the map of tiles
        :param side: starting side which
        contains the city
        :return: the tuples of cities in a list
        and side of the tile that big city is located in
        '''
        sets = set()
        sets.add((x, y, side))
        keep_searching = True
        while keep_searching:
            keep_searching = False
            dup = list(sets)
            for item in dup:
                item = list(item)
                if self.get(item[0], item[1]).city_list(item[2]) != []:
                    temp = self.get(item[0], item[1]).city_list(item[2])
                    for index in temp:
                        if (item[0], item[1], index) not in sets:
                            sets.add((item[0], item[1], index))
                            keep_searching = True

                info = self.neighbour(item)
                if not info == []:
                    if info not in sets:
                        sets.add(info)
                        keep_searching = True
        complete = True
        for w in sets:
            if w[2] == 0:
                if (w[0], w[1] + 1, 2) not in sets:
                    complete = False
            if w[2] == 1:
                if (w[0] + 1, w[1], 3) not in sets:
                    complete = False
            if w[2] == 2:
                if (w[0], w[1] - 1, 0) not in sets:
                    complete = False
            if w[2] == 3:
                if (w[0] - 1, w[1], 1) not in sets:
                    complete = False


        return (complete, sets)



def reverse(lists):
    '''

    :param lists: for trace_road, the tuples list
    :return: the required list of tuples that
    changes the direction for the backward
    trace_road_one_direction of the trace_road
    '''
    reverse_list = []
    if len(lists) == 0:
        return []
    for i in range(len(lists)):
        tuples = (lists[len(lists) - i - 1][0],
                  lists[len(lists) - i - 1][1],
                  lists[len(lists) - i - 1][3],
                  lists[len(lists) - i - 1][2])
        reverse_list.append(tuples)
    return reverse_list


