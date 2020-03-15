class CellularAutomaton:
    """
    This is a class for a one-dimensional cellular automaton.

    Attributes:
        rule (String): The rule that is applied to the current state.
        initialState (String): The current state of the elementary cellular automaton.

    Tests:
        >>> ca = CellularAutomaton(0, "00200")
        Traceback (most recent call last):
        ...
        ValueError: Initial state must contain only 0 and 1.
        >>> ca = CellularAutomaton(256, "00200")
        Traceback (most recent call last):
        ...
        ValueError: Initial state must contain only 0 and 1.
        >>> ca = CellularAutomaton(90, "00000000000000100000000000000")
        >>> next(ca)
        '00000000000001010000000000000'
        >>> ca._strIsBinary("00100")
        True
        >>> ca._strIsBinary("00200")
        False
        >>> ca._advance()
        '00000000000010001000000000000'
        >>> ca._applyRule(2)
        '0'
        >>> ca._applyRule(12)
        '1'
        >>> ca._cellsValues(12)
        '001'
        >>> ca._cellsValues(1)
        '000'
    """

    def __init__(self, rule, initialState):
        """
        The constructor for CellularAutomaton class. 

        Parameters: 
           rule (String): The rule of the cellular automaton. 
           initialState (String): The initial state of the cellular automaton.  

        Raises:
            ValueError: Initial state must contain only 0 and 1.
            ValueError: Rule must be in interval 0-256. 
        """
        if not self._strIsBinary(initialState):
            raise ValueError("Initial state must contain only 0 and 1.")
        if rule in range(0, 256):
            self.rule = rule
            self.state = initialState
        else:
            raise ValueError("Rule must be in interval 0-256.")

    def __iter__(self):
        return self

    def __next__(self):
        self.state = self._advance()
        return self.state

    def _strIsBinary(self, string):
        """
        The function checks if the given string is binary. 

        Parameters: 
            string (String): The string to be checked. 

        Returns: 
            True: If the given string is binary. 
            False: If the given string is not binary.
        """
        for character in string:
            if not character in '01':
                return False
        return True

    def __str__(self):
        """
        The function changes the format of the state string by replacing "0" with " " and "1" to "*". 

        Returns: 
            String: Representing the formatted state string.
        """
        printString = ""
        for char in self.state:
            if char == '0':
                printString = printString + " "
            else:
                printString = printString + "*"
        return printString

    def _advance(self):
        """ 
        The function advances the current state to the next state by appling the rule. 

        Returns: 
            String: A string representing the next state. 
        """
        newState = ""
        for index in range(len(self.state)):
            newState = newState + self._applyRule(index)
        return newState

    def _applyRule(self, elementIndex):
        """
        The function applies the rule to the element from the given index.

        The functions converts the rule to binary, gets the value of the element from the given index, from it's left and from it's right and then converts this pattern to int and then it will extract the value that needs to be set based on it.

        Parameters:
            elementIndex (int): The index of the element used to apply the rule.

        Returns:
            String: The value that needs to be set resulted from applying the rule. It's value will be 0 or 1.

        """
        binaryRule = '{0:08b}'.format(self.rule)
        cellPattern = self._cellsValues(elementIndex)
        patternInteger = int(cellPattern, 2)
        return binaryRule[7-patternInteger]

    def _cellsValues(self, elementIndex):
        """
        The function gets the elements from the given index, from its left and from its right.
        If the left or right elements are out of bounds their value will be 0.

        Parameters:
            elementIndex (int): The index of the element.

        Returns:
            String: Representing the left, middle and right element. 
        """
        left = self.state[elementIndex -
                          1] if elementIndex - 1 > 0 else 0
        middle = self.state[elementIndex]
        right = self.state[elementIndex +
                           1] if elementIndex + 1 < len(self.state) else 0

        return (f'{left}{middle}{right}')


if __name__ == "__main__":
    import doctest
    doctest.testmod()

ca = CellularAutomaton(90, "00000000000000100000000000000")
print(f'Rule: {ca.rule}, Initial State: {ca.state}')
print(ca)
# Advance only 10 more states
count = 0
for index in ca:
    if count < 10:
        print(ca)
        count += 1
    else:
        break
