import sqlite3 as lite
import pandas as pd

cities = (('New York City', 'NY'),
          ('Boston', 'MA'),
          ('Chicago', 'IL'),
          ('Miami', 'FL'),
          ('Dallas', 'TX'),
          ('Seattle', 'WA'),
          ('Portland', 'OR'),
          ('San Francisco', 'CA'),
          ('Los Angeles', 'CA'),
          ('Las Vegas', 'NV'),
          ('Atlanta', 'GA'))

weather = (('New York City',   2013,    'July',        'January',     62),
           ('Boston',          2013,    'July',        'January',     59),
           ('Chicago',         2013,    'July',        'January',     59),
           ('Miami',           2013,    'August',      'January',     84),
           ('Dallas',          2013,    'July',        'January',     77),
           ('Seattle',         2013,    'July',        'January',     61),
           ('Portland',        2013,    'July',        'December',    63),
           ('San Francisco',   2013,    'September',   'December',    64),
           ('Los Angeles',     2013,    'September',   'December',    75),
           ('Las Vegas',       2013,    'July',        'December',    85),
           ('Atlanta',         2013,    'July',        'January',     82))

con = lite.connect('getting_started.db')


with con:
    cur = con.cursor()

    # drop cities and weather tables
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")

    # create cities and weather tables
    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")

    # populate tables with tuples
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

    # join tables using city and select only relevant columns and rows
    cur.execute("select c.name, c.state, w.year, w.warm_month, w.cold_month, w.average_high from cities c join weather w on c.name = w.city where w.warm_month = 'July'")

    # load joined table into dataframe
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

    # creates a list of the city and states then convert to a string
    julycities = []
    for index, row in df.iterrows():
        julycities.append(row['name'] + ", " + row['state'])
    strjulycities = ', '.join(julycities)

    print "The cities that are warmest in July are: " + strjulycities


