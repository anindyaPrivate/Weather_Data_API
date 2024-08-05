from flask import Flask, render_template
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

station = pd.read_csv("data_small/stations.txt", skiprows=17)
station = station[['STAID', 'STANAME                                 ']]


# Define the route for the home page
@app.route("/")
def home():
    # Render the home.html template when the home route is accessed
    return render_template("home.html", data=station.to_html())


# Define a route that includes dynamic segments for station and date
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Set a static temperature value
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    # Render the data.html template with the temperature data
    return render_template("data.html", description=f"Data for station {station} on {date}", columns=["Station", "Date", "Temperature"], data=[[station, date, f"{temperature}°C"]])


@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    # Convert the result into a list of lists for rendering in the table
    data = [[row[col] for col in df.columns] for row in result]
    return render_template("data.html", description=f"All data for station {station}", columns=df.columns, data=data)


@app.route("/api/v1/yearly/<station>/<year>")
def all_year_Data(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")
    # Convert the result into a list of lists for rendering in the table
    data = [[row[col] for col in df.columns] for row in result]
    return render_template("data.html", description=f"Yearly data for station {station} in {year}", columns=df.columns, data=data)


# Check if the script is run directly (and not imported as a module)
if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)