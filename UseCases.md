# 📘 AI Study Planner – Use Cases & High-Level Design

This document describes the key use cases, actors, workflows, and the data flow for the AI Study Planner application.

## Actors
### Primary Actor

#### Student/User
A student who wants to create a personalized study schedule.

#### System Actors
-Study Plan Generator (CalendarAgent)

-Revision Generator (RevisionAgent)

-Summary Generator (SummaryAgent)

## 🟦 Use Case 1 — Create Study Plan
### Actor:
Student/User

#### Trigger:
User clicks “Generate Study Plan” after entering topics, difficulty, and availability.

#### Preconditions:
-User has entered a list of topics

-User has assigned difficulty levels

-User has entered weekly study hours

-App is running in Streamlit

#### Main Flow:
-User enters topics and difficulty levels.

-User inputs available hours for each day/week.

-User clicks Generate Study Plan.

-CalendarAgent creates a time-based schedule.

-RevisionAgent checks difficulty and adds extra revision sessions.

-System displays the schedule in a table.

-User downloads the schedule as a CSV.

#### Alternate Flows:

A1: If no hours are entered → system shows a message:
“Please enter study hours to generate a plan.”

A2: If a topic has no difficulty → system assigns default difficulty 3.

## 🟦 Use Case 2 — Add Revision for Difficult Topics
#### Actor:

System (RevisionAgent)

#### Trigger:
Schedule is generated and RevisionAgent receives difficulty data.

#### Preconditions:
-CalendarAgent must have already generated a schedule

-Difficulty dictionary must be available

#### Main Flow:
-For each topic in the schedule, the agent checks its difficulty.

-If difficulty ≥ 3 → add an extra revision session.

-Revision entries are appended to the schedule.

-Final merged schedule is displayed and exported.

#### Alternate Flows:

A1: No topics have difficulty ≥ 3 → no revision entries are created.


## 🟦 Use Case 3 — Export Study Plan to CSV
#### Actor:
Student/User

#### Trigger:
User clicks “Download CSV”.

#### Preconditions:
-Study plan (including revision) must be generated

-User must be on the final step

#### Main Flow:
-User clicks "Download CSV".

-System packages schedule DataFrame into a CSV file.

-User's browser downloads the file.

#### Alternate Flows:

A1: User tries to download before generating → show a warning.

A2: CSV export fails → show an error message.

