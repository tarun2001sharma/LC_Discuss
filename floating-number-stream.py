
'''
https://leetcode.com/discuss/interview-question/1671654/google-onsite-new-grad

Your task is to write a function that, given a distance d and a stream
of floating point values received one at a time, checks for groups of
three values within d distance of one another. Store the floating point values
in memory as they are received. When a group of three values meeting the
distance criteria is found, return the three values and remove them from the
memory.
'''

def find_triplet_within_distance(d, stream):
    # List to maintain a sliding window of the latest values
    window = []

    # Process each value in the stream
    for value in stream:
        # Add the new value to the window
        window.append(value)
        
        # Check if we have three values in the window
        if len(window) == 3:
            # Check if the three values satisfy the distance condition
            a, b, c = window
            if abs(a - b) <= d and abs(a - c) <= d and abs(b - c) <= d:
                # Return the group and clear the window
                result = window[:]
                window.clear()
                return result
        
        # If no group is found, and we have more than three values, pop the oldest
        if len(window) > 3:
            window.pop(0)

    # If no group is found in the stream, return None
    return None
