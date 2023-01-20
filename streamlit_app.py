import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title("It's over Anakin, I have the high ground")
streamlit.header("🥭 Your crush likes you back")
streamlit.text("and other hilarious jokes you can tell yourself")

streamlit.dataframe(my_fruit_list)
