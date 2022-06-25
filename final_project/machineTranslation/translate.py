"""
In this module, we create english_to_french, french_to_english functions.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey = apikey)
VERSION = '2022-05-02'
language_translator = LanguageTranslatorV3(version = VERSION, authenticator = authenticator)
language_translator.set_service_url(service_url = url)

def english_to_french(text):
    """
    This function converts english text in french text.
    """
    if(text == '' or text is None):
        return 'Please type something to convert.'
    tran = language_translator.translate(text = text, model_id='en-fr').get_result()
    tran = tran['translations']
    tran = tran[0]
    tran = tran['translation']
    return tran

def french_to_english(text):
    """
    This function create french text in english text.
    """
    if(text == '' or text is None):
        return 'Please type something to convert.'
    tran = language_translator.translate(text = text, model_id='fr-en').get_result()
    tran = tran['translations']
    tran = tran[0]
    tran = tran['translation']
    return tran
