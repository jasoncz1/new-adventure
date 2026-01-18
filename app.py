import streamlit as st
import pandas as pd

st.title("Customer record explorer")

uploaded_file = st.file_uploader("upload your customers.csv", type="csv")

if uploaded_file is not None:
    #1.load the csv into Pandas
    df = pd.read_csv(uploaded_file)

    #2. conversion:  turn the table into a list of dicts
    # 'records' tells pandas to make each row a dict
    customer_list = df.to_dict('records')

    #3. use the list of dicts to create a ui
    # let's create a "profile card" for each customer using a loop
    st.subheader("Customer Profiles")

    for person in customer_list:
        #each person is now a dictionary.  
        #we access data using keys person['keyname]
        with st.expander(f"profile: {person['Customer Name']}"):
            st.write(f"**ID:** {person['Customer ID']}")
            st.write(f"**birthday:** {person['Birthday']}")
            #architect bonus:  adding a button
            if st.button(f"email {person['Customer Name']}", key=person['Customer ID']):
                st.write(f"sending email to {person['Customer Name']}...")

else:
    st.info("Awaiting csv upload...")