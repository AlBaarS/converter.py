class InvalidTemperatureError(Exception):
    """Exception raised when the temperature converter was selected but an invalid temperature unit was submitted.

    Attributes:
        message -- explanation of the error
    """
    error_code: int = 1

    def __init__(self, arguments: str) -> None:
        self.message: str = f"""
An invalid temperature unit was parsed: {arguments}.
Make sure that you submit a valid temperature unit.
For help, use convert.py help temperature
    """

    def __str__(self) -> str:   # pragma: no cover
        return f"{self.message} (Error Code: {self.error_code})"
