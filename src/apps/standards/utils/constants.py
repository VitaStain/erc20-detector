from enum import Enum


class ContractStatus(str, Enum):
    WAIT_PROCESSING = "wait_processing"
    PROCESSING = "processing"
    PROCESSED = "processed"
    FAILED = "failed"
