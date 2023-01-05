import streamlit as st
import functions

todos = functions.get_todo_list()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todo_list(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.text("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox: # same as saying if it is True
        todos.pop(index)
        functions.write_todo_list(todos) # delete it from the .txt file
        del st.session_state[todo] # delete it from session state
        st.experimental_rerun() #needed for checkboxes, can also use st.rerun

st.text_input(label="", placeholder="Add a new todo",
              on_change=add_todo, key="new_todo")

st.session_state