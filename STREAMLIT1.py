import streamlit as st
import mysql.connector
from mysql.connector import Error
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="world"
        )
        if connection.is_connected():
            st.markdown(": 🦜")
            return connection
    except Error as e:
        st.error(f"Error in connection: {e}")

def execute_query(connection, query):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        return df
    except Error as e:
        st.error(f"Error executing query: {e}")
        return None

option = st.sidebar.selectbox("Select Type of Analysis", ["Home",
    "Temporal Analysis", "Spatial Analysis", "Species Analysis",
    "Environmental Conditions", "Distance and Behavior",
    "Observer Trends", "Conservation Insights"
])

# Display the selected page
connection = create_connection()

if connection:
    if option== "Home":
        st.header("Welcome Birds Analysis")
        option=st.sidebar.selectbox("Select",[
    "Antietam National Battlefield (ANTI)",
    "Catoctin Mountain Park (CATO)",
    "Chesapeake and Ohio Canal National Historical Park (CHOH)",
    "George Washington Memorial Parkway (GWMP)",
    "Harpers Ferry National Historical Park (HAFE)",
    "Manassas National Battlefield Park (MANA)",
    "Monocacy National Battlefield (MONO)",
    "National Capital Parks - East (NACE)",
    "Prince William Forest Park (PRWI)",
    "Rock Creek Park (ROCR)",
    "Wolf Trap National Park for the Performing Arts (WOTR)"])

        if option=="Antietam National Battlefield (ANTI)":
            st.header("Antietam National Battlefield")
            st.image(r"C:\Users\DELL\Downloads\1.jpg")
            st.write("Antietam National Battlefield (ANTI), located in Maryland, is a historically significant site commemorating the Civil War's Battle of Antietam. Beyond its historical importance, the battlefield is also a haven for birdwatchers. The park's diverse habitats—open fields, wooded areas, and wetlands—support a variety of bird species.")
            st.subheader("Common Birds:")
            st.write("- Eastern Bluebird")
            st.write("- Red-tailed Hawk")
            st.write("- Northern Cardinal")
            st.title("Eastern Bluebird")
            st.image(r"C:\Users\DELL\Downloads\0.1.webp")
            st.write("The Eastern Bluebird is a small thrush known for its vibrant blue plumage and rusty-red chest. It typically perches on low branches or fence posts, scanning for insects and small fruits, and is often observed nesting in cavities or birdhouses near open fields.")
            st.title("Red-tailed Hawk")
            st.image(r"C:\Users\DELL\Downloads\0.2.jpg")
            st.write("""

                     Hunting Style: Red-tailed Hawks are opportunistic hunters, often seen soaring high in the sky or perched on poles and trees, scanning for prey such as small mammals, reptiles, and birds.
                    Territorial Displays: They are highly territorial and perform aerial displays, including dives and circles, to mark and defend their territory.""")
            st.title("Northern Cardinal")
            st.image(r"C:\Users\DELL\Downloads\0.3.webp")
            st.write("""The Northern Cardinal exhibits the following behaviors:

Territorial Defense: Males are highly territorial, especially during the breeding season, and often sing loudly from prominent perches to ward off rivals.

Foraging and Feeding: Cardinals are ground foragers, often seen picking seeds, fruits, and insects, but they will also feed from bird feeders, particularly sunflower seeds.""")
        
        elif option=="Catoctin Mountain Park (CATO)":
            st.header("Catoctin Mountain Park (CATO)")
            st.image(r"C:\Users\DELL\Downloads\2.jpg")
            st.write("""Catoctin Mountain Park (CATO) is located in northern Maryland, offering scenic hiking trails, diverse wildlife, and a rich history. The park is also known for being home to Camp David, the presidential retreat, nestled within its beautiful, mountainous landscape.""")
            st.title("Cerulean Warbler")
            st.image(r"C:\Users\DELL\Downloads\0.01.jpg")
            st.write("A small, migratory songbird known for its vibrant blue plumage and distinctive song. It breeds in the park's deciduous forests.")
            st.title("Hooded Warbler")
            st.image(r"C:\Users\DELL\Downloads\002.webp")
            st.write("Recognizable by its bright yellow body and black hood, this warbler is often found in the park's understory vegetation.")
            st.title("American Redstart")
            st.image(r"C:\Users\DELL\Downloads\003.jpg")
            st.write("A striking black and orange warbler that flits through the park's forests, often fanning its tail to catch insects.")


        elif option == "Chesapeake and Ohio Canal National Historical Park (CHOH)":
            st.header("Chesapeake and Ohio Canal National Historical Park (CHOH)")
            st.image(r"C:\Users\DELL\Downloads\3.jpg")
            st.write("""The Chesapeake and Ohio Canal National Historical Park, stretching along the Potomac River, offers a blend of history and natural beauty. It’s a popular destination for hiking, biking, and birdwatching due to its diverse ecosystems.""")
            st.title("Great Blue Heron")
            st.image(r"C:\Users\DELL\Downloads\0001.jpg")
            st.write("A large wading bird with a striking blue-gray body and long neck, often seen fishing in the canal's waters.")
            st.title("Belted Kingfisher")
            st.image(r"C:\Users\DELL\Downloads\0002.jpg")
            st.write("Known for its loud, rattling call, this bird dives into the canal to catch small fish and aquatic prey.")
            st.title("Wood Duck")
            st.image(r"C:\Users\DELL\Downloads\0003.webp")
            st.write("A colorful duck species often spotted in the park's wetlands and wooded waterways.")

        elif option == "George Washington Memorial Parkway (GWMP)":
            st.header("George Washington Memorial Parkway (GWMP)")
            st.image(r"C:\Users\DELL\Downloads\4.jpg")
            st.write("""The George Washington Memorial Parkway, designed as a scenic roadway, is a corridor for recreation and wildlife, connecting important historical and natural sites along the Potomac River.""")
            st.title("Osprey")
            st.image(r"C:\Users\DELL\Downloads\00004.jpg")
            st.write("A fish-eating raptor often seen soaring or diving into the Potomac River to catch prey.")
    
            st.title("American Goldfinch")
            st.image(r"C:\Users\DELL\Downloads\00002.jpg")
            st.write("A bright yellow songbird commonly found in open fields and meadows along the parkway.")
    
            st.title("Eastern Phoebe")
            st.image(r"C:\Users\DELL\Downloads\0003.jpg")
            st.write("A small flycatcher known for its tail-wagging habit and sharp 'phoebe' call.")


        elif option == "Harpers Ferry National Historical Park (HAFE)":
            st.header("Harpers Ferry National Historical Park (HAFE)")
            st.image(r"C:\Users\DELL\Downloads\5.webp")
            st.write("""Located at the confluence of the Potomac and Shenandoah Rivers, Harpers Ferry is a historical site with stunning views and habitats for various bird species.""")
    
             
        
        elif option == "Manassas National Battlefield Park (MANA)":
           st.header("Manassas National Battlefield Park (MANA)")
           st.image(r"C:\Users\DELL\Downloads\6.webp")
           st.write("""Manassas National Battlefield Park in Virginia preserves the site of two major Civil War battles and features open fields, meadows, and woodlands, providing a sanctuary for various bird species.""")
    
            
 
        elif option == "Monocacy National Battlefield (MONO)":
            st.header("Monocacy National Battlefield (MONO)")
            st.image(r"C:\Users\DELL\Downloads\7.webp")
            st.write("""Monocacy National Battlefield in Maryland commemorates a pivotal Civil War battle and is also a peaceful refuge for birdlife amidst its fields and forests.""")
     
 
        elif option == "National Capital Parks - East (NACE)":
            st.header("National Capital Parks - East (NACE)")
            st.image(r"C:\Users\DELL\Downloads\8.jpg")
            st.write("""National Capital Parks - East is a collection of parks offering urban oases for wildlife and excellent birdwatching opportunities in Washington, D.C. and nearby areas.""")
    
            

        elif option == "Prince William Forest Park (PRWI)":
            st.header("Prince William Forest Park (PRWI)")
            st.image(r"C:\Users\DELL\Downloads\9.jpg")
            st.write("""Prince William Forest Park in Virginia offers a vast expanse of forested trails and streams, making it a haven for hikers and bird enthusiasts.""")
    
             
        elif option == "Rock Creek Park (ROCR)":
            st.header("Rock Creek Park (ROCR)")
            st.image(r"C:\Users\DELL\Downloads\9.webp")
            st.write("""Rock Creek Park in Washington, D.C. is an urban sanctuary offering a mix of wooded trails and open spaces that support a wide variety of bird species.""")
    
           
        
        elif option == "Wolf Trap National Park for the Performing Arts (WOTR)":
            st.header("Wolf Trap National Park for the Performing Arts (WOTR)")
            st.image(r"C:\Users\DELL\Downloads\11.jpg")
            st.write("""Wolf Trap National Park in Virginia is renowned for its outdoor performances but also features wooded trails and habitats that attract various bird species.""")
     


    elif option == "Temporal Analysis":
        st.title("Temporal Analysis")
        st.header("Monthwise Analysis")
        
        # Query 1: Bird Sightings by Year and Month
        query1 = """SELECT 
        YEAR(Date) AS Observation_Year,
        MONTH(Date) AS Observation_Month,
        COUNT(*) AS Bird_Sightings
        FROM 
        world.`1`
        GROUP BY 
        Observation_Year, Observation_Month
        ORDER BY 
        Observation_Year, Observation_Month;
        """
        df1 = execute_query(connection, query1)
        
        if df1 is not None:
            df1["Observation_Month"] = pd.Categorical(
                df1["Observation_Month"],
                categories=(list(range(1, 13))),
                ordered=True
            )
            st.write(df1)

            # Plot Temporal Analysis (Bird Sightings by Month)
            def plot1(df):
                plt.figure(figsize=(10, 6))
                sns.lineplot(data=df, x="Observation_Month", y="Bird_Sightings", hue="Observation_Year", marker='o')
                plt.title("Analysis of Birds Sighting", fontsize=20)
                plt.xlabel("Months", fontsize=15)
                plt.ylabel("Birds_Sights", fontsize=15)
                plt.xticks(rotation=60)
                plt.tight_layout()
                st.pyplot(plt)

            plot1(df1)

        else:
            st.write("No data found for Temporal Analysis")
        
        # Query 2: Unique Dates by Year and Month
        st.header("Count of Observation Days In Month")
        query2 = """SELECT 
        YEAR(Date) AS Observation_Year,
        MONTH(Date) AS Observation_Month,
        COUNT(DISTINCT Date) AS Unique_Dates
        FROM 
        world.`1`
        GROUP BY 
        Observation_Year, Observation_Month
        ORDER BY 
        Observation_Year, Observation_Month;
        """
        df2 = execute_query(connection, query2)
        
        if df2 is not None:
            df2["Observation_Month"] = pd.Categorical(
                df2["Observation_Month"],
                categories=(list(range(1, 13))),
                ordered=True
            )
            st.write(df2)

            # Plot Temporal Analysis (Unique Dates by Month)
            def plot2(df):
                plt.figure(figsize=(10, 6))
                sns.barplot(data=df, x="Observation_Month", y="Unique_Dates", hue="Observation_Year", dodge=True)
                plt.title("Observation Days in Month", fontsize=14)
                plt.xlabel("Months", fontsize=15)
                plt.ylabel("Unique_Dates", fontsize=15)
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(plt)

            plot2(df2)

        else:
            st.write("No data found for Unique Dates Analysis")

    elif option == "Spatial Analysis":
        st.title("Spatial Analysis")
        st.header("Locationwise Spcies Count")
        query3 = """SELECT 
    Location_Type, 
    COUNT(DISTINCT Common_name) AS Total_Species 
FROM 
    world.1
GROUP BY 
    Location_Type
ORDER BY 
    Total_Species DESC;
        """
        df3 = execute_query(connection, query3)

        if df3 is not None and not df3.empty:
            st.write(df3)

            # Plot Spatial Analysis (Total Species by Location Type)
            def plot3(df):
                plt.figure(figsize=(10, 6))
                sns.barplot(data=df, x="Location_Type", y="Total_Species", hue="Location_Type", dodge=True)
                plt.title("Total Species by Location Type", fontsize=14)
                plt.xlabel("Location Type", fontsize=15)
                plt.ylabel("Total Species", fontsize=15)
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(plt)

            plot3(df3)

        else:
            st.write("No data found for Spatial Analysis")
        
        st.header("Avg Temperature & Humidity")
        query4 = """SELECT AVG(Temperature) AS Avg_Temperature, AVG(Humidity) AS Avg_Humidity
        FROM world.1
        WHERE Location_Type = "forest";"""
        df4 = execute_query(connection, query4)

        if df4 is not None and not df4.empty:
            st.write(df4)
            fig, ax = plt.subplots(figsize=(8, 6))
            avg_values = df4.iloc[0]  # Extract the first row of the result
            values = [avg_values['Avg_Temperature'], avg_values['Avg_Humidity']]
            labels = ['Average Temperature', 'Average Humidity']

            sns.barplot(x=labels, y=values, ax=ax, palette='coolwarm')
            plt.title("Average Temperature and Humidity in Forest", fontsize=16)
            plt.ylabel("Average Value", fontsize=12)
            plt.tight_layout()
            st.pyplot(fig)

        query5 = """SELECT AVG(Temperature) AS Avg_Temperature, AVG(Humidity) AS Avg_Humidity
        FROM world.1
        WHERE Location_Type = "grassland";"""
        df5 = execute_query(connection, query5)
        st.write(df5)
        fig, ax = plt.subplots(figsize=(8, 6))
        avg_values = df5.iloc[0]  # Extract the first row of the result
        values = [avg_values['Avg_Temperature'], avg_values['Avg_Humidity']]
        labels = ['Average Temperature', 'Average Humidity']

        sns.barplot(x=labels, y=values, ax=ax, palette='coolwarm')
        plt.title("Average Temperature and Humidity in Grassland", fontsize=16)
        plt.ylabel("Average Value", fontsize=12)
        plt.tight_layout()
        st.pyplot(fig)
    
    elif option == "Species Analysis":
        st.title("Species Analysis")
        st.header("ID_Methode OF Birds")
        query6 = """ SELECT 
    ID_Method, 
    AVG(Interval_Length_Num) AS Avg_Interval_Length,
    COUNT(*) AS Activity_Count
FROM 
    world.`1`
GROUP BY 
    ID_Method
ORDER BY 
    Activity_Count DESC;
       """
        df6 = execute_query(connection, query6)
        if df6 is not None:
            st.write(df6)
        else:
            st.write("No data found for Species Analysis")
    
        if df6 is not None:
            # Create a figure and axis for the plot
            fig, ax = plt.subplots(figsize=(12, 6))

            # Create a barplot on the axis
            sns.barplot(data=df6, x="ID_Method", y="Activity_Count", color="gray", ax=ax)

            # Set axis labels
            ax.set_xlabel("ID_Method", fontsize=14)
            ax.set_ylabel("Activity_Count", fontsize=14)

            # Set title for the entire figure
            plt.title("Activity Count and Avg Interval Length by ID Method", fontsize=16)

            # Adjust layout and show the plot
            plt.tight_layout()
            st.pyplot(fig)

        # Execute query and retrieve data
        st.header("Sex Ratio")
        query7 = """SELECT 
            Common_Name,
            SUM(CASE WHEN Sex = 'Male' THEN 1 ELSE 0 END) AS Male_Count,
            SUM(CASE WHEN Sex = 'Female' THEN 1 ELSE 0 END) AS Female_Count,
            ROUND(
                CAST(SUM(CASE WHEN Sex = 'Male' THEN 1 ELSE 0 END) AS FLOAT) /
                NULLIF(SUM(CASE WHEN Sex = 'Female' THEN 1 ELSE 0 END), 0),
                2
            ) AS Male_Female_Ratio
        FROM 
            world.1
        WHERE 
            Sex IN ('Male', 'Female')  
        GROUP BY 
            Common_Name
        HAVING 
            SUM(CASE WHEN Sex = 'Male' THEN 1 ELSE 0 END) > 0 AND  
            SUM(CASE WHEN Sex = 'Female' THEN 1 ELSE 0 END) > 0    
        ORDER BY 
            Male_Count desc;"""

        # Assume execute_query is a function that connects to the DB and returns a DataFrame
        df7 = execute_query(connection, query7)

        # Display dataframe (for debugging purposes)
        if df7 is not None and not df7.empty:
            st.write(df7)

            # Plot setup
            fig, ax1 = plt.subplots(figsize=(10, 6))

            # Plot Male and Female counts as bars
            bar_width = 0.35
            index = range(len(df7))
            ax1.bar(index, df7['Male_Count'], bar_width, label='Male', color='blue')
            ax1.bar([p + bar_width for p in index], df7['Female_Count'], bar_width, label='Female', color='orange')

            # Plot Male-Female ratio as line plot (secondary axis)
            ax2 = ax1.twinx()  # Create a second y-axis
            ax2.plot(index, df7['Male_Female_Ratio'], color='green', marker='o', label='Male-Female Ratio', linewidth=2)

            # Adding labels and title
            ax1.set_xlabel('Species')
            ax1.set_ylabel('Count')
            ax2.set_ylabel('Male-Female Ratio')
            ax1.set_xticks([p + bar_width / 2 for p in index])
            ax1.set_xticklabels(df7['Common_Name'], rotation=60, ha="right")
            ax1.set_title('Male vs Female Count with Male-Female Ratio')

            # Adding legends
            ax1.legend(loc='upper left')
            ax2.legend(loc='upper right')

            # Show plot in Streamlit
            st.pyplot(fig)

    elif option == "Environmental Conditions":
        st.title("Environmental Conditions")
        st.header("Weather Condition")
        query8 = """ SELECT
            AVG(Temperature_clean) AS avg_temperature,
            AVG(Humidity_clean) AS avg_humidity,
            Sky AS avg_sky,
            Wind AS avg_wind,
            AVG(distance_num) AS avg_distance,
            COUNT(*) AS total_records
        FROM
            world.1
        GROUP BY
            Sky, Wind
        """
        df8 = execute_query(connection, query8)
        st.write(df8)
        
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plot Avg Temperature vs Avg Distance (as an example)
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df8, x='avg_sky', y='total_records', hue='avg_wind', palette="Set2")
        plt.title('Total Records by Sky and Wind Conditions', fontsize=16)
        plt.xlabel('Sky Condition', fontsize=12)
        plt.ylabel('Total Records', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)
        
        st.header("Impact OF Disturbance")
        query9="""SELECT 
    Disturbance, 
    AVG(Temperature) AS avg_temperature, 
    AVG(Humidity) AS avg_humidity, 
    COUNT(*) AS total_records
FROM 
    world.1
GROUP BY 
    Disturbance
ORDER BY 
    Disturbance;
"""
        df9=execute_query(connection,query9)
        if df9 is not None:
          st.write(df9)

    # Prepare data for stacked bar chart
          bar_width = 0.4
          index = np.arange(len(df9["Disturbance"]))

