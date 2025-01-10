# Language Translation Tool
## Overview
- The Language Translation Tool is a versatile and user-friendly application for translating text between multiple languages. Built using the Hugging Face MarianMT model, it leverages state-of-the-art machine translation technology to support both individual and batch translations. Whether you're translating casual text, business documents, or technical instructions, this tool provides an interactive, efficient, and accurate solution for all your translation needs.

## Features
- Multi-Language Support: Translate text between 10+ languages.
- Interactive CLI: Provides a simple, interactive command-line interface for easy usage.
- Translation Save Feature: Option to save translations to a file for later reference.
- Customizable Language Pairs: Expandable to support additional languages from the MarianMT library.
- Error Handling: Handles invalid inputs gracefully and provides user-friendly error messages.
- Future Ready: Designed for easy integration with web applications or GUIs.
  
### Supported Languages
- The tool currently supports the following languages, identified by their codes:

Language Name	Code
- English	en
- French	fr
- German	de
- Spanish	es
- Italian	it
- Portuguese	pt
- Dutch	nl
- Russian	ru
- Japanese	ja
- Chinese	zh

## Installation
#### Follow these steps to set up the project locally:

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps
1. Clone the Repository:
- git clone https://github.com/yourusername/language_translation.git
- cd language_translation

  
2. Create a Virtual Environment (Optional):
- python -m venv venv
- source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install Dependencies:
- pip install -r requirements.txt

4. Run the Application:
- python main.py
- Choose the source and target languages by entering either the language name (e.g., "English") or the code (e.g., "en").
- Enter the text you want to translate.
- View the translated output.
- Save the translation if desired by following the prompts.
- Saving Translations: Translations can be saved to a file named translations.txt.
  

## Future Enhancements
- Batch Translation:
  Translate multiple sentences or paragraphs at once.
  Accept input from a text file and output results to another file.
- Language Detection:
  Automatically detect the source language to eliminate manual input.
- Web-Based Interface:
  Build a simple web app using Flask or Django for a more interactive user experience.
- Support for Rare Languages:
  Expand the list of supported languages using the MarianMT model library.
- Speech-to-Text Translation:
  Integrate speech recognition to allow voice-based translations.
- Custom Model Training:
  Fine-tune models on specific datasets for domain-specific translations.
