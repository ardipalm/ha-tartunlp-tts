# TartuNLP Neurokõne TTS for Home Assistant

Estonian (and Võro) text-to-speech for Home Assistant, using the free public
[TartuNLP text-to-speech API](https://api.tartunlp.ai/text-to-speech/docs) by the
University of Tartu NLP research group.

Works as a regular TTS engine: pick it in an **Assist pipeline**, or use it with
`tts.speak` in automations.

> This is an unofficial community integration. It is not affiliated with or endorsed by
> the University of Tartu. Text you synthesise is sent to `api.tartunlp.ai`; see their
> [privacy terms](https://www.tartunlp.ai/andmekaitsetingimused). The API is a free public
> service with no uptime guarantee.

## Voices

| Language | Voices |
|---|---|
| Estonian (`et`) | mari (default), albert, indrek, kalev, kylli, lee, liivika, luukas, meelis, peeter, tambet, vesta |
| Võro (`vro`) | sulev, hella |

Options: `voice`, `speed` (0.5–2.0, default 1).

## Installation

### HACS (custom repository)

1. HACS → ⋮ → **Custom repositories** → add `https://github.com/ardipalm/ha-tartunlp-tts`, type **Integration**.
2. Install **TartuNLP Neurokõne TTS** and restart Home Assistant.

### Manual

Copy `custom_components/tartunlp_tts` into your `/config/custom_components/` folder and restart Home Assistant.

## Setup

1. Settings → Devices & services → **Add integration** → **TartuNLP Neurokõne**.
2. Settings → Voice assistants → your pipeline → **Text-to-speech**: choose *TartuNLP Neurokõne*, language Estonian, and a voice.

### Automation example

```yaml
action: tts.speak
target:
  entity_id: tts.tartunlp_neurokone
data:
  media_player_entity_id: media_player.living_room
  message: "Tere! Välisuks on lahti."
  options:
    voice: mari
    speed: 1.1
```

---

## Eesti keeles

Eestikeelne kõnesüntees Home Assistantile Tartu Ülikooli tasuta TartuNLP API kaudu.
Paigalda HACS-i kaudu (custom repository) või kopeeri `custom_components/tartunlp_tts`
kausta `/config/custom_components/`, taaskäivita HA ja lisa integratsioon
**TartuNLP Neurokõne**. Hääle valid Assist pipeline'i seadetes.

Tegemist on mitteametliku integratsiooniga, mis ei ole Tartu Ülikooliga seotud.
Etteloetav tekst saadetakse aadressile `api.tartunlp.ai`.

## License

MIT