# Create figure and axis
          fig, ax = plt.subplots(figsize=(10, 6))

# Plot temperature bars
          ax.bar(index - bar_width/2, df9["avg_temperature"], bar_width, label="Average Temperature", color='tomato')

# Plot humidity bars
          ax.bar(index + bar_width/2, df9["avg_humidity"], bar_width, label="Average Humidity", color='skyblue')

# Adding labels and title
          ax.set_title("Impact of Disturbance on Temperature and Humidity", fontsize=16)
          ax.set_xlabel("Disturbance Level", fontsize=12)
          ax.set_ylabel("Value", fontsize=12)
          ax.set_xticks(index)
          ax.set_xticklabels(df9["Disturbance"], rotation=45)
          ax.legend()

# Adjust layout and show the plot
          plt.tight_layout()
          st.pyplot(fig)

          
    elif option=="Distance and Behavior":
        st.title("Distance and Behavior")
        st.header("Observation Distance")
        query10=""" SELECT 
    distance_num AS Distance,
    COUNT(*) AS Total_Observations
FROM 
    world.`1`
WHERE 
    distance_num IS NOT NULL -- Exclude rows with NULL distance values
GROUP BY 
    distance_num
ORDER BY 
    Distance ASC;
"""
        df10=execute_query(connection,query10)
        st.write(df10)
        # Plotting
        plt.figure(figsize=(10, 6))

