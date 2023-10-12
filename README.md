# DritteFeedback
Service to translate and give sentiment feedback with provided text for use in DritteBack

### Setup LibreTranslate
## With docker
- Have docker installed
- Clone [libretranslate](https://github.com/LibreTranslate/LibreTranslate)
- Run run.bat
## With python library
`pip install libretranslate`
`libretranslate --port 5003`

### Install libraries app
`pip install flask textblob libretranslate requests`

### Init app
`python app.py`
