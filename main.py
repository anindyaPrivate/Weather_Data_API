from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)


# Define the route for the home page
@app.route("/")
def home():
    # Render the home.html template when the home route is accessed
    return render_template("home.html")


# Define a route that includes dynamic segments for station and date
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Set a static temperature value (for example purposes)
    temperature = 23
    # Return a JSON response containing the station, date, and temperature
    return {'station': station,
            'date': date,
            'temperature': temperature}

    # If you want to render an about.html template instead of returning JSON, uncomment the following line:
    # return render_template("about.html")


# Check if the script is run directly (and not imported as a module)
if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
