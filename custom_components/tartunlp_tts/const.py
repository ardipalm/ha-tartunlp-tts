"""Constants for TartuNLP TTS."""

DOMAIN = "tartunlp_tts"
API_URL = "https://api.tartunlp.ai/text-to-speech/v2"

# Only these voices may be used by third-party integrations; the usage licence of
# the other voices in the API config has changed (TartuNLP, 2026-10).
VOICES: dict[str, list[str]] = {
    "et": ["mari", "albert", "vesta", "kalev", "meelis"],
}
