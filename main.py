from translator import SUPPORTED_LANGUAGES, get_language_code, translate_text

def main():
    while True:
        print("\nSupported Languages:")
        for code, name in SUPPORTED_LANGUAGES.items():
            print(f"{code}: {name}")

        # Get source and target languages
        source_lang_name = input("\nEnter source language (e.g., 'English'): ").strip()
        target_lang_name = input("Enter target language (e.g., 'French'): ").strip()

        source_lang = get_language_code(source_lang_name)
        target_lang = get_language_code(target_lang_name)

        if source_lang is None or target_lang is None:
            print("\nInvalid language input. Please try again.")
            continue

        # Translate text
        user_text = input(f"\nEnter text to translate from {SUPPORTED_LANGUAGES[source_lang]} to {SUPPORTED_LANGUAGES[target_lang]}: ").strip()
        try:
            translated_text = translate_text(user_text, source_lang, target_lang)
            print(f"\nTranslated Text: {translated_text}\n")
        except Exception as e:
            print(f"\nError: {e}\n")

        # Save translation option
        save_option = input("Do you want to save this translation? (yes/no): ").strip().lower()
        if save_option in ['yes', 'y']:
            with open("translations.txt", "a", encoding="utf-8") as file:
                file.write(f"Source: {user_text}\n")
                file.write(f"Translated: {translated_text}\n\n")
            print("Translation saved to 'translations.txt'.")

        # Exit option
        exit_option = input("Do you want to translate another text? (yes/no): ").strip().lower()
        if exit_option not in ['yes', 'y']:
            print("\nThank you for using the translator! Goodbye!")
            break

if __name__ == "__main__":
    main()
