class AmericanDetectedError(Exception):
    """Exception raised when the user wishes to convert to football fields, hamburgers, etc.

    Attributes:
        message -- explanation of the error
    """
    error_code: int = 1

    def __init__(self, arguments: str) -> None:
        self.message: str = f"""
No valid unit string was found in your input: {arguments}.
This converter only uses real and freedom units, as recognized by ISO
    """

    def __str__(self) -> str:   # pragma: no cover
        return f"{self.message} (Error Code: {self.error_code})"
