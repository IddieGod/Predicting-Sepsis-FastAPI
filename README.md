<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔍 Predicting Sepsis with FastAPI 🔬</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            padding: 20px;
        }

        h1 {
            color: #007bff;
        }

        h2 {
            color: #6c757d;
        }

        code {
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 4px;
        }

        pre {
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 8px;
            overflow-x: auto;
        }

        pre code {
            display: block;
            white-space: pre;
        }

        .container {
            max-width: 800px;
            margin: auto;
        }

        .container img {
            width: 100%;
            height: auto;
            display: block;
            margin: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Predicting Sepsis with FastAPI 🔬</h1>
        <p>Predicting-Sepsis-FastAPI is a state-of-the-art solution designed to swiftly predict sepsis, a critical medical condition requiring prompt diagnosis and intervention. Leveraging FastAPI, this project offers a robust and efficient system for predicting the likelihood of sepsis based on various input parameters. The underlying machine learning model has been meticulously trained to provide accurate predictions, facilitating timely and informed decisions for healthcare professionals.</p>
        <h2>Project Structure</h2>
        <pre><code>
PREDICTING-SEPSIS-FASTAPI/
├── src/
│   ├── app.py
│   ├── models/
│   │   └── ML_Model.pkl
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── app.js
│   └── templates/
│       └── index.html
├── notebooks/
│   └── P5_sepsis_codeiddie.ipynb
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE
        </code></pre>
        <h3>src Folder</h3>
        <p>The src folder contains the source code of the FastAPI application. It typically includes the main application file, such as app.py, where the FastAPI instance is created, and routes and endpoints are defined. Additional modules or packages may be included for logical organization of the code.</p>
        <h3>Assets Folder</h3>
        <p>The Assets folder stores external files or resources used by the application. In the context of machine learning, this folder might contain pre-trained models, data files, or other necessary assets.</p>
        <h3>Dockerfile</h3>
        <p>The Dockerfile is used to build a Docker container for the FastAPI application. It specifies the base image, sets up the working directory, installs dependencies, copies the application code into the container, and defines the command to run the application. Dockerfiles ensure reproducible and portable environments.</p>
        <h2>Setup</h2>
        <p>Ensure Python 3 is installed before running the evaluation locally. Create and activate a virtual environment, then install the required packages listed in requirements.txt.</p>
        <h3>Windows:</h3>
        <pre><code>python -m venv venv &amp; venv\Scripts\activate &amp; python -m pip install -q --upgrade pip &amp; python -m pip install -qr requirements.txt</code></pre>
        <h3>Linux &amp; MacOs:</h3>
        <pre><code>python3 -m venv venv &amp; source venv/bin/activate &amp; python -m pip install -q --upgrade pip &amp; python -m pip install -qr requirements.txt</code></pre>
        <p>Explanation:</p>
        <ol>
            <li>Create a Python virtual environment to isolate project libraries.</li>
            <li>Activate the virtual environment.</li>
            <li>Upgrade Pip to the latest version.</li>
            <li>Install required libraries listed in requirements.txt.</li>
        </ol>
        <h2>Running FastAPI</h2>
        <p>To run the project, execute the following command at the repository root:</p>
        <pre><code>python src/app.py</code></pre>
        <h2>Article</h2>
        <p>For further insights, refer to the article linked <a href="https://www.linkedin.com/pulse/deploying-sepsis-prediction-api-using-fastapi-guide-maanenyi-nyande-vtbbf">here</a>.</p>
        <h2>Contribution</h2>
        <p>Contributions to the project are welcome! Feel free to provide feedback, report issues, or submit pull requests.</p>
        <p><strong>Contact Information:</strong></p>
        <ul>
            <li>Email: maanenyi.iddriss@azubiafrica.org</li>
            <li>GitHub: <a href="https://github.com/IddieGod/Predicting-Sepsis-FastAPI">IddieGod/Predicting-Sepsis-FastAPI</a></li>
        </ul>
    </div>
</body>
</html>
