from translate import Translator


def bot_translate(from_l, to_l, message):
    translator = Translator(from_lang=from_l, to_lang=to_l)
    translate_message = translator.translate(message)
    return translate_message
