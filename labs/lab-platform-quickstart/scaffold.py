#!/usr/bin/env python3
import os
import sys
import shutil

def generate_service(service_name: str, owner_team: str, output_dir: str = "generated-services"):
    template_dir = os.path.join(os.path.dirname(__file__), "templates", "fastapi-service")
    target_dir = os.path.join(output_dir, service_name)

    if os.path.exists(target_dir):
        print(f"Error: Directory {target_dir} already exists.")
        sys.exit(1)

    print(f"🚀 Generating Golden Path service: {service_name} (Owner: {owner_team})...")
    shutil.copytree(template_dir, target_dir)

    # Process template variables
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                content = f.read()
            
            updated_content = content.replace("{{SERVICE_NAME}}", service_name).replace("{{OWNER_TEAM}}", owner_team)
            
            with open(file_path, "w") as f:
                f.write(updated_content)

    print(f"✅ Service created successfully at: {target_dir}")
    print(f"👉 Next step: Run 'python3 -m uvicorn main:app --reload' inside {target_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 scaffold.py <service-name> <owner-team>")
        sys.exit(1)
    
    generate_service(sys.argv[1], sys.argv[2])
