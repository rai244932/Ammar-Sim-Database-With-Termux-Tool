#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AMMAR SIM DATABASE - Professional Phone Number Lookup Tool
Created by: AMMAR
Version: 2.0 PREMIUM (BORDERLESS DESIGN)
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
    BLACK = '\033[0;30m'
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    
    NEON_RED = '\033[91m'
    NEON_GREEN = '\033[92m'
    NEON_YELLOW = '\033[93m'
    NEON_BLUE = '\033[94m'
    NEON_PINK = '\033[95m'
    NEON_CYAN = '\033[96m'
    
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
    os.system('clear' if os.name == 'posix' else 'cls')

# ============================================
# BORDERLESS BANNER - صرف ٹیکسٹ
# ============================================
def show_banner():
    clear_screen()
    
    print(f"{C.NEON_YELLOW}")
    print("        █████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗")
    print("       ██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗")
    print("       ███████║██╔████╔██║██╔████╔██║███████║██████╔╝")
    print("       ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗")
    print("       ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║  ██║")
    print("       ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝")
    print(f"{C.RESET}")
    
    print(f"{C.NEON_GREEN}              SIM DATABASE PREMIUM EDITION v2.0              {C.RESET}")
    print("")
    print(f"{C.NEON_PINK}    OWNER    : {C.NEON_YELLOW}AMMAR{C.RESET}")
    print(f"{C.NEON_PINK}    WHATSAPP : {C.NEON_YELLOW}03018787786{C.RESET}")
    print(f"{C.NEON_PINK}    GROUP    : {C.NEON_YELLOW}AMMAR PRIVATE{C.RESET}")
    print(f"{C.NEON_PINK}    MODE     : {C.NEON_GREEN}PREMIUM{C.RESET}")
    print(f"{C.NEON_PINK}    API      : {C.NEON_GREEN}ONLINE{C.RESET}")
    print("")

# ============================================
# BORDERLESS MENU
# ============================================
def show_menu():
    print(f"{C.NEON_BLUE}                      MAIN MENU OPTIONS                      {C.RESET}")
    print("")
    print(f"          {C.NEON_YELLOW}[01]{C.NEON_CYAN} 🔍 SEARCH DATABASE          {C.NEON_PINK}[MAPS]{C.RESET}")
    print(f"          {C.NEON_YELLOW}[02]{C.NEON_CYAN} 📱 CONTACT & SUPPORT        {C.NEON_PINK}[GROUP]{C.RESET}")
    print(f"          {C.NEON_YELLOW}[00]{C.NEON_RED} ❌ EXIT SYSTEM               {C.NEON_PINK}[QUIT]{C.RESET}")
    print("")

# ============================================
# BORDERLESS SEARCH HEADER
# ============================================
def show_search_header(phone):
    print(f"{C.NEON_CYAN}                    INITIALIZING DATABASE SCAN                    {C.RESET}")
    print("")
    print(f"{C.NEON_GREEN}    TARGET   : {C.WHITE}{phone}{C.RESET}")
    print(f"{C.NEON_GREEN}    SECURITY : {C.NEON_YELLOW}BYPASSING FIREWALL...{C.RESET}")
    print("")

# ============================================
# BORDERLESS RESULTS TABLE
# ============================================
def display_results_table(results):
    if not results:
        print(f"{C.NEON_RED}                      ❌ NO DATA FOUND!                      {C.RESET}")
        print("")
        return
    
    print(f"{C.NEON_GREEN}                      📊 DATABASE RECORDS                      {C.RESET}")
    print("")
    
    for i, item in enumerate(results[:10]):
        key = item['key'].upper()
        value = item['value']
        
        if len(value) > 50:
            value = value[:47] + "..."
        
        print(f"  {C.NEON_CYAN}► {C.NEON_YELLOW}{key:<15}{C.NEON_PINK}: {C.WHITE}{value}{C.RESET}")
    
    print("")

# ============================================
# BORDERLESS ADDRESS BOX
# ============================================
def show_address_box(address):
    print(f"{C.NEON_GREEN}                         ADDRESS DETECTED                         {C.RESET}")
    print("")
    print(f"{C.WHITE}  {address}{C.RESET}")
    print("")

# ============================================
# BORDERLESS ERROR BOX
# ============================================
def show_error_box(error):
    print(f"{C.NEON_RED}                            ERROR                                    {C.RESET}")
    print("")
    print(f"{C.NEON_YELLOW}  {error}{C.RESET}")
    print("")

# ============================================
# DATA EXTRACTION FUNCTIONS
# ============================================
def extract_all_data(data):
    results = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            key_lower = str(key).lower()
            
            if any(x in key_lower for x in ["howler", "developer", "status", "count", "query", "success"]):
                continue
            
            if isinstance(value, (dict, list)):
                results.extend(extract_all_data(value))
            else:
                if value and str(value).strip() and str(value).lower() not in ["no", "null", "none", ""]:
                    results.append({'key': key, 'value': str(value)})
    
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                results.extend(extract_all_data(item))
            else:
                if item and str(item).strip() and str(item).lower() not in ["no", "null", "none", ""]:
                    results.append({'key': 'VALUE', 'value': str(item)})
    
    return results

