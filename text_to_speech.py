import azure.cognitiveservices.speech as ssdk
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SPEECH_KEY")
service_region = "eastus"


def tts(content):
    speech_config = ssdk.SpeechConfig(subscription=API_KEY, region=service_region)

    speech_config.speech_synthesis_voice_name = "en-US-AdamMultilingualNeural"

    # Set the format to MP3
    audio_output_config = ssdk.audio.AudioOutputConfig(filename="output.mp3")

    text = content

    # use the default speaker as audio output.
    speech_synthesizer = ssdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)

    result = speech_synthesizer.speak_text_async(text).get()
    # Check result
    if result.reason == ssdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized".format(text))
        return True
    elif result.reason == ssdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == ssdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

        return False
