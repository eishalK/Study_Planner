# 🤖 AI Development Log

Developer: Eishal

Timeline: Dec 2025

AI Assistants Used: ChatGPT, lovable

Purpose: Track all AI interactions, decisions, and risks while building the project.

# 🧠 Overview

Throughout this project, AI assistance played a major role in the entire development lifecycle. Beyond debugging and fixing errors, I also requested the full project to be created by GPT based on the requirements I provided. This included:

✨ Designing the agents (CalendarAgent, RevisionAgent, SummaryAgent)

✨ Writing the scheduling logic

✨ Creating the overall folder structure

✨ Building the CSV output logic

✨ Writing documentation (README, MD files, Use Cases, TestPlan, Release Roadmap)

✨ Improving edge-case handling

✨ Reviewing prompts and refining requirements

# 🤖 AI Tools Used
| Tool                      | Purpose                                             | Notes                                                       |
| ------------------------- | --------------------------------------------------- | ----------------------------------------------------------- |
| **ChatGPT**               | Main assistant for coding, debugging, documentation | Used extensively for agents, fixing logic, writing MD files |
| **lovable** | UI/UX and logic explanation for future prototype    | Not part of this MVP


# Chat gpt prompt
# Phase 1 — Requirements Gathering

## Prompt:
"I want to make a project in 4 hours suggest me a tech stack which is easy to implement for backend language I am using python suggest me a frontend language"

Gpt provided this tech to use in my project:

HTML + CSS + JavaScript (vanilla) – quickest for simple projects

OR Streamlit – if your project is data-heavy or interactive dashboards, this lets you build UI in Python directly without separate frontend code

OR React.js – if you want a more dynamic and modern frontend, but it takes slightly more setup


## Prompt:

“Design an assistant that converts a short-term academic goal into a concrete study schedule over the next 1–2 weeks. The user specifies what they need to prepare for (such as an exam or project milestone), which topics are involved, and what time slots they have available each day. The system should then generate a simple plan that assigns topics to specific days and sessions, balancing the workload and ensuring at least some revision time for more difficult topics. The focus is on turning vague intentions into an actionable schedule a student can realistically follow. Keep University students in mind of any discipline. (this is my requirements create a project using streamlit, python, pandas)”

GPT created a full functional project based on this prompt.

## Prompt:
"I want to enhance my UI and add a feature that it should change mode from light to dark"

Gpt provided the new code for this feature.

## Prompt:
"The schedule function is showing dataframe for both weeks by default, I want to remove that and in the dataframe show only the weeks that have been selected"

Gpt changed the default 2 weeks dataframe and set it so that only the selected week dataframe will be shown.

# Reflection: How AI Helped + Risks
## ✅ Benefits of Using GPT

Speed — GPT rapidly generated boilerplate, logic, and fixes.

Debugging Assistance — Helped identify root causes faster.

Learning Support — Explained errors, architecture, and workflows.

Code Consistency — Ensured cohesive structure across modules.

High-level planning — GPT produced the entire system design.

Documentation — Created logs, requirements, and comments.

## ⚠️ Potential Risks & Cautions

Even though AI accelerates development, it introduces risks:

### Over-Reliance

If GPT generates large portions, understanding the code becomes harder unless the developer reviews everything.

### Hidden Bugs

AI-generated code looks correct but sometimes:

Has edge-case failures

Needs manual debugging

May miss security checks

### Inconsistent Logic

AI can produce different styles unless controlled with structure and rules.


### Documentation Mismatch

AI might forget earlier decisions unless reminded, causing misalignment.

# lovable prompt
"I’m currently working on a Study Session Planner project, and I’ve been asked to imagine a refined, fully finished version of its UI for submission in 2 hours. I’ve tried searching for templates on Canva and Visily but couldn’t find anything suitable, and I’m exhausted from building this project alone. The current project takes academic inputs—such as goals, topics, and the number of weeks available (1–2)—and generates a personalized study plan in a table using Pandas. For the upgraded version, I want to envision a future-ready, advanced MVP that is more interactive, visually appealing, and feature-rich, with polished dashboards, interactive forms, improved tables and visualizations, and potential future enhancements, all based on the theme of my current project."