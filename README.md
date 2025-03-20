🎬 Movie Recommendation System

An AI-powered Movie Recommendation System built with Python, Streamlit, and Scikit-learn that suggests movies based on content similarity and fetches posters via the TMDb API. 🚀

✨ Features

✅ AI-powered recommendations using cosine similarity
✅ Dynamic UI with Streamlit for an intuitive experience
✅ Real-time movie posters from TMDb API
✅ Fast performance with precomputed similarity matrices
✅ Error handling for smooth execution

⸻

🛠️ Tech Stack
	•	Frontend: Streamlit
	•	Backend: Python
	•	Machine Learning: Scikit-learn, Pandas, NumPy
	•	API Integration: TMDb API
	•	Storage & Serialization: Pickle
	•	Version Control: Git & GitHub

⸻

🎥 Demo


<img width="1220" alt="Screenshot 2025-03-20 at 3 15 08 PM" src="https://github.com/user-attachments/assets/d279dbb9-e403-4562-90f3-205b4d250712" />


🚀 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the App

streamlit run app.py

🎉 You’re ready to explore movie recommendations!

⸻
⚡ How It Works

1️⃣ Select a movie from the dropdown list
2️⃣ Click “Show Recommendation”
3️⃣ Get 5 similar movies with posters
4️⃣ Click on a suggested movie for more details

⸻

📸 Screenshots

Home Page	Recommendations
	
<img width="1216" alt="Screenshot 2025-03-20 at 3 16 00 PM" src="https://github.com/user-attachments/assets/2c16192f-fd19-4dc6-ac9b-af00dfe80c6c" />









🏗️ Project Structure

📂 movie-recommendation-system
├── 📜 app.py  # Streamlit UI & Recommendation logic
├── 📜 movie_list.pkl  # Preprocessed movie dataset
├── 📜 similarity.pkl  # Cosine similarity matrix
├── 📜 requirements.txt  # Python dependencies
├── 📜 README.md  # Documentation
└── 📂 assets/  # Images & media



⸻

🎯 Future Enhancements

🔹 Add collaborative filtering for personalized recommendations
🔹 Implement user-based recommendations using Neural Networks
🔹 Deploy on AWS/GCP for cloud-based access

⸻

🤝 Contributing

🚀 Want to improve this project? Fork the repo, make changes, and create a pull request!

git checkout -b feature-branch
git commit -m "Add new feature"
git push origin feature-branch

