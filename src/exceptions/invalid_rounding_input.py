class InvalidRoundingInputError(Exception):
    """Exception raised when two units were found of different types

    Attributes:
        message -- explanation of the error
    """

    error_code: int = 1

    def __init__(self, rounding_input: str):
        self.message: str = f"Given rounding parameter {rounding_input} could not be converted to integer."
  
    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
