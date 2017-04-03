import math
import numpy
import time

from datetime import datetime, timedelta
from tabulate import tabulate

"""To Do:
1. Add method to remove jobs after timeout given by normal distribution
2. Sort out a proper way of looping discrete_time (I really don't think a
global variable is the way to go)
3. Output results in CSV(?) format for graphing in Excel
"""


class ProcessingJob:
    """A Processing Job with ID, start time and processing duration"""
    def __init__(self, id, start_time, proc_duration):
        self.id = id
        self.start_time = start_time
        self.proc_duration = proc_duration
        self.stop_time = start_time + proc_duration


class JobList:
    """Stores list of processing jobs with start times"""
    def __init__(self):
        self.jobs = []
        self.newest_id = 1

    def __len__(self):
        self.len = len(self.jobs)
        return self.len

    def addNew(self):
        # Add new job to the job dictionary with unique ID, storing start time
        start_time = discrete_time
        proc_duration = round(numpy.random.normal(loc=180, scale=30))
        job_id = self.newest_id
        self.newest_id += 1
        new_job = ProcessingJob(job_id, start_time, proc_duration)
        self.jobs.append(new_job)
        return job_id

    def calculateDelay(self):
        # Calculate the total waiting time, for all jobs, in seconds
        job_delay = 0
        current_time = discrete_time
        for start_time in [job.start_time for job in self.jobs]:
            delta_time = current_time - start_time
            job_delay += delta_time
        return job_delay

    def printJobs(self):
        # Print the current processing jobs in readable format
        display_table = [['Job ID', 'Start Time']]
        for job in self.jobs:
            display_table.append([job.id, job.start_time])
        print(tabulate(display_table))
        return True

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


    global discrete_time
    discrete_time = 0

    jobs = JobList()

    jobs.addNew()
    discrete_time += 1
    jobs.addNew()
    discrete_time += 2
    jobs.addNew()
    discrete_time += 3

    jobs.printJobs()

    error = jobs.calculateDelay()
    requests = len(jobs)

    print(error)

    new_PID = PID()

    print(new_PID.calculateControl(error, requests))

if __name__ == "__main__":
    main()
