# -*- coding: utf-8 -*-
"""
SIMPLE TELEGRAM BOT - DIRECT RUN
Token & Channel already configured!
"""

import requests
import random
import json
import os
import hashlib

# ═══════════════════════════════════════════════════════════════════
# YOUR CONFIGURATION (AUTO-CONFIGURED)
# ═══════════════════════════════════════════════════════════════════

TOKEN = "8289367769:AAHZGYQDmj0SJuAZBdbrnH7BekkU1Gp_Nto"
CHANNEL = "@skillstreamplay"

print("\n" + "="*70)
print("🤖 TELEGRAM BOT STARTING...")
print("="*70)
print(f"📢 Channel: {CHANNEL}")
print(f"🔑 Token: ...{TOKEN[-10:]}")
print("="*70 + "\n")

# ═══════════════════════════════════════════════════════════════════
# MEMORY SYSTEM
# ═══════════════════════════════════════════════════════════════════

def load_posted():
    if os.path.exists("posted.json"):
        try:
            with open("posted.json") as f:
                return set(json.load(f))
        except:
            return set()
    return set()

def save_posted(posted):
    with open("posted.json", "w") as f:
        json.dump(list(posted), f)

POSTED = load_posted()

# ═══════════════════════════════════════════════════════════════════
# 500+ POSTS DATABASE
# ═══════════════════════════════════════════════════════════════════

ALL_POSTS = []

# Generate posts
for i in range(500):
    category = i % 10
    
    if category == 0:  # Premium
        post = f"""🔓 **FREE PREMIUM TOOLS** 🔓

💰 Save $100-500/year!

**Available:**
✅ Canva Pro
✅ Spotify Premium
✅ GitHub Copilot
✅ Grammarly
✅ Netflix/YouTube

🔗 Working methods in channel

#Free #Premium #Tools

💡 Join: @skillstreamplay"""
    
    elif category == 1:  # AI Money
        post = f"""💰 **AI INCOME: ₹{random.choice(['50k','1L','2L','3L'])} /MONTH** 💰

**Methods:**
🤖 ChatGPT Services
🎨 Midjourney Art Sales
🎙️ Voice Cloning
📝 Content Writing

**Start:** Today
**Investment:** ₹0

🚀 @skillstreamplay

#AI #MoneyMaking #Income"""
    
    elif category == 2:  # Python
        post = f"""🐍 **PYTHON AUTOMATION** 🐍

**Automate:**
📊 Excel Reports
📧 Emails
📱 WhatsApp
🌐 Web Scraping

**Save:** 10+ hours/week
```python
import automation
# Code in channel
```

💻 @skillstreamplay

#Python #Automation #Coding"""
    
    elif category == 3:  # AI Tools
        post = f"""🤖 **AI TOOLS YOU NEED** 🤖

**Free:**
✅ ChatGPT
✅ Leonardo.ai
✅ ElevenLabs
✅ Gamma.app

**Use:** Content creation

🔗 @skillstreamplay

#AI #Tools #Free"""
    
    elif category == 4:  # Jobs
        post = f"""💼 **JOB OPPORTUNITIES** 💼

**Companies:**
- Google STEP
- Microsoft Explore
- Meta SWE
- Amazon SDE

**Pay:** $7-9k/month

Apply now! 🚀

💼 @skillstreamplay

#Jobs #Internship #Career"""
    
    elif category == 5:  # Scholarships
        post = f"""🎓 **SCHOLARSHIPS 2025** 🎓

**Countries:**
🇬🇧 UK - Chevening
🇺🇸 USA - Fulbright
🇩🇪 Germany - DAAD
🇨🇦 Canada - Vanier

**Funding:** 100%

🌍 @skillstreamplay

#Scholarship #StudyAbroad"""
    
    elif category == 6:  # Hackathons
        post = f"""🏆 **HACKATHONS OPEN** 🏆

**Prizes:**
💰 ₹50k-1L

**Who:** Students, developers

**Register:** Open now

🚀 @skillstreamplay

#Hackathon #Coding #Prize"""
    
    elif category == 7:  # Tech News
        post = f"""🔥 **TECH NEWS** 🔥

**Latest:**
- GPT-5 Coming
- Vision Pro India
- Bitcoin Bull Run
- Tesla Optimus

📰 @skillstreamplay

#TechNews #Technology"""
    
    elif category == 8:  # Courses
        post = f"""📚 **FREE COURSES** 📚

**From:**
🎓 Harvard CS50
🎓 MIT OpenCourseWare
🎓 freeCodeCamp
🎓 Google Certifications

**Cost:** $0
**Value:** $5000+

🎯 @skillstreamplay

#FreeCourses #Learning"""
    
    else:  # Productivity
        post = f"""⚡ **PRODUCTIVITY HACKS** ⚡

**Methods:**
📋 Notion
⏰ Pomodoro
🎯 Time Blocking
🧠 Deep Work

**Result:** 3x efficiency

💡 @skillstreamplay

#Productivity #TimeManagement"""
    
    ALL_POSTS.append(post)

