def jobScheduling(requestTime, jobProcess, timeFromStart):

	
	from collections import Set

	class Job(object):

		def __init__(self,r_time,p_time,number):
			self.r_time = r_time
			self.p_time = p_time
			self.number = number
		
		def __lt__(self,other):
			if self.get_p_time() < other.get_p_time():
				return True
			else:
				return False

		def get_r_time(self):
			return self.r_time
		def get_p_time(self):
			return self.p_time
		def get_number(self):
			return self.number

	jobs = []
	for job_index in range(len(jobProcess)):
		job = Job(requestTime[job_index],jobProcess[job_index],job_index)
		jobs.append(job)
	queue = []
	finished = set([])
	t = min(requestTime)
	req_num = 2
	sorted_reqs = sorted(requestTime)

	def get_available_jobs(t):
		return [job for job in jobs if job.get_r_time() <= t and job not in queue and job not in finished]

	while t < timeFromStart:
		print queue
		if queue != []:
			#just_finished = queue.pop(0)
			just_finished = queue[0]
			del queue[0]
			t = min(timeFromStart,t+just_finished.get_p_time())
			finished.add(just_finished)
		newly_avail = get_available_jobs(t)
		for newly_available in newly_avail:
			jobs.remove(newly_available)
		queue.extend(newly_avail)
		queue = sorted(queue)
		if queue == []:
			if jobs == []:
				return []
			else:
				t = sorted_reqs[req_num]
				req_num += 1

	return [job.get_number() for job in queue]

    '''
    there are n jobs 
    job i is requested at requestTime[i]
    job i takes jobProcess[i] time
    schedule the jobs such that the average time between a job request and starting the job is minimized
    return the job queue at time timeFromStart
    '''
    # greedy : always do cheapest job first
    	# SJF : shortest job first
