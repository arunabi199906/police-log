import streamlit as st
import pandas as pd 
import postgresSQL 
import plotly.express as px

#Database connetion
def create_connetion():
    try:
        connrtion=pymydql.connet(
            host='location',
            user='root',
            password='1234',
            cursorclass=pymysql.cursors.distcursor
        )
        return connention
    except Exception as e:
        st.error(f"Database Connetion Error.{e}")
    return None 

    #fetch data from database
    def fetch_data(query):
        connetion=create_connetion()
        if connention:
            try:
                with connrtion.cursor()as cursor:
                    cursor.execute(query)
                    result=cursor.fetchall()
                    df=nd dataframe(result)
                    return df
            finally:
                connetion.close()
        else:
            return pd.Dataframe()

   #streamlit
   
   st.set_page_config(page_title="securecheck police dashboard" layout="wide") 


   st.markdown("Real time monitoring and insighta for lawenforcement ")

   #full table
   st.header("police logs overview")
   query="SELECT * FROM Police_logs"
   data=fetch_data(query)
   st.datafrance(data use_container_width=true)

#quick metries
st.header("key metrics") 


col1, col2, col3, col4 =st.columns(4)

with col1:
    total_stops=data.shape[0]
    st.metric["Total police stops",total_stops]

 with col2:
    arresets =  data[data['stop_outcome'].str. contains("arrest",case=false,na=false)].shape(0)

 with col3:
    warings=  data[data['stop_outcome'].str.contains("waring", case=false,na=false)].shape(0)
 with col4:
    drug_related=data[data['drugs_related_stop'] ==].shape(0)
   st.metric("Drug Related stops",drug_related)

#charts
  st.header("Visual Insights")


tab1, tab2 =st.tabs(["stops by violation","Driver Gender Distribution"])
