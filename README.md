Suppose there is an enterprise with a paid subscription to use AI-agents platform. The company has a web-site. Each day a product owner wants to add a new or update old feature (for example, a button) to the web-site. The product owner decides to implement features using an AI-agents platform. How much will it cost?

I decided to calculate costs for that case. The artefacts committed in the folder:
* Sequence diagrams formed in Mermaid format with 2 scenarios (without bugs and with bugs). It shows a naive communication between AI-agents.
* Cost calculation in a spreadsheet for a scenario with bugs but added here in Python format.

The cost per button is equal to **$1.97 per cycle**. It seems low. But if a team of 5 developers make 60 cycles of such changes, debugs, commits per day then a naive system of 5 AI-agents would spend **$118.35 per day** only for tasks on adding interface elements. It would lead to costs of **$2367 per month**.

To sum up, it's an idea for a project named Cost calculator for AI-agents collaboration.

---


Special thanks to Andrei Antoshkin for the inspiring post how AI changes processes.
