#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AMMAR SIM DATABASE - Professional Phone Number Lookup Tool
Created by: AMMAR
Version: 2.0 PREMIUM (PERFECT ALIGNED)
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
# CONFIGURATION - YOUR NUMBERS ADDED
# ============================================
CONFIG = {
    "owner": "AMMAR",
    "version": "2.0 PREMIUM",
    "whatsapp": "03018787786",
    "group_link": "https://chat.whatsapp.com/F2zlsDXzwp05KKIrqj8vVj",
    "api_base": "https://howler-database-api.vercel.app/api/lookup?phone=",
    "saved_numbers": {
        "1": {"name": "AMMAR (OWNER)", "number": "03018787786"},
        "2": {"name": "GROUP LINK", "number": "group"},
        "3": {"name": "TEST NUMBER 1", "number": "03123456789"},
        "4": {"name": "TEST NUMBER 2", "number": "03234567890"}
    }
}

# ============================================
# UTILITY FUNCTIONS
# ============================================
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(text="PROCESSING"):
    chars = "⣾⣽⣻⢿⡿⣟⣯⣷"
    for i in range(20):
        for char in chars:
            sys.stdout.write(f'\r{C.NEON_CYAN}  ║ {text} {char} ║{C.RESET}')
            sys.stdout.flush()
            time.sleep(0.03)
    print()

# ============================================
# PERFECTLY ALIGNED BANNER
# ============================================
def show_banner():
    clear_screen()
    
    banner = f"""
{C.NEON_RED}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_RED}    ║{C.NEON_YELLOW}        █████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗      {C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW}       ██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗     {C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW}       ███████║██╔████╔██║██╔████╔██║███████║██████╔╝     {C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW}       ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗     {C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW}       ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║  ██║     {C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW}       ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     {C.NEON_RED}║
{C.NEON_RED}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
    
{C.NEON_BLUE}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_BLUE}    ║{C.NEON_GREEN}              SIM DATABASE PREMIUM EDITION v2.0              {C.NEON_BLUE}║
{C.NEON_BLUE}    ╠══════════════════════════════════════════════════════════════╣
{C.NEON_BLUE}    ║                                                                ║
{C.NEON_BLUE}    ║  {C.NEON_PINK}OWNER    : {C.NEON_YELLOW}AMMAR                                 {C.NEON_BLUE}║
{C.NEON_BLUE}    ║  {C.NEON_PINK}WHATSAPP : {C.NEON_YELLOW}03018787786                           {C.NEON_BLUE}║
{C.NEON_BLUE}    ║  {C.NEON_PINK}GROUP    : {C.NEON_YELLOW}AMMAR PRIVATE                          {C.NEON_BLUE}║
{C.NEON_BLUE}    ║  {C.NEON_PINK}MODE     : {C.NEON_GREEN}PREMIUM                                {C.NEON_BLUE}║
{C.NEON_BLUE}    ║  {C.NEON_PINK}API      : {C.NEON_GREEN}ONLINE                                 {C.NEON_BLUE}║
{C.NEON_BLUE}    ║                                                                ║
{C.NEON_BLUE}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
    """
    print(banner)

# ============================================
# PERFECTLY ALIGNED SEARCH HEADER
# ============================================
def show_search_header(phone):
    print(f"""
{C.NEON_CYAN}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_CYAN}    ║{C.WHITE}                    INITIALIZING DATABASE SCAN                    {C.NEON_CYAN}║
{C.NEON_CYAN}    ╠══════════════════════════════════════════════════════════════╣
{C.NEON_CYAN}    ║{C.NEON_GREEN}  TARGET   : {C.WHITE}{phone:<51}{C.NEON_CYAN}║
{C.NEON_CYAN}    ║{C.NEON_GREEN}  SECURITY : {C.NEON_YELLOW}BYPASSING FIREWALL...                {C.NEON_CYAN}║
{C.NEON_CYAN}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
    """)

# ============================================
# DATA EXTRACTION FUNCTIONS
# ============================================
def extract_all_data(data, indent=0):
    results = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            key_lower = str(key).lower()
            
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
# PERFECTLY ALIGNED RESULTS TABLE
# ============================================
def display_results_table(results):
    if not results:
        print(f"""
{C.NEON_RED}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_RED}    ║{C.WHITE}                    ❌ NO DATA FOUND!                           {C.NEON_RED}║
{C.NEON_RED}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
        """)
        return
    
    print(f"""
{C.NEON_GREEN}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_GREEN}    ║{C.NEON_YELLOW}                    📊 DATABASE RECORDS                       {C.NEON_GREEN}║
{C.NEON_GREEN}    ╠══════════════════════════════════════════════════════════════╣{C.RESET}
    """)
    
    for item in results:
        indent = "    " + "  " * item['indent']
        key = item['key'].upper()
        value = item['value']
        
        if len(value) > 60:
            value = value[:57] + "..."
        
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
        
        print(f"{indent}{key_color}► {key:<15} {C.NEON_PINK}: {C.WHITE}{value}")
    
    print(f"""
{C.NEON_GREEN}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
    """)

