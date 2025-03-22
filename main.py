import streamlit as st
import json 

#load & save library data

def load_library():
    try:
        with open("library.json","r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
def save_library():
    with open ("library.json","w") as file:
        json.dump(library, file, indent = 4)

#initialize library
library = load_library()

st.title("📚 Personal Library Management System")
menu =st.sidebar.radio("Select an option", ["View Library", "Add Books", "Remove Book", "Search Book", "Save & Exit"])
if menu == "View Library":
    st.sidebar.title("Your Library")
    if library:
        st.table(library)
    else:
        st.write("No book selected. Add some books")

# add books

elif menu == "Add Books":
    st.sidebar.title("➕ Add a new book.")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value = 1997, max_value=2200, step = 1 )
    genre = st.text_input("Genre")
    read_status = st.checkbox ("Mark as Read")

    if st.button("➕ Add Book"):
        library.append({
            "title": title, 
            "author":author, 
            "year": year, 
            "genre": genre, 
            "read_status": read_status
            })
        save_library()
        st.success("✅ Book added successfully.")
        st.rerun()

#remove book

elif menu == "Remove Book":
    st.sidebar.title("➖ Remove a book")
    book_titles = [book ["title"] for book in library]

    if book_titles: 
        selected_book =st.selectbox ("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            library[:] = [book for book in library if book ["title"] != selected_book]
            save_library()
            st.success("✅ Book removed successfully.")
            st.rerun()
        else:
            st.warning("⚠ No book is present in library.")

#search book
elif menu == "Search Book":
    st.sidebar.title ("🔍 Search a book")
    search_term = st.text_input("Enter title or author name")
    if st.button("🔍 Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book ["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("⚠ No book is found!")

#save & exit
elif menu == "Save & Exit":
    save_library()
    st.success("✅ Library saved successfully.")



