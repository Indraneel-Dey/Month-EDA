import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

df = pd.read_csv('Month Data.csv')
profile = ProfileReport(df)

st.write('Indraneel Dey')
st.write('21f3002696')
st.write('Indian Institute of Technology, Madras')
st.title('Profile Report of Monthly Capital and Labor Costs')
st.write(df)
st_profile_report(profile)
