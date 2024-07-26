from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import openpyxl

voters_set = set('/home/vathsalya/voting_results.xlsx')

def vote_cast():
    selected_candidate_name = candidate_combobox.get()
    voting_results_file = "voting_results.xlsx"  

    if selected_candidate_name == "Select Candidate" or voting_results_file in voters_set:
        messagebox.showinfo("Error", "your are already submitted the vote.")
    else:
        messagebox.showinfo("Vote Cast", f"You voted for {selected_candidate_name}!")
        save_to_excel(selected_candidate_name, voting_results_file)
        voters_set.add(voting_results_file)

def save_to_excel(candidate_name, file_path):
    try:
        wb = openpyxl.load_workbook(file_path)
    except FileNotFoundError:
        wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append([candidate_name])
    wb.save(file_path)
root = Tk()
root.title("Voting System")
root.geometry("400x300")
root.configure(bg="#3D59AB")
candidates = ["Select Candidate", "Candidate 1", "Candidate 2", "Candidate 3"]
candidate_combobox = Combobox(root, values=candidates,width=20)
candidate_combobox.set("Select Candidate")
candidate_combobox.pack(pady=100)
vote_button = Button(root, text="Vote Cast", command=vote_cast,width=10)
vote_button.pack(pady=20)
root.mainloop()
