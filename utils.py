import os
from dotenv import load_dotenv
from affinda import AffindaAPI, TokenCredential
import openpyxl
import streamlit as st


load_dotenv()
token = os.getenv("AFFINDA_TOKEN")
credential = TokenCredential(token=token)
client = AffindaAPI(credential=credential)

my_organisation = client.get_all_organizations()[0]
resume_parser_workspace = client.get_all_workspaces(my_organisation.identifier)[0]
resume_collection = client.get_all_collections(resume_parser_workspace.identifier)[0]


def get_parsed_resumes(files):
    resumes = []    
    for file in files:
        resume = client.create_document(file=file, file_name=file.name, collection=resume_collection.identifier)
        resumes.append(resume.as_dict())
    return resumes


def create_excelsheet():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    # headers = ["Name", "Email", "Phone", "Education", "Work Experience"]
    headers = ['Name', 'Email', 'Phone']
    sheet.append(headers)
    return sheet, workbook


def add_data_to_excelsheet(sheet, workbook, resumes):
    for resume in resumes:
        parsed_data = resume['data']
        name = parsed_data['name']['first'] + ' ' + parsed_data['name']['middle']  + parsed_data['name']['last']
        email = '\n'.join(parsed_data['emails'])
        phone = '\n'.join(parsed_data['phone_numbers'])
        sheet.append([name, email, phone])
    workbook.save("resumes.xlsx")
