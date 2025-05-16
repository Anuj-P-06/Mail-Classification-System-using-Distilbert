# Mail-Classification-System-using-Distilbert

## Table of Contents  
- [Project Overview](#project-overview)  
- [Reasons for Making This Project](#reasons-for-making-this-project)  
- [Tools and Technologies Used](#tools-and-technologies-used)  
- [Tasks Performed](#tasks-performed)  
- [Web App Screenshots and UI](#web-app-screenshots-and-ui)  
- [Results and Findings](#results-and-findings)

---

## Project Overview:
This project is a **Spam Detection System** built using a fine-tuned **DistilBERT** model to classify SMS or email messages as either **spam** or **ham** (not spam). It uses Hugging Face Transformers for model training, and a Flask-based web application with a clean HTML/CSS/JavaScript interface for user interaction. The model leverages transfer learning with state-of-the-art NLP techniques to provide accurate and efficient spam classification.

---

## Reasons for Making This Project:
- **Natural Language Processing Practice**: To gain hands-on experience with real-world text classification tasks using transformer-based models.
- **Transfer Learning**: To utilize pre-trained models like DistilBERT for quick adaptation to downstream tasks.
- **Web App Integration**: To combine ML with full-stack development using Flask and front-end technologies.
- **Deployment Ready**: To create a complete, interactive project that can be deployed online.
- **Research-Oriented**: Part of a research initiative titled *Spam Detection System Using LLM*, showcasing applied AI for communication filtering.

---

## Tools and Technologies Used:
- **Python** → Data preprocessing, model fine-tuning, backend logic  
- **Hugging Face Transformers** → Pre-trained DistilBERT model for NLP  
- **Datasets Library** → For loading and preprocessing the SMS spam dataset  
- **Scikit-learn** → For computing evaluation metrics  
- **Flask** → For backend API and routing  
- **HTML/CSS/JavaScript** → Frontend interface  
- **Torch (PyTorch)** → Deep learning backend for model inference  

---

## Tasks Performed:

### 1) Dataset Preparation:
- Loaded the spam/ham message dataset using Hugging Face Datasets.
- Tokenized messages using DistilBERT tokenizer.
- Preprocessed text with truncation and padding for model input.

### 2) Model Fine-Tuning:
- Fine-tuned DistilBERT on the binary classification task (Spam vs Ham).
- Used Trainer API from Hugging Face with evaluation and logging.
- Computed accuracy as a metric during training.

### 3) Model Saving:
- Saved the fine-tuned model and tokenizer locally in a directory for later inference.

### 4) Flask Web Application:
- Created a Flask backend to load the fine-tuned model.
- Built routes to receive user input and return prediction results.
- Rendered predictions on a custom HTML frontend with styling and interactivity.

### 5) Frontend Design:
- Developed a simple and responsive UI using HTML, CSS, and JS.
- Created a message input form with real-time classification on submission.
- Displayed classification result with clear labels (Spam or Ham).

---

## Web App Screenshots and UI:

![UI Screenshot](![Image](https://github.com/user-attachments/assets/02666624-d125-49f1-852e-c5f7daf2e571))

> Replace the image link with an actual screenshot once available.

You can also test it locally:
```bash
python app.py
```

## Results and Findings:

- ✅ Successfully fine-tuned DistilBERT for spam classification with high accuracy.  
- ✅ Created a fully functional web app for message classification.  
- ✅ Model can handle short message spam detection in real-time.  
- ✅ Demonstrated that LLMs like DistilBERT are effective even for small-scale NLP tasks.  
- ✅ Can be extended for multilingual or domain-specific spam detection tasks.  
- ✅ User-friendly interface makes it deployable as a lightweight anti-spam solution.  

