import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Set the title of the app
    st.title("Simple Streamlit App with Graphs")

    # Generate sample data
    data = pd.DataFrame({
        'X': np.arange(10),
        'Y': np.random.randint(1, 10, size=(10,))
    })

    # Display the sample data
    st.write("Sample Data:")
    st.write(data)

    # Create a line chart
    st.line_chart(data.set_index('X'))

    # Create a bar chart
    st.bar_chart(data.set_index('X'))

# Run the app
if __name__ == "__main__":
    main()
