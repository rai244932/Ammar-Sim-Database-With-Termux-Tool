#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, time, requests, json

# ============================================
# CYBER-NEON COLOR ENGINE
# ============================================
class C:
    G = '\033[92m' # Green
    Y = '\033[93m' # Yellow
    R = '\033[91m' # Red
    C = '\033[96m' # Cyan
    W = '\033[97m' # White
    M = '\033[95m' # Magenta
    S = '\033[0m'  # Reset

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# ============================================
# UPDATED: AUTO-FORMAT NUMBER (UPDATE 1)
# ============================================
def format_number(phone):
    phone = phone.replace("+", "").replace(" ", "").replace("-", "")
    if phone.startswith("0"):
        return "92" + phone[1:]
    elif phone.startswith("92"):
        return phone
    else:
        return "92" + phone

# ============================================
# DYNAMIC ADAPTIVE DESIGN (UPDATE 2)
# ============================================
def display_detailed_results(results):
    if not results:
        print(f"\n  {C.R}[!] NO ENCRYPTED RECORDS FOUND.{C.S}")
        return

    # باکس کے سائز کا تعین (Dynamic Width)
    max_val_len = max(len(str(item['value'])) for item in results)
    width = max_val_len + 20
    if width > 70: width = 70
    if width < 45: width = 45
    
    line = "═" * (width - 2)
    
    print(f"\n  {C.M}╔{line}╗")
    print(f"  {C.M}║{C.Y}          DATABASE RECORD RECOVERY          {C.M}║")
    print(f"  {C.M}╠{line}╣")
    
    for item in results:
        key = item['key'].upper()
        val = str(item['value'])
        
        # ٹیکسٹ ریپنگ (بڑے ایڈریس کے لیے)
        wrapped_val = (val[:width-22] + '..') if len(val) > (width-20) else val
        
        print(f"  {C.M}║ {C.G}{key:<12} {C.C}» {C.W}{wrapped_val:<{width-18}} {C.M}║")
    
    print(f"  {C.M}╚{line}╝")

# ============================================
# CORE ENGINE
# ============================================
def search_engine(phone):
    clear()
    formatted_num = format_number(phone)
    
    print(f"\n  {C.C}[~] {C.W}TARGET ID: {C.Y}{formatted_num}{C.S}")
    print(f"  {C.G}[+] {C.W}ACCESSING AMMAR-RAI TECH™ SERVERS...{C.S}")
    
    # لوڈنگ ایفیکٹ
    for i in range(3):
        sys.stdout.write(f"\r  {C.C}[*] {C.W}DECRYPTING{'.'*(i+1)}{C.S}")
        sys.stdout.flush()
        time.sleep(0.5)

    try:
        url = f"https://howler-database-api.vercel.app/api/lookup?phone={formatted_num}"
        res = requests.get(url, timeout=15)
        
        if res.status_code == 200:
            data = res.json()
            results = []
            for k, v in data.items():
                if any(x in str(k).lower() for x in ["status", "success", "developer", "count"]): continue
                if v and str(v).lower() not in ["null", "none", "no"]:
                    results.append({'key': str(k), 'value': str(v)})
            
            display_detailed_results(results)
            
            # آٹو سیو ریکارڈ
            if results:
                with open("ammar_database.json", "a") as f:
                    json.dump({formatted_num: data}, f)
                    f.write("\n")
                print(f"  {C.G}[✔] {C.W}RECORD ARCHIVED IN {C.Y}ammar_database.json{C.S}")
        else:
            print(f"  {C.R}[!] SERVER ACCESS DENIED: {res.status_code}{C.S}")
            
    except Exception as e:
        print(f"  {C.R}[!] CONNECTION TIMEOUT!{C.S}")
    
    input(f"\n  {C.Y}Press [ENTER] to return...{C.S}")

# ============================================
# MAIN INTERFACE
# ============================================
def main():
    while True:
        clear()
        print(f"{C.G}   █████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗ ")
        print(f"   ██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗")
        print(f"   ███████║██╔████╔██║██╔████╔██║███████║██████╔╝")
        print(f"   ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗")
        print(f"   ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║  ██║")
        print(f"   {C.C}DEV: {C.Y}AMMAR RAI {C.W}| {C.C}BRAND: {C.M}AMMAR-RAI TECH™ {C.W}v5.0{C.S}")
        
        print(f"\n  {C.W}[01] {C.G}DECRYPT PHONE NUMBER")
        print(f"  {C.W}[02] {C.C}SHOW SAVED ARCHIVES")
        print(f"  {C.W}[00] {C.R}TERMINATE SYSTEM")
        
        cmd = input(f"\n  {C.G}RAI-AMMAR{C.W}@{C.C}DB{C.W}:~# {C.Y}").strip()
        
        if cmd in ['1', '01']:
            num = input(f"  {C.C}[?] {C.W}Enter Phone: {C.G}").strip()
            if num: search_engine(num)
        elif cmd in ['2', '02']:
            clear()
            print(f"\n  {C.Y}--- SAVED SEARCH HISTORY ---{C.S}\n")
            if os.path.exists("ammar_database.json"):
                os.system("cat ammar_database.json")
            else:
                print(f"  {C.R}No history found.{C.S}")
            input(f"\n  {C.W}Press Enter...")
        elif cmd in ['0', '00']:
            print(f"  {C.R}SHUTTING DOWN...{C.S}")
            break

if __name__ == "__main__":
    main()
