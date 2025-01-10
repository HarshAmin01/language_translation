from transformers import MarianMTModel, MarianTokenizer

# List of supported languages
SUPPORTED_LANGUAGES = {
    "en": "English",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "ru": "Russian",
    "ja": "Japanese",
    "zh": "Chinese"
}

def get_language_code(input_language):
    """
    Retrieve the language code from the language name.
    Args:
        input_language (str): The name or code of the language.
    Returns:
        str or None: The language code if found, otherwise None.
    """
    input_language = input_language.strip().lower()
    for code, name in SUPPORTED_LANGUAGES.items():
        if input_language == code.lower() or input_language == name.lower():
            return code
    return None

def initialize_model(source_lang, target_lang):
    """
    Initialize the MarianMT model and tokenizer for a given language pair.
    Args:
        source_lang (str): Source language code.
        target_lang (str): Target language code.
    Returns:
        tuple: Model and tokenizer.
    """
    model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

def translate_text(text, source_lang, target_lang):
    """
    Translate a given text using MarianMT.
    Args:
        text (str): The text to translate.
        source_lang (str): Source language code.
        target_lang (str): Target language code.
    Returns:
        str: The translated text.
    """
    model, tokenizer = initialize_model(source_lang, target_lang)
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
