# AI Chatbot for Mental Health Support

An AI-powered chatbot designed to provide initial mental health support and resources in a conversational format. The application uses a Streamlit frontend for an intuitive user interface and a Flask backend to serve the AI model's responses.

### Features
* **Conversational Interface:** A user-friendly chat interface for interacting with the chatbot.
* **AI-Powered Responses:** Utilizes a custom-trained model to generate relevant and empathetic responses.
* **Scalable Architecture:** Separate frontend and backend components for easy development and deployment.

### Technologies
This project is built using the following technologies:
* **Python:** The core programming language.
* **Streamlit:** For building the interactive chatbot frontend.
* **Flask:** For creating the REST API backend.
* **TensorFlow:** Used for the underlying AI model.
* **Requests:** For handling API calls between the frontend and backend.

### Getting Started

Follow these instructions to set up and run the chatbot on your local machine.

#### Prerequisites
* [Python 3.8+](https://www.python.org/downloads/) installed.
* [Git](https://git-scm.com/downloads) installed.

#### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Jagadesh2401/AI-Chatbot-for-Mental-Health-Support.git](https://github.com/Jagadesh2401/AI-Chatbot-for-Mental-Health-Support.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd AI-Chatbot-for-Mental-Health-Support
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

The application consists of two parts: a backend API and a Streamlit frontend. Both must be run in separate terminal windows.

1.  **Start the Backend API:**
    Open a new terminal and run the following command:
    ```bash
    python app.py
    ```
    This will start the Flask server on `http://127.0.0.1:5000`. Keep this terminal window open.

2.  **Start the Streamlit Frontend:**
    Open a **second** terminal, navigate to the project directory, and run the following command:
    ```bash
    streamlit run chatbot_frontend.py
    ```
    This will open the chatbot application in your web browser.

### Contributing
Contributions are welcome! If you'd like to improve this project, feel free to open a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.