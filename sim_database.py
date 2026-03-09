#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AMMAR SIM DATABASE - Professional Phone Number Lookup Tool
Created by: AMMAR
Version: 3.0 PREMIUM (AUTO-ADJUSTABLE)
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
    "version": "3.0 PREMIUM",
    "whatsapp": "03018787786",
    "group_link": "https://chat.whatsapp.com/F2zlsDXzwp05KKIrqj8vVj",
    "api_base": "https://howler-database-api.vercel.app/api/lookup?phone="
}

# ============================================
# TERMINAL SIZE DETECTION
# ============================================
def get_terminal_size():
    """Get terminal width and height"""
    try:
        columns, rows = os.get_terminal_size()
        return columns, rows
    except:
        return 80, 24  # Default size

def center_text(text, width=None):
    """Center text according to terminal width"""
    if width is None:
        width, _ = get_terminal_size()
    return text.center(width)

def create_border_line(char="─", width=None):
    """Create border line with exact width"""
    if width is None:
        width, _ = get_terminal_size()
    return char * (width - 4)  # -4 for the corners

# ============================================
# AUTO-ADJUSTABLE BOX FUNCTIONS
# ============================================
def print_top_border(color=C.NEON_BLUE):
    """Print top border with auto width"""
    width, _ = get_terminal_size()
    print(f"{color}    ╔{create_border_line('═', width-4)}╗{C.RESET}")

def print_mid_border(color=C.NEON_BLUE):
    """Print middle border with auto width"""
    width, _ = get_terminal_size()
    print(f"{color}    ╠{create_border_line('═', width-4)}╣{C.RESET}")

def print_bottom_border(color=C.NEON_BLUE):
    """Print bottom border with auto width"""
    width, _ = get_terminal_size()
    print(f"{color}    ╚{create_border_line('═', width-4)}╝{C.RESET}")

def print_line(text, color=C.WHITE, border_color=C.NEON_BLUE):
    """Print a line inside box with auto padding"""
    width, _ = get_terminal_size()
    content_width = width - 8  # -8 for borders and padding
    text = str(text)[:content_width]
    padding = content_width - len(text)
    print(f"{border_color}    ║{C.RESET} {color}{text}{' ' * padding}{border_color}║{C.RESET}")

def print_centered_line(text, color=C.WHITE, border_color=C.NEON_BLUE):
    """Print centered text inside box"""
    width, _ = get_terminal_size()
    content_width = width - 8
    centered = text.center(content_width)
    print(f"{border_color}    ║{C.RESET} {color}{centered}{border_color}║{C.RESET}")

# ============================================
# BANNER WITH AUTO-ADJUST
# ============================================
def show_banner():
    """Display banner with auto-adjustable design"""
    clear_screen()
    width, _ = get_terminal_size()
    
    # Top Border
    print_top_border(C.NEON_RED)
    
    # AMMAR ASCII Art (Fixed width version)
    ascii_lines = [
        "██████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗",
        "██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗",
        "███████║██╔████╔██║██╔████╔██║███████║██████╔╝",
        "██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗",
        "██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║  ██║",
        "╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝"
    ]
    
    for line in ascii_lines:
        print_centered_line(line, C.NEON_YELLOW, C.NEON_RED)
    
    print_mid_border(C.NEON_RED)
    print_centered_line("SIM DATABASE PREMIUM EDITION v3.0", C.NEON_GREEN, C.NEON_RED)
    print_bottom_border(C.NEON_RED)
    
    # Info Box
    print_top_border(C.NEON_BLUE)
    print_centered_line("", C.WHITE, C.NEON_BLUE)
    print_line(f"OWNER    : AMMAR", C.NEON_PINK, C.NEON_BLUE)
    print_line(f"WHATSAPP : 03018787786", C.NEON_PINK, C.NEON_BLUE)
    print_line(f"GROUP    : AMMAR PRIVATE", C.NEON_PINK, C.NEON_BLUE)
    print_line(f"MODE     : PREMIUM", C.NEON_GREEN, C.NEON_BLUE)
    print_line(f"API      : ONLINE", C.NEON_GREEN, C.NEON_BLUE)
    print_centered_line("", C.WHITE, C.NEON_BLUE)
    print_bottom_border(C.NEON_BLUE)

