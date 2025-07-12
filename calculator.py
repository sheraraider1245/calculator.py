import streamlit as st

def calculator_with_buttons():
    st.set_page_config(layout="centered") # Or "wide" for more space
    st.title("Streamlit Calculator with Buttons")

    # --- Initialize session state ---
    if 'expression' not in st.session_state:
        st.session_state.expression = ""
    if 'result' not in st.session_state:
        st.session_state.result = None
    if 'last_button' not in st.session_state:
        st.session_state.last_button = None # To help with preventing multiple operators

    # --- Display Area ---
    # Use a text input for display, making it read-only
    display_value = st.session_state.expression
    if st.session_state.result is not None:
        display_value = str(st.session_state.result) # Show result if available

    st.text_input("Calculator Display", value=display_value, disabled=True, key="display")


    # --- Button Logic ---
    def handle_button(char):
        current_expr = st.session_state.expression
        last_btn = st.session_state.last_button

        if char.isdigit() or char == '.':
            # If a result was just shown, clear expression for new number
            if st.session_state.result is not None:
                st.session_state.expression = char
                st.session_state.result = None # Clear result
            else:
                st.session_state.expression += char
        elif char in ['+', '-', '*', '/']:
            # Prevent adding multiple operators consecutively, unless it's a negative sign at the start
            if not current_expr and char == '-': # Allow leading negative
                st.session_state.expression += char
            elif current_expr and last_btn not in ['+', '-', '*', '/']:
                st.session_state.expression += char
            elif current_expr and current_expr[-1] in ['+', '-', '*', '/'] and char != current_expr[-1]:
                 # Replace last operator if a different one is pressed
                st.session_state.expression = current_expr[:-1] + char

        st.session_state.last_button = char

    def calculate_result():
        try:
            # Evaluate the expression string
            # IMPORTANT: For a real-world production app, avoid using eval() directly with untrusted input
            # due to security risks. For a simple calculator, it's generally fine.
            st.session_state.result = eval(st.session_state.expression)
            st.session_state.expression = str(st.session_state.result) # Keep result for further operations
        except Exception as e:
            st.error(f"Error: Invalid expression! {e}")
            st.session_state.result = None
            st.session_state.expression = "" # Clear on error

    def clear_all():
        st.session_state.expression = ""
        st.session_state.result = None
        st.session_state.last_button = None

    # --- Button Layout ---
    # Create columns for a grid layout
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button("7", on_click=handle_button, args=("7",), use_container_width=True)
        st.button("4", on_click=handle_button, args=("4",), use_container_width=True)
        st.button("1", on_click=handle_button, args=("1",), use_container_width=True)
        st.button("0", on_click=handle_button, args=("0",), use_container_width=True)
    with col2:
        st.button("8", on_click=handle_button, args=("8",), use_container_width=True)
        st.button("5", on_click=handle_button, args=("5",), use_container_width=True)
        st.button("2", on_click=handle_button, args=("2",), use_container_width=True)
        st.button(".", on_click=handle_button, args=(".",), use_container_width=True)
    with col3:
        st.button("9", on_click=handle_button, args=("9",), use_container_width=True)
        st.button("6", on_click=handle_button, args=("6",), use_container_width=True)
        st.button("3", on_click=handle_button, args=("3",), use_container_width=True)
        st.button("=", on_click=calculate_result, use_container_width=True)
    with col4:
        st.button("/", on_click=handle_button, args=("/",), use_container_width=True)
        st.button("*", on_click=handle_button, args=("*",), use_container_width= True)
        st.button("-", on_click=handle_button, args=("-",), use_container_width= True)
        st.button("+", on_click=handle_button, args=("+",), use_container_width= True)

    # Clear button spanning all columns
    st.button("C", on_click=clear_all, use_container_width=True)


if __name__ == "__main__":
    calculator_with_buttons()