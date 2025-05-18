# https://school.programmers.co.kr/learn/courses/30/lessons/42627

from heapq import heappush, heappop

def solution(jobs):
  count = len(jobs)
  heap = []
  current_time = 0
  clear_job = []
  current_job = []
  clear_time = 0
    
  job_dic = {}
    
  for index, job in enumerate(jobs):
    request_time = job[0]
    job.append(index)
    if request_time not in job_dic:
      job_dic[request_time] = [job]
    else:
      job_dic[request_time].append(job)
    
  while True:
    if current_time in job_dic:
      for job in job_dic[current_time]:
        heappush(heap, [job[1], job[0], job[2]])
      
    if len(current_job) == 0 and heap:
      current_job = heappop(heap)
    
    current_time += 1
    if current_job:
      current_job[0] -= 1
      
      if current_job[0] == 0:
        current_job.append(current_time)
        clear_job.append(current_job[:]) 
        current_job = []
    
    if len(clear_job) == count:
      break
    
  for job in clear_job:
    clear_time+= job[-1] - job[1]
    
  return int(clear_time / count)
