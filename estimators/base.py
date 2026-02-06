from abc import ABC, abstractmethod
from typing import List
from models.fee_estimate import FeeEstimate

class FeeEstimator(ABC):
    @abstractmethod
    def name(self)-> str:
        pass

    @abstractmethod
    def get_estimates(self)-> List[FeeEstimate]:
        pass