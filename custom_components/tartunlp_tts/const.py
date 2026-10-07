"""Constants for TartuNLP TTS."""

DOMAIN = "tartunlp_tts"
API_URL = "https://api.tartunlp.ai/text-to-speech/v2"

# From GET https://api.tartunlp.ai/text-to-speech/v2 (2026-10-07)
VOICES: dict[str, list[str]] = {
    "et": [
        "mari",
        "albert",
        "indrek",
        "kalev",
        "kylli",
        "lee",
        "liivika",
        "luukas",
        "meelis",
        "peeter",
        "tambet",
        "vesta",
    ],
    "vro": ["sulev", "hella"],
}
