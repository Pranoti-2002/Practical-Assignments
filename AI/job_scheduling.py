import heapq 
class Job:
    def __init__(self , id , priority , duration):
        self.id=id
        self.priority=priority 
        self.duration=duration 
    
    def __lt__(self , other):
        return self.priority <other.priority 

def schedule_jobs(jobs):
    scheduler=[] 
    result=[] 

    for job in jobs:
        heapq.heappush(scheduler , job) 
    while scheduler:
           current_job=heapq.heappop(scheduler) 
           result.append(current_job) 
    return result 

job1=Job(1 ,2 , 4) 
job2=Job(2 ,4 , 3)  
job3=Job(3 , 3 , 5) 

jobs=[job1 , job2 , job3] 

scheduled_jobs=schedule_jobs(jobs) 
for job in scheduled_jobs:
    print(f"Job {job.id}: Priority {job.priority} , Duration {job.duration}")  