# ============================================
# MAP FUNCTION
# ============================================
def open_map(address):
    if address and len(address) > 5:
        clean_addr = address.replace('null', '').replace('no', '').replace('none', '').strip()
        if clean_addr and len(clean_addr) > 3:
            search_url = f"https://www.google.com/maps/search/{clean_addr.replace(' ', '+')}"
            
            print(f"""
{C.NEON_GREEN}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_GREEN}    ║{C.NEON_YELLOW}              📍 LOCATION FOUND! OPENING MAPS...              {C.NEON_GREEN}║
{C.NEON_GREEN}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
            """)
            
            os.system(f"termux-open-url '{search_url}'")
            return True
    return False

# ============================================
# SEARCH FUNCTION
# ============================================
def search_database(phone):
    show_banner()
    show_search_header(phone)
    
    if phone.lower() == "group":
        print(f"""
{C.NEON_CYAN}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_CYAN}    ║{C.NEON_GREEN}                    OPENING GROUP LINK...                      {C.NEON_CYAN}║
{C.NEON_CYAN}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
        """)
        os.system(f"termux-open-url '{CONFIG['group_link']}'")
        input(f"\n{C.NEON_YELLOW}    Press ENTER to continue...{C.RESET}")
        return
    
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
            print(f"""
{C.NEON_RED}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_RED}    ║{C.WHITE}                  DATABASE CONNECTION FAILED                      {C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW}                  STATUS CODE: {response.status_code}                           {C.NEON_RED}║
{C.NEON_RED}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
            """)
            input(f"\n{C.NEON_YELLOW}    Press ENTER to continue...{C.RESET}")
            return
        
        data = response.json()
        
        print(f"""
{C.NEON_GREEN}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_GREEN}    ║{C.WHITE}                    DATABASE ACCESS GRANTED                      {C.NEON_GREEN}║
{C.NEON_GREEN}    ╠══════════════════════════════════════════════════════════════╣
{C.NEON_GREEN}    ║{C.NEON_CYAN}                    FETCHING RECORDS...                         {C.NEON_GREEN}║
{C.NEON_GREEN}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
        """)
        
        time.sleep(1)
        
        if data and data != {}:
            results = extract_all_data(data)
            display_results_table(results)
            
            address = find_address(data)
            
            if address:
                print(f"""
{C.NEON_GREEN}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_GREEN}    ║{C.NEON_YELLOW}                       ADDRESS DETECTED                         {C.NEON_GREEN}║
{C.NEON_GREEN}    ╠══════════════════════════════════════════════════════════════╣
{C.NEON_GREEN}    ║{C.WHITE}  {address[:76]}{'...' if len(address) > 76 else '':<2}{C.NEON_GREEN}║
{C.NEON_GREEN}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
                """)
                
                while True:
                    choice = input(f"\n{C.NEON_CYAN}    📍 OPEN IN GOOGLE MAPS? (y/n): {C.WHITE}").lower()
                    if choice in ['y', 'n', 'yes', 'no']:
                        break
                    print(f"{C.NEON_RED}    ❌ Please enter 'y' or 'n'{C.RESET}")
                
                if choice in ['y', 'yes']:
                    open_map(address)
        else:
            print(f"""
{C.NEON_RED}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_RED}    ║{C.WHITE}                      NO RECORDS FOUND!                          {C.NEON_RED}║
{C.NEON_RED}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
            """)
        
    except Exception as e:
        print(f"""
{C.NEON_RED}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_RED}    ║{C.WHITE}                        ERROR:                                  {C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW}  {str(e)[:76]:<76}{C.NEON_RED}║
{C.NEON_RED}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
        """)
    
    input(f"\n{C.NEON_YELLOW}    Press ENTER to return to main menu...{C.RESET}")

# ============================================
# NUMBER SELECTION MENU
# ============================================
def select_number():
    print(f"""
{C.NEON_BLUE}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_BLUE}    ║{C.NEON_GREEN}                   SELECT SAVED NUMBER                        {C.NEON_BLUE}║
{C.NEON_BLUE}    ╠══════════════════════════════════════════════════════════════╣{C.RESET}
    """)
    
    for key, value in CONFIG["saved_numbers"].items():
        print(f"    {C.NEON_YELLOW}[{key}]{C.NEON_CYAN} {value['name']}{C.RESET}")
    
    print(f"    {C.NEON_YELLOW}[0]{C.NEON_CYAN} MANUAL ENTRY{C.RESET}")
    print(f"""
{C.NEON_BLUE}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
    """)
    
    choice = input(f"{C.NEON_GREEN}    ⚡ SELECT OPTION: {C.WHITE}").strip()
    
    if choice == "0":
        return input(f"{C.NEON_CYAN}    📞 ENTER NUMBER: {C.WHITE}").strip()
    elif choice in CONFIG["saved_numbers"]:
        return CONFIG["saved_numbers"][choice]["number"]
    else:
        print(f"{C.NEON_RED}    ❌ INVALID OPTION!{C.RESET}")
        time.sleep(1)
        return None

