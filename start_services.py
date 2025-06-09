#!/usr/bin/env python3

import os
import subprocess
import shutil
import argparse
import platform

def run_command(cmd, cwd=None):
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)

def ensure_docker_network(name):
    print(f"Ensuring Docker network '{name}' exists...")
    result = subprocess.run(["docker", "network", "ls", "--format", "{{.Name}}"], capture_output=True, text=True)
    networks = result.stdout.splitlines()
    if name not in networks:
        print(f"Creating network: {name}")
        subprocess.run(["docker", "network", "create", name], check=True)
    else:
        print(f"Network '{name}' already exists.")

def stop_existing_containers(profile=None):
    print("Stopping and removing existing containers for the unified project 'localai'...")
    cmd = ["docker", "compose", "-p", "localai"]
    if profile and profile != "none":
        cmd.extend(["--profile", profile])
    cmd.extend(["-f", "docker-compose.yml", "down", "--remove-orphans"])
    run_command(cmd)

def start_local_ai(profile=None):
    print("Starting local AI services...")
    cmd = ["docker", "compose", "-p", "localai"]
    if profile and profile != "none":
        cmd.extend(["--profile", profile])
    cmd.extend(["-f", "docker-compose.yml", "up", "-d"])
    run_command(cmd)

def generate_searxng_secret_key():
    print("Checking SearXNG settings...")
    settings_path = os.path.join("searxng", "settings.yml")
    settings_base_path = os.path.join("searxng", "settings-base.yml")

    if not os.path.exists(settings_base_path):
        print(f"Warning: Base settings file not found at {settings_base_path}")
        return

    if not os.path.exists(settings_path):
        print("Creating settings.yml from base...")
        shutil.copyfile(settings_base_path, settings_path)

    print("Generating SearXNG secret key...")

    try:
        random_key = subprocess.check_output(["openssl", "rand", "-hex", "32"]).decode('utf-8').strip()
        subprocess.run(["sed", "-i", f"s|ultrasecretkey|{random_key}|g", settings_path], check=True)
        print("SearXNG secret key generated successfully.")
    except Exception as e:
        print(f"Error generating SearXNG secret key: {e}")

def main():
    parser = argparse.ArgumentParser(description='Start local AI services (no Supabase or n8n-import).')
    parser.add_argument('--profile', choices=['cpu', 'gpu-nvidia', 'gpu-amd', 'none'], default='cpu',
                        help='Docker Compose profile to use')
    args = parser.parse_args()

    generate_searxng_secret_key()
    ensure_docker_network("gainsec-ai-stack")
    stop_existing_containers(args.profile)
    start_local_ai(args.profile)

if __name__ == "__main__":
    main()
