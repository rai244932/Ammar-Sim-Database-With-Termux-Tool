#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AMMAR SIM DATABASE - Professional Phone Number Lookup Tool
Created by: AMMAR
Version: 2.0 (Premium Edition)
"""

import os
import sys
import time
import json
import requests
from datetime import datetime

# ============================================
# PREMIUM COLOR CODES - NEON & METALLIC THEME
# ============================================
class Colors:
    # Regular Colors
    BLACK = '\033[0;30m'
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    
    # Neon Variants
    NEON_RED = '\033[91m'
    NEON_GREEN = '\033[92m'
    NEON_YELLOW = '\033[93m'
    NEON_BLUE = '\033[94m'
    NEON_PINK = '\033[95m'
    NEON_CYAN = '\033[96m'
    
    # Background Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Text Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    DIM = '\033[2m'
    
    # Reset
    RESET = '\033[0m'
    
    # Box Drawing Characters
    BOX_TL = '┌'
    BOX_TR = '┐'
    BOX_BL = '└'
    BOX_BR = '┘'
    BOX_H = '─'
    BOX_V = '│'
    BOX_T = '┬'
    BOX_B = '┴'
    BOX_L = '├'
    BOX_R = '┤'

C = Colors()

# ============================================
# CONFIGURATION
# ============================================
CONFIG = {
    "owner": "AMMAR",
    "version": "2.0 PREMIUM",
    "whatsapp": "03018787786",
    "group_link": "https://chat.whatsapp.com/F2zlsDXzwp05KKIrqj8vVj?mode=gi_t",
    "api_base": "https://howler-database-api.vercel.app/api/lookup?phone="
}

# ============================================
# UTILITY FUNCTIONS
# ============================================
def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(text="PROCESSING", duration=1.5):
    """Display loading animation"""
    chars = "⣾⣽⣻⢿⡿⣟⣯⣷"
    for _ in range(int(duration * 10)):
        for char in chars:
            sys.stdout.write(f'\r{C.NEON_CYAN}{text} {char}{C.RESET}')
            sys.stdout.flush()
            time.sleep(0.05)
    print()

def type_effect(text, color=C.NEON_GREEN, delay=0.03):
    """Typewriter effect for text"""
    for char in text:
        sys.stdout.write(f'{color}{char}{C.RESET}')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def center_text(text, width=60):
    """Center text within given width"""
    return text.center(width)

# ============================================
# PREMIUM BANNER DESIGN - AMMAR EDITION
# ============================================
def show_banner():
    """Display premium animated banner with AMMAR name"""
    clear_screen()
    
    # ASCII Art Banner with AMMAR name
    banner = f"""
{C.NEON_RED}    ╔══════════════════════════════════════════════════════════╗
{C.NEON_RED}    ║{C.NEON_YELLOW}  █████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗ {C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW} ██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗{C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW} ███████║██╔████╔██║██╔████╔██║███████║██████╔╝{C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW} ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗{C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW} ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║  ██║{C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW} ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝{C.NEON_RED}║
{C.NEON_RED}    ╚══════════════════════════════════════════════════════════╝{C.RESET}
    