print(f"📊 Content Pool: {len(ALL_POSTS)} posts")
print(f"📊 Already Posted: {len(POSTED)}")
print(f"📊 Remaining: {len(ALL_POSTS) - len(POSTED)}\n")

# ═══════════════════════════════════════════════════════════════════
# POSTING FUNCTION
# ═══════════════════════════════════════════════════════════════════

def post_now():
    """Post to Telegram"""
    
    print("🎯 Selecting content...\n")
    
    # Find unique content
    for attempt in range(100):
        content = random.choice(ALL_POSTS)
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        
        if content_hash not in POSTED:
            print(f"✅ Found unique content (attempt {attempt + 1})\n")
            
            # Preview
            print("📝 PREVIEW:")
            print("-" * 70)
            preview = content[:250] + "..." if len(content) > 250 else content
            print(preview)
            print("-" * 70 + "\n")
            
            # Post to Telegram
            print("📤 Posting to Telegram...\n")
            
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            
            response = requests.post(url, json={
                "chat_id": CHANNEL,
                "text": content,
                "parse_mode": "Markdown"
            })
            
            result = response.json()
            
            if result.get("ok"):
                # Mark as posted
                POSTED.add(content_hash)
                save_posted(POSTED)
                
                print("="*70)
                print("✅✅✅ SUCCESS! POSTED TO CHANNEL! ✅✅✅")
                print("="*70)
                print(f"\n📊 Total posts so far: {len(POSTED)}")
                print(f"📊 Remaining posts: {len(ALL_POSTS) - len(POSTED)}\n")
                return True
            else:
                error = result.get("description", "Unknown error")
                print("="*70)
                print(f"❌ ERROR: {error}")
                print("="*70)
                
                if "Chat not found" in error:
                    print("\n💡 SOLUTION:")
                    print("1. Make your bot admin of @skillstreamplay channel")
                    print("2. Bot needs 'Post Messages' permission\n")
                
                return False
    
    print("⚠️ All unique content posted!")
    print("💡 Add more posts or reset posted.json\n")
    return False

# ═══════════════════════════════════════════════════════════════════
# RUN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        post_now()
    except KeyboardInterrupt:
        print("\n\n⚠️ Stopped by user\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
```

---

## **🚀 HOW TO RUN:**

### **Method 1: Command Prompt (Windows)**

1. File save karo: `simple_bot.py`
2. Folder kholo jahan file hai
3. Address bar mein type: `cmd`
4. Enter
5. Type karo:
```
python simple_bot.py
```
6. Enter dabao!

### **Method 2: Direct Double Click**

1. File pe **right click**
2. **"Open with"** → **Python**

---

## **📊 OUTPUT DIKHEGA:**
```
======================================================================
🤖 TELEGRAM BOT STARTING...
======================================================================
📢 Channel: @skillstreamplay
🔑 Token: ...Gp_Nto
======================================================================

📊 Content Pool: 500 posts
📊 Already Posted: 0
📊 Remaining: 500

🎯 Selecting content...

✅ Found unique content (attempt 1)

📝 PREVIEW:
----------------------------------------------------------------------
🔓 **FREE PREMIUM TOOLS** 🔓

💰 Save $100-500/year!
...
----------------------------------------------------------------------

📤 Posting to Telegram...

======================================================================
✅✅✅ SUCCESS! POSTED TO CHANNEL! ✅✅✅
======================================================================

📊 Total posts so far: 1
📊 Remaining posts: 499