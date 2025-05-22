<h1 align="center">🧠 HRBot: Conversational AI for Human Resources</h1>
<h3 align="center">Fine-tuned LLaMA 3.2B Model | GGUF Conversion | Ollama Deployment</h3>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

![hr_bot_presentation](https://github.com/user-attachments/assets/b8e8cb2f-5f5f-472b-bc51-3f48a5912b0f)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 📖 Introduction:
The **HRBot** project is designed to revolutionize Human Resource automation using a conversational AI fine-tuned specifically for HR-related queries. Built on top of the **LLaMA 3.2B Instruct** model, this project encapsulates model fine-tuning, conversion to **GGUF format**, and deployment via **Ollama** for a seamless local experience.

HRBot is capable of answering frequently asked questions, providing company policy insights, and acting as a digital assistant for HR departments.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🌐 Project Description

### 📌 Overview
In this capstone project, I embark on a journey to create an **Industry-Specific Large Language Model (LLM) Bot** using state-of-the-art pre-trained models from platforms like Hugging Face. The core objective is to build an intelligent bot that can effectively engage with users by answering questions and providing insights tailored to the **Human Resources** domain.

This project not only sharpens technical proficiency in NLP, LLMs, and model deployment, but also deepens understanding of industry-specific knowledge, challenges, and communication patterns.

### 🎯 Project Objectives
1. **Industry Selection:** Focus on the Human Resources industry to contextualize all aspects of data curation and model development.
2. **Data Collection:** Curate HR-specific datasets involving policies, benefits, recruitment Q&A, onboarding/offboarding, employee relations, and more.
3. **Model Selection & Training:** Choose a base LLM (LLaMA 3.2B Instruct) and fine-tune it using NVIDIA GeForce RTX 3090 with a training cap of 25 epochs.
4. **Bot Development:** Design a chatbot capable of understanding and responding to HR-related queries with relevance and accuracy.
5. **Demonstration:** Record a video demonstrating the bot’s capabilities with real-world HR queries and conversations.
6. **[Optional - Research Paper:]** Extend the work into a research paper during the Industry Immersion module, highlighting findings and use cases from this project.

### 🏭 Chosen Industry
- **Human Resources (HR)** under the broader **Technology and Information Technology (IT)** category.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 📋 Capstone Execution Goals:
1. **Fine-Tuning LLMs:** Fine-tune the LLaMA 3.2B Instruct model on curated HR datasets to specialize in HR dialogues.
2. **Model Conversion:** Convert the trained model to GGUF format for lightweight and efficient inference.
3. **Local LLM Deployment:** Use **Ollama** to run the GGUF model on local machines with minimal setup.
4. **Conversational Flow:** Enable multi-turn conversations tailored for HR domains such as leave policies, benefits, hiring, and more.
5. **Future Extension:** Enable integration into HR platforms, internal chat tools, and employee self-service portals.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🛠️ Technologies Used:
- **Model Architecture:** LLaMA 3.2B Instruct
- **Fine-Tuning Frameworks:** Hugging Face Transformers, LLaMA-Factory
- **Model Format:** GGUF (for efficient local inference)
- **Local Inference Runtime:** Ollama
- **Tokenizers & Optimizers:** BitsAndBytes, Flash Attention
- **Training Tools:** Transformers, Accelerate, Datasets

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🚀 Getting Started

### ✅ Prerequisites
Ensure you have the following installed:
- Python 3.10+
- Ollama ( ollama run KolekarPramod/hr_bot_v3 )
- Git
- CUDA (for GPU-based inference, optional)

### 📦 Clone the Repository
```bash
[git clone https://github.com/KolekarPramod/hrbot-llama3.git](https://github.com/KolekarPramod/hrChatBot.git)
cd hrChatBot
pip install -r requirements.txt
python hr.py