# ============================================
# MENU WITH AUTO-ADJUST
# ============================================
def show_menu():
    """Display main menu with auto-adjustable design"""
    width, _ = get_terminal_size()
    
    print_top_border(C.NEON_BLUE)
    print_centered_line("🔥 MAIN MENU OPTIONS 🔥", C.NEON_GREEN, C.NEON_BLUE)
    print_mid_border(C.NEON_BLUE)
    print_centered_line("", C.WHITE, C.NEON_BLUE)
    print_line("[01] 🔍 SEARCH DATABASE     [MAPS]", C.NEON_CYAN, C.NEON_BLUE)
    print_line("[02] 📞 CONTACT NUMBER      [SAVED]", C.NEON_CYAN, C.NEON_BLUE)
    print_line("[03] 👥 WHATSAPP GROUP      [OPEN]", C.NEON_CYAN, C.NEON_BLUE)
    print_line("[04] ℹ️ NUMBER INFORMATION  [SEARCH]", C.NEON_CYAN, C.NEON_BLUE)
    print_line("[00] ❌ EXIT SYSTEM         [QUIT]", C.NEON_RED, C.NEON_BLUE)
    print_centered_line("", C.WHITE, C.NEON_BLUE)
    print_bottom_border(C.NEON_BLUE)

# ============================================
# SEARCH HEADER WITH AUTO-ADJUST
# ============================================
def show_search_header(phone):
    """Display search header with auto-adjustable design"""
    print_top_border(C.NEON_CYAN)
    print_centered_line("INITIALIZING DATABASE SCAN", C.WHITE, C.NEON_CYAN)
    print_mid_border(C.NEON_CYAN)
    print_line(f"TARGET   : {phone}", C.NEON_GREEN, C.NEON_CYAN)
    print_line(f"SECURITY : BYPASSING FIREWALL...", C.NEON_YELLOW, C.NEON_CYAN)
    print_bottom_border(C.NEON_CYAN)

# ============================================
# RESULTS TABLE WITH AUTO-ADJUST
# ============================================
def display_results_table(results):
    """Display results with auto-adjustable design"""
    if not results:
        print_top_border(C.NEON_RED)
        print_centered_line("❌ NO DATA FOUND!", C.WHITE, C.NEON_RED)
        print_bottom_border(C.NEON_RED)
        return
    
    print_top_border(C.NEON_GREEN)
    print_centered_line("📊 DATABASE RECORDS", C.NEON_YELLOW, C.NEON_GREEN)
    print_mid_border(C.NEON_GREEN)
    
    for i, item in enumerate(results[:8]):  # Show first 8 results
        key = item['key'].upper()
        value = item['value']
        
        if len(value) > 40:
            value = value[:37] + "..."
        
        print_line(f"{key}: {value}", C.WHITE, C.NEON_GREEN)
    
    print_bottom_border(C.NEON_GREEN)

# ============================================
# ADDRESS BOX WITH AUTO-ADJUST
# ============================================
def show_address_box(address):
    """Display address with auto-adjustable design"""
    print_top_border(C.NEON_GREEN)
    print_centered_line("📍 ADDRESS DETECTED", C.NEON_YELLOW, C.NEON_GREEN)
    print_mid_border(C.NEON_GREEN)
    
    # Split long address into multiple lines
    words = address.split()
    line = ""
    for word in words:
        if len(line + word) < 50:
            line += word + " "
        else:
            print_line(line.strip(), C.WHITE, C.NEON_GREEN)
            line = word + " "
    if line:
        print_line(line.strip(), C.WHITE, C.NEON_GREEN)
    
    print_bottom_border(C.NEON_GREEN)

# ============================================
# ERROR BOX WITH AUTO-ADJUST
# ============================================
def show_error_box(error):
    """Display error with auto-adjustable design"""
    print_top_border(C.NEON_RED)
    print_centered_line("❌ ERROR", C.WHITE, C.NEON_RED)
    print_mid_border(C.NEON_RED)
    print_line(str(error)[:60], C.NEON_YELLOW, C.NEON_RED)
    print_bottom_border(C.NEON_RED)

# ============================================
# CONTACT NUMBER INFO
# ============================================
def show_contact_number():
    """Display contact number information"""
    show_banner()
    
    print_top_border(C.NEON_CYAN)
    print_centered_line("📞 CONTACT NUMBER INFO", C.NEON_PINK, C.NEON_CYAN)
    print_mid_border(C.NEON_CYAN)
    print_line("", C.WHITE, C.NEON_CYAN)
    print_line("OWNER NUMBER    : 03018787786", C.NEON_GREEN, C.NEON_CYAN)
    print_line("OWNER NAME      : AMMAR", C.NEON_GREEN, C.NEON_CYAN)
    print_line("NETWORK         : PAKISTAN", C.NEON_GREEN, C.NEON_CYAN)
    print_line("TYPE            : MOBILE", C.NEON_GREEN, C.NEON_CYAN)
    print_line("STATUS          : ACTIVE", C.NEON_GREEN, C.NEON_CYAN)
    print_line("", C.WHITE, C.NEON_CYAN)
    print_bottom_border(C.NEON_CYAN)
    
    input(f"\n{C.NEON_YELLOW}    Press ENTER to continue...{C.RESET}")

