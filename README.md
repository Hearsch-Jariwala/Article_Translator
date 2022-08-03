[![Python application test with Github Actions](https://github.com/Hearsch-Jariwala/Article_Translator/actions/workflows/main.yml/badge.svg)](https://github.com/Hearsch-Jariwala/Article_Translator/actions/workflows/main.yml)

# Article Translator

CLI tool that uses a pre-trained model to generate summary for an article in english then translate to spanish. 
We will use the open source Hugging Face library to load and use a transformer model.

[Huggingface Reference](https://huggingface.co/Helsinki-NLP/opus-mt-en-es)
## Overview

 1. Retrieve article website to summarize
 2. Load the model from huggingface 
 3. Generate article summary 
 4. Return the translation

## Usage

```
python3 main.py --url "https://en.wikipedia.org/wiki/Artificial_intelligence"
```


Example output
```
Translation in Spanish: 
La inteligencia artificial (AI) es la inteligencia demostrada por las máquinas, en oposición a la inteligencia natural mostrada por los animales, incluidos los humanos.La investigación de IA se ha definido como el campo de estudio de los agentes inteligentes, que se refiere a cualquier sistema que percibe su entorno y realiza acciones que maximicen sus posibilidades de alcanzar sus objetivos[a] El término "inteligencia artificial" había sido usado previamente para describir máquinas que imitan y muestran habilidades cognitivas "humanas" que están asociadas con la mente humana, tales como "aprendizaje" y "solución de problemas"Esta definición ha sido rechazada desde entonces por los principales investigadores de IA que ahora describen IA en términos de racionalidad y actuación racional, lo que no limita cómo la inteligencia puede articularse[b] Las aplicaciones de IA incluyen motores avanzados de búsqueda web (e)g, Google), sistemas de recomendación (utilizados por YouTube, Amazon y Netflix), comprensión del habla humana (como Siri y Alexa), coches autoconductores (eg, Tesla), la toma de decisiones automatizada y la competencia al más alto nivel en los sistemas de juego estratégico (como el ajedrez y Go)[2] A medida que las máquinas se vuelven cada vez más capaces, las tareas que se consideran que requieren "inteligencia" a menudo se eliminan de la definición de IA, un fenómeno conocido como el efecto IA[3] Por ejemplo, el reconocimiento óptico de caracteres se excluye con frecuencia de lo que se considera IA,[4] habiéndose convertido en una tecnología de rutina[5] La inteligencia artificial fue fundada como una disciplina académica en 1956, y en los años posteriores ha experimentado varias oleadas de optimismo,[6][7] seguido por la decepción y la pérdida de financiación (conocida como un "invierno de AI"),[8][9] seguido por nuevos enfoques, éxito y financiación renovada.
```

## Development 

Creating virtual environment:

 1. `python3 -m venv venv`
 2. `source venv/bin/activate`(MacOS)
 3. `source venv/Scripts/activate`(Windows)

Contributing guidelines:

Run `make all` before pushing code.
