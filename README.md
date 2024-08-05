# 🌦️ Weather Data API

A Flask-based web application to access and display weather data. This project provides a user-friendly interface for fetching weather data based on station and date information.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Routes](#routes)
- [Example](#example)

## 🌟 Introduction

This web application uses Flask to serve weather data from a collection of CSV files. Users can access data for specific stations and dates, as well as retrieve all data for a given station or yearly data.

## ✨ Features

- Home page displaying weather data
- Retrieve weather data based on station and date
- Retrieve all weather data for a specific station
- Retrieve yearly weather data for a specific station
- Easy-to-use URL format for accessing data

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.12
- Flask
- pandas

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/weather-data-api.git
    cd weather-data-api
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the `data_small` directory contains the necessary CSV files:
    ```
    data_small/
    ├── stations.txt
    ├── TG_STAID000001.txt
    ├── TG_STAID000002.txt
    └── ...
    ```

### Running the Application

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

## 🚀 Usage

### Home Page

The home page displays weather data in a table format. Navigate to the following URL:
