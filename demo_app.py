import streamlit as st
from DataLoader import DataLoader
from LogisticRegressor import LogisticRegressor

# To run the APP: streamlit run streamlit_app.py
if __name__ == '__main__':
    st.header('Logistic Regression')
    st.markdown('*Author: Leonardo Simões*')

    # Data Loader
    st.header('Data loader')
    dataLoader = DataLoader()
    dataLoader.check_labels()
    dataLoader.check_separator()
    file = dataLoader.load_file()

    if file is not None:
        df = dataLoader.load_data(file)

        # Logistic Regression
        st.header('Logistic Regression')
        regressor = LogisticRegressor(df)
        regressor.logistic()
        st.markdown('<hr/>', unsafe_allow_html=True)