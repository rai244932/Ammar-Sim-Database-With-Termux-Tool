#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AMMAR SIM DATABASE - Professional Phone Number Lookup Tool
Created by: AMMAR
Version: 2.0 PREMIUM (FIXED EDITION)
"""

import os
import sys
import time
import json
import requests
from datetime import datetime

# ============================================
# PREMIUM COLOR CODES
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
    
    # Reset
    RESET = '\033[0m'
    BOLD = '\033[1m'

C = Colors()

# ============================================
# CONFIGURATION
# ============================================
CONFIG = {
    "owner": "AMMAR",
    "version": "2.0 PREMIUM",
    "whatsapp": "03018787786",
    "group_link": "https://chat.whatsapp.com/F2zlsDXzwp05KKIrqj8vVj",
    "api_base": "https://howler-database-api.vercel.app/api/lookup?phone="
}

# ============================================
# UTILITY FUNCTIONS
# ============================================
def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(text="PROCESSING"):
    """Display loading animation"""
    chars = "⣾⣽⣻⢿⡿⣟⣯⣷"
    for i in range(20):
        for char in chars:
            sys.stdout.write(f'\r{C.NEON_CYAN}┃ {text} {char} ┃{C.RESET}')
            sys.stdout.flush()
            time.sleep(0.03)
    print()

# ============================================
# PREMIUM BANNER - AMMAR EDITION
# ============================================
def show_banner():
    """Display premium banner with AMMAR name"""
    clear_screen()
    
    banner = f"""
{C.NEON_RED}    ╔══════════════════════════════════════════════════════════╗
{C.NEON_RED}    ║{C.NEON_YELLOW}  █████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗ {C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW} ██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗{C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW} ███████║██╔████╔██║██╔████╔██║███████║██████╔╝{C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW} ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗{C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW} ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║  ██║{C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW} ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝{C.NEON_RED}║
{C.NEON_RED}    ╚══════════════════════════════════════════════════════════╝{C.RESET}
    
