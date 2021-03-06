# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-06 21:48:25
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-07 01:07:43

import streamlit as st 
from PIL import Image
import style
import random
st.markdown("<h1 style='text-align: center;'>DeepStyle</h1>", unsafe_allow_html=True)
st.markdown(
	"""
	**DeepStyle** is a Style Transfer web application implemented using transfer learning in PyTorch.
	""")

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

ran_num = random.randint(1,9999999)

selected_model = style_name
saved_model = "saved_models/"+style_name+".pth"

input_img = "./images/content-images/"+img

output_image = "./images/output-images/"+selected_model+"-"+str(ran_num)+"-"+img

st.sidebar.header('Selected Style')
sty_img = Image.open('./images/style-images/'+style_name+'.jpg')
st.sidebar.image(sty_img,width=300)

st.sidebar.markdown("""#### DeepStyle is built and maintained by **Prateek Agrawal**. Please contact in case of queries or just to say Hi!!!.""")
github = '[GitHub](http://github.com/prateekagrawaliiit)'
linkedin = '[LinkedIn](https://www.linkedin.com/in/prateekagrawal1405/)'
email = '<a href="mailto:prateekagrawaliiit@gmail.com">Email</a>'
st.sidebar.markdown("""""")
st.sidebar.markdown(github, unsafe_allow_html=True)
st.sidebar.markdown(linkedin, unsafe_allow_html=True)
st.sidebar.markdown(email, unsafe_allow_html=True)

st.write("""- ### Selected Source Image :""")
image = Image.open(input_img)
st.image(image,width=500)


stylize_btn = st.button("Stylize the selected Image")

if stylize_btn:
	model = style.load_model(saved_model)
	style.stylize(model,input_img,output_image)
	st.write("""- ### Converted Image :""")
	image = Image.open(output_image)
	st.image(image,width=500)
