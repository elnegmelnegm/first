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
    area_input = st.text_input("Area of standard {}".format(i+1), key="standard_value_st{}".format(i))
    if area_input == "":
      standard_values_st.append(0)
    else:
      standard_values_st.append(float(area_input))
 # Calculate average and standard deviation
  average = round(np.mean([x for x in standard_values_st if x != 0]), 2)
  standard_deviation = round(np.std([x for x in standard_values_st if x != 0]), 2)
  RSD = round(standard_deviation*100/average,2)
# Display results
  st.write("Average of standard:", average)
  st.write("Standard deviation :", standard_deviation)
  st.write("Relative standard deviation :", RSD)  
with col2:
  st.subheader("Sample")
  standard_values_s = []
 
  for i in range(3):
    area_input_s = st.text_input("Area of sample {}".format(i+1), key="standard_value_s{}".format(i))
    if area_input_s == "":
      standard_values_s.append(0)
    else:
        standard_values_s.append(float(area_input_s))

# Calculate average and standard deviation
  average_s = round(np.mean([x for x in standard_values_s if x != 0]), 2)

# Display results
  st.write("Average of sample:", average_s)
    #st.write("Standard deviation:", standard_deviation)
########sample
with st.container():
  st.subheader("The percentage of assay")
  standard_concentration = st.text_input("Concentration of standard (µg/mL)", key="standard_concentration")
  if standard_concentration == "":
    standard_concentration = 0
  else:
    standard_concentration = float(standard_concentration)
  sample_concentration = st.text_input("Concentration of sample (µg/mL)", key="sample_concentration")
  if sample_concentration == "":
    sample_concentration = 0
  else:
    sample_concentration = float(sample_concentration)

  standard_purity = st.text_input("Purity of standard (%)", key="purity")
  if standard_purity == "":
    standard_purity = 0
  else:
    standard_purity = float(standard_purity)
  assay = average_s*standard_purity*standard_concentration/(average*sample_concentration)
  assay2 = round(assay,2)
  st.write("Assay:", assay2, "% ")



