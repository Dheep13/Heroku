from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Deepan_CallidusResume.docx"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | John Doe"
PAGE_ICON = ":wave:"
NAME = "Deepan Shanmugam"
DESCRIPTION = """
Senior Consultant\n @ SAP
\n SAP Commissions and Data Integration | SAP CPQ | SAP HANA | SAP Conversational AI | LCNC | AppGyver | Python | SAP BTP | NodeJS
"""
EMAIL = "deepanshanmugam13@gmail.com"
# SOCIAL_MEDIA = {
#     "YouTube": "https://youtube.com/c/codingisfun",
#     "LinkedIn": "https://www.linkedin.com/in/deepanshanmugam/",
#     "GitHub": "https://github.com",
#     "Twitter": "https://twitter.com",
# }
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/deepanshanmugam/"
}
# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# }

PROJECTS = {
    ":bulb: Chatbot For SAP Commissions": "https://blogs.sap.com/2021/10/06/chatbot-for-sap-commissions-using-saps-conversational-ai-and-python-app/",
    ":bulb: Integrating SAP Appgyver with SAP Commissions": "https://blogs.sap.com/2021/11/08/integrating-sap-appgyver-with-sap-commissions-part-1/",
    ":bulb: Dashboards for SAP CPQ": "https://blogs.sap.com/2021/10/28/a-simple-dashboard-using-sap-cpqs-custom-table-api-and-python-app/",
    ":bulb: Replicate Data from SuccessFactors to Commissions using Speech-To-Text": "https://blogs.sap.com/2022/11/07/replicate-data-from-successfactors-to-commissions-using-speech-to-text/",
}



