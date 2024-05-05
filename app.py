# ---
# lambda-test: false
# ---
# ## Demo Streamlit application.
#
# This application is the example from https://docs.streamlit.io/library/get-started/create-an-app.
#
# Streamlit is designed to run its apps as Python scripts, not functions, so we separate the Streamlit
# code into this module, away from the Modal application code.


def main():
    import numpy as np
    import pandas as pd
    import streamlit as st

    st.title("Storyturner")
    st.write('Turn Any Concept into Stories for Your Kids')

    # Some number in the range 0-23
    age_to_filter = st.slider("hour", 0, 23, 17)
    #filtered_data = data[data[DATE_COLUMN].dt.hour == age_to_filter]


if __name__ == "__main__":
    main()