{C.NEON_BLUE}    ╔══════════════════════════════════════════════════════════╗
{C.NEON_BLUE}    ║{C.NEON_GREEN}         SIM DATABASE PREMIUM EDITION v2.0            {C.NEON_BLUE}║
{C.NEON_BLUE}    ╠══════════════════════════════════════════════════════════╣
{C.NEON_BLUE}    ║{C.WHITE}                                                    {C.NEON_BLUE}║
{C.NEON_BLUE}    ║{C.NEON_PINK}      👤 OWNER    : {C.NEON_YELLOW}AMMAR                     {C.NEON_BLUE}║
{C.NEON_BLUE}    ║{C.NEON_PINK}      📞 WHATSAPP : {C.NEON_YELLOW}03018787786               {C.NEON_BLUE}║
{C.NEON_BLUE}    ║{C.NEON_PINK}      📱 GROUP    : {C.NEON_YELLOW}AMMAR PRIVATE              {C.NEON_BLUE}║
{C.NEON_BLUE}    ║{C.NEON_PINK}      ⚡ MODE     : {C.NEON_GREEN}PREMIUM                    {C.NEON_BLUE}║
{C.NEON_BLUE}    ║{C.NEON_PINK}      🌐 API      : {C.NEON_GREEN}ONLINE                     {C.NEON_BLUE}║
{C.NEON_BLUE}    ║{C.WHITE}                                                    {C.NEON_BLUE}║
{C.NEON_BLUE}    ╚══════════════════════════════════════════════════════════╝{C.RESET}
    """
    print(banner)

# ============================================
# DATA EXTRACTION FUNCTIONS
# ============================================
def extract_all_data(data, indent=0):
    """Extract and display all data in beautiful format"""
    results = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            key_lower = str(key).lower()
            
            # Skip unwanted keys
            if any(x in key_lower for x in ["howler", "developer", "status", "count", "query", "success"]):
                continue
            
            if isinstance(value, (dict, list)):
                sub_results = extract_all_data(value, indent + 1)
                if sub_results:
                    results.extend(sub_results)
            else:
                if value and str(value).strip() and str(value).lower() not in ["no", "null", "none", ""]:
                    results.append({
                        'key': key,
                        'value': str(value),
                        'indent': indent
                    })
    
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                sub_results = extract_all_data(item, indent + 1)
                if sub_results:
                    results.extend(sub_results)
            else:
                if item and str(item).strip() and str(item).lower() not in ["no", "null", "none", ""]:
                    results.append({
                        'key': 'VALUE',
                        'value': str(item),
                        'indent': indent
                    })
    
    return results

def find_address(data):
    """Find address in data"""
    if isinstance(data, dict):
        for key, value in data.items():
            if 'address' in str(key).lower():
                if value and 'no' not in str(value).lower() and 'null' not in str(value).lower():
                    return str(value)
            if isinstance(value, (dict, list)):
                result = find_address(value)
                if result:
                    return result
    elif isinstance(data, list):
        for item in data:
            result = find_address(item)
            if result:
                return result
    return None

def display_results_table(results):
    """Display results in a beautiful table format"""
    if not results:
        print(f"\n{C.NEON_RED}  ╔══════════════════════════════════════════════════╗")
        print(f"  ║{C.WHITE}           ❌ NO DATA FOUND!                {C.NEON_RED}║")
        print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
        return
    
    print(f"\n{C.NEON_GREEN}  ╔══════════════════════════════════════════════════╗")
    print(f"  ║{C.NEON_YELLOW}           📊 DATABASE RECORDS FOUND          {C.NEON_GREEN}║")
    print(f"  ╠══════════════════════════════════════════════════╣{C.RESET}")
    
    for item in results:
        indent = "  " * item['indent']
        key = item['key'].upper()
        value = item['value']
        
        # Truncate long values
        if len(value) > 50:
            value = value[:47] + "..."
        
        # Color coding based on key type
        if 'name' in key.lower():
            key_color = C.NEON_PINK
        elif 'phone' in key.lower() or 'mobile' in key.lower():
            key_color = C.NEON_CYAN
        elif 'address' in key.lower():
            key_color = C.NEON_YELLOW
        elif 'email' in key.lower():
            key_color = C.NEON_BLUE
        elif 'cnic' in key.lower() or 'id' in key.lower():
            key_color = C.NEON_GREEN
        else:
            key_color = C.WHITE
        
        print(f"{C.NEON_BLUE}  ║{C.RESET} {indent}{key_color}▸ {key:<12}{C.NEON_PINK}: {C.WHITE}{value}")
    
    print(f"{C.NEON_GREEN}  ╚══════════════════════════════════════════════════╝{C.RESET}")

# ============================================
# MAP FUNCTION
# ============================================
def open_map(address):
    """Open address in Google Maps"""
    if address and len(address) > 5:
        clean_addr = address.replace('null', '').replace('no', '').replace('none', '').strip()
        if clean_addr and len(clean_addr) > 3:
            search_url = f"https://www.google.com/maps/search/{clean_addr.replace(' ', '+')}"
            
            print(f"\n{C.NEON_GREEN}  ╔══════════════════════════════════════════════════╗")
            print(f"  ║{C.NEON_YELLOW}     📍 LOCATION FOUND! OPENING MAPS...        {C.NEON_GREEN}║")
            print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
            
            os.system(f"termux-open-url '{search_url}'")
            return True
    return False

# ============================================
# SEARCH FUNCTION
# ============================================
def search_database(phone):
    """Search phone number in database"""
    show_banner()
    
    print(f"\n{C.NEON_CYAN}  ╔══════════════════════════════════════════════════╗")
    print(f"  ║{C.WHITE}           INITIALIZING DATABASE SCAN            {C.NEON_CYAN}║")
    print(f"  ╠══════════════════════════════════════════════════╣")
    print(f"  ║{C.NEON_GREEN}  📱 NUMBER : {C.WHITE}{phone}{C.NEON_CYAN}")
    print(f"  ║{C.NEON_GREEN}  🔐 STATUS : {C.NEON_YELLOW}BYPASSING FIREWALL...{C.NEON_CYAN}")
    print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
    
    # Format phone number
    original_phone = phone
    if phone.startswith('0'):
        phone = '+92' + phone[1:]
    elif not phone.startswith('+'):
        phone = '+92' + phone
    
    loading_animation("CONNECTING TO DATABASE")
    
    try:
        url = f"{CONFIG['api_base']}{phone}"
        response = requests.get(url, timeout=20)
        
        if response.status_code != 200:
            print(f"\n{C.NEON_RED}  ╔══════════════════════════════════════════════════╗")
            print(f"  ║{C.WHITE}          ❌ DATABASE CONNECTION FAILED         {C.NEON_RED}║")
            print(f"  ║{C.NEON_YELLOW}      STATUS CODE: {response.status_code}{C.NEON_RED}")
            print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
            input(f"\n{C.NEON_YELLOW}  Press ENTER to continue...{C.RESET}")
            return
        
        data = response.json()
        
        print(f"\n{C.NEON_GREEN}  ╔══════════════════════════════════════════════════╗")
        print(f"  ║{C.WHITE}            ✅ DATABASE ACCESS GRANTED            {C.NEON_GREEN}║")
        print(f"  ╠══════════════════════════════════════════════════╣")
        print(f"  ║{C.NEON_CYAN}  📊 FETCHING RECORDS...{C.NEON_GREEN}")
        print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}\n")
        
        time.sleep(1)
        
        if data and data != {}:
            # Extract all data
            results = extract_all_data(data)
            display_results_table(results)
            
            # Find address for maps
            address = find_address(data)
            
            if address:
                print(f"\n{C.NEON_GREEN}  ╔══════════════════════════════════════════════════╗")
                print(f"  ║{C.NEON_YELLOW}              📍 ADDRESS DETECTED                {C.NEON_GREEN}║")
                print(f"  ╠══════════════════════════════════════════════════╣")
                print(f"  ║{C.WHITE}  {address[:70]}{'...' if len(address) > 70 else ''}{C.NEON_GREEN}║")
                print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
                
                while True:
                    choice = input(f"\n{C.NEON_CYAN}  📍 OPEN IN GOOGLE MAPS? (y/n): {C.WHITE}").lower()
                    if choice in ['y', 'n', 'yes', 'no']:
                        break
                    print(f"{C.NEON_RED}  ❌ Please enter 'y' or 'n'{C.RESET}")
                
                if choice in ['y', 'yes']:
                    open_map(address)
        else:
            print(f"\n{C.NEON_RED}  ╔══════════════════════════════════════════════════╗")
            print(f"  ║{C.WHITE}            ❌ NO RECORDS FOUND!                {C.NEON_RED}║")
            print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
        
    except requests.exceptions.Timeout:
        print(f"\n{C.NEON_RED}  ❌ ERROR: Connection timeout!{C.RESET}")
    except requests.exceptions.ConnectionError:
        print(f"\n{C.NEON_RED}  ❌ ERROR: No internet connection!{C.RESET}")
    except Exception as e:
        print(f"\n{C.NEON_RED}  ❌ ERROR: {str(e)}{C.RESET}")
    
    input(f"\n{C.NEON_YELLOW}  Press ENTER to return to main menu...{C.RESET}")

# ============================================
# ABOUT SECTION
# ============================================
def show_about():
    """Display about section"""
    show_banner()
    
    print(f"\n{C.NEON_CYAN}  ╔══════════════════════════════════════════════════╗")
    print(f"  ║{C.NEON_PINK}            📱 CONTACT & SUPPORT INFO          {C.NEON_CYAN}║")
    print(f"  ╠══════════════════════════════════════════════════╣")
    print(f"  ║{C.WHITE}                                            {C.NEON_CYAN}║")
    print(f"  ║{C.NEON_GREEN}  👤 OWNER     : {C.WHITE}AMMAR                {C.NEON_CYAN}║")
    print(f"  ║{C.NEON_GREEN}  📞 WHATSAPP  : {C.WHITE}03018787786         {C.NEON_CYAN}║")
    print(f"  ║{C.WHITE}                                            {C.NEON_CYAN}║")
    print(f"  ║{C.NEON_YELLOW}  👥 GROUP LINK:{C.WHITE}                   {C.NEON_CYAN}║")
    print(f"  ║{C.NEON_CYAN}  {CONFIG['group_link']}{C.NEON_CYAN}║")
    print(f"  ║{C.WHITE}                                            {C.NEON_CYAN}║")
    print(f"  ║{C.NEON_MAGENTA}  ⭐ VERSION   : {CONFIG['version']}           {C.NEON_CYAN}║")
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
            print(f"  ║{C.WHITE}                                            {C.NEON_BLUE}║")
            print(f"  ║  {C.NEON_YELLOW}[01]{C.NEON_CYAN} 🔍 SEARCH DATABASE          {C.NEON_PINK}[MAPS]{C.WHITE}     {C.NEON_BLUE}║")
            print(f"  ║  {C.NEON_YELLOW}[02]{C.NEON_CYAN} 📱 CONTACT & SUPPORT        {C.NEON_PINK}[GROUP]{C.WHITE}   {C.NEON_BLUE}║")
            print(f"  ║  {C.NEON_YELLOW}[00]{C.NEON_RED} ❌ EXIT SYSTEM               {C.NEON_PINK}[QUIT]{C.WHITE}   {C.NEON_BLUE}║")
            print(f"  ║{C.WHITE}                                            {C.NEON_BLUE}║")
            print(f"  ╚══════════════════════════════════════════════════╝{C.RESET}")
            
            print(f"\n{C.NEON_CYAN}  ╭{'─' * 50}╮")
            choice = input(f"  {C.NEON_GREEN}⚡ AMMAR@{C.NEON_YELLOW}TERMUX{C.NEON_BLUE} ~${C.WHITE} ").strip()
            print(f"  {C.NEON_CYAN}╰{'─' * 50}╯{C.RESET}")
            
            if choice in ['01', '1']:
                print(f"\n{C.NEON_YELLOW}  📞 Enter Pakistani number (e.g., 03018787786):{C.WHITE}")
                phone = input(f"  {C.NEON_CYAN}⤷ {C.WHITE}").strip()
                if phone and phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
                    search_database(phone)
                else:
                    print(f"\n{C.NEON_RED}  ❌ Invalid number format!{C.RESET}")
                    time.sleep(2)
            
            elif choice in ['02', '2']:
                show_about()
            
            elif choice in ['00', '0']:
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
    try:
        main()
    except Exception as e:
        print(f"{C.NEON_RED}  ❌ FATAL ERROR: {str(e)}{C.RESET}")
        time.sleep(3)
        sys.exit(1)
