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

The home page displays weather data in a table format. Navigate to the following URL:http://127.0.0.1:5000

### API Routes

#### 1. Get Data Based on Station and Date

URL format:http://127.0.0.1:5000/api/v1/<station>/<date>

Example:http://127.0.0.1:5000/api/v1/10/1988-10-25


#### 2. Get All Data for a Station

URL format:http://127.0.0.1:5000/api/v1/<station>

Example:http://127.0.0.1:5000/api/v1/10

#### 3. Get Yearly Data for a Station

URL format:http://127.0.0.1:5000/api/v1/yearly/<station>/<year>

Example:http://127.0.0.1:5000/api/v1/yearly/10/1988


To get temperature data for a different year, replace `1988` with the desired year.

## 📝 Example

Example of getting data for station 10 on October 25, 1988:http://127.0.0.1:5000/api/v1/10/1988-10-25


This will display the temperature data for the specified station and date.

## 📄 Home Page Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Weather Data API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            color: #333;
            margin: 0;
            padding: 0;
        }
        h1 {
            background-color: #4682b4;
            color: white;
            padding: 20px;
            text-align: center;
            margin: 0;
        }
        p {
            padding: 10px 20px;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            background-color: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        .url {
            font-weight: bold;
            color: #4682b4;
        }
        .note {
            font-style: italic;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Weather Data API</h1>
    <div class="container">
        <p class="note">Welcome to the Weather Data API home page. Use the following URL formats to access weather data.</p>
        <p class="url">URL format: <br>http://127.0.0.1:5000/api/v1/station/date</p>
        <p>Getting Data based on Station and date: <br><span class="url">http://127.0.0.1:5000/api/v1/10/1988-10-25</span></p>
        <p>Getting All the data based on Station: <br><span class="url">http://127.0.0.1:5000/api/v1/10</span></p>
        <p>Year wise data: <br><span class="url">http://127.0.0.1:5000/api/v1/yearly/10/1988</span></p>
        <p>{{data|safe}}</p>
    </div>
    <div class="container">
        <h2>Guide: How to Get Temperature Data for a Different Year</h2>
        <p>To get temperature data for a different year, change the year in the URL format for year-wise data.</p>
        <p>For example, to get data for the year 1990, use:</p>
        <p class="url">http://127.0.0.1:5000/api/v1/yearly/10/1990</p>
        <p>Simply replace <span class="url">1988</span> with any other year of your choice.</p>
    </div>
</body>
</html>
```

Enjoy using the Weather Data API! 🌦️📊


This `README.md` file includes properly formatted sections with code blocks and URLs that can be easily copied.





