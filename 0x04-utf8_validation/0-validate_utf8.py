def validUTF8(data):
    # Function to count the number of leading '1's in a byte
    def countLeadingOnes(byte):
        count = 0
        mask = 1 << 7
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    # Loop through the data
    index = 0
    while index < len(data):
        # Get the number of bytes for the current character
        leading_ones = countLeadingOnes(data[index])

        # If the leading ones do not match the UTF-8 format, return False
        if leading_ones == 1 or leading_ones > 4:
            return False

        # Check if we have enough bytes for this character
        if index + leading_ones > len(data):
            return False

        # Check if the following bytes have the correct format
        for i in range(1, leading_ones):
            if countLeadingOnes(data[index + i]) != 1:
                return False

        index += leading_ones

    return True

# Testing the function with sample data
data1 = [65]
print(validUTF8(data1))  # Output: True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # Output: True

data3 = [229, 65, 127, 256]
print(validUTF8(data3))  # Output: False

