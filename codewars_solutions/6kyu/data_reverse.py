# A stream of data is received and needs to be reversed.

# Each segment is 8 bits long, meaning the order of these segments needs to be
# reversed, for example:

# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)

# should become:

# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)

# The total number of bits will always be a multiple of 8.

# The data is given in an array as such:

# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

def data_reverse(data):

    data_dict = {}
    for i in range(0, len(data)):
        if(i+1) % 8 == 0:
            data_dict[(i+1)/8] = data[i-7:i+1]
        else:
            continue
            
    rev_data = []
    for key in sorted(data_dict.keys(), reverse = True):
        rev_data.extend(data_dict[key])
        
    return rev_data