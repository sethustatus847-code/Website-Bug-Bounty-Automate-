# Website-Bug-Bounty-Automate-

# ⚡ DarkVoid Vulnerability Scanner

Termux හෝ Linux පරිසරයක ධාවනය කළ හැකි, Flask මත පදනම් වූ සරල සහ ඵලදායී Web Vulnerability Scanner එකක්. මෙය ඉලක්කගත වෙබ් අඩවියක ඇති විවෘත Ports (Open Ports) සහ අතහැර දමා ඇති ආරක්ෂක HTTP Headers (Missing Security Headers) පරීක්ෂා කර වාර්තාවක් ලබා දෙයි.

---

## 🛠️ මෙය වැඩ කරන ආකාරය (How it Works)

මෙම මෙවලම ප්‍රධාන කොටස් 3කින් සමන්විත වේ:
1. **Frontend (Dashboard):** HTML සහ CSS භාවිතයෙන් නිර්මාණය කර ඇති අඳුරු තේමාවක් සහිත (Dark Theme) වෙබ් අතුරුමුහුණතකි. මෙයින් පරිශීලකයාට ඉලක්කගත URL එක ඇතුළත් කළ හැක.
2. **Backend (Flask):** පරිශීලකයා ලබා දෙන URL එක ලබාගෙන, එය `scanner.py` ගොනුවේ ඇති ප්‍රධාන පරීක්ෂා කිරීමේ තර්කයට (Logic) යොමු කරයි.
3. **Scanner Core (Python Logic):** 
   * **Port Scanning:** `nmap` මෙවලම භාවිතයෙන් ඉලක්කගත සර්වර් එකේ වඩාත් පොදු TCP Ports (Top 100) පරීක්ෂා කර විවෘතව ඇති පෝට් ලැයිස්තුගත කරයි.
   * **Header Analysis:** `requests` ලයිබ්‍රරිය හරහා සර්වර් එකට HTTP Request එකක් යවා, ප්‍රතිචාරයේ (Response) පැමිණෙන Headers පරීක්ෂා කරයි. `X-Frame-Options`, `Content-Security-Policy` වැනි ආරක්ෂක Headers නොමැති නම් ඒවා හඳුනාගෙන වාර්තා කරයි.

---

## 🚀 Termux එකේ Run කරන විදිහ (Step-by-Step)

### පියවර 1: Termux Setup කරගැනීම
Termux යෙදුම විවෘත කර පහත විධානයන් ලබා දෙන්න (මෙයින් අවශ්‍ය පැකේජ උපුටා ගනී):

pkg update -y && pkg upgrade -y
pkg install python nmap -y
pip install flask requests

පියවර 2 🔪

