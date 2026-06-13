class InvalidRoundingInputError(Exception):
    """Exception raised when the rounding argument is/contains a string or is a float

    Attributes:
        message -- explanation of the error
    """

    error_code: int = 1

    def __init__(self, rounding_input: str) -> None:
        self.message: str = f"Given rounding parameter {rounding_input} could not be converted to integer."

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.message} (Error Code: {self.error_code})"
