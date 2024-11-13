'''
This was my last coding interview of the onsite process. Here's the question


Write a function that takes the following 3 queries:


	1. manager, a, b      -> represents that a is manager of b
	2. peer, a, b         -> both a and b have the same manager
	3. is_manager a, b    -> you should return whether a is manager of b
Assume every input is valid.
Assume every query is coming one at a time, not a list of queries.
Interviewer said I might come across a case where a peer query came with two managerless employees


My answer was a class that had three global variables: managerless_people, peer_to_manager, managers that represented a connection between a and b. Lots of if statements and assignments.


My code wasn't the cleanest and I felt like my interviewer was not paying attention at all at what I was saying.
'''

class EmployeeHierarchy:
    def __init__(self):
        self.manager = {}
        self.managerless_ppl = set()

    def find_manager(self, employee):
        if employee not in self.manager:
            self.manager[employee] = None
        
        path = []
        while self.manager[employee] is not None:
            path.append(employee)
            employee = self.manager[employee]
        
        # either return the manager hierarchy or the senior most manager or the immediate manager
        return path[0]
        # return path[-1]
        # return path
    
    def add_manager(self, a, b):
        # adds a as the manager of b
        
    def is_peer(self, a, b):
        root_a = self.find_root_manager(a)
        root_b = self.find_root_manager(b)
        if root_a != root_b:
            self.manager[root_b] = root_a
    
    def add_peer(self, a, b):
        # a and b will have same peers
        '''
This was my last coding interview of the onsite process. Here's the question


Write a function that takes the following 3 queries:


	1. manager, a, b      -> represents that a is manager of b
	2. peer, a, b         -> both a and b have the same manager
	3. is_manager a, b    -> you should return whether a is manager of b
Assume every input is valid.
Assume every query is coming one at a time, not a list of queries.
Interviewer said I might come across a case where a peer query came with two managerless employees


My answer was a class that had three global variables: managerless_people, peer_to_manager, managers that represented a connection between a and b. Lots of if statements and assignments.


My code wasn't the cleanest and I felt like my interviewer was not paying attention at all at what I was saying.
'''

class EmployeeHierarchy:
    def __init__(self):
        self.manager = {}
        self.managerless_ppl = set()

    def find_manager(self, employee):
        if employee not in self.manager:
            self.manager[employee] = None
        
        path = []
        while self.manager[employee] is not None:
            path.append(employee)
            employee = self.manager[employee]
        
        # either return the manager hierarchy or the senior most manager or the immediate manager
        return path[0]
        # return path[-1]
        # return path
    
    def add_manager(self, a, b):
        # adds a as the manager of b
        self.manager[b] = a
        if b in self.managerless_people:
            self.managerless_people.remove(b)
        if a not in self.manager:
            self.managerless_people.add(a)
        
    def is_peer(self, a, b):
        root_a = self.find_root_manager(a)
        root_b = self.find_root_manager(b)
        if root_a != root_b:
            self.manager[root_b] = root_a
    
    def add_peer(self, a, b):
        # a and b will have same peers
        root_a = self.
    
    def is_manager(self, a, b):
        """Process 'is_manager a b' query: check if a is manager of b."""
        current = b
        while current is not None:
            if current == a:
                return True
            current = self.manager.get(current)
        return False
    
    def is_manager(self, a, b):
        """Process 'is_manager a b' query: check if a is manager of b."""
        current = b
        while current is not None:
            if current == a:
                return True
            current = self.manager.get(current)
        return False