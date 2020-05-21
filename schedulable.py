class Schedulable():

	def schedule(self):
		self.schedule = Schedule() #if not self.schedule else self.schedule
		return self.schedule

	def schedulable(self, start_date, end_date):
		return not self.scheduled(start_date - self.lead_days(), end_date)

	def scheduled(self, start_date, end_date):
		self.schedule().is_scheduled(self, start_date, end_date)



class Schedule():
	
	def is_scheduled(self, schedulable, start_date, end_date):
		print("This {0} is not scheduled\n between {1} and {2}".format(type(schedulable), start_date, end_date))
		return False