# GainSec-Local-AI-Stack

* Current Version: 0.6

This is a work in progress as I continue to research, experiment and utilize AI impelementations. Everything runs locally, and can be used as individual services, via OpenWeb-UI or N8N.

### Here's some example of what you can do all within one chat thread:

<img src="https://gainsec.com/wp-content/uploads/2025/06/chat1.jpg" alt="Stable-Diffusion" width="600"/>
<img src="https://gainsec.com/wp-content/uploads/2025/06/chat2.jpg" alt="Web Search" width="600"/>
<img src="https://gainsec.com/wp-content/uploads/2025/06/chat3.jpg" alt="Whisper Transcriptions" width="600"/>
<img src="https://gainsec.com/wp-content/uploads/2025/06/chat4.jpg" alt="Crawl4AI Web Access" width="600"/>

### Local Agentic RAG Implementation:
<img src="https://gainsec.com/wp-content/uploads/2025/06/image-3.png" alt="RAG PDF OpenWeb-UI" width="600"/>
<img src="https://gainsec.com/wp-content/uploads/2025/06/post-rag.jpg" alt="RAG PDF N8N Workflow" width="600"/>

### Crawl4AI To Local File Output (Agentic RAG Implementation Coming Soon):
<img src="https://gainsec.com/wp-content/uploads/2025/06/crawl4ai-local-files.jpg" alt="Craw4AI Local File Output" width="600"/>
<img src="https://gainsec.com/wp-content/uploads/2025/06/image-10.png" alt="Craw4AI Local File N8N Workflow" width="600"/>

## Current Stack

* Open-WebUI – Web interface for running and managing LLMs like Ollama.
* Ollama – Local LLM runner/manager for models like LLaMA, Mistral, etc.
* Whisper – OpenAI’s speech/video file/audio file-to-text (audio transcription).
* N8N – Workflow automation tool, like open-source Zapier.
* Redis – In-memory key-value store, often used for caching.
* Postgres – Powerful open-source relational database.
* SearXNG – Privacy-respecting metasearch engine.
* Stable Diffusion – Text-to-image AI generator.
* Crawl4AI – Web crawler + requester

## Files

Haven't put much up in this public repo yet, but below is what I have currently available.

### N8N WorkFlows

[/GainSec-Local-AI-Stack/n8n-workflows/OpenWebUI-UploadTo-WhisperServer-N8N-Workflow.json](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/n8n-workflows/OpenWebUI-UploadTo-WhisperServer-N8N-Workflow.json) - Allows you to integrate your own Whisper Server into OpenWebUI via N8N. Upload the mp3 to Open-WebUI, it causes a local file trigger in N8N which reads the MP3 file, sends to the whisper server, extracts the transcript from the response and writes it to a file. 

[/GainSec-Local-AI-Stack/n8n-workflows/crawl4ai_outputfiles-final.json](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/n8n-workflows/crawl4ai_outputfiles.json) - Used along with the Open-WebUI Function, this takes the recieved input, transforms it into a useful format, sends it to crawl4AI API, and outputs a bunch of different files from Crawl4AI's response. It creates a raw output file, a URL list (uses a code node to extract ALL Urls), a Link list (grabs all Links from crawl4ai structured output), markdown file, HTML file and Screenshot of Website.

