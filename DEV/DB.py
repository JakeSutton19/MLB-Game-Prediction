## Create Database for visulaization of data and building of models


import sqlite3 as sq
import pandas as pd



# Add data to new dB
'''
filename="MLB"

con = sq.connect(filename+".db")

df = pd.read_csv('Data/dataset1.csv')

columns = df.columns

df.to_sql('Data',con, schema=columns, index=False, if_exists="replace")

con.commit()
con.close()

'''



#Grab, put in df and then output results


try:

	with sq.connect("MLB.db") as con:
	    cur = con.cursor()


	cur.execute('select * from Data')

	# Fetch all rows
	#rows = cur.fetchall()

	# Print results
	#for row in rows:
	#	print(row)


	df = pd.DataFrame(cur.fetchall())
	print(df.tail(5))

except:
	print("Error: Didn't work.")

finally:
	print("Done")
	con.close()

