# Meeting Preparation Crew

This project uses `CrewAI` to help you prepare for meetings by researching both the company and the person you are meeting. The agents in this project gather relevant information such as company news, product launches, social media activity (specifically on X, formerly Twitter), and the professional background of the individual you are meeting.

## Features

- **Company Research:** An AI agent gathers information about the company, including recent product launches, news, events, and social media presence on X.
- **Personal Bio Research:** Another AI agent focuses on the professional background of the individual, including their career, current role, and social media activity on X.
- **Markdown Output:** The bio research is saved in a markdown file (`bio_summary.md`) for easy reference.
- **Customizable Topics:** Use the `topic` variables like `{company}`, `{person_name}`, `{person_position}`, and `{website}` to tailor the search and research.

## Project Structure

The project is organized as follows:

```plaintext
├── main.py             # The main script that kicks off the CrewAI agents.
├── README.md           # This documentation file.
├── bio_summary.md      # Generated file containing a detailed bio of the person.
└── requirements.txt    # List of dependencies (Optional: for future use)

Getting Started

Prerequisites

Ensure you have Python 3.7+ installed. You'll also need to install the following packages:

CrewAI
openai
serper

You will need API keys for:

Serper API for web search functionality.

OpenAI API for language model access.

Installation

Clone the repository (or create the folder manually):

git clone https://github.com/your-repo/MeetingPrepCrew.git

cd MeetingPrepCrew

Set up a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\Activate

Install dependencies:

pip install crewai openai serper
Set up API keys:

Set the API keys for Serper and OpenAI in your environment:

Windows PowerShell:

$env:SERPER_API_KEY="your-serper-key"
$env:OPENAI_API_KEY="your-openai-key"

Mac/Linux:

export SERPER_API_KEY="your-serper-key"
export OPENAI_API_KEY="your-openai-key"

Running the Project

Edit the main script (main.py) to include the details of the company and person you're meeting.

Example:

prepare_for_meeting(
    company="Tesla",
    person_name="Elon Musk",
    person_position="CEO",
    website="https://www.tesla.com"
)
Run the script:

python main.py

The result will print out in the console, and a markdown file (bio_summary.md) will be generated containing the bio summary of the person.

Example Output
Console Output
plaintext

Company Research Results for Tesla:
- Recent News: ...
- Product Launches: ...
- Social Media Activity on X: ...

Personal Bio Results for Elon Musk:
- Professional Background: ...
- Current Position: CEO at Tesla
- Social Media (X) Activity: ...
Markdown Output (bio_summary.md)

# Bio Summary: Elon Musk

- **Position**: CEO at Tesla
- **Career**: Elon Musk has held positions at SpaceX, Tesla, and other companies...
- **Social Media Activity**: Frequent updates on X (formerly Twitter) regarding SpaceX launches and Tesla products.

Customization

You can modify the inputs to gather information for other companies or people by editing the prepare_for_meeting() function in main.py. Simply adjust the company, person_name, person_position, and website parameters to fit your meeting.

Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

License
This project is licensed under the MIT License.

---

### Key Sections in the README:

- **Overview of the project** and its purpose.
- **Features** explaining what the project does.
- **Installation instructions** for dependencies and setting up API keys.
- **Running the project** with example inputs and outputs.
- **Customization** section explaining how users can modify the project for their own meetings.
- **Contributing** section if others want to contribute to your project.

Let me know if you need any further modifications to the README!