import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names=["Nimish Pandey","Mehul Upase","Shreyash Dhanawade"]
usernames=["npandey","mupase","sdhanawade"]
passwords=["123","456","789"]
hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)