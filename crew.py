from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, FileWriterTool
from dotenv import load_dotenv


load_dotenv()






file_read_tool = FileReadTool(file_path="C:/Users/l43ar/Downloads/newbrdtosrs/brdsrs/src/brdsrs/BRD.txt")





@CrewBase
class BrdToSrs():
	"""BrdToSrs crew"""

	
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	
	@agent
	def business_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['business_analyst'],
			tools = [file_read_tool],
			verbose=True
		)

	@agent
	def technical_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['technical_analyst'],
			tools = [file_read_tool],
			verbose=True
		)
	
	@agent
	def requirement_categorizer(self) -> Agent:
		return Agent(
			config=self.agents_config['requirement_categorizer'],

			tools = [file_read_tool,FileWriterTool()],
			verbose=True
		)
	
	@agent
	def srs_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['srs_writer'],
			tools = [file_read_tool,FileWriterTool()],
			verbose=True
		)
	
	@agent
	def srs_formatter(self) -> Agent:
		return Agent(
			config=self.agents_config['srs_formatter'],
			tools = [file_read_tool,FileWriterTool()],
			verbose=True
		)
	
	
	
	@task
	def business_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['business_analysis_task'],
		)

	@task
	def technical_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['technical_analysis_task'],
		)
	
	@task
	def requirement_categorize_task(self) -> Task:
		return Task(
			config=self.tasks_config['requirement_categorize_task'],
		)
	
	@task
	def srs_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['srs_write_task'],
		)
	
	@task
	def srs_format_task(self) -> Task:
		return Task(
			config=self.tasks_config['srs_format_task'],
			output_file='srs6.md',
		)
	

	


	@crew
	def crew(self) -> Crew:
		"""Creates the BrdToSrs crew"""
		
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
			
		)