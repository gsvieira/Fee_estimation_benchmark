from estimators.base import FeeEstimator
class EstimationRunner:
    def run(self, estimator: FeeEstimator):
        result = estimator.get_estimates()
        #save to db

    def run_all(self):
        pass