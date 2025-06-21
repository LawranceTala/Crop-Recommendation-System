# Crop-Recommendation-System
 This project recommends the most suitable crop to grow based on environmental and soil conditions like nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall. It uses a machine learning model trained on real agricultural data and provides predictions through a FastAPI backend with a ReactJS frontend interface.

⚙️ Setup for Anaconda Python Package Manager
✅ Step-by-step:
1. Install Anaconda
If you don’t have Anaconda installed, download and install it from:
🔗 https://www.anaconda.com/products/distribution
2. Install Python Packages
 pip install -r backend/requirements.txt
📝 Note: Make sure you have a requirements.txt file inside your backend folder

📚 Training the Model
✅ Step-by-step:
Downloading the Dataset

Download the dataset from Kaggle:
[🔗 Crop Recommendation Dataset | Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

Place the downloaded Crop_recommendation.csv file in the root directory of this project.

Open the Notebook

Launch Jupyter Notebook (you can use Anaconda Navigator or run jupyter notebook in your terminal).

Open the file:
Update Dataset Path

In the second code cell, make sure the dataset path is correct
data = pd.read_csv("Crop_recommendation.csv")
Run All Cells

Execute all the cells one by one to:

Preprocess the data

Train multiple models (RandomForest, XGBoost, etc.)

Evaluate performance

Save the best-performing model using joblib or pickle

Saveing Models

Trained models will be saved as .pkl files in the root or model/ directory.

Example: RandomForest.pkl, XGBoost.pkl, etc.

 Running the API
✅ Step-by-step:

Navigate to the backend folder
cd backend
Run the FastAPI server using Uvicorn
uvicorn server:app --reload 
Access the API

Once the server is running, you can visit the following in your browser:
Swagger UI: http://localhost:8080/docs

API Endpoint

The API expects a JSON input like this:

{
  "data": [90, 42, 43, 20.879, 82.002, 6.5, 202.93]
}
It returns a response with the predicted crop name.

Running the Frontend (ReactJS)
✅ Step-by-step:
Install Node.js and NPM

Download and install Node.js (which includes npm):
🔗 https://nodejs.org

Install Frontend Dependencies

Open a terminal inside the frontend folder:
cd frontend
npm install
Connect to the Backend

Open src/App.js

Replace the API URL with your local FastAPI server:

const response = await axios.post("http://localhost:8080/predict", data);

Customize the UI

You can modify the styles in:
src/App.css

Start the Frontend
npm starAccess the App

Open your browser and go to:
http://localhost:3000

 Project Structure
Crop-Recommendation-System/
├── backend/
│   ├── server.py
│   ├── requirements.txt
│   ├── ... (other backend files)
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── ...
│   ├── package.json
│   └── ... (other frontend files)
├── notebook.ipynb
├── Crop_recommendation.csv
├── RandomForest.pkl
├── XGBoost.pkl
├── README.md

 




