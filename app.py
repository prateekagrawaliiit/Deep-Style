# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-06 21:48:25
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-11 11:57:58

import streamlit as st 
from PIL import Image
import style
import io
import os
import shutil
import random
files_input = os.listdir('./images/content-images/')
files_output = os.listdir('./images/output-images/')
filtered_input = [file for file in files_input if file.endswith('.jpg') and file != 'amber.jpg']
filtered_output = [file for file in files_output if file.endswith('.jpg')]
for file in filtered_input:
	os.remove('./images/content-images/'+file)
for file in filtered_output:
	os.remove('./images/output-images/'+file)
st.markdown("<h1 style='text-align: center;'>DeepStyle</h1>", unsafe_allow_html=True)
st.markdown(
	"""
	**DeepStyle** is a Style Transfer web application implemented using transfer learning in PyTorch.
	""")
style_name = st.sidebar.selectbox('Select Style',('Candy','Mosaic','Rain Princess','Udnie'))
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
output_image =""
input_img = ""
upload = ""
img ='selected'
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
	input_img = './images/content-images/'+str(ran_num)+'.jpg'
	print(input_img)
	with open(input_img, 'wb') as f:
		f.write(uploaded_file.getbuffer()) 
	output_image = "./images/output-images/"+selected_model+"-"+str(ran_num)+"-selected"+str(ran_num) +'.jpg'

else:
	st.markdown("<h2 style='text-align: center;'>OR</h2>", unsafe_allow_html=True)
	img = st.selectbox('Choose one from the following :',('Select','Amber','Cat'))
	if img=='Amber':
		img = 'amber.jpg'
	elif img=='Select':
		img = 'not_selected'
	else:
		img='cat.png'
	input_img = "./images/content-images/"+img
	output_image = "./images/output-images/"+selected_model+"-"+str(ran_num)+"-"+img

st.sidebar.header('Selected Style')
sty_img = Image.open('./images/style-images/'+style_name+'.jpg')
st.sidebar.image(sty_img,width=300)

a_file = open("./images/output-images/dummy.txt")
lines = a_file.readlines()
count = int(lines[0])
_text = 'Total Images Stylized : '+str(count)
st.sidebar.text(_text)

if img!='not_selected':
	st.write("""- ### Selected Source Image :""")
	image = Image.open(input_img)
	st.image(image,width=500)

stylize_btn = st.button("Stylize the selected Image")

if stylize_btn:
	with open('./images/output-images/dummy.txt','w+') as f:
		f.write(str(count+1))
	f.close()

	model = style.load_model(saved_model)
	style.stylize(model,input_img,output_image)
	st.write("""- ### Converted Image :""")
	image = Image.open(output_image)
	st.image(image,width=500)

st.sidebar.markdown("""#### DeepStyle is built and maintained by **Prateek Agrawal**. Please contact in case of queries or just to say Hi!!!.""")
github = '[GitHub](http://github.com/prateekagrawaliiit)'
linkedin = '[LinkedIn](https://www.linkedin.com/in/prateekagrawal1405/)'
email = '<a href="mailto:prateekagrawaliiit@gmail.com">Email</a>'
st.sidebar.markdown("""""")
st.sidebar.markdown(github, unsafe_allow_html=True)
st.sidebar.markdown(linkedin, unsafe_allow_html=True)
st.sidebar.markdown(email, unsafe_allow_html=True)
