from typing import List
from models.fee_estimate import FeeEstimate
from estimators.base import FeeEstimator
import requests

class BitcoinCoreEstimator(FeeEstimator):
    def url(self):
        return "http://127.0.0.1:8332"
    
    def name(self) -> str:
        return "Bitcoin Core"
    
    def get_estimates(self) -> List[FeeEstimate]:
        targets = [1, 3, 6]
        estimates = []
        for conf_target in targets:
            json_response = self.bitcoinRpc("estimatesmartfee", [conf_target])

            if json_response.get("feerate"):
                sat_vb = json_response["feerate"] * 1e8 / 1000
                estimates.append(FeeEstimate(conf_target, sat_vb))

        return estimates
    
    def bitcoinRpc(self, method: str, params=[]):
        # TODO: change authentication
        payload = {
            "jsonrpc": "2.0",
            "id": "feeEstimateBenchmark",
            "method": method,
            "params": params
        }
        response = requests.post(self.url(), json=payload, auth=("mempool", "mempool"))
        
        response.raise_for_status()
        return response.json()