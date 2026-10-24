# Phase 1 (v14xx)

Suppose there is an enterprise with a paid subscription to use AI-agents platform. The company has a web-site. Each day a product owner wants to add a new or update old feature (for example, a button) to the web-site. The product owner decides to implement features using an AI-agents platform. How much will it cost?

I decided to calculate costs for that case. The artefacts committed in the folder:
* Sequence diagrams formed in Mermaid format with 2 scenarios (without bugs and with bugs). It shows a naive communication between AI-agents.
* Cost calculation in a spreadsheet for a scenario with bugs but added here in Python format.

The cost per button is equal to **$1.97 per cycle**. It seems low. But if a team of 5 developers make 60 cycles of such changes, debugs, commits per day then a naive system of 5 AI-agents would spend **$118.35 per day** only for tasks on adding interface elements. It would lead to costs of **$2367 per month**.

To sum up, it's an idea for a project named Cost calculator for AI-agents collaboration.

# Phase 2 (v1513)

Another new architecture of an AI agents system. I'm using the same example with a button added to the project.

In a new Sequence diagram, I showed the interaction between the Code AI agent and three new agents: the QA Analyst AI agent, the API Automation AI agent, and the E2E UI Automation AI agent. I added a test environment and an orchestrator for logic and memory management. There is a test case where a UI test fails due to a bug, and the agents localize and fix the error themselves.

In this model, adding a button to a web-site with 50k tokens repo context costs **~$0.46 per almost perfect run**.
