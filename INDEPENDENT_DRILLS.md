# Independent Coding Drills — The "No-AI" Muscle Builder

> **Uddeshya:** AI crutch ko chhod kar dimaag ke andar "Logic to Code Translation" ka asli muscle banana. Yahan AI ka koi role nahi hai — yahan sirf tumhara dimaag, ek notebook, aur tumhara keyboard hoga.

---

## The 3 Iron Rules (Kadi Shartein)

1. **Rule 1: The Pen & Paper Blueprint (Code se pehle Notebook)**
   - Screen par ek bhi line type karne se pehle physical notebook aur pen uthao.
   - 4 sawal likho:
     - Input kya hai?
     - Loop kisme chalega?
     - Andar kya condition check hogi?
     - Output variable kya return karega?
   - *Jab tak notebook par Hindi/English mein flow nahi likha, tab tak VS Code nahi khulega.*

2. **Rule 2: The 15-Minute Struggle (Zero AI Window)**
   - Jab koi error aaye ya logic na bane:
   - Agle **15 minute tak AI chat bilkul band** rahegi.
   - Terminal ka error traceback dhyan se padho (Line number aur error type).
   - Sirf `SYNTAX_CHEATSHEET.md` ya official documentation dekh sakte ho.
   - 15 minute ke struggle ke baad hi aage ka rasta banta hai.

3. **Rule 3: The Blank File Rule**
   - Har challenge ek bilkul **khaali file** (`challenge_01.py`) se shuru hoga.
   - Purani files se copy-paste karna sakht mana hai. Syntax dekhna theek hai, copy karna nahi.

---

## 4 Progressive Challenge Tracks (Akele Solve Karne Ke Liye)

### Track 1: Pure Logic & Data Wrangling (No APIs, Pure Python)
- [ ] **Challenge 1.1 (Frequency Counter):** Ek lambe paragraph mein har word ki frequency count karke top 3 most repeated words print karo bina kisi external library ke.
- [ ] **Challenge 1.2 (Nested Data Filtering):** Ek list of dicts (10 students ke marks aur subjects) lo. Un students ke naam nikalo jinke Python mein 75+ aur Math mein 60+ hain.
- [ ] **Challenge 1.3 (Deduplication with Priority):** Ek list mein duplicate job entries hain (same company, same title, par alag salaries). Sirf highest salary wali unique entry retain karo.

### Track 2: Backend & Database (PostgreSQL + FastAPI Scratch)
- [ ] **Challenge 2.1 (Pure SQL Scratch):** Ek blank file banao jo Supabase se connect kare, ek nayi table `test_candidates` banaye, 3 rows insert kare aur `WHERE` filter se read kare.
- [ ] **Challenge 2.2 (FastAPI Micro-Service):** Ek blank file mein FastAPI app banao jisme `POST /wordcount` ho jo user se text lekar total characters aur total words ka JSON return kare. `pytest` se test karo.
- [ ] **Challenge 2.3 (Vector Search Re-implementation):** Bina `matcher.py` dekhe, ek nayi script likho jo Gemini se embedding nikaal kar `jobs` table par `<=>` se 1 closest job dhoondh ke laye.

### Track 3: Error Recovery & Defensive Coding
- [ ] **Challenge 3.1 (Retry with Backoff Scratch):** Ek function banao jo jaan-boojh kar 2 baar fail ho aur 3rd attempt mein pass ho. Use `try/except` aur `for/else` loop se retry handle karo bina kisi AI library ke.
- [ ] **Challenge 3.2 (Clean API Validator):** Ek public API (jaise weather ya quote API) ko `requests` se call karo. Agar internet na ho ya 404 aaye, toh program crash hone ke bajaye friendly fallback return kare.

### Track 4: The Capstone Blank-Screen Test
- [ ] **Challenge 4.1 (Mini Job Matcher in 30 Lines):** Ek completely blank file mein bina koi purani file khole:
  1. User se query lo.
  2. Gemini se embed karo.
  3. Supabase se top match nikaalo.
  4. Terminal mein print karo.
  *(Time limit: 25 minutes. Zero hints).*

---

## Self-Evaluation Checklist (Main Kab Ready Hoon?)
Jab tum Track 1 se Track 4 ke challenges notebook par blueprint banakar bina chat mein "hint do" likhe solve kar loge, tab tumhara subconscious dimaag code likhna shuru kar chuka hoga.
