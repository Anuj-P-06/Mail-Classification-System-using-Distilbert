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

### 1) Model Fine-Tuning:
- Tokenized SMS messages using DistilBERT tokenizer.
- Fine-tuned the `distilbert-base-uncased` model on a binary classification task (spam vs ham).
- Used the Hugging Face `Trainer` API for training and evaluation.
- Tracked model performance using accuracy metrics.
- Saved the trained model and tokenizer to a local directory.

### 2) Flask Backend:
- Created API endpoints using Flask to render the HTML template and accept user input.
- Loaded the fine-tuned model and tokenizer at runtime.
- Performed inference on user-provided text and returned predictions as "Spam" or "Ham".

### 3) Model Saving:
- Saved the fine-tuned model and tokenizer locally in a directory for later inference.

### 4) Frontend Design (UI/UX):
- Built a responsive and interactive UI using **HTML**, **CSS**, and **JavaScript**.
- Integrated an animated **custom cursor**:  
  - A **small circle** follows the mouse pointer smoothly.
  - The circle **compresses (scales down)** when the pointer slows down or hovers over elements.
  - The circle **expands (scales up)** dynamically on fast movement or interaction.
- Designed a **transition effect** between interaction states for a more fluid and modern UX.
- Added form input for the user to enter a message and receive classification results dynamically.
- Displayed output prediction ("Spam" or "Ham") with clean styling and feedback animation.
- Ensured the frontend is mobile-friendly and styled with custom fonts, colors, and transitions.

## Web App Screenshots and UI:

![Image](https://github.com/user-attachments/assets/02666624-d125-49f1-852e-c5f7daf2e571)
![Image](https://github.com/user-attachments/assets/f13e4faa-8db2-4ac0-beb5-b882f3176a4f)
![Image](https://github.com/user-attachments/assets/a9014ebe-3487-425d-89f5-b5fc0bb0fc99)

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

