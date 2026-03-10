#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, time, json, requests
from datetime import datetime

# ============================================
# NEON MATRIX COLOR ENGINE
# ============================================
class Color:
    G = '\033[92m' # Green
    Y = '\033[93m' # Yellow
    R = '\033[91m' # Red
    C = '\033[96m' # Cyan
    M = '\033[95m' # Magenta
    W = '\033[97m' # White
    B = '\033[1m'  # Bold
    S = '\033[0m'  # Reset

# ============================================
# ADVANCED UTILITIES
# ============================================
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def typing_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading_animation(duration=2):
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f"\r  {Color.C}[{char}] {Color.W}SYSTEM ACCESSING DATABASE...{Color.S}")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\r" + " " * 50 + "\r", end="")

# ============================================
# STYLISH INTERFACE FUNCTIONS
# ============================================
def show_banner():
    clear()
    banner = f"""{Color.G}
    {Color.C}   ▄████████   ▄▄▄▄███▄▄▄  ▄▄▄▄███▄▄▄    ▄████████    ▄████████ 
    {Color.C}  ███    ███ ▄██▀▀▀███▀▀▀███▀▀▀███▀▀▀███  ███    ███   ███    ███ 
    {Color.G}  ███    ███ ███   ███   ███   ███   ███  ███    ███   ███    ███ 
    {Color.G}  ███    ███ ███   ███   ███   ███   ███  ███    ███  ▄███▄▄▄▄██▀ 
    {Color.Y}▀███████████ ███   ███   ███   ███   ███▀███████████ ▀▀███▀▀▀▀▀   
    {Color.Y}  ███    ███ ███   ███   ███   ███   ███  ███    ███ ▀███████████ 
    {Color.R}  ███    ███ ███   ███   ███   ███   ███  ███    ███   ███    ███ 
    {Color.R}  ███    █▀   ▀█   ███   █▀    ███   █▀   ███    █▀    ███    ███ 
    {Color.S}"""
    print(banner)
    print(f"  {Color.B}{Color.W}┌──────────────────────────────────────────────────────────┐")
    print(f"  {Color.W}│ {Color.G}OWNER    {Color.W}: {Color.Y}AMMAR RAI{Color.W}          {Color.G}BRAND {Color.W}: {Color.M}AMMAR-RAI TECH™{Color.W} │")
    print(f"  {Color.W}│ {Color.G}CONTACT  {Color.W}: {Color.Y}923018787786{Color.W}       {Color.G}MODE  {Color.W}: {Color.C}ULTRA-PREMIUM{Color.W}   │")
    print(f"  {Color.B}{Color.W}└──────────────────────────────────────────────────────────┘{Color.S}")

def show_menu():
    print(f"\n  {Color.C}╔═══════════════════════ PRIMARY SYSTEM ══════════════════════╗")
    print(f"  {Color.W}║  {Color.Y}[01] {Color.W}SIM SCANNER       {Color.W}║  {Color.Y}[02] {Color.W}SAVE HISTORY      {Color.W}║")
    print(f"  {Color.W}║  {Color.Y}[03] {Color.W}CONTACT OWNER     {Color.W}║  {Color.Y}[04] {Color.W}JOIN PRIVATE      {Color.W}║")
    print(f"  {Color.W}║  {Color.Y}[00] {Color.R}TERMINATE SYSTEM  {Color.W}║  {Color.Y}[99] {Color.G}CHECK UPDATE      {Color.W}║")
    print(f"  {Color.C}╚═════════════════════════════════════════════════════════════╝")

def save_to_history(phone, data):
    with open("search_history.txt", "a") as f:
        f.write(f"Date: {datetime.now()} | Phone: {phone} | Data: {data}\n")

# ============================================
# CORE LOGIC
# ============================================
def search_engine(phone):
    show_banner()
    print(f"  {Color.G}[+] {Color.W}INITIALIZING TARGET: {Color.Y}{phone}")
    loading_animation(2)
    
    # URL Format
    if phone.startswith('0'): phone = '92' + phone[1:]
    
    try:
        api_url = f"https://howler-database-api.vercel.app/api/lookup?phone={phone}"
        response = requests.get(api_url, timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            print(f"  {Color.M}◢◤ DATA RECOVERED SUCCESSFULLY ◢◤{Color.S}\n")
            
            # Professional Table Design
            print(f"  {Color.C}╭───────────────────────────────────────────────────╮")
            found = False
            for k, v in data.items():
                if any(x in str(k).lower() for x in ["status", "success", "count"]): continue
                if v and str(v).lower() not in ["null", "none", "no"]:
                    print(f"  {Color.C}│ {Color.G}{k.upper():<12} {Color.W}➤  {Color.W}{v}")
                    found = True
            
            if not found:
                print(f"  {Color.C}│ {Color.R}MESSAGE: {Color.W}NO ENCRYPTED RECORDS FOUND.         ")
            
            print(f"  {Color.C}╰───────────────────────────────────────────────────╯")
            
            if found:
                save_to_history(phone, data)
                print(f"  {Color.G}[✔] {Color.W}RECORD AUTO-SAVED IN {Color.Y}search_history.txt")
        else:
            print(f"  {Color.R}[!] SERVER REJECTED CONNECTION (Error {response.status_code})")
            
    except Exception as e:
        print(f"  {Color.R}[!] FATAL ERROR: {str(e)}")
    
    input(f"\n  {Color.Y}Press [ENTER] to return to Mainframe...{Color.S}")

def main():
    try:
        while True:
            show_banner()
            show_menu()
            choice = input(f"  {Color.G}RAI-AMMAR{Color.W}@{Color.C}DATABASE{Color.W}:~# {Color.Y}").strip()
            
            if choice == '01' or choice == '1':
                num = input(f"  {Color.C}[?] {Color.W}Enter Target Phone (e.g 03xxxxxxxxx): {Color.G}").strip()
                if num: search_engine(num)
            elif choice == '02' or choice == '2':
                os.system('cat search_history.txt' if os.name == 'posix' else 'type search_history.txt')
                input("\n  Press Enter to continue...")
            elif choice == '03' or choice == '3':
                typing_effect(f"  {Color.G}Contacting Ammar Rai on WhatsApp...")
                time.sleep(1)
                os.system("termux-open-url 'https://wa.me/923018787786'")
            elif choice == '04' or choice == '4':
                os.system("termux-open-url 'https://chat.whatsapp.com/F2zlsDXzwp05KKIrqj8vVj'")
            elif choice == '00' or choice == '0':
                typing_effect(f"  {Color.R}System Shutdown Initiated...")
                break
            else:
                print(f"  {Color.R}[!] Invalid Command Selection!")
                time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n  {Color.R}[!] Operation Interrupted by User.")
        sys.exit()

if __name__ == "__main__":
    main()
