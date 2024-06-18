#Thomas Phuti Mpherwane                     #10-April-2024

#This function let user to have an option to either delete,modify or add new movie
import streamlit as st

def main():
    
    st.set_page_config(layout='centered', page_title='Alpha Movies', page_icon='🎬')
    st.markdown("<h1 style='text-align: center; color: red; font-size: 32px;'>🎬 Alpha Movies</h1>", unsafe_allow_html=True)
    #st.title("Alpha Movies - Modification page")
    st.title("Manage Inventories")

    st.write("This page allow user to manage movies available in the store")
    option = st.selectbox("Select an option:", ("Delete Movie", "Add New Movie", "Update Movie Details"))

    if option == "Delete Movie":
        st.write("You have selected the delete movie option, please confirm: ")
        st.page_link("pages/delete_movie.py", label = "Delete Movie")
    elif option == "Add New Movie":
        st.write("You have selected the add new movie option, please confirm: ")
        st.page_link("pages/add_movie.py", label = "Add a movie")
        # Add your code to add a new movie here
    elif option == "Update Movie Details":
        st.write (" You have selected update movie details, please confirm: ")
        st.page_link("pages/update_movie.py", label = "Add a movie")
        #Add Code here

if __name__ == "__main__":
    main()