[/GainSec-Local-AI-Stack/n8n-workflows/V1_Local_RAG_AI_Agent.json] (https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/n8n-workflows/V1_Local_RAG_AI_Agent.json) - Local RAG AI Agent implementation from [Self-hosted AI Package](https://github.com/coleam00/local-ai-packaged)

[/GainSec-Local-AI-Stack/n8n-workflows/V3_Local_Agentic_RAG_AI_Agent.json] (https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/n8n-workflows/V3_Local_Agentic_RAG_AI_Agent.json) - Local RAG AI Agent implementation from [Self-hosted AI Package](https://github.com/coleam00/local-ai-packaged)


### Open-WebUI Functions/Pipes

[/GainSec-Local-AI-Stack/openweb-ui-functions/crawl4ai-openwebui-function.py](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/openweb-ui-functions/crawl4ai-openwebui-function.py) - Open-WebUI Function that takes user input and sends it to N8N to be used by Crawl4AI 

[/GainSec-Local-AI-Stack/openweb-ui-functions/n8npipe-local-agentic-rag.py](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/openweb-ui-functions/n8npipe-local-agentic-rag.py) - Open-WebUI Function that pipes into the RAG AI Agentic Implementations from [Self-hosted AI Package](https://github.com/coleam00/local-ai-packaged)

### Scripts

[/GainSec-Local-AI-Stack/setup_dirs.sh](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/setup_dirs.sh) - Script to create all the required directories and give them proper permissions

[/GainSec-Local-AI-Stack/example.env](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/example.env) - Example .env file that is used alongside the docker docker compose

[/GainSec-Local-AI-Stack/docker-compose.yml](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/docker-compose.yml) - The docker compose that is used to pull-up all the services

[/GainSec-Local-AI-Stack/start_services.py](https://github.com/GainSec/GainSec-Local-AI-Stack/blob/main/start_services.py) - Python script to properly spin up all the services + run some other checks

### Directories

`/GainSec-Local-AI-Stack/shared` - Where most data lives that is used across services or exported/output

`/GainSec-Local-AI-Stack/shared/crawl/` - Where the N8N crawl4ai workflow outputs files to along with some subdirectories: `html`, `image`, `links`, `markdown`, `pdf`, `urls` (the raw output is saved into `/shared/crawl/`)

`/GainSec-Local-AI-Stack/shared/transcripts` - Where the N8N Whisper workflow outputs transcriptions

`/GainSec-Local-AI-Stack/shared/uploads` - Where Open-WebUI stores uploads which are then grabbed by the N8N Whisper workflow

## Installation

1. Follow Ollama Instructions to use your GPU with docker: [Instructions](https://github.com/ollama/ollama/blob/main/docs/docker.md)

2. `cp example.env .env && nano .env` - Modify values as seen fit

3. `chmod +x setup_dirs.sh && ./setup_dirs.sh` - Create directories required by the services/volumes if they don't exist

4. `sudo python3 start_services.py --profile=gpu-nvidia` - For other profile options see ColeAm00's original script I modified [Other Profiles](https://github.com/coleam00/local-ai-packaged?tab=readme-ov-file#for-amd-gpu-users-on-linux)

5. Navigate to [N8N](http://localhost:5678), create a local account.

6. Now hit the `+` button on the top left, add at the least, these three credentials: `ollama account - Base Url: http://ollama:11434/`, `OpenAPI Account - Base URL: http://ollama:11434/v1` (API Key doesn't matter unless you set it to something), `Postgres account - Host: postgres, Database: postgres, User: postgres, Password: whatever you set in your .env`

7. Feel free to import the included workflows as well at this point.

8. Navigate to [Open-WebUI](http://localhost:3000), create a local account.

9. Click your username on the bottom left then select `Admin Panel`.

10. Select `Settings` then select `Connections`. Deactivate OpenAI API and activate Ollama API. Hit the `+` button and enter `http://ollama:11434` in URL. Toggle the switch on and hit the refresh button next to the toggle to confirm connection. Under Connections is Models, which should show your list of available models. If not, enter the ollama docker and download some. Hit Save.

11. Select `Tools` and hit the `+` button. Enter the URL as `http://crawl4ai:11235`, add a name of description of `crawl4ai`, turn on the toggle and hit the refresh button. (Make sure you leave the openapi.json default value there). Change visibility to Public. Hit Save.

12. Repeat the same process for Whisper. URL: `http://whisper-server:9000` and stable diffusion. URL: `http://sd-a1111:8080` Hit Save.

13. Now Select `Web Search`. Change the `Web Search Engine` value to `searxng` and the `Searxng Query URL` to `http://searxng:8080/search?q=<query>&format=json`. Turn the toggle on and hit save.

14. Select `Audio` and change the STT Model to `large` - Note this is separate then the Whisper-Server we're also running, as Open-WebUI has a built-in whisper server. If you end up not doing anything custom to your whisper service then feel free to just use this one rather then a whole separate service. Hit Save

15. Select `Images` Turn both toggles to on, and change the `Image Generation Engine` to `Automatic1111`. Note that the stable diffusion service atm takes the longest to spin up because it builds it each time. I will fix that in the future and will hopefully find better inference files so newer and better models can be used. Within `AUTOMATIC1111 Base URL` enter `http://sd-a1111:8080/` and hit the refresh to the right. At this time, you should see the default model as `v1-5-pruned-*`. Hit Save.

16. To the left of `Settings` select `Functions`. Hit the `+` button and paste the `n8npipe-local-agentic-rag.py` script into it. Name it `N8N-Pipe-Local-Agentic-Rag-Pipe` Give it any description and hit save. Now hit the gear next to it and enter the N8N Webhook URL from the N8N Workflow, toggle it to enabled and hit save. Do the same for the `crawl4ai-openwebui-function.py` fuction.

17. Now hit `New Chat` select your model or Fuction, select your tool (Web Search, Image, or hit the `+` and select whisper-server or crawl4ai) and enjoy!

18. If you want to hit any of the services directory they can be hit 

| **Service**              | **Container Name**   | **Host Port** | **Container Port** | **URL**                    |
|--------------------------|----------------------|---------------|--------------------|----------------------------|
| n8n                      | `n8n`                | 5678          | 5678               | http://localhost:5678      |
| ollama                   | `ollama`             | 11434         | 11434              | http://localhost:11434     |
| open-webui               | `open-webui`         | 3000          | 8080               | http://localhost:3000      |
| qdrant                   | `qdrant`             | 6333          | 6333               | http://localhost:6333      |
| neo4j (browser)          | `neo4j`              | 7474          | 7474               | http://localhost:7474      |
| neo4j (bolt protocol)    | `neo4j`              | 7687          | 7687               | bolt://localhost:7687      |
| postgres                 | `postgres`           | 5433          | 5432               | psql://localhost:5433      |
| searxng                  | `searxng`            | 8080          | 8080               | http://localhost:8080      |
| stable-diffusion (UI)    | `sd-a1111`           | 7860          | 7860               | http://localhost:7860      |
| stable-diffusion (alt)   | `sd-a1111`           | 8081          | 8080               | http://localhost:8081      |
| whisper-server           | `whisper-server`     | 9002          | 9000               | http://localhost:9002      |
| crawl4ai                 | `crawl4ai`           | 8860          | 11235              | http://localhost:8860      |

## Get more explainations and details such as how to use the N8N Workflows in detail, troubleshooting and more by visting the URLs below:
* [GainSec.com](https://gainsec.com)
* [Part 1](https://gainsec.com/2025/06/01/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-1/)
* [Part 2](https://gainsec.com/2025/06/02/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-2-searxng/)
* [Part 3](https://gainsec.com/2025/06/03/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-3-image-generation-via-stable-diffusion/)
* [Part 4](https://gainsec.com/2025/06/04/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-4-transcription-via-whisper/)
* [Part 5](https://gainsec.com/2025/06/07/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-5-open-webui-to-crawl4ai-local-files/)
* [Part 6](https://gainsec.com/2025/06/08/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-6-open-webui-to-crawl4ai-chat/)
* [Part 7](https://gainsec.com/2025/06/09/the-quickest-and-simplest-guide-to-spinning-up-a-powerful-local-ai-stack-part-7-current-stack-docker-deploy/)
* [More Coming Soon](https://gainsec.com/)

## Authors

* **Jon Gaines** - [GainSec](https://github.com/GainSec)

## Acknowledgments

* Cole Medin & the N8N-IO Team. Using Cole's docker-compose and start_services.py as a starting point. [Local-AI-Packaged](https://github.com/coleam00/local-ai-packaged)