# Create a line plot
        sns.lineplot(data=df10, x="Distance", y="Total_Observations", marker="o", color="purple")

# Add titles and labels
        plt.title("Trend of Total Observations by Distance", fontsize=16)
        plt.xlabel("Distance (meters)", fontsize=12)
        plt.ylabel("Total Observations", fontsize=12)
        plt.xticks(rotation=45)

# Adjust layout
        plt.tight_layout()

# Display the plot in Streamlit
        st.pyplot(plt)
        
        st.header("Flyover_Observation")
        query11="""SELECT 
    Flyover_Observed, 
    COUNT(*) AS Total_Observations,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM world.`1`), 2) AS Percentage_Of_Total
FROM 
    world.`1`
WHERE 
    Flyover_Observed IS NOT NULL -- Exclude rows with NULL values
GROUP BY 
    Flyover_Observed
ORDER BY 
    Total_Observations DESC;
"""
        df11=execute_query(connection,query11)
        st.write(df11)

        plt.figure(figsize=(8, 8))

        # Define the colors for the pie chart
        colors = ["#FF9999", "#66B3FF", "#99FF99", "#FFCC99"]

        # Plot the pie chart
         # Define new labels
        labels = ["Non-Flyover", "Flyover"]

        # Plot pie chart with updated labels
        plt.figure(figsize=(8, 8))
        plt.pie(
         df11['Total_Observations'], 
         labels=labels, 
         autopct='%1.1f%%', 
         startangle=90, 
         colors=["#FF9999", "#66B3FF"], 
         wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}
         )

        # Add title
        plt.title("Flyover Observations Distribution", fontsize=16, fontweight="bold", color="darkblue")

        # Ensure the chart is circular
        plt.axis('equal')

        # Display the pie chart
        st.pyplot(plt)

    elif option=="Observer Trends":
        st.title("Observer Trends")
        st.header("Observers Observation Count")
        query12="""SELECT 
    Observer, 
    COUNT(*) AS Total_Observations,
    COUNT(DISTINCT Common_Name) AS Total_Species
FROM 
    world.`1`
WHERE 
    Observer IS NOT NULL
GROUP BY 
    Observer
ORDER BY 
    Total_Observations DESC;
"""    
        df12=execute_query(connection,query12)
        st.write(df12)
        
        
        plt.figure(figsize=(10, 6))

        sns.lineplot(x='Observer', y='Total_Observations', data=df12, marker='o', label='Total Observations', color='lightcoral')
        sns.lineplot(x='Observer', y='Total_Species', data=df12, marker='o', label='Total Species', color='skyblue')

        # Adding titles and labels
        plt.title('Total Observations and Total Species Reported by Observer', fontsize=16)
        plt.xlabel('Observer', fontsize=12)
        plt.ylabel('Count', fontsize=12)

        # Rotating the x-axis labels for better readability
        plt.xticks(rotation=45)

        # Display the plot within Streamlit
        plt.tight_layout()
        plt.legend()
        st.pyplot(plt)

        st.header("Visit Count")
        query13="""SELECT 
    Visit,
    COUNT(*) AS Total_Observations,
    COUNT(DISTINCT Common_Name) AS Total_Species,
    ROUND(COUNT(DISTINCT Common_Name) / COUNT(*) * 100, 2) AS Species_Diversity_Percent
FROM 
    world.`1`
WHERE 
    Visit IS NOT NULL  -- Ensure we're only considering rows with non-null visit data
GROUP BY 
    Visit
ORDER BY 
    Visit;
"""    
        df13=execute_query(connection,query13)
        st.write(df13)
        # Pie chart for Total Observations per Visit
        plt.figure(figsize=(8, 8))

        # Pie chart, where the slices will be ordered and labeled by visit
        plt.pie(df13['Total_Observations'], labels=df13['Visit'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(df13)))

        # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Distribution of Total Observations by Visit', fontsize=16)

        # Display the plot in Streamlit
        st.pyplot(plt) 

    elif option=="Conservation Insights":
        st.title("Conservation Insights")
        

        query14=""" SELECT 
    PIF_Watchlist_Status, 
    Regional_Stewardship_Status, 
    COUNT(DISTINCT Common_Name) AS Total_Species,
    COUNT(*) AS Total_Observations
FROM 
    world.`1`
WHERE 
    PIF_Watchlist_Status IS NOT NULL
GROUP BY 
    PIF_Watchlist_Status, Regional_Stewardship_Status
ORDER BY 
    Total_Species DESC;

"""
        df14=execute_query(connection,query14)
        st.write(df14)
        plt.figure(figsize=(10, 6))
        sns.barplot(x='PIF_Watchlist_Status', y='Total_Species', hue='Regional_Stewardship_Status', data=df14)

        # Adding titles and labels
        plt.title('Total Species Count by PIF Watchlist and Regional Stewardship Status', fontsize=16)
        plt.xlabel('PIF Watchlist Status', fontsize=12)
        plt.ylabel('Total Species Count', fontsize=12)
        plt.xticks(rotation=45)

        # Display the plot
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
        
        st.header("Parkwise Count")
        query15="""SELECT 
    AOU_Code, 
    COUNT(DISTINCT Common_Name) AS Total_Species,  -- Count the unique species for each AOU_Code
    COUNT(*) AS Total_Observations  -- Total number of observations for each AOU_Code
FROM 
    world.`1`
WHERE 
    AOU_Code IS NOT NULL  -- Exclude rows where AOU_Code is missing
GROUP BY 
    AOU_Code  -- Group by AOU_Code to get species and observations for each code
ORDER BY 
    AOU_Code ; """
        df15=execute_query(connection,query15)
        st.write(df15)
        # Get the top 10 AOU_Codes based on Total Species
        top_aou_codes = df15.nlargest(10, 'Total_Species')

        # Create the bar plot
        plt.figure(figsize=(12, 6))
        sns.barplot(x='AOU_Code', y='Total_Species', data=top_aou_codes, color='lightblue', label='Total Species')
        sns.barplot(x='AOU_Code', y='Total_Observations', data=top_aou_codes, color='salmon', label='Total Observations')

        # Adding titles and labels
        plt.title('Top 10 AOU Codes: Total Species and Total Observations', fontsize=16) 
        plt.xlabel('AOU Code', fontsize=12)
        plt.ylabel('Count', fontsize=12)

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)

        # Display the plot
        plt.tight_layout()
        plt.legend()
        plt.show()
        st.pyplot(plt)
     