# 🏃‍♂️ **RetailRunner** 🚀

### **Description:**
RetailRunner is a mobile and backend solution designed to streamline **order fulfillment** for companies. Workers receive tasks, store products, and upload **photo verifications** using **Firebase**. This project leverages **FastAPI** for the backend, **Flutter** for the mobile app, **PostgreSQL** for the database, and **Firebase** for photo management and push notifications. 📦📸

---

### 🔧 **Technologies Used:**
- **Backend:** FastAPI ⚙️, PostgreSQL 🗃️
- **Frontend:** Flutter 📱
- **Database:** PostgreSQL 🗂️
- **Authentication:** JWT (JSON Web Tokens) 🔐
- **Cloud Storage:** Firebase for photo uploads ☁️
- **Push Notifications:** Firebase Cloud Messaging 📲
- **Containerization:** Docker for environment setup 🐳

---

### 🌟 **Features:**
- **User Authentication:** JWT-based login/signup 🔑
- **Order Management:** Assign, fetch, and track orders for workers 📋
- **Photo Uploads:** Upload photos to Firebase for verification 📸
- **Admin Review:** Admins can approve/reject orders based on photo verifications ✅❌
- **Push Notifications:** Real-time updates using Firebase Cloud Messaging 🔔

---

### 🚀 **Installation & Setup:**

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/retailrunner.git

Navigate to the project folder:

cd retailrunner

Set up Docker environment:

    Install Docker if you haven't already. 🐳

    Build and run the Docker containers:

    docker-compose up --build

Backend setup:

    Install Python dependencies:

pip install -r backend/requirements.txt

Run the backend FastAPI server:

    uvicorn backend.app.main:app --reload

Frontend setup:

    Install Flutter dependencies:

flutter pub get

Run the Flutter app on your emulator or device:

        flutter run

📱 Usage:

    Access the FastAPI backend at http://localhost:8005.

    Use the mobile app to sign in as a worker or admin and manage orders.

    Admin users can approve or reject orders based on the submitted photos.

🛠️ Contributing:

We welcome contributions! Please follow the steps below to contribute:

    Fork the repository. 🍴

    Create a new branch:

git checkout -b feature-name

Commit your changes:

git commit -m "Add feature"

Push your branch:

    git push origin feature-name

    Open a pull request. 🔄

📝 License:

This project is proprietary. You are free to view, learn from, and fork the code, but commercial usage and redistribution are not allowed without prior permission. Please see LICENSE for more details. 🔒
💬 Contact & Support:

If you have any questions or need support, feel free to open an issue or contact me directly. 😊
