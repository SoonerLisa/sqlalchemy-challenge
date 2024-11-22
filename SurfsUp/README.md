# sqlalchemy-challenge
Module 10 Challenge
README

Module 10: sqlalchemy-challenge

Request: Create a climate analysis and data exploration for vacation planning to the Honolulu, Hawaii area.

Data analyst: Lisa Miller

Repository URL: https://github.com/SoonerLisa/sqlalchemy-challenge.git

This assignment is 2-part.

Data Sources (provided):
    Part 1 Data:
        hawaii.sqlite (SQLite file)
    Part 2 Data:
        csv files: hawaii_measurements and hawaii_stations 


Part 1: Analyze and Explore the Climate Data
     Analysis File (for both sub-sections): climate_starter_JupyterNotebook.ipynb (jupyter notebok)

     1-Used SQLAlchemy to create_engine() to connect hawaii.sqlite database.
     2-Used SQLAlchemy automap_base() function to reflect tables into classes, and then saved references to the classes named 'station' and 'measurement'.
     3-Linked Python to the database by creating a SQLAlchemy session.
     4-Performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

     Subsections (2)
      1-Precipitation analysis
        •Found the most recent date in the dataset.
        •Queried the previous 12 months of precipitation data from the most recent date.
        *HINT (given, and executed) -Don't pass the date as a veriable to your query.
        •Selected only the 'date' and 'prcp' values.
        •Loaded the query results into a Pandas DataFrame. Explicitly set the column names.
        •Sorted the DataFrame values by 'date'.
        •Plotted the results with DataFrameplot method.
        •Used Pandas to print the summary statistics for the precipitation data.
      2-Station analysis
        •Designed a query to calculate the total number of stations in the dataset.
        •Designed a query to find the most-active stations (the stations that have the most rows are the most active).
        •Listed the stations and observation counts in decending order.
        *HINT (given, and executed) -Used the func.count function in the query.
        •Answered the question: Which station ID has the greatest number of observations?
        •Designed a query that calculates the lowest, highest, and average temperatures filtered on the most-active station ID found in previous query.
        *HINT (given, and executed) -Used functions such as func.min, func.max, and func.avg.
        •Filtered by the station that has the greatest number of observations.
        Queried the previous 12 months of TOBS data for that station.
        •Plotted the results as a histogram with bins=12.

Part 2: Design Climate App
    Analysis file: app.py (python)
    Data: .csv files hawaii.
    1-Design a Flask API based on the new queries. Use Flask to create routes.
    2-/api/v1.0/precepitation 
        •Converted query results from percipitation analysis for the last 12 months of data, to a dictionary using 'date' as the key and 'prcp' as the value.
        •Returned the JSON representation of the dictionary.
    3-/api/v1.0/stations
        •Returned a JSON list of stations from the dataset.
    4-api/v1.0/tobs
        •Queried the dates and temperature observations of the most-active station for the previous year of data.
        •Returned a JSON list of temperature observations for the previous year.
    5-api/v1.0/<start> and /api/v1.0/<end>
        •Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
        •For the specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
        •For the specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
        *HINT (given, and executed) -Joined the station and measurement tables for some of the queries.
        •Used the Flask jsonify function to convert the API data to a valid JSON response object.
Closed Session.

Disclosure: No outside sources were used in this analysis. All resources were within the TCC Data Analytics boot camp materials and BCS (Boot Camp Spot).