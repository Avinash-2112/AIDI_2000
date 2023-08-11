import streamlit as st
import requests
import json


# Define the main function that will run the Streamlit app.
def main():
    st.title("Language Translation Tool")  # Set the app title.
    input_text = st.text_area("Enter Text to Translate", "")  # Create a text area for user input.

    # Define a list of target languages for the dropdown.
    target_languages = ["German", "French", "Spanish"]

    # Add a dropdown menu to select the target language.
    target_language = st.selectbox("Select Target Language", target_languages)

    # Check if the "Translate" button is clicked.
    if st.button("Translate"):
        # Call the translate_text function and get the translated text.
        translated_text = translate_text(input_text, target_language)

        # Display a label and the translated text.
        st.text("Translated Text:")
        st.write(translated_text)


# Define a function to translate the input text using the backend API.
def translate_text(input_text, target_language):
    # Create a dictionary with input data for translation.
    data = {
        'input_text': input_text,
        'target_language': target_language
    }

    # Make a POST request to the translation API endpoint.
    response = requests.post('http://127.0.0.1:5000/translate', json=data)

    # Check if the response status code is 200 (OK) before decoding JSON.
    if response.status_code == 200:
        try:
            # Get the translated text from the JSON response.
            translated_text = response.json().get('translated_text')
            return translated_text
        except json.JSONDecodeError:
            return "Translation not available"
    else:
        return "Translation request failed"


# Run the main function when the script is executed directly.
if __name__ == "__main__":  # streamlit run frontend.py
    main()


