import streamlit as st
import pycountry
import pandas as pd
import plotly.express as px

# set up the app with wide view preset and a title

st.set_page_config(layout="wide", initial_sidebar_state="expanded" )
st.header("WHO Coronavirus (COVID-19) Dashboard")
st.markdown(":blue[**COVID-19 Spread in the World upto 20 December 2022, reported to WHO.**]")


# import our data as a pandas dataframe

covid = pd.read_csv("data/covid_cases.csv")



def get_iso3(iso2):
    #Function takes in iso_alpha2 country codes and returns the iso_alpha 3 codes"""
    try:
        return pycountry.countries.get(alpha_2=iso2).alpha_3
    except:
        #In case we have errors that row of data will be left out.
        #Try except is a good way to handle possible errors that might occur while running a function"""
        pass
covid['iso_alpha'] = covid.Country_code.apply(lambda x: get_iso3(x))



# put all widgets in sidebar and have a subtitle

with st.sidebar:
    st.header("Overview")
    menu = ["Cases","Deaths"]
    #menu = ["Cumulative cases","New cases", "Cumulative deaths","New deaths"]
    selection = st.selectbox("**Visualizing the Global Spread of COVID-19 on a Choropleth Map.**", menu)

    col1, col2 = st.columns(2)
    with col2:
        st.write("##")
        st.write("##")
        st.title('**649,753,806**')
        st.markdown("cumulative cases")

        st.title('**6,648,457**')
        st.markdown("cumulative deaths")
    
        
    
    
if selection == 'Cases':
    tab1, tab2 = st.tabs(["Cumulative cases", "New cases"])

    with tab1:
        fig= px.choropleth(covid,
                           title = "COVID-19 Global Cumulative cases",
                           locations ="iso_alpha",
                           color ="Cumulative_cases", 
                           hover_name ="Country", # column to add to hover information
                           color_continuous_scale = px.colors.sequential.Viridis,
                           animation_frame = "Date_reported") # animation based on the dates
        fig.update_layout(height = 600) # Enlarge the figure
        fig.update_geos(visible=False)
        st.plotly_chart(fig, use_container_width=True, theme='streamlit') 
    
    with tab2:
        fig= px.choropleth(covid,
                           title = "COVID-19 Global New cases",
                           locations ="iso_alpha",
                           color ="New_cases", 
                           hover_name ="Country", # column to add to hover information
                           color_continuous_scale = px.colors.sequential.Viridis,
                           animation_frame = "Date_reported") # animation based on the dates
        fig.update_layout(height = 600) # Enlarge the figure
        fig.update_geos(visible=False)
        st.plotly_chart(fig, use_container_width=True, theme='streamlit') 


if selection == 'Deaths':

    tab3, tab4 = st.tabs(["Cumulative deaths", "New deaths"])

    with tab3:
        fig= px.choropleth(covid,
               title = "COVID-19 Global Cummulative deaths",
               locations ="iso_alpha",
               color ="Cumulative_deaths", 
               hover_name ="Country", # column to add to hover information
               color_continuous_scale = px.colors.sequential.Viridis,
               animation_frame = "Date_reported") # animation based on the dates
        fig.update_layout(height = 600) # Enlarge the figure
        fig.update_geos(visible=False)
        st.plotly_chart(fig, use_container_width=True, theme='streamlit') 
    
    with tab4:
        fig= px.choropleth(covid,
               title = "COVID-19 Global New deaths",
               locations ="iso_alpha",
               color ="New_deaths", 
               hover_name ="Country", # column to add to hover information
               color_continuous_scale = px.colors.sequential.Viridis,
               animation_frame = "Date_reported") # animation based on the dates
        fig.update_layout(height = 600) # Enlarge the figure
        fig.update_geos(visible=False)
        st.plotly_chart(fig, use_container_width=True, theme='streamlit') 

# create plot 
##Cumulative cases per day
    
covid["Date_reported"] = pd.to_datetime(covid["Date_reported"])
daily_cumulative = covid.groupby("Date_reported")["Cumulative_cases"].sum().reset_index()
fig = px.bar(daily_cumulative, 
             title = "a) COVID-19 Daily Cumulative Cases",
             x='Date_reported', 
             y='Cumulative_cases',
             hover_data = ['Date_reported',"Cumulative_cases"],
             labels={'Date_reported':'daily_reports'},
             #color_discrete_sequence = ['light grey']
                    )
fig.update_layout(height=400, clickmode='event+select')
fig.update_traces(marker_color = 'rgba(128, 0, 32, 0.7)',
                  marker_line_width = 0,
                  selector=dict(type="bar"))
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

st.markdown(":blue[**Globally**], as of :blue[**20 December 2022**], there were :blue[**649,753,806 Cumulative Cases.**]")

## Cumulative deaths per day

daily_cumulative1 = covid.groupby("Date_reported")["Cumulative_deaths"].sum().reset_index()
fig = px.bar(daily_cumulative1, 
             title = "b) COVID-19 Daily Cumulative Deaths",
             x='Date_reported', 
             y='Cumulative_deaths',
             hover_data = ['Date_reported',"Cumulative_deaths"],
             labels={'Date_reported':'daily_reports'},
             color_discrete_sequence = ['#7393B3'], 
                    )
fig.update_layout(height=400, clickmode='event+select')
fig.update_traces(marker_color = 'rgba(128, 0, 32, 0.7)',
                  marker_line_width = 0,
                  selector=dict(type="bar"))
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

st.markdown(":blue[**Globally**], as of :blue[**20 December 2022**], there were :red[**6,648,457 Cumulative Deaths.**]")




### TASKS
## 1. GENERATE THREE MORE ANIMATED GRAPHS i.e. new cases, cumulative deaths, new deaths
## 2. Give your graphs titles and if possible add explanative text after each graph
## 3. Use widgets in the sidebar to help the user chooose between the four animations: e.g. select box, button, radio 
## 4. create bar graphs to show the cumulative cases per day and cumulative daeaths per day 
## 5. deploy your app to streamlit cloud
## 6. submit the link to your streamlit app on dexvirtual


