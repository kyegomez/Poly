from typing import Any


class Poly:
    """
    A class to create Polymorphic type objects

    ...
    Attributes
    ----------
    data: Any
        the data to determine the type of
    data_type: type
        the deterined type of the data
    -----------

    Methods
    -------
    determine_type():
        Determines the type of the type of data
    select_type():
        selects the approrate type from the typing module or any other types or custom types
    """

    def __init__(self, data: Any):
        """
        Constructs all the necessary attributes for the poly object

        Parameters:
        -----------
            data: Any
                the data to determine the type of        
        """
        self.data = data
        self.data_type = self.determine_type()

    def determine_type(self):
        """
        Determines the type of the data

        Returns
        ------
        type:
        The determined type of the data
        """
        return type(self.data)
    
    def select_type(self):
        """
        Selects the approate type from the typing module or any other types or custom types

        Returns:
        -------
        type:
            the selected type
        """
        return self.data_type
    