# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-06 21:48:25
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-06 22:16:11

import streamlit as st 
from PIL import Image
import style

st.title('DeepStyle')
st.markdown(
	"""
	**DeepStyle** is a Style Transfer web application implemented using transfer learning in PyTorch.
	""")
st.sidebar.title('DeepStyle')

img = st.sidebar.selectbox('Select Image',('Amber','Cat'))
if img=='Amber':
	img = 'amber.jpg'
else:
	img='cat.png'

style_name = st.sidebar.selectbox('Select Image',('Candy','Mosaic','Rain Princess','Udnie'))
if(style_name=='Candy'):
	style_name='candy'
elif(style_name=='Mosaic'):
	style_name='mosaic'
elif(style_name=='Rain Princess'):
	style_name='rain_princess'
else:
	style_name='udnie'

selected_model = style_name
saved_model = "saved_models/"+style_name+".pth"

input_img = "./images/content-images/"+img

output_image = "./images/output-images/"+selected_model+"-"+img

st.sidebar.header('Selected Style')
sty_img = Image.open('./images/style-images/'+style_name+'.jpg')
st.sidebar.image(sty_img,width=300)

st.write("""Selected Source Image :""")
image = Image.open(input_img)
st.image(image,width=500)


stylize_btn = st.button("Stylize the selected Image")

if stylize_btn:
	model = style.load_model(saved_model)
	style.stylize(model,input_img,output_image)
	st.write("""Converted Image :""")
	image = Image.open(output_image)
	st.image(image,width=500)