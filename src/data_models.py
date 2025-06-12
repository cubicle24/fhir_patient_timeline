from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Patient:
    id: str
    mrn: str
    firstName: str
    lastName: str
    middelName: Optional[str] = None
    dob: Optional[datetime] = None
    gender: Optional[str] = None


@dataclass
class Condition:
    subject: Patient
    code: str
    codingSystem: str
    displayText: Optional[str] = code
    clinicalStatus: str
    onsetDate: Optional[datetime] = None
    verificationStatus: str
