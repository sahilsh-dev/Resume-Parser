import os
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import utils 


st.title('Resume Parser App')
st.write(
    '''The resume parser application can be used to extract information from resumes.
    It provides a user-friendly interface to upload resumes and returns an excel file with the extracted information.'''
)
st.write('')
st.write('')

st.subheader('Upload Resumes')
uploaded_files = st.file_uploader('Choose files', accept_multiple_files=True, type=['pdf', 'docx', 'doc'])
st.write('')

excel_created = False
if uploaded_files:
    with st.status("Parsing resumes...", expanded=True) as status:
        st.write("Uploading files...")
        resumes = utils.get_parsed_resumes(uploaded_files)

        st.write("Getting the parsed data...")
        sheet, workbook = utils.create_excelsheet()

        st.write("Creating excel sheet...")
        utils.add_data_to_excelsheet(sheet, workbook, resumes)
        workbook.save("resumes.xlsx")
        status.update(label="Excel File Created ", state="complete", expanded=False)
        excel_created = True
        
st.write('')

if excel_created:
    parsed_data = pd.read_excel("resumes.xlsx")
    AgGrid(parsed_data, height=200)
    st.write('')
    with open("resumes.xlsx", "rb") as file:
        st.download_button(
            label="Download excel file",
            data=file,
            file_name="resumes.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

    st.balloons()
    st.write('')
    st.write('''
        The excel file contains the extracted information from the resumes. Thanks for visiting! \n
        Made with 💗 by Sahil Sharma       
    ''')
    os.remove("resumes.xlsx")
