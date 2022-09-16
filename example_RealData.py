import ats_lib as ats

frequency=20
filename = "./data/L0/MSU/A1/2022/09/MSU_A1_2022-09-01.nc"

# Read the data
data_raw = ats.reader.netcdf(filename)

# Clean the data (in case of duplicates and time reorders)
data = ats.data.clean(data_raw)

# Get fluctuations with detrend as mean.
data_primes = ats.math.primes(data, window=frequency*20*60, detrend="mean")
print(data_primes)

# Compute TKE
data_tke = ats.math.tke(data_primes)

print(data_tke)

plt = ats.plot.simple(data_tke['tke'], label="KTE")
plt.show()


