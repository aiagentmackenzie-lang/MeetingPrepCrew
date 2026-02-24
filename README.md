# Meeting Preparation Crew

This project leverages **CrewAI** to streamline your meeting preparation by researching both the company and the individual you are meeting. The agents gather critical information such as company news, product launches, social media activity (specifically on X), and the professional background of your contact to ensure you are fully briefed.

## Features

* **Company Research:** An AI agent gathers insights about the organization, including recent product launches, major news, events, and their social media presence.
* **Personal Bio Research:** A specialized agent focuses on the professional background of the individual, including their career trajectory, current responsibilities, and recent activity on X.
* **Markdown Output:** The research results are automatically saved to a markdown file (`bio_summary.md`) for quick reading or printing before your meeting.
* **Customizable Inputs:** Easily tailor searches using variables like `{company}`, `{person_name}`, `{person_position}`, and `{website}`.

---

## Project Structure

```text
MeetingPrepCrew/
├── main.py             # Main script to execute CrewAI agents
├── README.md           # Project documentation
├── bio_summary.md      # Generated research report
└── requirements.txt    # Project dependencies
Getting Started
Prerequisites

Python 3.7+

Serper API Key: For web search functionality.

OpenAI API Key: For language model processing.

Installation

1. Clone the repository:

Bash
git clone [https://github.com/aiagentmackenzie-lang/MeetingPrepCrew.git](https://github.com/aiagentmackenzie-lang/MeetingPrepCrew.git)
cd MeetingPrepCrew
2. Set up a virtual environment (recommended):

Bash
python -m venv venv
# Windows:
.\venv\Scripts\Activate
# Mac/Linux:
source venv/bin/activate
3. Install dependencies:

Bash
pip install crewai openai serper
4. Set up API keys:

Bash
# Windows PowerShell:
$env:SERPER_API_KEY="your-serper-key"
$env:OPENAI_API_KEY="your-openai-key"

# Mac/Linux:
export SERPER_API_KEY="your-serper-key"
export OPENAI_API_KEY="your-openai-key"
Running the Project
Update the main.py script with the specific details of your upcoming meeting:

Python
prepare_for_meeting(
    company="Tesla",
    person_name="Elon Musk",
    person_position="CEO",
    website="[https://www.tesla.com](https://www.tesla.com)"
)
Run the script:

Bash
python main.py
Example Output (bio_summary.md)

Markdown
# Bio Summary: Elon Musk

- **Position**: CEO at Tesla
- **Career**: Background spanning SpaceX, Tesla, and X.
- **Social Media Activity**: Frequent updates regarding engineering milestones and corporate strategy.
Customization
You can modify the inputs for any meeting by editing the prepare_for_meeting() function parameters in main.py. This allows you to pivot between different industries or seniority levels seamlessly.

Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

License
This project is licensed under the MIT License.

Contact Information
For further information or assistance, please contact the project maintainer at:
aiagent.mackenzie@gmail.com
