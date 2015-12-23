from enum import Enum


class CreditCardOperationEnum(Enum):
    AuthOnly = 1,
    AuthAndCapture = 2,
    AuthAndCaptureWithDelay = 3
