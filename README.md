# GainSec-Local-AI-Stack
Notes, custom scripts, workflows, etc from doing AI research / prototyping a local stack.

## Get more explainations and details by visting the URLs below:
[GainSec](https://gainsec.com)
[Part 1](https://gainsec.com/2025/06/01/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-1/)
[Part 2](https://gainsec.com/2025/06/02/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-2-searxng/)
[Part 3](https://gainsec.com/2025/06/03/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-3-image-generation-via-stable-diffusion/)
[Part 4](https://gainsec.com/2025/06/04/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-4-transcription-via-whisper/)
[Part 5](https://gainsec.com/2025/06/07/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-5-open-webui-to-crawl4ai-local-files/)
[More Coming Soon](https://gainsec.com)

## Current Stack
So because I'm still using cole's docker-compose there's a bunch of stuff that isn't needed which I'll remove, clean and polish in Part 6 or 7. For now, if you visit the links above, you'll find the current configurations/docker-compose.yml and other tips, notes, etc.

So I'll only list what I'm actually utiilzing ATM and expect the docker-compose to be added to this repo sooner then later.

* Open-WebUI – Web interface for running and managing LLMs like Ollama.
* Ollama – Local LLM runner/manager for models like LLaMA, Mistral, etc.
* Whisper – OpenAI’s speech-to-text (audio transcription).
* N8N – Workflow automation tool, like open-source Zapier.
* Redis – In-memory key-value store, often used for caching.
* Postgres – Powerful open-source relational database.
* SearXNG – Privacy-respecting metasearch engine.
* Stable Diffusion – Text-to-image AI generator.
* Crawl4AI – Web crawler for building datasets for AI training.

## Files

Haven't put much up in this public repo yet, but here is what is currently available:

[OpenWebUI-UploadTo-WhisperServer-N8N-Workflow.json](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/OpenWebUI-UploadTo-WhisperServer-N8N-Workflow.json) || Allows you to integrate your own Whisper Server into OpenWebUI via N8N. Upload the mp3 to Open-WebUI, it causes a local file trigger in N8N which reads the MP3 file, sends to the whisper server, extracts the transcript from the response and writes it to a file. 
 
[crawl4ai-openwebui-function.py](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/crawl4ai-openwebui-function.py) || Open-WebUI Function that takes user input and sends it to N8N to be used by Crawl4AI 

[crawl4ai_outputfiles-final.json](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/crawl4ai_outputfiles.json) || Used along with the Open-WebUI Function, this takes the recieved input, transforms it into a useful format, sends it to crawl4AI API, and outputs a bunch of different files from Crawl4AI's response. It creates a raw output file, a URL list (uses a code node to extract ALL Urls), a Link list (grabs all Links from crawl4ai structured output), markdown file, HTML file and Screenshot of Website.

## Authors

* **Jon Gaines** - [GainSec](https://github.com/GainSec)

## Acknowledgments

* Cole Medin & the N8N-IO Team. Using Cole's docker-compose as a starting point. [Local-AI-Packaged](https://github.com/coleam00/local-ai-packaged)