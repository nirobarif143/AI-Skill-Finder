# AI Dynamic Skill Finder: Remote Market Edition
Final project for the Building AI course

## Summary
The AI Dynamic Skill Finder is a Python-based tool that analyzes real-time global remote job advertisements (via API) to identify which technical keywords and skills are currently in highest demand. It provides job seekers with a data-driven report to optimize their learning and resumes.

---

## Background
The modern job market, especially for digital and IT roles, evolves too quickly for traditional career advice to keep up.

* **Problem:** Job seekers struggle to determine the exact, current technical skills (e.g., AWS vs. Azure, React vs. Vue) that employers are prioritizing, leading to wasted study time.
* **Frequency:** This uncertainty affects nearly every graduate and career-changer globally.
* **Motivation:** As an IT professional, I recognized the need for an **unbiased, data-driven tool** to bridge the gap between education and employment, focusing specifically on the high-growth remote sector.

---

## How is it used?
The solution is a command-line application that acts as a **Smart Digital Assistant** to analyze job trends.

The user runs the Python script and types their desired job category (e.g., `DevOps`, `Marketing`, or `Cloud Engineer`). The program executes a four-step process to produce a statistical report: 

[Image of Data Flow Diagram for job market analysis]


1.  **Collection:** Connects to the live Remotive API.
2.  **Cleaning:** Filters out boilerplate text and common English words (Stop-Word Removal).
3.  **Analysis:** Counts the frequency of the remaining, meaningful technical terms.
4.  **Reporting:** Displays the top 20 skills using a clear **ASCII bar visualization** and a corresponding percentage score.

The primary users are job seekers, career counselors, and students looking for actionable market insight.

---

## Data sources and AI methods
The project relies exclusively on easily accessible internet data, avoiding the need for specialized hardware or complex APIs requiring authentication keys.

| Component | Description |
| :--- | :--- |
| **Data Source** | **Remotive API (JSON):** A free and open API providing current, global remote job data. The data is fetched in JSON format using Python's standard `urllib` library. |
| **AI Method 1** | **Natural Language Processing (NLP) Fundamentals:** The core logic uses **Tokenization** (breaking text into words) and an extensive **Stop-Word Removal** filter to focus analysis only on relevant technical jargon. |
| **AI Method 2** | **Frequency Analysis:** A statistical approach that calculates the **demand score** (frequency percentage) for each skill. The highest frequency equals the highest market demand. |

---

## Challenges
It's important to understand the limitations of a simple AI solution:

* **API Rate Limits:** The program is restricted by the API's constraints on how many times it can query the data in a given period.
* **Contextual Understanding:** The current simple model cannot understand context. It cannot differentiate between "need **SQL** knowledge" (a requirement) and "familiarity with **SQL** is a plus" (a secondary requirement).
* **Soft Skill Filtering:** While the filter is extensive, it remains challenging to perfectly separate generic job language from genuine soft skills (e.g., distinguishing "MANAGEMENT" as a skill from "project management").

---

## What next?
This project can grow significantly by adding new features and overcoming current limitations:

1.  **Historical Tracking:** Integrate a database (like SQLite) to store daily results. This would allow the application to track skill popularity **over time** (e.g., see if AWS is gaining or losing popularity compared to Azure over the last 6 months).
2.  **Web Interface:** Develop a simple front-end UI (using HTML/JavaScript) so that the tool is accessible to non-programmers who are not comfortable running Python scripts from the command line.
3.  **Advanced NLP:** Implement a library like NLTK or spaCy to use techniques like **Lemmatization** (grouping words like 'develop' and 'developing' together) and **Named Entity Recognition (NER)** for cleaner skill extraction.

---

## Acknowledgments
* Concept inspired by the final project requirements of the **Building AI course** by Reaktor and the University of Helsinki.
* Live job data provided courtesy of the **Remotive API**.