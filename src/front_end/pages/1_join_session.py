import streamlit as st
import uuid


def is_session_id_null():
    try:
        st.session_state.session_id
    except AttributeError:
        return True
    return st.session_state.session_id is None or \
           st.session_state.session_id == ""


def join_session(session_id):
    if is_session_id_null():
        message = f"You're already in a session: {st.session_state.session_id}"
    else:
        st.session_state.session_id = session_id
        message = f"You've joined the session {st.session_state.session_id}"

    st.write(message)


def generate_session_id(st_obj):
    if is_session_id_null():
        st.session_state.session_id = uuid.uuid4()

    st_obj.write(f"Your session id is {st.session_state.session_id}")


if __name__ == '__main__':

    # initialize session_id variable
    if 'session_id' not in st.session_state:
        st.session_state['session_id'] = None

    st.set_page_config(layout="wide")

    st.title('Create or Join a Game')

    left_column, right_column = st.columns(2)


    left_column.header("Invite friends to your session")

    session_id_button = left_column.button(
        "Generate new session id",
        on_click=generate_session_id(left_column),
    )

    right_column.header("Join a session")

    user_added_session_id = right_column.text_input(
        "Enter the session id you'd like to join",
    )
    button = right_column.button(
        "Join session",
        on_click=join_session(user_added_session_id),
    )
