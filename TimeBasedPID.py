import math
import numpy
import time

from datetime import datetime, timedelta
from tabulate import tabulate

"""To Do:
1. Sort out a proper way of looping discrete_time (I really don't think a
global variable is the way to go)
2. Output results in CSV(?) format for graphing in Excel
"""


class ProcessingJob:
    """A Processing Job with ID, start time and processing duration"""
    def __init__(self, id, start_time, duration):
        self.id = id
        self.start_time = start_time
        self.duration = duration
        self.stop_time = start_time + duration


class JobList:
    """Stores list of processing jobs with start times"""
    def __init__(self):
        self.jobs = []
        self.newest_id = 1

    def __len__(self):
        self.len = len(self.jobs)
        return self.len

    def addNew(self, start_time):
        # Add new job to the job dictionary with unique ID, storing start time
        duration = round(numpy.random.normal(loc=180, scale=30))
        job_id = self.newest_id
        self.newest_id += 1
        new_job = ProcessingJob(job_id, start_time, duration)
        self.jobs.append(new_job)
        return job_id

    def calculateDelay(self, current_time):
        # Calculate the total waiting time, for all jobs, in seconds
        job_delay = 0
        for start_time in [job.start_time for job in self.jobs]:
            delta_time = current_time - start_time
            job_delay += delta_time
        return job_delay

    def updateFinishedJobs(self, current_time):
        finished_jobs = []
        for job in self.jobs:
            print([job.id for job in self.jobs])
            print("Updating job %i with stop_time %i" % (job.id, job.stop_time))
            if job.stop_time <= current_time:
                print("%i is less than %i"%(job.stop_time, current_time))
                finished_jobs.append(job)
            else:
                print("%i is greater than %i"%(job.stop_time, current_time))
        [self.jobs.remove(job) for job in finished_jobs]
        return finished_jobs

    def printJobs(self):
        # Print the current processing jobs in readable format
        display_table = [['Job ID', 'Start Time', 'Stop Time']]
        for job in self.jobs:
            display_table.append([job.id, job.start_time, job.stop_time])
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
        integral_term = ((self.I * self.delta * error)
                        + (requests * self.delta * self.delta))
        return integral_term

    def calculateControl(self, error, requests):
        control_variable = (self.calculateProportional(error)
                            + self.calculateIntegral(error, requests))
        return control_variable


def main():

    global discrete_time
    discrete_time = 0

    jobs = JobList()

    jobs.addNew(discrete_time)
    discrete_time += 1
    jobs.addNew(discrete_time)
    discrete_time += 2
    jobs.addNew(discrete_time)
    discrete_time += 3

    discrete_time += 100

    # print(discrete_time)
    jobs.updateFinishedJobs(discrete_time)
    jobs.printJobs()

    discrete_time += 80

    # print(discrete_time)
    jobs.updateFinishedJobs(discrete_time)
    jobs.printJobs()

    # error = jobs.calculateDelay(discrete_time)
    # requests = len(jobs)
    #
    # print(error)
    #
    # new_PID = PID()
    #
    # print(new_PID.calculateControl(error, requests))

if __name__ == "__main__":
    main()