def find_address(data):
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

# ============================================
# MAP FUNCTION
# ============================================
def open_map(address):
    if address and len(address) > 5:
        clean_addr = address.replace('null', '').replace('no', '').replace('none', '').strip()
        if clean_addr and len(clean_addr) > 3:
            search_url = f"https://www.google.com/maps/search/{clean_addr.replace(' ', '+')}"
            
            print(f"{C.NEON_GREEN}                📍 LOCATION FOUND! OPENING MAPS...                {C.RESET}")
            print("")
            
            os.system(f"termux-open-url '{search_url}'")
            return True
    return False

# ============================================
# SEARCH FUNCTION
# ============================================
def search_database(phone):
    show_banner()
    show_search_header(phone)
    
    # Format phone number
    if phone.startswith('0'):
        phone = '+92' + phone[1:]
    elif not phone.startswith('+'):
        phone = '+92' + phone
    
    print(f"{C.NEON_CYAN}    CONNECTING TO DATABASE...{C.RESET}")
    time.sleep(1.5)
    
    try:
        url = f"{CONFIG['api_base']}{phone}"
        response = requests.get(url, timeout=20)
        
        if response.status_code != 200:
            show_error_box(f"CONNECTION FAILED - STATUS: {response.status_code}")
            input(f"\n{C.NEON_YELLOW}    Press ENTER to continue...{C.RESET}")
            return
        
        data = response.json()
        
        print(f"{C.NEON_GREEN}                    DATABASE ACCESS GRANTED                    {C.RESET}")
        print("")
        time.sleep(1)
        
        if data and data != {}:
            results = extract_all_data(data)
            display_results_table(results)
            
            address = find_address(data)
            
            if address:
                show_address_box(address)
                
                choice = input(f"\n{C.NEON_CYAN}    📍 OPEN IN GOOGLE MAPS? (y/n): {C.WHITE}").lower()
                if choice in ['y', 'yes']:
                    open_map(address)
        else:
            print(f"{C.NEON_RED}                      NO RECORDS FOUND!                      {C.RESET}")
            print("")
        
    except Exception as e:
        show_error_box(str(e))
    
    input(f"\n{C.NEON_YELLOW}    Press ENTER to return to main menu...{C.RESET}")

# ============================================
# ABOUT SECTION
# ============================================
def show_about():
    show_banner()
    
    print(f"{C.NEON_CYAN}                   CONTACT & SUPPORT INFO                   {C.RESET}")
    print("")
    print(f"{C.NEON_GREEN}    OWNER     : {C.WHITE}AMMAR{C.RESET}")
    print(f"{C.NEON_GREEN}    WHATSAPP  : {C.WHITE}03018787786{C.RESET}")
    print("")
    print(f"{C.NEON_YELLOW}    GROUP     : {C.WHITE}AMMAR PRIVATE{C.RESET}")
    print(f"{C.NEON_YELLOW}    LINK      : {C.WHITE}{CONFIG['group_link']}{C.RESET}")
    print("")
    print(f"{C.NEON_MAGENTA}    VERSION   : {CONFIG['version']}{C.RESET}")
    print("")
    
    choice = input(f"{C.NEON_CYAN}    [1] OPEN GROUP  [0] BACK: {C.WHITE}")
    if choice == '1':
        os.system(f"termux-open-url '{CONFIG['group_link']}'")

# ============================================
# MAIN MENU
# ============================================
def main():
    try:
        while True:
            show_banner()
            show_menu()
            
            choice = input(f"{C.NEON_GREEN}⚡ AMMAR@{C.NEON_YELLOW}TERMUX{C.NEON_BLUE} ~${C.WHITE} ").strip()
            print("")
            
            if choice in ['01', '1']:
                phone = input(f"{C.NEON_YELLOW}    📞 Enter Pakistani number: {C.WHITE}").strip()
                if phone and phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
                    search_database(phone)
                else:
                    print(f"{C.NEON_RED}    ❌ Invalid number format!{C.RESET}")
                    time.sleep(2)
            
            elif choice in ['02', '2']:
                show_about()
            
            elif choice in ['00', '0']:
                print(f"{C.NEON_RED}              THANK YOU FOR USING AMMAR SIM              {C.RESET}")
                print(f"{C.NEON_YELLOW}                  🔥 AMMAR PREMIUM EDITION 🔥            {C.RESET}")
                time.sleep(2)
                clear_screen()
                sys.exit(0)
            
            else:
                print(f"{C.NEON_RED}    ❌ Invalid option!{C.RESET}")
                time.sleep(2)
    
    except KeyboardInterrupt:
        print(f"\n{C.NEON_RED}    ⚡ INTERRUPTED BY USER{C.RESET}")
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
        print(f"{C.NEON_RED}    ❌ FATAL ERROR: {str(e)}{C.RESET}")
        time.sleep(3)
        sys.exit(1)
