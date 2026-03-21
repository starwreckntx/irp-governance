#!/usr/bin/env python3
"""
DNS Re-resolution Daemon for Tailscale Funnel Bridge
Prevents IPv4 pin (--resolve) from failing on A record rotation

Runs on PurpBox, monitors Funnel endpoint DNS, updates nginx/traefik
or signals the bridge service when the Tailscale A record changes.
"""

import socket
import time
import subprocess
import sys
from datetime import datetime

# Configuration
TAILSCALE_DOMAIN = "abacusclaw-3e8f11465-d66c8dd68-7xw4v.tail902902.ts.net"
CHECK_INTERVAL = 300  # 5 minutes
BRIDGE_SERVICE = "funnel-bridge"  # systemd service name
LOG_FILE = "/var/log/dns-resolver.log"

def log(msg):
    timestamp = datetime.now().isoformat()
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def get_current_ip():
    try:
        return socket.gethostbyname(TAILSCALE_DOMAIN)
    except socket.gaierror as e:
        log(f"DNS resolution failed: {e}")
        return None

def restart_bridge_service():
    try:
        subprocess.run(["sudo", "systemctl", "restart", BRIDGE_SERVICE], 
                      check=True, capture_output=True)
        log(f"Restarted {BRIDGE_SERVICE} service")
        return True
    except subprocess.CalledProcessError as e:
        log(f"Failed to restart service: {e}")
        return False

def main():
    log("DNS Re-resolution Daemon started")
    log(f"Monitoring: {TAILSCALE_DOMAIN}")
    log(f"Check interval: {CHECK_INTERVAL}s")
    
    current_ip = get_current_ip()
    if current_ip:
        log(f"Initial resolution: {current_ip}")
    else:
        log("WARNING: Initial DNS resolution failed")
    
    while True:
        time.sleep(CHECK_INTERVAL)
        
        new_ip = get_current_ip()
        if not new_ip:
            log("DNS resolution failed, will retry")
            continue
        
        if new_ip != current_ip:
            log(f"IP CHANGE DETECTED: {current_ip} -> {new_ip}")
            current_ip = new_ip
            
            # Restart the bridge service to pick up new IP
            if restart_bridge_service():
                log("Bridge service restarted successfully")
            else:
                log("ERROR: Bridge service restart failed")
        else:
            log(f"IP unchanged: {current_ip}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Daemon stopped by user")
        sys.exit(0)
    except Exception as e:
        log(f"Daemon crashed: {e}")
        sys.exit(1)
