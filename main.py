import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool  # Assuming SerperDevTool is your preferred web search tool
from langchain_openai import ChatOpenAI  # Import ChatOpenAI for LLM setup

# Setting environment variables (make sure to replace these with your actual keys)
os.environ["SERPER_API_KEY"] = "d2fd408fadf55b44b304f7f61bff135d477b40e9"
os.environ["OPENAI_API_KEY"] = "sk-gt1NTXK87AnCnuGW_kl7MmWgWDrvBOb_1c2Y13tZIXT3BlbkFJ_SUXB4rVV08ALM3cFJx7OqZvDlwH0Rv9aSrE5Q0tgA"

# Create search tool
search_tool = SerperDevTool()

# Researcher agent to gather company info
company_researcher = Agent(
    role='Company Researcher',
    goal='Research the company {company} and find any relevant news, product launches, and events',
    verbose=True,
    memory=True,
    llm=ChatOpenAI(model_name="gpt-4o-mini"),  # Updated to use gpt-4o-mini
    backstory=(
        "You are an expert at uncovering business details, "
        "exploring company news, product launches, and events to give a comprehensive brief."
    ),
    tools=[search_tool]
)

# Personal bio agent to gather individual info
bio_researcher = Agent(
    role='Personal Bio Researcher',
    goal='Gather information about {person_name}, their professional background, and current position at {company}',
    verbose=True,
    memory=True,
    llm=ChatOpenAI(model_name="gpt-4o-mini"),  # Updated to use gpt-4o-mini
    backstory=(
        "With a keen eye for detail, you specialize in finding professional bios, "
        "online profiles, and career details."
    ),
    tools=[search_tool],
    output_file='bio_summary.md'  # Output file defined in the agent
)

# Task for researching the company
company_research_task = Task(
    description=(
        "Research the company {company} based on the provided website or name. "
        "Look for recent news, product launches, events, and anything relevant for the meeting."
    ),
    expected_output="A detailed brief summarizing recent updates, launches, and news about {company}.",
    agent=company_researcher,
    tools=[search_tool]
)

# Task for researching the individual
bio_research_task = Task(
    description=(
        "Research the person {person_name}, their professional background, current position at {company}, "
        "and any relevant public profiles or information."
    ),
    expected_output="A detailed bio summarizing {person_name}'s career, online profiles, and current role at {company}.",
    agent=bio_researcher,
    tools=[search_tool],
    output_file='bio_summary.md'  # Output file defined in the task
)

# Assemble the crew
meeting_preparation_crew = Crew(
    agents=[company_researcher, bio_researcher],
    tasks=[company_research_task, bio_research_task],
    process=Process.sequential
)

# Kick off the crew and provide necessary inputs
def prepare_for_meeting(company, person_name, person_position, website=None):
    inputs = {
        'company': company,
        'person_name': person_name,
        'person_position': person_position,
        'website': website
    }
    result = meeting_preparation_crew.kickoff(inputs=inputs)
    print(result)

    # Check and print the bio summary
    output_file = 'bio_summary.md'
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            content = file.read()
            if content:
                print(f"\nContents of {output_file}:")
                print(content)
            else:
                print(f"Error: {output_file} is empty.")
    else:
        print(f"Error: {output_file} was not generated.")

# Example usage
if __name__ == "__main__":
    prepare_for_meeting(
        company="CrewAI",
        person_name="Joao Moura",
        person_position="CEO",
        website="https://www.crewai.com"
    )
