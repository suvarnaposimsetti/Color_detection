import streamlit as st
import pandas as pd
import subprocess

def save_to_excel(df, file_name="results.xlsx"):
    df.to_excel(file_name, index=False)

def run_another_script():
    script_path = "/home/rguktongole/ss4.py"
    subprocess.run(["python3", script_path])

def main():
    st.sidebar.title('HOME')
    app_mode = st.sidebar.selectbox('', ['ABOUT', 'CANDIDATE DETAILS', 'RESULTS', 'SUBMITTED IDS']) 
    
    if app_mode == 'ABOUT':
        st.markdown('')
        st.image("/opt/lampp/htdocs/wtlab/project/candi.png", caption="")
        st.markdown(
            'In this application students can cast their votes using face recognition. The voting system currently being used is a Paper Based System, in which the voter simply picks up ballots sheets from electoral officials, ticks off who they would like to vote for, and then casts their votes. The electoral officials gather all the votes being cast into a Ballot Box. At the end of the elections, the electoral officials count the votes for each candidate and determine the winner of each election category. The objective of replacing the Traditional system with the Online Voting System Using Face Recognition is this smart system reduces the time for voting and also the system is reliable, faster and Students can cast their votes from virtually anywhere, whether it be the lecture hall, library, or their dorm room. In this, the voter uses their College Id to log in to the voting portal here voter cast their vote by using facial recognition when the face is matched with the Database containing Candidate Facial Information. It simplifies the voting process and makes it more accessible to everyone who is Eligible To Vote and ensuring that each student casts only one vote and their identity is secured.')
        st.markdown(
            """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 350px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 350px;
            margin-left: -350px;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )

        allowed_ids = ["1055", "1062", "1053", "1065", "1004","1042","1054","1049","1009","1044","1009","1024"]

        try:
            df = pd.read_excel("student_data.xlsx")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Name", "Student ID"])

        st.title("LOGIN")
        name = st.text_input("Enter your name:")
        student_id = st.text_input("Enter your student ID:")

        if student_id not in allowed_ids:
            st.error("Please enter a valid ID.")
        elif df["Student ID"].isin([student_id]).any():
            st.error("This ID has already been submitted.")
        elif st.button("Submit"):
            df = df.append({"Name": name, "Student ID": student_id}, ignore_index=True)

            df.to_excel("student_data.xlsx", index=False)
            st.success("Form submitted successfully!")
            run_another_script()

    elif app_mode == 'CANDIDATE DETAILS':
        st.markdown('## Candidate Details')

        
        st.markdown('### Candidate 1')
        st.image("/home/rguktongole/Pictures/p4.png", caption="TL")
        st.markdown("candidate1")

        
        st.markdown('### Candidate 2')
        st.image("/home/rguktongole/Pictures/p2.png", caption="seetha")
        st.markdown("###candidate2")

        
        st.markdown('### Candidate 3')
        st.image("/home/rguktongole/Pictures/p3.png", caption="geetha")
        st.markdown("candidate3")

    elif app_mode == 'RESULTS':
        try:
            existing_df = pd.read_excel("voting_results.xlsx")
            st.markdown('## RESULTS')
            st.dataframe(existing_df)
        except FileNotFoundError:
            st.warning("No existing results file found.")

    elif app_mode == 'SUBMITTED IDS':  
        try:
            df = pd.read_excel("student_data.xlsx")
            st.markdown('## SUBMITTED IDS')
            st.dataframe(df)
        except FileNotFoundError:
            st.warning("No submitted IDs found.")

if __name__ == "__main__":
    main()

