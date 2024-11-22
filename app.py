# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import numpy as np

#Flask setup
app=Flask (__name__)
# Create an engine to connect to the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session (link) from Python to the DB
Session = sessionmaker(bind=engine)

#from HINT, create route in Flask to perform a join of station and measurement tables.
# Create a list to hold the JSON data
@app.route('/api/joined_data')
def get_joined_data():
    session = Session()
    # Perform a join query
    results = session.query(Measurement, Station).filter(Measurement.station == Station.station).all()
    joined_data = []
    for measurement, station in results:
        joined_data.append({
            'date': measurement.date,
            'precipitation': measurement.prcp,
            'station_id': station.station,
            'station_name': station.name
        })
        # Return the JSON response
    session.close()
    return jsonify(joined_data)

@app.route('/api/v1.0/stations')
def stations():
    # Create our session (link) from Python to the DB
    session = Session()
    results = session.query(stations.name).all()
    stations_list = [result[0] for result in results]
    session.close()
    return jsonify(stations_list)

@app.route('/api/v.1.0/tobs')
def get_tobs():
    session = Session()
    most_recent_date = datetime(2017, 8, 23)
    date = most_recent_date - datetime.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= date).\
        order_by(Measurement.date.desc()).all()
    tobs_list = []
    for date, tobs in results:
         tobs_dict = {}
         tobs_dict['date'] = date
         tobs_dict['temperature_observation'] = tobs
         tobs_list.append(tobs_dict)
    session.close()
    return jsonify(tobs_list)

@app.route('/api/v1.0/precipitation')
def get_precipitation():
    session = Session()
    most_recent_date = datetime(2017, 8, 23)
    date = most_recent_date - datetime.timedelta(days=365)
    
    # Query to get precipitation data for the last 12 months
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= date).\
        order_by(Measurement.date).all().desc

    # Convert results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in results}
    session.close()   
    return jsonify(precipitation_dict)

@app.route('/api/v1.0/<start>')
def get_temp_start(start):
    session = Session()
    # Query to calculate TMIN, TAVG, TMAX for all dates >= start
    results = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).all()

    # Create a dictionary to hold the results
    temp_dict = {
        'TMIN': results[0][0],
        'TAVG': results[0][1],
        'TMAX': results[0][2]
    }
    session.close()
    return jsonify(temp_dict) #to return the min,avg,max temps from all dates >=start date

@app.route('/api/v1.0/<start>/<end>')
def get_temp_start_end(start, end):
    session = Session()
    # Query to calculate TMIN, TAVG, TMAX for the date range from start to end
    results = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Create a dictionary to hold the results
    temp_dict = {
        'TMIN': results[0][0],
        'TAVG': results[0][1],
        'TMAX': results[0][2]
    }
    session.close()
    return jsonify(temp_dict) #return dict = to previous query but for date range start/end.

if __name__ == "__main__":
        app.run(debug=True)

Session.close()