# ============================================
# ABOUT SECTION
# ============================================
def show_about():
    show_banner()
    
    print(f"""
{C.NEON_CYAN}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_CYAN}    ║{C.NEON_PINK}                   CONTACT & SUPPORT INFO                       {C.NEON_CYAN}║
{C.NEON_CYAN}    ╠══════════════════════════════════════════════════════════════╣
{C.NEON_CYAN}    ║                                                                ║
{C.NEON_CYAN}    ║  {C.NEON_GREEN}OWNER     : {C.WHITE}AMMAR                                      {C.NEON_CYAN}║
{C.NEON_CYAN}    ║  {C.NEON_GREEN}WHATSAPP  : {C.WHITE}03018787786                                {C.NEON_CYAN}║
{C.NEON_CYAN}    ║                                                                ║
{C.NEON_CYAN}    ║  {C.NEON_YELLOW}GROUP LINK : {C.WHITE}                                         {C.NEON_CYAN}║
{C.NEON_CYAN}    ║  {C.NEON_CYAN}{CONFIG['group_link']}  {C.NEON_CYAN}║
{C.NEON_CYAN}    ║                                                                ║
{C.NEON_CYAN}    ║  {C.NEON_MAGENTA}VERSION    : {CONFIG['version']}                              {C.NEON_CYAN}║
{C.NEON_CYAN}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
    """)
    
    print(f"\n{C.NEON_YELLOW}    🚀 OPEN GROUP LINK IN BROWSER?{C.RESET}")
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
            
            print(f"""
{C.NEON_BLUE}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_BLUE}    ║{C.NEON_GREEN}                      MAIN MENU OPTIONS                          {C.NEON_BLUE}║
{C.NEON_BLUE}    ╠══════════════════════════════════════════════════════════════╣
{C.NEON_BLUE}    ║                                                                ║
{C.NEON_BLUE}    ║      {C.NEON_YELLOW}[01]{C.NEON_CYAN} 🔍 SEARCH DATABASE          {C.NEON_PINK}[MAPS]          {C.NEON_BLUE}║
{C.NEON_BLUE}    ║      {C.NEON_YELLOW}[02]{C.NEON_CYAN} 📱 CONTACT & SUPPORT        {C.NEON_PINK}[GROUP]        {C.NEON_BLUE}║
{C.NEON_BLUE}    ║      {C.NEON_YELLOW}[03]{C.NEON_CYAN} 📞 SAVED NUMBERS            {C.NEON_PINK}[QUICK]        {C.NEON_BLUE}║
{C.NEON_BLUE}    ║      {C.NEON_YELLOW}[00]{C.NEON_RED} ❌ EXIT SYSTEM               {C.NEON_PINK}[QUIT]         {C.NEON_BLUE}║
{C.NEON_BLUE}    ║                                                                ║
{C.NEON_BLUE}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
            """)
            
            print(f"\n{C.NEON_CYAN}    ╭{'─' * 60}╮")
            choice = input(f"    {C.NEON_GREEN}⚡ AMMAR@{C.NEON_YELLOW}TERMUX{C.NEON_BLUE} ~${C.WHITE} ").strip()
            print(f"    {C.NEON_CYAN}╰{'─' * 60}╯{C.RESET}")
            
            if choice in ['01', '1']:
                phone = input(f"\n{C.NEON_YELLOW}    📞 Enter Pakistani number: {C.WHITE}").strip()
                if phone and phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
                    search_database(phone)
                else:
                    print(f"\n{C.NEON_RED}    ❌ Invalid number format!{C.RESET}")
                    time.sleep(2)
            
            elif choice in ['02', '2']:
                show_about()
            
            elif choice in ['03', '3']:
                phone = select_number()
                if phone:
                    search_database(phone)
            
            elif choice in ['00', '0']:
                print(f"""
{C.NEON_RED}    ╔══════════════════════════════════════════════════════════════╗
{C.NEON_RED}    ║{C.WHITE}              THANK YOU FOR USING AMMAR SIM                    {C.NEON_RED}║
{C.NEON_RED}    ║{C.NEON_YELLOW}                  🔥 AMMAR PREMIUM EDITION 🔥                 {C.NEON_RED}║
{C.NEON_RED}    ╚══════════════════════════════════════════════════════════════╝{C.RESET}
                """)
                time.sleep(2)
                clear_screen()
                sys.exit(0)
            
            else:
                print(f"\n{C.NEON_RED}    ❌ Invalid option! Please choose 01, 02, 03, or 00{C.RESET}")
                time.sleep(2)
    
    except KeyboardInterrupt:
        print(f"\n\n{C.NEON_RED}    ⚡ INTERRUPTED BY USER{C.RESET}")
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
