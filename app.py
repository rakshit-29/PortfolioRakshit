import streamlit as st
import pandas as pd
import numpy as np
import base64
from io import BytesIO
import os
import streamlit.components.v1 as stc
import plotly.graph_objects as go


import constants as ct

import matplotlib
matplotlib.use('Agg')  # To Prevent Errors
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image


def main():

    menu = ["Home", "About Rakshit"]
    choice = st.sidebar.selectbox("Navigator", menu)

    if choice == "Home":
        stc.html(ct.HTML_BANNER)

        image = Image.open('image_profile.jpeg')

        st.image(image)



    if choice == "About Rakshit":

        st.write("I am a Data Science and Machine Learning enthusiast, and wish to excel in the field of AI."
                 " Inclined towards finding solutions to scientific issues in the health industry and space technology."
                 " Currently, enrolled in Lakehead University. I would like to pursue masters degree in AI after some work experience as a ML software engineer and hopefully a doctorate for the same."
                 " On the other side, I, am a great cook, sing, play some instruments, play video games, attend festivals, and, like to workout too. 😅")

        st.subheader("LinkedIn")
        stc.html(ct.embed_component['linkedin'], height=400)

        st.subheader("GitHub")
        stc.html(ct.embed_component['github'], height=400)

        with open("Saxena_Rakshit_resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.subheader("Resume")
        st.download_button(label="Download my resume",
                           data=PDFbyte,
                           file_name="Resume_Rakshit_V_Saxena.pdf",
                           mime='application/octet-stream',)

        st.sidebar.write('📧: rakshit290900@gmail.com')
        st.sidebar.write('📞: +1-807-357-6601')

        st.subheader('Skills & Technologies 👨‍💻️')

        def skill_tab():
            rows, cols = len(ct.info['skills']) // ct.skill_col_size, ct.skill_col_size
            skills = iter(ct.info['skills'])
            if len(ct.info['skills']) % ct.skill_col_size != 0:
                rows += 1
            for x in range(rows):
                columns = st.columns(ct.skill_col_size)
                for index_ in range(ct.skill_col_size):
                    try:
                        columns[index_].button(next(skills))
                    except:
                        break

        with st.spinner(text="Loading Skills...⌛"):
            skill_tab()

        st.subheader('Education 📖')

        fig = go.Figure(data=[go.Table(
            header=dict(values=list(ct.info['edu'].columns),
                        fill_color='Thistle',
                        align='left', height=65, font_size=20),
            cells=dict(values=ct.info['edu'].transpose().values.tolist(),
                       fill_color='LavenderBlush',
                       align='left', height=40, font_size=15))])

        fig.update_layout(width=750, height=400)
        st.plotly_chart(fig)

        st.subheader('Certifications 🏅')
        ibm_image = Image.open('ibm_ds_certificateJpeg.jpg')

        st.image(ibm_image, caption='IBM Data Science Professional Certificate, more to come...⌛')

        stc.html(ct.html_ender)


if __name__ == '__main__':
    main()