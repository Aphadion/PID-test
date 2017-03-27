import math
from datetime import datetime, timedelta
import time

"""To Do:
1. Add method to remove jobs after timeout given by normal dist.
2. Set functions to iterate over discrete "time" (for now)
3. Output results in CSV(?) format for graphing in Excel
"""


class JobList:
    """Stores list of processing jobs with start times"""
    def __init__(self):
        self.dict = {}
        self.newest_id = 1

    def __len__(self):
        self.len = len(self.dict)
        return self.len

    def addNew(self):
        # Add new job to the job dictionary with unique ID, storing start time
        start_time = datetime.utcnow()
        job_id = format(self.newest_id, '04d')
        self.newest_id += 1
        self.dict[job_id] = start_time
        return job_id

    def calculateDelay(self):
        # Calculate the total waiting time, for all jobs, in seconds
        job_delay = 0
        current_time = datetime.utcnow()
        for start_time in self.dict.values():
            delta_time = current_time - start_time
            job_delay += delta_time.total_seconds()

        return job_delay

class PID:
    """Performs PID strategy calculation actions"""
    def __init__(self, P=0.5, I=0.001, D=0.15, delta=0.1,
                 Int_max=500, Int_min=0):
        self.P = P
        self.I = I
        self.D = D
        self.delta = delta
        self.Int_max = Int_max
        self.Int_min = Int_min

    def calculateProportional(self, error):
        proportional_term = self.P * error
        return proportional_term

    def calculateIntegral(self, error, requests):
        integral_term = (self.I * self.delta * error) + \
                        (requests * self.delta * self.delta)
        return integral_term

    def calculateControl(self, error, requests):
        control_variable = self.calculateProportional(error) + \
                                    self.calculateIntegral(error, requests)
        return control_variable

def main():

    jobs = JobList()

    jobs.addNew()
    time.sleep(1)
    jobs.addNew()
    time.sleep(1)
    jobs.addNew()
    time.sleep(2)

    print(jobs.dict)

    error = jobs.calculateDelay()
    requests = len(jobs)

    print(error)

    new_PID = PID()

    print(new_PID.calculateControl(error, requests))

if name == "__main__":
    main()
