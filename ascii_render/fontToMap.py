# Creates a 2d array with each array containing an 8x16 representation of a glyph
def create_arrays(path):
    f = open(path, "r", encoding='utf-8-sig')
    array = []
    cur_letter = []
    count = 0
    while True:
        count += 1
        x = f.readline().strip()
        if (count > 16):
            array.append(cur_letter)
            count = 1
            cur_letter = []
        if (len(x) == 0):
            break
        else:
            for i in x:
                if (i == '.'):
                    cur_letter.append(0)
                elif (i == '@'):
                    cur_letter.append(1)
    verify(array)

    return array


def verify(i):
    for j in i:
        if (len(j) != 128):
            raise TypeError("glyph incorrect dimensions")
