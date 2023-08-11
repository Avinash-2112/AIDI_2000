# Import necessary modules from the Flask framework.
from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)  # Create an instance of Flask application.

# Define pre-trained model names for translation between different languages.
model_name_en_de = "Helsinki-NLP/opus-mt-en-de"  # English to German
model_name_en_fr = "Helsinki-NLP/opus-mt-en-fr"  # English to French
model_name_en_es = "Helsinki-NLP/opus-mt-en-es"  # English to Spanish

# Load pre-trained models for English-German, English-French, and English-Spanish translations.
model_de = MarianMTModel.from_pretrained(model_name_en_de)
tokenizer_de = MarianTokenizer.from_pretrained(model_name_en_de)

model_fr = MarianMTModel.from_pretrained(model_name_en_fr)
tokenizer_fr = MarianTokenizer.from_pretrained(model_name_en_fr)

model_es = MarianMTModel.from_pretrained(model_name_en_es)
tokenizer_es = MarianTokenizer.from_pretrained(model_name_en_es)


@app.route('/translate', methods=['POST'])  # Define a route for POST requests at "/translate".
def translate_text():
    data = request.get_json()  # Get JSON data from the request.
    input_text = data['input_text']  # Extract input text from the JSON data.
    target_language = data['target_language']  # Extract target language from the JSON data.

    # Select the appropriate translation model based on the target language.
    if target_language == "German":
        model = model_de  # Set the translation model to English-German model.
        tokenizer = tokenizer_de  # Set the tokenizer to English-German tokenizer.
    elif target_language == "French":
        model = model_fr  # Set the translation model to English-French model.
        tokenizer = tokenizer_fr  # Set the tokenizer to English-French tokenizer.
    elif target_language == "Spanish":
        model = model_es  # Set the translation model to English-Spanish model.
        tokenizer = tokenizer_es  # Set the tokenizer to English-Spanish tokenizer.
    else:  # If the target language is not supported, return an error message.
        return jsonify({'translated_text': "Translation to this language is not supported."})

    input_ids = tokenizer.encode(input_text, return_tensors="pt")  # Tokenize the input text.
    translation = model.generate(input_ids)  # Generate the translation.
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)  # Decode the translated tokens.

    return jsonify({'translated_text': translated_text})  # Return the translated text in JSON format.


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app when the script is executed directly.
