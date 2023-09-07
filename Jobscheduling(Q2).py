class Job:
    def __init__(self,Id,DL,P):
        self.taskId=Id
        self.deadline=DL
        self.profit=P
def scheduleJobs(jobs,T):
    prft = 0
    slot=[-1]*T
    jobs.sort(key=lambda x: x.profit,reverse=True)
    for jobs in jobs:
        for j in reversed(range(min(T,jobs.deadline))):
            if slot[j]==-1:
                slot[j]=jobs.taskId
                prft+=jobs.profit
                break
    print("The scheduled jobs are: ",list(filter(lambda x:x!=-1,slot)))
    print("Total profit: ",prft)
if __name__=='__main__':
    n=int(input("Enter the no of jobs: "))
    jobs=[]
    for i in range (n):
        taskId=input("Enter the taskId for job {}:".format(i+1))
        deadline=int(input("Enter the deadline for job {}:".format(i+1)))
        profit=int(input("Enter the profit for job {}:".format(i+1)))
        jobs.append(Job(taskId,deadline,profit))
    T=int(input("Enter the total time: "))
    scheduleJobs(jobs,T)


# Enter the number :6
# Enter the taskId of 1 : 1
# Enter the profit of 1 : 200
# Enter the deadline of 1 : 2
# Enter the taskId of 2 : 2
# Enter the profit of 2 : 180
# Enter the deadline of 2 : 3
# Enter the taskId of 3 : 3
# Enter the profit of 3 : 120
# Enter the deadline of 3 : 2
# Enter the taskId of 4 : 4
# Enter the profit of 4 : 100
# Enter the deadline of 4 : 3
# Enter the taskId of 5 : 5
# Enter the profit of 5 : 50
# Enter the deadline of 5 : 4
# Enter the taskId of 6 : 6
# Enter the profit of 6 : 30
# Enter the deadline of 6 : 1
# Enter the Timeline4
# Scheduled jobs are : [3, 1, 2, 5]
# The total Profit : 550
