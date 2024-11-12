'''
Medium Question from LC. I was asked to get all the possible combinations of a series of "musical notes" given the following rules:


Every sequence must have a sum of 12
Possible notes that make up the sequence can only be 1, 2 and 3
There are only certain valid transitions, they're given in this dictionary {1: [2, 3], 2: [1, 2], 3: [1]}. Meaning, only 2 and 3 are allowed after 1 and so on
First note and last note must have a valid transition. Example of valid sequence: [1, 2, 2, 2, 1, 1, 3]. Example of not valid: [1, 2, 2, 2, 2, 2, 1] reason is because 1 cannot be followed by another 1 (last and first notes transition is invalid)
Return every possible valid sequence in an array of possible sequences. You may return it in any order.


My approach was to make a DFS algorithm to go through every possible combination. Before calling recursively my function i'd check if it's valid transition and sum is not above 12


Interviewer later would ask me about time and space complexity which was a bit hard for me but came up with exponential order for both. In the worst case scenario


Still missing 1 coding interview and 1 behavioral. Wish me luck!!!
'''

# Dictionary of allowed transitions for each note
transitions = {
    1: [2, 3],  # After a 1, only 2 or 3 can follow
    2: [1, 2],  # After a 2, only 1 or 2 can follow
    3: [1]      # After a 3, only 1 can follow
}

# Target sum for each sequence
target_sum = 12

# This function will be our main recursive function to build sequences
def find_sequences(current_sequence, current_sum):
    # If the sum is exactly 12, check if the first and last notes are compatible
    if current_sum == target_sum:
        first_note = current_sequence[0]
        last_note = current_sequence[-1]
        
        # Check if the last note can transition to the first note
        if first_note in transitions[last_note]:
            # If valid, we add it to the results
            results.append(current_sequence)
        return

    # If the sum exceeds 12, stop (no need to explore further)
    if current_sum > target_sum:
        return

    # Get the last note in the current sequence
    last_note = current_sequence[-1]
    
    # For each possible next note according to transition rules
    for next_note in transitions[last_note]:
        # Append the next note and continue building the sequence
        find_sequences(current_sequence + [next_note], current_sum + next_note)

# This will hold all valid sequences
results = []

# Start the sequence with each possible note (1, 2, or 3)
for start_note in [1, 2, 3]:
    find_sequences([start_note], start_note)

# Print all valid sequences found
for sequence in results:
    print(sequence)
