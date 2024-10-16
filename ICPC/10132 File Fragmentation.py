import sys
def solver():
    """
    function solver is the function that construct and solve the 'file fragment problem'
    """
    input_ = sys.stdin.readline().strip()
    """ we read the first line of the stdin which supposed to be an integer which indicates the number of cases following """
    NumberOfCases = int(input_)
    """ first input line is an integer """
    
    sys.stdin.readline()
    while NumberOfCases > 0:
        """
        outer while loop for cases in the input
        """
        List_of_fragments = []
        """ list of fragments in the current case """
        input_ = sys.stdin.readline().strip()
        """ variable to read inputs """
        while input_ != "":
            """
            inner while loop to add fragments of current case in 'List_of_fragments'
            """
            List_of_fragments.append(input_.split()[0])
            """ adding the fragments to the list"""
            input_ = sys.stdin.readline().strip()
            """ next fragment """
        
        combinations_counter = {}
        """
        a dictionary, its keys are all possile combinations of 2 fragments of the current case and its values are their reputations
        """
        for i in range(len(List_of_fragments)):
            """
            outer for loop to go throw all fragments in the list
            """
            for j in range(i + 1, len(List_of_fragments)):
                """
                inner for loop to add all combinations of 2 fragments and calculate their reputations in the current case
                """
                combinations_counter[List_of_fragments[i] + List_of_fragments[j]] = combinations_counter.get(List_of_fragments[i] + List_of_fragments[j], 0) + 1
                """first possible combination is the concatination of i followed by j """
                """we increase the reputation indicator if we already have the key 'i+j' in the dictionary """
                combinations_counter[List_of_fragments[j] + List_of_fragments[i]] = combinations_counter.get(List_of_fragments[j] + List_of_fragments[i], 0) + 1
                """second possible combination is the concatination of j followed by i """
                """we increase the reputation indicator if we already have the key 'j+i' in the dictionary """

        File = max(combinations_counter, key=combinations_counter.get)
        """ 'File' is the key with most reputaions """
        print(File)
        """output of first case"""
        if NumberOfCases > 1:
            """
            is there any other cases?
            """
            print()
            """if yes the print a blank line"""
        
        NumberOfCases = NumberOfCases - 1
        """ reduce number of cases by one and go to outer while """

solver()