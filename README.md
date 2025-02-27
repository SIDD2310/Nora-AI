# NORA AI

Welcome to **NORA AI!** This application is designed to assist children—especially those with limited language exposure—in developing stronger communication and language skills. Through engaging conversations with an AI agent, children can explore various topics, expand their vocabulary, and spark their imaginations. The system also provides a **research-based analysis** to parents or caregivers, offering practical insights into the child's developmental journey.

---

## Table of Contents
1. [Overview](#overview)
2. [Market Potential](#market-potential)
3. [Key Features](#key-features)
4. [Architecture & Workflow](#architecture--workflow)
5. [Contributing](#contributing)
6. [License](#license)

---

## Overview

**Why this project?**  
Children with limited language exposure are more at risk of language and communication delays. This project aims to provide a **playful yet impactful** way for children to engage in conversations with a friendly AI character (named “Nora” by default), helping them practice their language skills in a supportive environment. 

Parents or educators receive:
- A **complete transcript** of the conversation.
- An **automated analysis** based on early childhood development frameworks.
- Suggestions for **conversation starters**, **hands-on activities**, and **additional resources** to further enrich the child’s language environment.

---

## Market Potential

The global *language learning market* is experiencing significant growth, projected to reach *$120.5 billion by 2030, growing at a **CAGR of 10.5%*. 

With an increasing demand for *multilingual education* and *early language development tools, there is a significant opportunity for AI-driven solutions like **Nora AI* to make a lasting impact. 

The market segment for *children’s language learning, in particular, remains largely underserved, highlighting the potential for **broad adoption in homes, schools, and early education programs worldwide*.

---

## Key Features

1. **Real-Time, Interactive Conversation (ElevenLabs Conversational AI)**  
   - An embedded ElevenLabs Conversational AI widget allows **real-time** interaction with the child.  
   - Child-friendly voice output ensures the experience is **engaging and accessible**.  

2. **Multi-Language Support**  
   - Supports **Chinese, Dutch, Arabic, English, and Hindi**.  
   - Children can speak in any of these languages, and Nora will respond accordingly.

3. **Automated Transcript Retrieval**  
   - Fetch the child’s conversation transcript with a single click.  
   - Transcript includes both the AI’s and the child’s dialogues (labeled “Nora” and “Little Explorer” respectively).

4. **Language Development Analysis (Google Generative AI - “Gemini”)**  
   - Automatically sends the conversation transcript to a **Large Language Model** (Gemini) for analysis.  
   - Delivers a **research-based report** containing:  
     - Child’s speech and language usage.  
     - Main topics and child’s engagement patterns.  
     - Positive developmental highlights.  
     - Areas for support and improvement.  
     - Suggested conversation starters and hands-on activities.

5. **Customizable UI (Streamlit)**  
   - **Space, Sea, Jungle, Farm Exploration Theme** (with custom fonts and visuals) for a playful and appealing interface.  
   - Easily adaptable for other themes or branding if desired.

6. **User-Friendly Dashboard**  
   - Built with **Streamlit** for an intuitive experience.  
   - Responsive layout with columns for images, AI widget, and content sections.

7. **EYLF (Early Years Learning Framework) Integration**  
   - The analysis references **EYLF Outcomes** to help parents and educators understand the child’s progress within recognized developmental standards.

---

## Architecture & Workflow

1. **Streamlit Frontend**  
   - Hosts the web application.   
   - Integrates the ElevenLabs conversational widget via embedded HTML.

2. **ElevenLabs Conversational AI**  
   - Handles real-time speech-based interaction with the child.  
   - Stores conversation transcripts and allows programmatic retrieval.

3. **Transcript Processing**  
   - When the user clicks **“Get Conversation Transcript,”** the most recent conversation data is fetched from ElevenLabs via their API.

4. **Google Generative AI (Gemini) Analysis**  
   - The transcript is sent to Gemini, which generates a **detailed analysis** focusing on language development best practices.

5. **Display of Insights**  
   - The app returns a structured **report** for parents, including **speech analysis**, **positive highlights**, **recommendations**, etc.

---

## Contributing

We welcome contributions from the community!  
- **Bug Reports & Feature Requests**: Open an issue on GitHub.  
- **Pull Requests**: Fork the repository, create a new branch, and submit a pull request with your proposed changes.

---

## License

This project is licensed under the [MIT License](LICENSE).  
Feel free to modify and distribute the app in accordance with this license.

---

**Thank you for exploring NORA AI!**  
We hope this tool provides an engaging platform for children to expand their vocabulary and fosters delightful conversations at home or in the classroom.

If you have any questions or feedback, please open an issue on GitHub or reach out to the project maintainers. Happy learning!

