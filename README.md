AI Personal Safety & Digital Protection App
Hackathon Project

Algorithmix

---

## Project Overview

This project is an AI-powered personal safety and digital protection application designed to help users navigate cities more safely and protect their digital identity. The app analyzes environmental signals such as street lighting, nearby public places, and emergency infrastructure to estimate the safety of walking routes. It also includes emergency detection features and digital privacy tools.

The goal is to combine geospatial data, machine learning concepts, and real-time APIs to create a practical safety assistant.

---

## Key Features

1. Safe Route Recommendation
   The system analyzes possible walking routes and calculates a safety score using data from OpenStreetMap. Factors considered include:

* Street lighting
* Nearby public places (restaurants, shops, transport stops)
* Police stations and hospitals
* Known danger zones

The safest available route is recommended to the user.

2. Voice Emergency Detection
   The application listens for emergency keywords such as:
   "help", "emergency", or "save me".

If detected, the system triggers an SOS alert.

3. SOS Location Sharing
   Users can send their live location during emergencies.
   The location can be shared with trusted contacts through a Google Maps link.

4. Digital Safety Scanner
   The system can check whether a user's email address has appeared in known data breaches and suggests basic digital safety steps.

5. Suspicious Image Detection (Prototype)
   Users can upload an image to check for possible manipulation or suspicious metadata.

---

## Technology Stack

Frontend

* HTML
* JavaScript
* Leaflet.js (map visualization)

Backend

* Python
* Flask

Libraries

* requests
* flask-cors
* geopy
* osmnx
* networkx
* numpy

Data Sources

* OpenStreetMap
* Overpass API
* OSRM routing API

---

## Project Structure

safety-app-india/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── data_sources/
│   └── utils/
│
├── frontend/
│   ├── components/
│   └── assets/
│
├── data/
│   ├── crime/
│   ├── lighting/
│   └── osm_cache/
│
├── database/
└── models/

---

## Installation Guide

1. Clone the repository

git clone 

2. Navigate to project folder

cd safety-app-india

3. Create virtual environment

python -m venv venv

4. Activate environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

5. Install dependencies

pip install -r requirements.txt

---

## Running the Application

1. Start backend server

python backend/app.py

2. Open frontend in browser

Open frontend/index.html

---

## Future Improvements

* Integration with real-time crime datasets
* AI-based risk prediction models
* Mobile application version
* Real-time emergency alert system
* Deepfake detection for uploaded media

---

## Team Vision

Our goal is to create a smart assistant that helps people make safer travel decisions and protects their digital identity using accessible AI technologies.

---

## Hackathon Category

AI | Cybersecurity | SafetyTech
