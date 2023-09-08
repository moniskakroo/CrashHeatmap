import folium
from folium.plugins import HeatMap
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'C:\Users\\mwazir\OneDrive - hwlochner.com\Desktop\Crash data\crash.csv')

df.shape
#df['S4_CRASH_TYPE'].plot.hist()
sns.countplot(x='S4_CRASH_TYPE', data=df)
# Create a base map centered at a specific location (e.g., for demonstration purposes)
# You can adjust the coordinates and zoom level as needed.
m = folium.Map(location=[0, 0], zoom_start=10)
locations = df1[['LATITUDE', 'LONGITUDE']].values.tolist()
# Add the heatmap layer to the map
HeatMap(locations).add_to(m)

# Display the map
m.save('crash_heatmap.html')

'''import folium
from folium.plugins import HeatMap
import pandas as pd
import matplotlib.pyplot as plt

# Read your crash data CSV file
df1 = pd.read_csv('your_crash_data.csv')

# Extract the time information and normalize it to a scale between 0 and 1
df1['CRASH_DATE_AND_TIME'] = pd.to_datetime(df1['CRASH_DATE_AND_TIME'])
df1['Time_Normalized'] = (df1['CRASH_DATE_AND_TIME'].dt.hour * 60 + df1['CRASH_DATE_AND_TIME'].dt.minute) / (24 * 60)

# Define a color gradient for different times of the day
color_gradient = {
    0.0: 'blue',    # Midnight
    0.25: 'purple', # Early morning
    0.5: 'green',   # Morning
    0.75: 'orange', # Afternoon
    1.0: 'red'      # Evening
}

# Create a base map
m = folium.Map(location=[0, 0], zoom_start=10)

# Iterate through time intervals and create heatmap layers
for interval_start, interval_color in color_gradient.items():
    interval_end = (interval_start + 0.25) % 1.0  # Create 6-hour intervals (adjust as needed)
    
    # Filter data for the current time interval
    interval_data = df1[(df1['Time_Normalized'] >= interval_start) & (df1['Time_Normalized'] < interval_end)]
    
    # Convert coordinates to a list
    locations = interval_data[['LATITUDE', 'LONGITUDE']].values.tolist()
    
    # Add a heatmap layer with the appropriate color and opacity
    HeatMap(locations, gradient={0: 'white', 0.5: interval_color}, min_opacity=0, max_opacity=0.6).add_to(m)

# Save and display the map
m.save('dynamic_heatmap.html')'''

'''import folium
from folium.plugins import HeatMapWithTime
import pandas as pd
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def create_animated_heatmap(df):
    # Create a base map
    m = folium.Map(location=[df['LATITUDE'].mean(), df['LONGITUDE'].mean()], zoom_start=10)

df=pd.read_csv(r'C:\Users\\mwazir\OneDrive - hwlochner.com\Desktop\Crash data\crash.csv')

df['CRASH_DATE_AND_TIME'] = pd.to_datetime(df['CRASH_DATE_AND_TIME'])
df['Day'] = df['CRASH_DATE_AND_TIME'].dt.date

# Create a list of unique days for the animation frames
unique_days = df['Day'].unique()


# Initialize HeatMapWithTime
heat_data = []
for day in unique_days:
    day_data = df[df['Day'] == day]
    locations = day_data[['LATITUDE', 'LONGITUDE']].values.tolist()
    heat_data.append(locations)

hm = HeatMapWithTime(heat_data, index=unique_days, auto_play=True, radius=15)

# Add HeatMapWithTime to the map
hm.add_to(m)

# Save the animated heatmap as an HTML file
m.save(r'C:\Users\mwazir\OneDrive - hwlochner.com\Desktop\Crash data/animated_heatmap.html')

#Use ChromeDriverManager to automatically download and manage ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
try:
    # Read your crash data CSV file
    df = pd.read_csv('crash_data.csv')

    # Create the animated heatmap
    create_animated_heatmap(df)
    
    # Navigate to the saved HTML file using Selenium
    driver.get(r'C:\Users\mwazir\OneDrive - hwlochner.com\Desktop\Crash data/animated_heatmap.html')  # Replace with the actual file path

    # Add additional Selenium actions as needed
    
finally:
    # Close the ChromeDriver instance
    driver.quit()'''




