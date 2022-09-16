import ats_lib as ats

time_start = "2020-08-31 20:00:00"
time_end = "2020-08-31 21:00:00"
frequency=20

# Create test data 
data = ats.test.create(time_start,time_end,frequency, trend=False) 
# This will create DataFrame with time as index and random 
# generated data 'u' (with cosine as longwave variability. 
# Optionally a linear trend can be set: trend=True)
print(data)

# Plot the test data:
plt = ats.plot.simple(data, label="test data")

# Add some gaps to the data. Default set creates one gap in the middle. 
data_bad = ats.test.gap(data, gap_size=10000)
plt = ats.plot.simple(data_bad, label="test data with gaps")

# Let's add non-default gap (say 15 000 points from 2020-08-31 20:05:00):
data_bad = ats.test.gap(data, gap_start="2020-08-31 20:05:00", gap_size=15000)
data_bad = ats.test.gap(data_bad, gap_start="2020-08-31 20:45:00", gap_size=5000)
plt = ats.plot.simple(data_bad, label="test data with gaps (non-default)")

# Add legend and show plot
plt.legend()
plt.show()
