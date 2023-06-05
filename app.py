import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
image_path = 'https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png'
st.image(image_path)
with st.container():
  st.title("Assay Calculations App")
  st.write("Please connect this app to your lab to calculate the assay based on the HPLC measurements it receives from EDA lab. ")
  
col1, col2 = st.columns([1,1])

with col1:
  st.subheader("Standard")
  standard_values_st = []
  for i in range(5):
    standard_values_st.append(float(st.number_input("Area of standard", key="standard_value_{}".format(i), default="0")))
  average = round(np.mean(standard_values_st),2)
  standard_deviation = round(np.std(standard_values_st),2)
  RSD = round(standard_deviation*100/average,2)
  st.write("Average of standard:", average)
  st.write("Standard deviation :", standard_deviation)
  st.write("Relative standard deviation :", RSD)

with col2:
  st.subheader("Sample")
  standard_values_s = []
  for i in range(3):
    standard_values_s.append(float(st.number_input("Area of sample", key="standard_value_sample_{}".format(i), default="0")))
  average_s = round(np.mean(standard_values_s),2)
  st.write("Average of sample:", average_s)

########sample
with st.container():
  st.subheader("The percentage of assay")
  standard_concentration = float(st.number_input("Concentration of standard (µg/mL)", key="standard_concentration", default="0"))
  sample_concentration = float(st.number_input("Concentration of sample (µg/mL)", key="sample_concentration", default="0"))
  standard_purity = float(st.number_input("Purity of standard (%)", key="purity", default="0"))
  assay = average_sstandard_puritystandard_concentration/(average*sample_concentration)
  assay2 = round(assay,2)
  st.write("Assay:", assay2, "% ")





