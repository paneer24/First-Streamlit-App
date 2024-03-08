import streamlit as st
import pandas as pd
from PIL import Image
st.title('File Uploading')
#Image
img_file=st.file_uploader('Upload Image',type=['jpg'])
if img_file is not None:
    # st.write(type(img_file))
    file_details={'file_name':img_file.name,'file_type':img_file.type,
                  'file_size':img_file.size}
    st.write(file_details)
    st.image(Image.open(img_file))
#Audio
st.subheader('3.Uploading Audio')
audio_file=st.file_uploader('Upload Audio',type=['wav','mp3'])
if audio_file is not None:
    # st.write(type(img_file))
    file1_details={'file_name':img_file.name,'file_type':img_file.type,
                  'file_size':img_file.size}
    st.write(file1_details)
    st.audio(audio_file)
#Video
video_file=st.file_uploader('Upload Video',type=['mp4','mkv'])
if video_file is not None:
    # st.write(type(img_file))
    file2_details={'file_name':video_file.name,'file_type':video_file.type,
                  'file_size':video_file.size}
    st.write(file2_details)
    st.video(video_file) 
#CSV