# ============================================
# WHATSAPP GROUP INFO
# ============================================
def show_whatsapp_group():
    """Display WhatsApp group information"""
    show_banner()
    
    print_top_border(C.NEON_CYAN)
    print_centered_line("👥 WHATSAPP GROUP INFO", C.NEON_PINK, C.NEON_CYAN)
    print_mid_border(C.NEON_CYAN)
    print_line("", C.WHITE, C.NEON_CYAN)
    print_line("GROUP NAME      : AMMAR PRIVATE", C.NEON_GREEN, C.NEON_CYAN)
    print_line("GROUP TYPE      : WHATSAPP GROUP", C.NEON_GREEN, C.NEON_CYAN)
    print_line("CREATED BY      : AMMAR", C.NEON_GREEN, C.NEON_CYAN)
    print_line("MEMBERS         : PRIVATE", C.NEON_GREEN, C.NEON_CYAN)
    print_line("", C.WHITE, C.NEON_CYAN)
    print_bottom_border(C.NEON_CYAN)
    
    print(f"\n{C.NEON_YELLOW}    Open group link in browser?{C.RESET}")
    choice = input(f"{C.NEON_CYAN}    [1] OPEN GROUP  [0] BACK: {C.WHITE}")
    if choice == '1':
        os.system(f"termux-open-url '{CONFIG['group_link']}'")

# ============================================
# DATA EXTRACTION FUNCTIONS
# ============================================
def extract_all_data(data):
    """Extract all data from API response"""
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

# ============================================
# MAP FUNCTION
# ============================================
def open_map(address):
    """Open address in Google Maps"""
    if address and len(address) > 5:
        clean_addr = address.replace('null', '').replace('no', '').replace('none', '').strip()
        if clean_addr and len(clean_addr) > 3:
            search_url = f"https://www.google.com/maps/search/{clean_addr.replace(' ', '+')}"
            
            print_top_border(C.NEON_GREEN)
            print_centered_line("📍 LOCATION FOUND! OPENING MAPS...", C.NEON_YELLOW, C.NEON_GREEN)
            print_bottom_border(C.NEON_GREEN)
            
            os.system(f"termux-open-url '{search_url}'")
            return True
    return False

# ============================================
# SEARCH FUNCTION
# ============================================
def search_database(phone):
    """Search phone number in database"""
    show_banner()
    show_search_header(phone)
    
    # Format phone number
    original_phone = phone
    if phone.startswith('0'):
        phone = '+92' + phone[1:]
    elif not phone.startswith('+'):
        phone = '+92' + phone
    
    # Loading animation
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
        
        print_top_border(C.NEON_GREEN)
        print_centered_line("✅ DATABASE ACCESS GRANTED", C.WHITE, C.NEON_GREEN)
        print_bottom_border(C.NEON_GREEN)
        
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
            print_top_border(C.NEON_RED)
            print_centered_line("❌ NO RECORDS FOUND!", C.WHITE, C.NEON_RED)
            print_bottom_border(C.NEON_RED)
        
    except Exception as e:
        show_error_box(str(e))
    
    input(f"\n{C.NEON_YELLOW}    Press ENTER to return to main menu...{C.RESET}")

# ============================================
# MAIN MENU
# ============================================
def main():
    """Main program loop"""
    try:
        while True:
            show_banner()
            show_menu()
            
            print(f"\n{C.NEON_CYAN}    ╭{'─' * 50}╮")
            choice = input(f"    {C.NEON_GREEN}⚡ AMMAR@{C.NEON_YELLOW}TERMUX{C.NEON_BLUE} ~${C.WHITE} ").strip()
            print(f"    {C.NEON_CYAN}╰{'─' * 50}╯{C.RESET}")
            
            if choice in ['01', '1']:
                phone = input(f"\n{C.NEON_YELLOW}    📞 Enter Pakistani number: {C.WHITE}").strip()
                if phone and phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
                    search_database(phone)
                else:
                    print(f"\n{C.NEON_RED}    ❌ Invalid number format!{C.RESET}")
                    time.sleep(2)
            
            elif choice in ['02', '2']:
                show_contact_number()
            
            elif choice in ['03', '3']:
                show_whatsapp_group()
            
            elif choice in ['04', '4']:
                phone = input(f"\n{C.NEON_YELLOW}    📞 Enter number to search: {C.WHITE}").strip()
                if phone and phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
                    search_database(phone)
                else:
                    print(f"\n{C.NEON_RED}    ❌ Invalid number format!{C.RESET}")
                    time.sleep(2)
            
            elif choice in ['00', '0']:
                print_top_border(C.NEON_RED)
                print_centered_line("THANK YOU FOR USING AMMAR SIM", C.WHITE, C.NEON_RED)
                print_centered_line("🔥 AMMAR PREMIUM EDITION 🔥", C.NEON_YELLOW, C.NEON_RED)
                print_bottom_border(C.NEON_RED)
                time.sleep(2)
                clear_screen()
                sys.exit(0)
            
            else:
                print(f"\n{C.NEON_RED}    ❌ Invalid option!{C.RESET}")
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
