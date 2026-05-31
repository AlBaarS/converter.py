#!/bin/python3
from src.orchestrator import Orchestrator

import sys

if __name__ == "__main__":
    input_args: str = " ".join(sys.argv[1:])
    print(Orchestrator().orchestrate_conversion(input_args))
