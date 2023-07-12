import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

def showthis():
    # Title
    st.title("Exploring Streamlit Capabilities")

    if not st.checkbox(":green[Go 2 next feature]",key='1'):
        return


    # Header
    st.header("Text and Markdown")
    if not st.checkbox(":green[Go 2 next feature]",key='2'):
        return
    
    # Text
    st.text("This is a text widget.")
    if not st.checkbox(":green[Go 2 next feature]",key='3'):
        return
    

    # Markdown
    st.markdown("### This is a markdown widget.")
    if not st.checkbox(":green[Go 2 next feature]",key='4'):
        return
    

    # Displaying code
    st.code("""
import streamlit as st
st.title('Hello, Streamlit!')
            """)
    if not st.checkbox(":green[Go 2 next feature]",key='5'):
        return

    # Displaying data
    st.header("Displaying Data")
    if not st.checkbox(":green[Go 2 next feature]",key='6'):
        return

    # DataFrame
    data = pd.DataFrame({
        "Name": ["John", "Emily", "Josh"],
        "Age": [28, 35, 42],
        "City": ["New York", "London", "Sydney"]
    })

    st.dataframe(data)
    if not st.checkbox(":green[Go 2 next feature]",key='7'):
        return

    # Table
    st.table(data)

    if not st.checkbox(":green[Go 2 next feature]",key='8'):
        return
    # Plotting
    st.header("Plotting")

    # # Line chart
    # x = np.linspace(0, 10, 100)
    # y = np.sin(x)
    # plt.plot(x, y)
    # st.pyplot()

    # if not st.checkbox(":green[Go 2 next feature]",key='9'):
    #     return
    # # Bar chart
    # data = {
    #     "Category": ["A", "B", "C", "D"],
    #     "Values": [10, 15, 7, 12]
    # }
    # df = pd.DataFrame(data)
    # st.bar_chart(df.set_index("Category"))

    # if not st.checkbox(":green[Go 2 next feature]",key='10'):
    #     return
    # # Interactive widgets
    st.header("Interactive Widgets")

    # Slider
    number = st.slider("Select a number", 0, 10, 5)
    st.write("You selected:", number)

    # Checkbox
    if st.checkbox("Show data"):
        st.dataframe(data)

    # Selectbox
    option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
    st.write("You selected:", option)

    if not st.checkbox(":green[Go 2 next feature]",key='11'):
        return
    # Button
    if st.button("Click me"):
        st.write("Button clicked!")

    if not st.checkbox(":green[Go 2 next feature]",key='12'):
        return
    # Sidebar
    st.sidebar.header("Sidebar")
    st.sidebar.text("This is the sidebar.")

    if not st.checkbox(":green[Go 2 next feature]",key='13'):
        return
    # File uploader
    st.header("File Uploader")
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file is not None:
        st.write("File uploaded successfully.")

    if not st.checkbox(":green[Go 2 next feature]",key='14'):
        return
    # Progress bar
    st.header("Progress Bar")
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

    if not st.checkbox(":green[Go 2 next feature]",key='15'):
        return
    # Help and documentation
    st.header("Help and Documentation")
    st.help(pd.DataFrame)
    st.markdown("[Streamlit Documentation](https://docs.streamlit.io)")

showthis()