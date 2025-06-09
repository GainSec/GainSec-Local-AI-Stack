"""
title: Crawl4AI Open-WebUI Function 
author: Jon Gaines
author_url: https://gainsec.com
version: 0.5
"""

from typing import Optional, Callable, Awaitable
from pydantic import BaseModel, Field
import time
import requests
import re


class Pipe:
    class Valves(BaseModel):
        n8n_url: str = Field(
            default="http://host.docker.internal:5678/webhook-test/crawl-url",  # Adjust if needed
            description="N8N Webhook URL",
        )
        n8n_bearer_token: str = Field(
            default="", description="Optional bearer token for auth"
        )
        emit_interval: float = Field(default=2.0)
        enable_status_indicator: bool = Field(default=True)

    def __init__(self):
        self.type = "pipe"
        self.id = "n8n_crawl_pipe"
        self.name = "N8N Crawl4AI Pipe"
        self.valves = self.Valves()
        self.last_emit_time = 0

    async def emit_status(
        self,
        emitter: Callable[[dict], Awaitable[None]],
        level: str,
        message: str,
        done: bool,
    ):
        now = time.time()
        if (
            emitter
            and self.valves.enable_status_indicator
            and (done or now - self.last_emit_time >= self.valves.emit_interval)
        ):
            await emitter(
                {
                    "type": "status",
                    "data": {
                        "status": "complete" if done else "in_progress",
                        "level": level,
                        "description": message,
                        "done": done,
                    },
                }
            )
            self.last_emit_time = now

    async def pipe(
        self,
        body: dict,
        __user__: Optional[dict] = None,
        __event_emitter__: Optional[Callable[[dict], Awaitable[None]]] = None,
        __event_call__: Optional[Callable[[dict], Awaitable[dict]]] = None,
    ) -> dict:
        await self.emit_status(
            __event_emitter__, "info", "Calling N8N workflow...", False
        )

        messages = body.get("messages", [])
        if not messages:
            await self.emit_status(
                __event_emitter__, "error", "No input messages found", True
            )
            return {"error": "No input messages"}

        message_text = messages[-1]["content"]
        match = re.search(r"https?://\S+", message_text)
        if not match:
            await self.emit_status(
                __event_emitter__, "error", "No URL found in message", True
            )
            return {"error": "No URL found in message"}

        url_input = match.group(0)

        payload = {"chatInput": url_input, "sessionId": str(time.time())}

        headers = {"Content-Type": "application/json"}
        if self.valves.n8n_bearer_token:
            headers["Authorization"] = f"Bearer {self.valves.n8n_bearer_token}"

        try:
            response = requests.post(
                self.valves.n8n_url, json=payload, headers=headers, timeout=30
            )
            response.raise_for_status()
            print("Status Code:", response.status_code)
            print("Raw Response:", response.text)
            data = response.json()
            result = data.get("output", "No 'output' field found in N8N response")
        except Exception as e:
            await self.emit_status(
                __event_emitter__, "error", f"N8N call failed: {e}", True
            )
            return {"error": str(e)}

        body["messages"].append({"role": "assistant", "content": result})
        await self.emit_status(__event_emitter__, "info", "N8N call complete", True)
        return body