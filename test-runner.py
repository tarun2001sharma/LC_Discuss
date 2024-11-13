'''
There is a testRunner funtion that takes multiple unit test and returns if those uts are executed together & then there is some error or not. 
If no error then return true other wise false. You have been given N unit tests, and you know that when you run all test cases at a time then it fails.
Now you need to find at least one pair of UTs, which fails when executed at the same time using the test runner.

Its easy when we assume that the testRunner takes O(1) to execute any number of test cases. But for the case when the test runner takes O(n) time 
to execute n test cases at a time then find the optimal way to find one pair of failed UTs.

Note there may be multiple pairs that fail with each other, but need to report only one. Also all the UTs are running ok when executed individaullay.

Any suggestion on how to solve this with optimal manner?
'''

def testRunner(test_set):
    """
    Mock testRunner function.
    Returns False if the subset of test cases causes a failure.
    Returns True if the subset passes.
    """
    # This is just a placeholder function. In an actual scenario,
    # this function would be provided and would run the test cases.
    # Replace this with the actual `testRunner` implementation.
    # Example failing pair for testing: {'UT2', 'UT3'}
    failing_pairs = {('UT2', 'UT3')}
    for test1 in test_set:
        for test2 in test_set:
            if test1 != test2 and (test1, test2) in failing_pairs:
                return False
    return True

def find_failing_pair(UTs):
    def helper(subset):
        # Base case: if only two test cases left, return as a potential failing pair
        if len(subset) == 2:
            return subset
        
        # Divide the set into two halves
        mid = len(subset) // 2
        left_subset = subset[:mid]
        right_subset = subset[mid:]
        
        # Run testRunner on each half
        if not testRunner(left_subset):  # Check if left half has a conflict
            return helper(left_subset)
        elif not testRunner(right_subset):  # Check if right half has a conflict
            return helper(right_subset)
        else:
            # Check if combining left and right halves causes a failure
            combined_subset = left_subset + right_subset
            if not testRunner(combined_subset):
                # If combined subset fails, but both halves individually passed,
                # then we have a conflicting pair across the two halves.
                # Use binary search on combined subsets to find the conflicting pair.
                return find_cross_pair(left_subset, right_subset)
            else:
                return None  # Should not reach here if we know there's a failing pair
    
    def find_cross_pair(left_subset, right_subset):
        # Binary search between two halves to find one failing pair
        for test1 in left_subset:
            for test2 in right_subset:
                if not testRunner([test1, test2]):
                    return [test1, test2]
        return None  # Should not reach here if we know there's a failing pair
    
    # Start the search with the full set of unit tests
    result = helper(UTs)
    return result

# Example usage:
UTs = ["UT1", "UT2", "UT3", "UT4"]
failing_pair = find_failing_pair(UTs)
print("Failing pair:", failing_pair)
