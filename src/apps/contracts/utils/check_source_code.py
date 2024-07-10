from typing import List


def check_source_code(functions: List[str], source_code: str) -> bool:
    """Find functions in contract source code and return True if all were found"""
    for function in functions:
        if function in source_code:
            continue
        else:
            return False
    return True
