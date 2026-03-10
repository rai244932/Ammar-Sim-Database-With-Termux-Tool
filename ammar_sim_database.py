#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import requests

# ============================================
# PREMIUM COLOR CODES (TERMUX OPTIMIZED)
# ============================================
class C:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'

# ============================================
# UTILITIES
# ============================================
def clear():
    os.system('clear')

def banner():
    clear()
    print(f"{C.CYAN}")
    print(r"      █████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗ ")
    print(r"     ██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗")
    print(r"     ███████║██╔████╔██║██╔████╔██║███████║██████╔╝")
    print(r"     ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗")
    print(r"     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║  ██║")
    print(f"{C.RESET}")
    print(f"  {C.WHITE}╔══════════════════════════════════════════════╗")
    print(f"  ║ {C.GREEN}DEVELOPER {C.WHITE}: {C.YELLOW}AMMAR RAI{C.WHITE}                       ║")
    print(f"  ║ {C.GREEN}WHATSAPP  {C.WHITE}: {C.YELLOW}923018787786{C.WHITE}                    ║")
    print(f"  ║ {C.GREEN}TOOL MODE {C.WHITE}: {C.CYAN}PREMIUM V3 (TERMUX){C.WHITE}             ║")
    print(f"  ╚══════════════════════════════════════════════╝{C.RESET}\n")

def menu():
    print(f"  {C.CYAN}┌──────────────────────────────────────────┐{C.RESET}")
    print(f"  {C.CYAN}│ {C.YELLOW}[01]{C.WHITE} SEARCH DATABASE     {C.CYAN}│ {C.YELLOW}[02]{C.WHITE} SUPPORT    {C.CYAN}│{C.RESET}")
    print(f"  {C.CYAN}├──────────────────────────────────────────┤{C.RESET}")
    print(f"  {C.CYAN}│ {C.YELLOW}[03]{C.WHITE} JOIN GROUP         {C.CYAN}│ {C.YELLOW}[00]{C.RED} EXIT       {C.CYAN}│{C.RESET}")
    print(f"  {C.CYAN}└──────────────────────────────────────────┘{C.RESET}\n")

def search(phone):
    banner()
    print(f"  {C.GREEN}[~] {C.WHITE}SCANNING: {C.YELLOW}{phone}{C.RESET}")
    print(f"  {C.GREEN}[~] {C.WHITE}DATABASE: {C.CYAN}CONNECTING...{C.RESET}\n")
    time.sleep(1.5)
    
    # Formatting
    if phone.startswith('0'): phone = '+92' + phone[1:]
    elif not phone.startswith('+'): phone = '+92' + phone
    
    try:
        url = f"https://howler-database-api.vercel.app/api/lookup?phone={phone}"
        res = requests.get(url, timeout=15)
        if res.status_code == 200:
            data = res.json()
            print(f"  {C.MAGENTA}⚡ RECORD FOUND ⚡{C.RESET}")
            print(f"  {C.WHITE}──────────────────────────────────────────{C.RESET}")
            
            # Extract and Display
            found = False
            for k, v in data.items():
                if any(x in str(k).lower() for x in ["status", "success", "developer"]): continue
                if v and str(v).lower() not in ["null", "none"]:
                    print(f"  {C.CYAN}➤ {C.GREEN}{k.upper():<10} {C.WHITE}│ {C.WHITE}{v}{C.RESET}")
                    found = True
            
            if not found:
                print(f"  {C.RED}NO DATA AVAILABLE IN THIS SECTOR.{C.RESET}")
            
            print(f"  {C.WHITE}──────────────────────────────────────────{C.RESET}")
        else:
            print(f"  {C.RED}❌ SERVER ERROR!{C.RESET}")
    except:
        print(f"  {C.RED}❌ CONNECTION ERROR!{C.RESET}")
    
    input(f"\n  {C.YELLOW}Press Enter to go back...{C.RESET}")

def main():
    while True:
        banner()
        menu()
        cmd = input(f"  {C.GREEN}AMMAR-RAI{C.WHITE}@{C.YELLOW}TERMUX{C.CYAN} ~# {C.WHITE}").strip()
        
        if cmd in ['1', '01']:
            num = input(f"  {C.YELLOW}📞 Enter Number: {C.WHITE}").strip()
            if num: search(num)
        elif cmd in ['2', '02']:
            print(f"  {C.GREEN}Contact: {C.WHITE}923018787786")
            time.sleep(2)
        elif cmd in ['3', '03']:
            os.system("termux-open-url 'https://chat.whatsapp.com/F2zlsDXzwp05KKIrqj8vVj'")
        elif cmd in ['0', '00']:
            print(f"  {C.RED}System Exited.{C.RESET}")
            break
        else:
            print(f"  {C.RED}Invalid Option!{C.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
