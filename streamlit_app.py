import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("It's over Anakin, I have the high ground")
streamlit.header("🥭 Your crush likes you back")
streamlit.text("and other hilarious jokes you can tell yourself")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick me:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
