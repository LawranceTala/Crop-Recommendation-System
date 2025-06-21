# Crop-Recommendation-System
 This project recommends the most suitable crop to grow based on environmental and soil conditions like nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall. It uses a machine learning model trained on real agricultural data and provides predictions through a FastAPI backend with a ReactJS frontend interface.

# Setup for Anaconda Python Package Manager

✅ Step-by-step:
1. Install Anaconda
If you don’t have Anaconda installed, download and install it from:
🔗 https://www.anaconda.com/products/distribution
2. Install Python Packages
 pip install -r backend/requirements.txt
📝 Note: Make sure you have a requirements.txt file inside your backend folder

# Training the Model

✅ Step-by-step:
1:Downloading the Dataset

2:Download the dataset from Kaggle:
[🔗 Crop Recommendation Dataset | Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

3:Place the downloaded Crop_recommendation.csv file in the root directory of this project.

4: Open the  jupiter Notebook

5:Launch Jupyter Notebook (you can use Anaconda Navigator or run jupyter notebook in your terminal).

6:Open the file:

7:Update Dataset Path

8:In the second code cell, make sure the dataset path is correct
9:data = pd.read_csv("Crop_recommendation.csv")

10:Run All Cells

11:Execute all the cells one by one to:

12:Preprocess the data

13:Train multiple models (RandomForest, XGBoost, etc.)

14:Evaluate performance

15:Save the best-performing model using joblib or pickle

**Saving Models**

1:Trained models will be saved as .pkl files in the root or model/ directory.

2:Example: RandomForest.pkl, XGBoost.pkl, etc.


##  Running the API
 
✅ Step-by-step:

1:Navigate to the backend folder
cd backend
2;Run the FastAPI server using Uvicorn
    uvicorn server:app --reload 
3:Access the API

4:Once the server is running, you can visit the following in your browser:
    Swagger UI: http://localhost:8080/docs

#API Endpoint

1:The API expects a JSON input like this:

{
  "data": [90, 42, 43, 20.879, 82.002, 6.5, 202.93]
}
2:It returns a response with the predicted crop name.


##  Running the Frontend (ReactJS)

✅ Step-by-step:
1:Install Node.js and NPM

2:Download and install Node.js (which includes npm):
🔗 https://nodejs.org

3:Install Frontend Dependencies

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

4;Start the Frontend
 npm start

 Access the App

 Open your browser and go to:
 http://localhost:3000



 