{C.NEON_BLUE}    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{C.NEON_BLUE}    ┃{C.NEON_GREEN}            SIM DATABASE PREMIUM EDITION v2.0           {C.NEON_BLUE}┃
{C.NEON_BLUE}    ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{C.NEON_BLUE}    ┃{C.WHITE}     ╔═══════════════════════════════════════════╗     {C.NEON_BLUE}┃
{C.NEON_BLUE}    ┃{C.WHITE}     ║{C.NEON_PINK}    ░▒▓█ OWNER: {C.NEON_YELLOW}AMMAR {C.NEON_PINK}█▓▒░      {C.WHITE}║     {C.NEON_BLUE}┃
{C.NEON_BLUE}    ┃{C.WHITE}     ╚═══════════════════════════════════════════╝     {C.NEON_BLUE}┃
{C.NEON_BLUE}    ┃                                                          ┃
{C.NEON_BLUE}    ┃  {C.NEON_CYAN}▸ WHATSAPP:{C.WHITE} 03018787786       {C.NEON_CYAN}▸ MODE:{C.NEON_YELLOW} PREMIUM {C.NEON_BLUE}┃
{C.NEON_BLUE}    ┃  {C.NEON_CYAN}▸ GROUP:{C.WHITE} AMMAR PRIVATE      {C.NEON_CYAN}▸ API:{C.NEON_GREEN} ONLINE  {C.NEON_BLUE}┃
{C.NEON_BLUE}    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{C.RESET}
    """
    print(banner)

# ============================================
# MAIN FUNCTIONS
# ============================================
def extract_address(data):
    """Extract valid address from nested data"""
    if isinstance(data, dict):
        for key, value in data.items():
            key_lower = str(key).lower()
            
            if 'address' in key_lower:
                if value and 'no' not in str(value).lower() and 'null' not in str(value).lower():
                    return str(value)
            
            if isinstance(value, (dict, list)):
                result = extract_address(value)
                if result:
                    return result
    
    elif isinstance(data, list):
        for item in data:
            result = extract_address(item)
            if result:
                return result
    
    return None

def display_results(data, indent=0):
    """Display search results in beautiful format"""
    address_found = None
    
    if isinstance(data, dict):
        for key, value in data.items():
            key_lower = str(key).lower()
            
            # Skip unwanted keys
            if any(x in key_lower for x in ["howler", "developer", "status", "count", "query", "success"]):
                continue
            
            # Check for address
            if 'address' in key_lower and value:
                if 'no' not in str(value).lower() and 'null' not in str(value).lower():
                    address_found = str(value)
            
            # Display with proper formatting
            prefix = "  " * indent
            if isinstance(value, (dict, list)):
                print(f"{C.NEON_BLUE}  {prefix}{C.NEON_YELLOW}► {C.NEON_GREEN}{key.upper()}{C.RESET}")
                sub_address = display_results(value, indent + 1)
                if sub_address and not address_found:
                    address_found = sub_address
            else:
                display_value = str(value)[:60] + ('...' if len(str(value)) > 60 else '')
                print(f"{C.NEON_BLUE}  {prefix}{C.NEON_CYAN}  ├─ {C.WHITE}{key:<15}{C.NEON_PINK}: {C.NEON_YELLOW}{display_value}{C.RESET}")
    
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, dict):
                print(f"{C.NEON_BLUE}  {'  ' * indent}{C.NEON_MAGENTA}► [{i+1}]{C.RESET}")
                sub_address = display_results(item, indent + 1)
                if sub_address and not address_found:
                    address_found = sub_address
    
    return address_found

def open_map(address):
    """Open address in Google Maps"""
    if address and len(address) > 5 and all(x not in address.lower() for x in ['no', 'null', 'none']):
        clean_addr = address.replace('null', '').replace('no', '').replace('none', '').strip()
        search_url = f"https://www.google.com/maps/search/{clean_addr.replace(' ', '+')}"
        
        print(f"\n{C.NEON_GREEN}  ╔══════════════════════════════════════════════════╗")
        print(f"  ║{C.NEON_YELLOW}     📍 LOCATION FOUND! OPENING MAPS...        {C.NEON_GREEN}║")
        print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
        
        os.system(f"termux-open-url '{search_url}'")
        return True
    return False

def search_database(phone):
    """Search phone number in database"""
    show_banner()
    
    print(f"\n{C.NEON_CYAN}  ╔══════════════════════════════════════════════════╗")
    print(f"  ║{C.WHITE}           INITIALIZING DATABASE SCAN            {C.NEON_CYAN}║")
    print(f"  ╠══════════════════════════════════════════════════╣")
    print(f"  ║{C.NEON_GREEN}  📱 TARGET:{C.WHITE} {phone:<35}{C.NEON_CYAN}║")
    print(f"  ║{C.NEON_GREEN}  🔐 SECURITY:{C.WHITE} BYPASSING FIREWALL...     {C.NEON_CYAN}║")
    print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
    
    # Format phone number
    if phone.startswith('0'):
        phone = '+92' + phone[1:]
    elif not phone.startswith('+'):
        phone = '+92' + phone
    
    loading_animation("CONNECTING TO DATABASE", 1.5)
    
    try:
        url = f"{CONFIG['api_base']}{phone}"
        response = requests.get(url, timeout=20)
        
        if response.status_code != 200:
            print(f"\n{C.NEON_RED}  ╔══════════════════════════════════════════════════╗")
            print(f"  ║{C.WHITE}          ❌ DATABASE CONNECTION FAILED         {C.NEON_RED}║")
            print(f"  ║{C.NEON_YELLOW}      STATUS: {response.status_code}                     {C.NEON_RED}║")
            print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
            input(f"\n{C.NEON_YELLOW}  Press ENTER to continue...{C.RESET}")
            return
        
        data = response.json()
        
        print(f"\n{C.NEON_GREEN}  ╔══════════════════════════════════════════════════╗")
        print(f"  ║{C.WHITE}            ✅ DATABASE ACCESS GRANTED            {C.NEON_GREEN}║")
        print(f"  ╠══════════════════════════════════════════════════╣")
        print(f"  ║{C.NEON_CYAN}  📊 FETCHING RESULTS...                        {C.NEON_GREEN}║")
        print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}\n")
        
        time.sleep(1)
        
        # Display results header
        print(f"{C.NEON_BLUE}  ╔══════════════════════════════════════════════════╗")
        print(f"  ║{C.NEON_PINK}            🔍 SEARCH RESULTS FOUND            {C.NEON_BLUE}║")
        print(f"  ╠══════════════════════════════════════════════════╣{C.RESET}")
        
        if data and data != {}:
            address = display_results(data)
            
            print(f"{C.NEON_BLUE}  ╚══════════════════════════════════════════════════╝{C.RESET}")
            
            # Handle address for maps
            if address:
                print(f"\n{C.NEON_GREEN}  ╔══════════════════════════════════════════════════╗")
                print(f"  ║{C.WHITE}              📍 ADDRESS DETECTED                {C.NEON_GREEN}║")
                print(f"  ╠══════════════════════════════════════════════════╣")
                print(f"  ║{C.NEON_YELLOW}  {address[:70]}{'...' if len(address) > 70 else ''}{C.NEON_GREEN}║")
                print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
                
                choice = input(f"\n{C.NEON_CYAN}  📍 OPEN IN GOOGLE MAPS? (y/n): {C.WHITE}").lower()
                if choice in ['y', 'yes']:
                    open_map(address)
            else:
                print(f"\n{C.NEON_RED}  ╔══════════════════════════════════════════════════╗")
                print(f"  ║{C.WHITE}         ⚠️ NO VALID ADDRESS FOUND             {C.NEON_RED}║")
                print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
        
        else:
            print(f"{C.NEON_BLUE}  ║{C.NEON_RED}            ❌ NO RECORDS FOUND!              {C.NEON_BLUE}║")
            print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
        
    except requests.exceptions.Timeout:
        print(f"\n{C.NEON_RED}  ❌ ERROR: Connection timeout!{C.RESET}")
    except requests.exceptions.ConnectionError:
        print(f"\n{C.NEON_RED}  ❌ ERROR: No internet connection!{C.RESET}")
    except Exception as e:
        print(f"\n{C.NEON_RED}  ❌ ERROR: {str(e)}{C.RESET}")
    
    input(f"\n{C.NEON_YELLOW}  Press ENTER to return to main menu...{C.RESET}")

def show_about():
    """Display about section with group links"""
    show_banner()
    
    print(f"\n{C.NEON_CYAN}  ╔══════════════════════════════════════════════════╗")
    print(f"  ║{C.NEON_PINK}            📱 CONTACT & SUPPORT INFO          {C.NEON_CYAN}║")
    print(f"  ╠══════════════════════════════════════════════════╣")
    print(f"  ║{C.WHITE}                                            {C.NEON_CYAN}║")
    print(f"  ║{C.NEON_GREEN}  👤 OWNER:{C.WHITE} AMMAR                       {C.NEON_CYAN}║")
    print(f"  ║{C.NEON_GREEN}  📞 WHATSAPP:{C.WHITE} 03018787786              {C.NEON_CYAN}║")
    print(f"  ║{C.WHITE}                                            {C.NEON_CYAN}║")
    print(f"  ║{C.NEON_YELLOW}  👥 AMMAR PRIVATE GROUP:{C.WHITE}                {C.NEON_CYAN}║")
    print(f"  ║{C.NEON_CYAN}  {CONFIG['group_link'][:65]}{C.NEON_CYAN}║")
    print(f"  ║{C.WHITE}                                            {C.NEON_CYAN}║")
    print(f"  ║{C.NEON_MAGENTA}  ⭐ VERSION: {CONFIG['version']}                     {C.NEON_CYAN}║")
    print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
    
    print(f"\n{C.NEON_YELLOW}  🚀 Open group link in browser?{C.RESET}")
    choice = input(f"{C.NEON_CYAN}  [1] OPEN GROUP  [0] BACK: {C.WHITE}")
    
    if choice == '1':
        os.system(f"termux-open-url '{CONFIG['group_link']}'")

# ============================================
# MAIN MENU
# ============================================
def main():
    """Main program loop"""
    try:
        while True:
            show_banner()
            
            print(f"\n{C.NEON_BLUE}  ╔══════════════════════════════════════════════════╗")
            print(f"  ║{C.NEON_GREEN}              🔥 MAIN MENU OPTIONS 🔥            {C.NEON_BLUE}║")
            print(f"  ╠══════════════════════════════════════════════════╣")
            print(f"  ║{C.WHITE}                                                {C.NEON_BLUE}║")
            print(f"  ║  {C.NEON_YELLOW}[01]{C.NEON_CYAN} 🔍 SEARCH DATABASE          {C.NEON_MAGENTA}[MAPS]{C.WHITE}     {C.NEON_BLUE}║")
            print(f"  ║  {C.NEON_YELLOW}[02]{C.NEON_CYAN} 📱 CONTACT & SUPPORT        {C.NEON_MAGENTA}[GROUP]{C.WHITE}   {C.NEON_BLUE}║")
            print(f"  ║  {C.NEON_YELLOW}[00]{C.NEON_RED} ❌ EXIT SYSTEM               {C.NEON_MAGENTA}[QUIT]{C.WHITE}   {C.NEON_BLUE}║")
            print(f"  ║{C.WHITE}                                                {C.NEON_BLUE}║")
            print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
            
            print(f"\n{C.NEON_CYAN}  ╭{'─' * 50}╮")
            choice = input(f"  {C.NEON_GREEN}⚡ AMMAR@{C.NEON_YELLOW}TERMUX{C.NEON_BLUE} ~${C.WHITE} ").strip()
            print(f"  {C.NEON_CYAN}╰{'─' * 50}╯{C.RESET}")
            
            if choice == '01' or choice == '1':
                print(f"\n{C.NEON_YELLOW}  📞 Enter Pakistani number (e.g., 03018787786):{C.WHITE}")
                phone = input(f"  {C.NEON_CYAN}⤷ {C.WHITE}").strip()
                if phone and phone.replace('+', '').replace('-', '').isdigit():
                    search_database(phone)
                else:
                    print(f"\n{C.NEON_RED}  ❌ Invalid number format!{C.RESET}")
                    time.sleep(2)
            
            elif choice == '02' or choice == '2':
                show_about()
            
            elif choice == '00' or choice == '0':
                print(f"\n{C.NEON_RED}  ╔══════════════════════════════════════════════════╗")
                print(f"  ║{C.WHITE}         👋 THANK YOU FOR USING AMMAR SIM        {C.NEON_RED}║")
                print(f"  ║{C.NEON_YELLOW}            🔥 AMMAR PREMIUM EDITION 🔥         {C.NEON_RED}║")
                print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
                time.sleep(2)
                clear_screen()
                sys.exit(0)
            
            else:
                print(f"\n{C.NEON_RED}  ❌ Invalid option! Please choose 01, 02, or 00{C.RESET}")
                time.sleep(2)
    
    except KeyboardInterrupt:
        print(f"\n\n{C.NEON_RED}  ⚡ INTERRUPTED BY USER{C.RESET}")
        time.sleep(1)
        clear_screen()
        sys.exit(0)

# ============================================
# PROGRAM START
# ============================================
if __name__ == "__main__":
    # Check if running in Termux
    try:
        main()
    except Exception as e:
        print(f"{C.NEON_RED}  ❌ FATAL ERROR: {str(e)}{C.RESET}")
        time.sleep(3)
        sys.exit(1)
