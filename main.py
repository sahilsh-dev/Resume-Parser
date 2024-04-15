import streamlit as st
from utils import get_parsed_resumes


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

if uploaded_files:
    st.success('Files uploaded successfully', icon="✅")
    resumes = get_parsed_resumes(uploaded_files)
    resumes    
    
