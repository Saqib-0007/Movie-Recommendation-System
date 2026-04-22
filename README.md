# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** that suggests movies similar to a selected movie using **similarity scores** and machine learning techniques. The system analyzes movie metadata and recommends movies based on content features such as genre, keywords, cast, and overview.

## 📌 Features

* 🎯 Movie recommendations based on selected movie
* 🔍 Fast and accurate similarity-based suggestions
* 💻 Interactive web interface using Streamlit
* 📦 Preprocessed model files using Pickle
* ⚡ Lightweight and efficient recommendation engine
* 🌐 Deployed online using Heroku

## 🚀 Technologies Used

* Python
* Streamlit
* NumPy
* Pandas
* Heroku
* Pickle (for model serialization)

## 📂 Project Structure

```bash
Movie-Recommendation-System/
│── app.py
│── movies.pkl
│── similarity.pkl
│── requirements.txt
│── README.md
```

## ⚙️ How It Works

1. Movie data is cleaned and preprocessed using Pandas and NumPy.
2. Important movie features are transformed into vectors.
3. Similarity scores are calculated between movies.
4. Pickle files store processed data and similarity matrix.
5. When a user selects a movie, the system recommends the most similar movies instantly.

## 📥 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

## 💻 Usage

* Open the Streamlit app in your browser
* Select a movie from the dropdown
* Get top recommended similar movies instantly

## 🌐 Deployment

This project is deployed using Heroku.

## 📈 Future Improvements

* Improve recommendation accuracy
* Add user ratings system
* Deploy on modern cloud platforms

## 👨‍💻 Author

Your Name
GitHub: https://github.com/Saqib-0007
