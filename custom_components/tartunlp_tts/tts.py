"""TartuNLP Neurokõne TTS entity."""

from __future__ import annotations

from typing import Any

import aiohttp

from homeassistant.components.tts import (
    ATTR_VOICE,
    TextToSpeechEntity,
    TtsAudioType,
    Voice,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import API_URL, VOICES

ATTR_SPEED = "speed"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the TTS entity."""
    async_add_entities([TartuNLPTTSEntity(hass, entry)])


class TartuNLPTTSEntity(TextToSpeechEntity):
    """Speaks Estonian (and Võro) via the TartuNLP public API."""

    _attr_name = "TartuNLP Neurokõne"
    _attr_supported_languages = list(VOICES)
    _attr_default_language = "et"
    _attr_supported_options = [ATTR_VOICE, ATTR_SPEED]

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self._session = async_get_clientsession(hass)
        self._attr_unique_id = entry.entry_id

    @callback
    def async_get_supported_voices(self, language: str) -> list[Voice] | None:
        return [Voice(v, v.capitalize()) for v in VOICES.get(language, [])]

    async def async_get_tts_audio(
        self, message: str, language: str, options: dict[str, Any]
    ) -> TtsAudioType:
        voices = VOICES.get(language, VOICES["et"])
        voice = options.get(ATTR_VOICE)
        if voice not in voices:
            voice = voices[0]
        speed = min(max(float(options.get(ATTR_SPEED, 1)), 0.5), 2.0)

        try:
            async with self._session.post(
                API_URL,
                json={"text": message, "speaker": voice, "speed": speed},
                timeout=aiohttp.ClientTimeout(total=30),
            ) as resp:
                if resp.status != 200:
                    raise HomeAssistantError(
                        f"TartuNLP returned {resp.status}: {await resp.text()}"
                    )
                return "wav", await resp.read()
        except (aiohttp.ClientError, TimeoutError) as err:
            raise HomeAssistantError(f"TartuNLP request failed: {err}") from err
