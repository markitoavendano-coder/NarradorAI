\# NarradorAI



Open-source Python toolkit for building automated narrated video production workflows.



NarradorAI is an early-stage project focused on simplifying the technical steps involved in turning scripts into narration-ready content.



The long-term goal is to create a modular toolkit that can be integrated into larger content-production and automation workflows.



\## Current Features



\### TTS-safe text splitting



NarradorAI can split long scripts into smaller segments suitable for text-to-speech processing.



The splitter:



\* preserves complete sentences whenever possible;

\* respects a configurable maximum segment length;

\* normalizes unnecessary whitespace;

\* handles sentences that exceed the maximum length;

\* validates invalid segment limits.



Example:



```python

from engine.splitter import split\_text



text = (

&#x20;   "Esta es la primera frase. "

&#x20;   "Esta es la segunda frase. "

&#x20;   "Esta es una tercera frase más larga."

)



segments = split\_text(text, max\_chars=60)



for segment in segments:

&#x20;   print(segment)

```



\## Automated Tests



The text-splitting engine includes automated tests covering:



\* empty input;

\* short texts;

\* multi-segment texts;

\* maximum character limits;

\* unusually long sentences;

\* invalid configuration values.



Run the test suite with:



```bash

python -m unittest discover -s tests -v

```



\## Project Structure



```text

NarradorAI/

├── engine/

│   ├── \_\_init\_\_.py

│   ├── merger.py

│   ├── splitter.py

│   └── tts.py

├── tests/

│   └── test\_splitter.py

├── .gitignore

├── config.py

├── main.py

├── README.md

└── requirements.txt

```



\## Roadmap



Planned development includes:



\* text-to-speech generation;

\* support for multiple narrator voices;

\* long-script processing;

\* audio segment merging;

\* audio normalization;

\* synchronized subtitle generation;

\* automatic project file organization;

\* multimedia workflow integrations;

\* n8n automation support;

\* preparation of narrated content for different platforms.



\## Project Philosophy



NarradorAI is being developed incrementally.



Each module should be independently testable and useful before additional automation layers are added. The goal is to build a reliable foundation instead of creating a large system that is difficult to maintain.



\## Status



Early development.



The text-splitting engine is functional and covered by automated tests. Additional modules are under development.



\## Contributing



NarradorAI is an open-source project and contributions, suggestions, bug reports, and ideas are welcome.



More contribution guidelines will be added as the project develops.



