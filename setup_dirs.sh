#!/bin/bash

set -e

echo "📁 Creating required directories..."

# Directories to create
mkdir -p ~/gainsec-local-ai-stack/{n8n/backup/workflows,openwebui-tools,searxng,whisper-models}
mkdir -p ~/gainsec-local-ai-stack/shared/{uploads,transcripts,crawl/{html,image,links,markdown,pdf,urls}}
mkdir -p ~/gainsec-local-ai-stack/stable-diffusion/{models,outputs,embeddings,extensions,configs,cache,repositories}
mkdir -p ~/gainsec-local-ai-stack/neo4j/{logs,config,plugins,data/transactions/{neo4j,system},data/dbms,data/databases/{neo4j/schema/index/token-lookup-1.0/{1,2},system/schema/index/token-lookup-1.0/{1,2},system/schema/index/range-1.0/{3,5,7,9,11}}}

echo "🛡️ Setting directory permissions..."

# Set ownership (assuming user/group 'nigel')
chown -R nigel:nigel ~/gainsec-local-ai-stack/{shared,n8n,openwebui-tools,searxng,whisper-models,stable-diffusion}
chown -R 7474:7474 ~/gainsec-local-ai-stack/neo4j/data ~/gainsec-local-ai-stack/neo4j/logs

# Set permissions
chmod -R 755 ~/gainsec-local-ai-stack/neo4j
chmod -R 775 ~/gainsec-local-ai-stack/{shared,n8n,openwebui-tools,searxng,whisper-models,stable-diffusion}

echo "✅ All directories created and permissions set."
