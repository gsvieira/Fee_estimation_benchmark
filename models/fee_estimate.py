from dataclasses import dataclass
from typing import Optional

@dataclass
class FeeEstimate:
    targetblock: int
    feerate_sat_vb: float
    confidence: Optional[float] = None