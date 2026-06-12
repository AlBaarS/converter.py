class InvalidNumberOfInputArgumentsError(Exception):
    """Exception raised when the input string is incorrectly formatted.

    Attributes:
        message -- explanation of the error
    """
    error_code: int = 1

    def __init__(self, arguments: list[str]) -> None:
        self.message: str = f"""
An invalid number of input arguments was parsed: {arguments}.
Make sure that your input follows the required format: <value><input_unit> to <output_unit>
Examples:
    convert.py 2.4m to ft
    convert.py 1.2 l to cup round 2
    convert.py 40 square meters to square feet
    """

    def __str__(self) -> str:
        return f"{self.message} (Error Code: {self.error_code})"
