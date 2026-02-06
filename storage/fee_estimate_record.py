from dataclasses import dataclass
from typing import Optional

@dataclass
class FeeEstimateRecord:
    source: str
    timestamp: str
    targetblock: int
    feerate_sat_vb: float
    confidence: Optional[float] = None