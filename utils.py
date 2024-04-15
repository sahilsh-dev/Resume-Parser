import os
from dotenv import load_dotenv
from affinda import AffindaAPI, TokenCredential


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
