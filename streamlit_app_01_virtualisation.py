import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import graphviz as graphviz
import plotly.express as px
# Load datasets
df1 = pd.read_csv("assets/A/rs_session_239_AU1719_1.1.csv")
# df2 = pd.read_csv("assets/B/RJ_Session_247_AU_1081.1.csv")

# Display header for MGNREGA Projects
st.title("MGNREGA Data Analysis")

# Display information about MGNREGA projects
st.header("MGNREGA Projects Information")
st.dataframe(df1)


# Visualization 1: Horizontal Bar Chart for Central funds released
st.subheader("Visualization 1: Horizontal Bar Chart - Central Funds Released")
fig, ax = plt.subplots()
ax.barh(df1['States'], df1['Central funds released 2016-17'])
ax.set_xlabel('Central funds released 2016-17')
ax.set_ylabel('States')
ax.set_title('Central funds released 2016-17 by States')
st.pyplot(fig)

# Visualization 2: Pie Chart for Districts
st.subheader("Visualization 2: Donut Chart - Districts Distribution")

fig = px.pie(df1, values='Districts - Total', names='States', hole=0.4)
fig.update_layout(title='Districts Distribution by States', showlegend=False)

st.plotly_chart(fig)

# Visualization 3: Horizontal Bar Chart for Panchayats
st.subheader("Visualization 3: Horizontal Bar Chart - Panchayats Distribution")
fig, ax = plt.subplots()
ax.barh(df1['States'], df1['Panchayats - Total'])
ax.set_xlabel('Panchayats - Total')
ax.set_ylabel('States')
ax.set_title('Panchayats Distribution by States')
st.pyplot(fig)

# Visualization 4: Altair Scatter Plot for Blocks
st.subheader("Visualization 4: Altair Scatter Plot - Blocks Distribution")
chart = alt.Chart(df1).mark_circle().encode(
    x='Blocks - Total',
    y='Blocks - Drought Effected',
    color='States',
    tooltip=['States', 'Blocks - Total', 'Blocks - Drought Effected']
).interactive()
st.altair_chart(chart, use_container_width=True)

# Visualization 5: Graphviz Chart for Drought Effected Panchayats
st.subheader("Visualization 5: Graphviz Chart - Drought Effected Panchayats")
graph_data = '\n'.join([f'"{state}" -> "Drought Effected Panchayats: {count}"' for state, count in zip(df1['States'], df1['Panchayats - Drought Effected'])])
st.graphviz_chart(f'digraph {{ {graph_data} }}')




df = pd.read_csv("assets/B/RJ_Session_247_AU_1081.1.csv")
# Display header
st.title("MGNREGA Employment Data Analysis")

# Display information about MGNREGA employment
st.header("Employment Generated Information")
st.dataframe(df)

# Visualization 1: Bar Chart for Number of Projects Assisted in 2017-18
st.subheader("Visualization 1: Horizontal Bar Chart - Number of Projects Assisted in 2017-18")
chart1 = alt.Chart(df).mark_bar().encode(
    x='2017-18 - Number of projects assisted',
    y=alt.Y('State/UT:N', sort='-x'),
    tooltip=['State/UT', '2017-18 - Number of projects assisted']
).properties(width=500)
st.altair_chart(chart1, use_container_width=True)

# Visualization 2: Line Chart for Estimated Employment Generated Over Years
st.subheader("Visualization 2: Line Chart - Estimated Employment Generated Over Years")
df_long = df.melt(id_vars=['State/UT'], value_vars=['2015-16 - Estimated employment generated - (No. of persons)',
                                                    '2016-17 - Estimated employment generated (No. of persons)',
                                                    '2017-18 - Estimated employment generated (No. of persons)'],
                   var_name='Year', value_name='Estimated Employment Generated')

chart2 = alt.Chart(df_long).mark_line().encode(
    x='Year:N',
    y='Estimated Employment Generated:Q',
    color='State/UT:N',
    tooltip=['State/UT:N', 'Year:N', 'Estimated Employment Generated:Q']
).interactive()
st.altair_chart(chart2, use_container_width=True)

# Visualization 3: Scatter Plot for Projects Assisted and Employment Generated in 2017-18
st.subheader("Visualization 3: Scatter Plot - Projects Assisted vs Employment Generated in 2017-18")

fig, ax = plt.subplots()
scatter = ax.scatter(
    df['2017-18 - Number of projects assisted'],
    df['2017-18 - Estimated employment generated (No. of persons)'],
    c=df.index,  # Use index for color variation
    cmap='viridis',
    s=100,  # Marker size
    alpha=0.7  # Marker transparency
)

# Add labels and title
ax.set_xlabel("Number of Projects Assisted")
ax.set_ylabel("Estimated Employment Generated (No. of persons)")
ax.set_title("Scatter Plot - Projects Assisted vs Employment Generated in 2017-18")

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label("Index")

# Show the plot
st.pyplot(fig)

