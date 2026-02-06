from typing import List
from estimators.base import FeeEstimator
from models.fee_estimate import FeeEstimate

class MempollEstimator(FeeEstimator):
    def name(self) -> str:
        return "mempool.space"
    def get_estimates(self) -> List[FeeEstimate]:
        return super().get_estimates()