PROGRAMMING ="PROGRAMMING"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON )


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.markdown('hello <span style="font-family:Courier; color:Blue; font-size: 20px;">hello</span>',unsafe_allow_html=True)
    # st.markdown('I only want to make only'<span style="color:blue;">'THIS'</span>'word blue',,unsafe_allow_html=True)
    
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write( 
    """
- ✔️ Senior Consultant at SAP India, with 12+ years of IT experience working on various SAP Callidus Cloud and On-Premise solutions

- ✔️ Responsible for architecture, design, development, testing & deployments of SAP SPM solutions, namely, SAP Sales Cloud Commissions,Data Integration for SAP Commissions and SAP Configure Price Quote

- ✔️ Predominantly involved in Data Integration activities for Commissions system

- ✔️ Currently involved in Incident Handling/Delivering Solutions on SAP Configure Price Quote (CPQ) and Innovations around SPM solutions

  ✔️ Experience working on projects across domains such as Insurance, HealthCare, Banking, Logistics and Supply Chain Management and Telecom domains
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
# st.write(
#     """
# - 👩‍💻 Programming: Python, Shell (bash), Batch scripting, Oracle PL SQL, HANA SQL Script, Knockout JS
# - 📊 Data Visulization: PowerBi, MS Excel, Plotly
# - 📚 Modeling: Logistic regression, linear regression, decition trees
# - 🗄️ Databases: Postgres, MongoDB, MySQL
# """
# )

# st.markdown(<p 'Hello' <span style='color:green'>'world'</span></p>,unsafe_allow_html=True)
st.write(
    """
- 👩‍💻 **_Programming_** : Python, Shell (bash), Batch scripting, Oracle PL SQL, HANA SQL Script, Knockout JS)

- :computer: **_Applications_** :  SAP Callidus Commissions, SAP Commissions Data Loader, SAP Configure Price Quote, SAP Territory & Quota Management, SAP Workflow, SAP Conversational AI, SAP Appgyver, SAP Business Technology Platform, SAP Cloud Platform Integration, Data Integration using RESTful APIs (Commissions and CPQ)

- 🗄️ **_Databases_** :  HANA, Oracle, MySQL, MongoDB
""")


# st.write(
#     """
# - 👩‍💻 **_Programming_**:  Python, Shell (bash), Batch scripting, Oracle PL SQL, HANA SQL Script, Knockout JS

# - 📚 **_Applications_** :  SAP Callidus Commissions, SAP Commissions Data Loader, SAP Configure Price Quote, SAP Territory & Quota Management, SAP Workflow, SAP Conversational AI, SAP Appgyver, SAP Business Technology Platform, SAP Cloud Platform Integration, Data Integration using RESTful APIs (Commissions and CPQ)

# - 🗄️ **_Databases_** :  HANA, Oracle, MySQL, MongoDB
# """
# )



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write(":checkered_flag:", """**Senior Consultant @ SAP**""")
st.write("10/2019 - Present")
st.write(
    """
**_Technologies_**: SAP Commissions, Oracle PL SQL, Shell Scripting, SAP Workflow, SAP Territory Quota and Management, SAP Configure Price Quote (CPQ), SAP Conversational AI, SAP Cloud Platform Integration, SAP Commissions Data Loader, SAP Appgyver, SAP BTP, SAP Cloud Foundry, SAP API Business HUB""")
st.write("""
**Roles & Responsibilities :** 
\n•	Started off as Data Integration and Commissions specialist and was involved primarily in building Oracle and HANA stage hooks for Commissions 
\n•	Responsible for requirements gathering and preparing functional and technical solution design documents for Commissions/Data Integration.
\n•	Currently Involved in incident handling and delivering solutions on SAP Configure Price Quote (CPQ)
\n•	Part of the innovation team within SAP, contributing and working on ideas to enhance Callidus solutions

"""
)

st.write(""" _______________________________________________________________________________________________________________________________________""")

# --- JOB 2
st.write(":checkered_flag:", """**Associate @ Tata Consultancy Services**""")
st.write("May 2018 - September 2019")
st.write(
    """
**_Technologies_**: SAP Commissions, Oracle PL SQL, Shell Scripting""")
st.write("""
**Roles & Responsibilities :** 
\n•	Callidus enhancements and performance tuning
\n•	Commissions Rule Writing and Data Integration
\n•	Involved in RFPs for Callidus projects 
"""
)

st.write(""" _______________________________________________________________________________________________________________________________________""")

# --- JOB 3
st.write(":checkered_flag:", """**Product Specialist @ Cognizant Technology Solutions**""")
st.write("October 2014 - May 2018 ")
st.write(
    """
**_Technologies_**: SAP Commissions, SAP Workflow, Oracle PL SQL, Shell Scripting""")
st.write("""
**Roles & Responsibilities :** 
\n•	Data Integration-Integrating the legacy system with Callidus Commissions.
\n•	Preparation of mapping specification documents for both Callidus Commissions inbounds and outbounds.
\n•	Build Oracle Procedures/Packages, shell scripts for specific data integration/migration requirements.
\n•	Resolve issues related to pipeline jobs.
\n•	Build and test workflow screens for onboarding of agents

"""
)

st.write(""" _______________________________________________________________________________________________________________________________________""")

# --- JOB 4
st.write(":checkered_flag:", """**Xactly Express Consultant @ Open Symmetry**""")
st.write("March 2014 - October 2014")
st.write(
    """
**_Technologies_**: Xactly Express""")
st.write("""
**Roles & Responsibilities :** 
\n•	Building compensation plans for payees in the Xactly express system.
\n•	Data Mapping between Salesforce and Xactly Express.

"""
)

st.write(""" _______________________________________________________________________________________________________________________________________""")

# --- JOB 5
st.write(":checkered_flag:", """**Senior Software Engineer @ Accenture**""")
st.write("April 2010 – March 2014")
st.write(
    """
**_Technologies_**: SAP Commissions, SAP Workflow, Oracle PL SQL, Shell Scripting""")
st.write("""
**Roles & Responsibilities:** """)
st.markdown("- :point_right:Truecomp Rule Writing")
st.markdown("- :point_right:Resolving Truecomp application and pipeline job related issues")
st.markdown("- :point_right:Production Sev1 & Sev2 incidents") 


# st.write("The following list won’t indent no matter what I try:")
# st.markdown("Item 1")
# st.markdown("- Item 2")
# st.markdown("- Item 3")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: outside;
}
</style>
''', unsafe_allow_html=True)

# # --- JOB 2
# st.write('\n')
# st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
# st.write("01/2018 - 02/2022")
# st.write(
#     """
# - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
# - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
# - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
# """
# )

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Innovations and POCs")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
