# Handoff — Learning Session History

*Last updated: 2026-08-29*

Ye file batati hai ab tak kya hua, kaha atka tha, kaha dobara dhyan dena hai. `ROADMAP.md` plan hai, ye file **kahani** hai — kaise wahan tak pahunche.

---

## Abhi kaha hu

**Phase 3 — RAG ka basic loop chal raha hai.** `rag01.py` (menu + budget) aur `rag02.py` (college rules + chunking) dono kaam kar rahe hain, verified.

Bacha hua: chunk size aur overlap, citations, re-ranking.

---

## Ab tak poora hua (verified, real output ke saath)

### Phase 0-1 — Python, NumPy, Pandas, SQL
Sab complete. `ROADMAP.md` ke "Ho chuka" section mein list hai. Blank-file re-test se verify kiya gaya tha, sab pass.

### Phase 1 — LLM APIs (Gemini, `google-genai`, free tier)
File: `llm01.py`, `llm02.py`

- Pehla API call — `client.models.generate_content()`
- System instruction — jawab ka **shape** control (guzarish, guarantee nahi)
- Structured output — `response_schema` + `enum.Enum` (pabandi, guarantee)
- Streaming — `generate_content_stream()`, `end=""`, `flush=True`
- Error handling — `ClientError` (4xx, hamari taraf) vs `ServerError` (5xx, unki taraf), retry loop with `time.sleep()` + `break`
- Token counting — `count_tokens()` (andaza, call se pehle) vs `usage_metadata.total_token_count` (asli, call ke baad)

Baaki: `[ ] thinking dekhna (include_thoughts=True)` — abhi jo model use ho raha hai wo support nahi karta, koi paid/naya model chahiye.

### Phase 2 — Embeddings + Vector DB
File: `embed01.py`
- `embed_content()` se text → 3072-number vector (normalized, norm=1.0)
- `np.dot()` se similarity (normalized hai to dot = cosine)
- `np.argmax()` se sabse milta-julta item dhoondhna
- Verified: "kuch teekha khana hai" query ne sahi se "Andhra Chilli Fry" dhoond nikala, jabki keyword search fail hoti (kahin "teekha" shabd hi nahi hai items mein)

Files: `chroma01.py` (Gemini embeddings + Chroma), `chroma02.py` (Chroma ke apne embeddings)
- `PersistentClient(path=...)` — disk par save, program band hone ke baad bhi data bachta hai. `Client()` sirf memory mein.
- `add` / `upsert` / `update` — `update()` nayi id par chup-chaap kuch nahi karta, error bhi nahi deta. Ye khud pakda tha.
- `if collection.count() == 0:` — pehli baar wala kaam (menu embed + add) andar, query wala kaam bahar. Gemini ki call bachti hai.
- distance = doori, **chhota achha** — `np.dot` similarity ke ulta. Chroma khud sort karke deta hai.
- `metadatas=[{...}]` + `where={...}` — embedding "kitna kareeb" dekhta hai, metadata "andar aane doon ya nahi". `n_results` upar ki hadd hai, guarantee nahi.
- Chroma ka apna embedding model chhota hai, sirf English samajhta hai — Hinglish "meetha"/"teekha" par tukka marta hai. Gemini sahi karta hai. Almirah aur embedding model do alag cheezein hain.

---

### Phase 3 — RAG (scratch se)
Files: `rag01.py` (khane ka menu + budget wala sawal), `rag02.py` (college rules + chunking)

- Poora loop: sawal embed -> Chroma se tukde -> tukde + sawal ek prompt mein -> Gemini
- **Tarteeb mayne rakhti hai** — pehle `generate_content` upar tha aur `res` neeche, to Chroma ka koi role hi nahi tha. Dhoondho pehle, poochho baad mein.
- **Threshold** — `res["distances"][0][0] > 0.8` ho to Gemini call karo hi mat. "delhi se mumbai flight" 0.884 par ruk gaya.
- **Distance ki hadd** — distance batata hai tukda *milta-julta* hai, ye nahi ki usme *jawab* hai. "samosa kitne baje tak" 0.472 par aaya (bahut paas) par tukde mein timing thi hi nahi.
- **Grounding instruction ka santulan** — bahut kadi to sahi jawab bhi rok deti hai ("100 rupaye" par "I don't know"). `"calculation is allowed"` jodne se theek hua.
- **Sabse badi seekh — data ek jagah rakho.** Rules `contents` mein aur "list di hai" `system_instruction` mein baant diya tha. Model ne kaha "please provide the list", aur jawab kabhi aata kabhi nahi. Sab kuch ek prompt mein saaf label ke saath daalte hi har baar sahi chala.
- **Chunking** — `text.split("

")`, har tukda alag embed + alag id. `n_results` 2-3 rakho: "college kitne ghante khula hai" ka jawab do alag rules (11am + 5pm) jodne se bana.

---

## Baar-baar hui galtiyan (in par dobara dhyan dena — teaching pattern)

Ye galtiyan multiple sessions mein repeat hui hain, isliye inko revision ke waqt zaroor check karna:

1. **"gaddi vs card" (poori list vs current item)** — `contents=reviews` (poori list) likh dena jab `contents=review` (loop ka current item) chahiye tha. Ye `llm01.py` aur `embed01.py` dono mein hua.
2. **API call loop ke andar** — `embed_content()` ya `generate_content()` ko har baar loop ke andar call karna jab sirf ek baar bahar call karke result ko loop mein use karna chahiye. Cost/quota issue create karta hai (embedding quota isi wajah se khatam hua tha, `gemini-embedding-001` se `gemini-embedding-2` switch karna pada).
3. **`np.argmax()` ek scalar par** — single number par `argmax` hamesha 0 deta hai. List banani padti hai (`scores = []`, loop mein `.append()`) tabhi `argmax` sahi kaam karta hai.
4. **`time.sleep()` ko hi retry samajhna** — sirf sona (wait) response wapas nahi laata, dobara **API call** karna padta hai. Nested loop chahiye: outer loop items ke liye, inner loop attempts ke liye.
5. **Print loop ke bahar** — sirf last iteration ka result dikhna, kyunki `print()` galti se loop ke bahar tha.
6. **Casing mismatch** — `"positive"` vs `"Positive"` compare fail hona. Fix: `.strip().lower()`, ya better — structured output (enum) jo guarantee kare.
7. **Persistent store mein purana ganda data** — do baar phase. Pehle `chroma01.py` mein `"vector, vectorq"` wali galat entry, phir `chroma02.py` mein ids `"1"-"4"` se `"0"-"3"` badalne par anaath `"4"`. Almirah purani cheezein khud nahi phenkti. Aadat: `len(list)` aur `collection.count()` milaake dekho.
8. **List mein comma chhoot jana** — `"a"` `"b"` agal-bagal likhne par Python dono ko chipka ke ek string bana deta hai, bina error ke. `len()` se pakda jata hai.
10. **`join` ulta likhna** — `list.join("
")` error deta hai. `"
".join(list)` sahi hai — join gond par lagta hai, cheezon par nahi.
11. **`()` vs `[]` comprehension mein** — `(str(i) for i in ...)` generator banata hai, list nahi. Chroma ne usko `ids: 1` gina aur "Unequal lengths" error diya. Aur generator ek baar hi chalta hai.
9. **Dead code chhodna** — kaam khatam hone ke baad bekaar `import` aur variables file mein pade rehte hain (`chroma02.py` mein `genai`, `chroma01.py` mein `numpy`/`types`).

Purani cheezein (Phase 0 se): outer vs inner variable confusion, accumulator (`total = m + m` instead of `total = total + m`), running-best loop ka starting value, `sorted()` ka result throw away karna, f-string ke andar quotes.

---

## Teaching feedback jo maine follow karna hai

- **Ek session mein ek hi nayi cheez.** Chroma sikhate waqt maine ek saath teen cheezein daal di — Chroma, Gemini embeddings, aur "ek baar vs har baar" — upar se purana ganda data. Unhone bola "suspense inception movie bana di." Sahi bola. Fix: Gemini hata ke sirf Chroma se shuru kiya, phir ek-ek karke joda.
- **Output kabhi guess mat karo.** `KAAM` block mein maine `[['aam meetha hota hai']]` likh diya bina chalaye — galat nikla. Pehle chalao, phir likho.

- **Library ke andar ka formula mat dikhao jab tak na maanga ho.** `corrcoef` ke internals dikhाने se confuse hua tha. Tool sikhao, uske guts nahi.
- **Plain prose, minimal formatting.** Bahut zyada tables/bold/headers use karne par pushback mila tha — "adapt claude app persona, not claude code."
- **CLAUDE.md/ROADMAP/memory mein duplication mat karo.** Single source of truth: `CLAUDE.md` = teaching rules, `ROADMAP.md` = plan/progress, `NOTES.md` = apni notes, memory files = sirf pointers.

---

## Chhoti pending cheezein

- `chroma01.py` mein `import numpy as np` aur `types` bekaar pade hain.
- `where` mein number wali shartein (`{"price": {"$lt": 100}}`) sirf batayi hain, chalake nahi dekhi.
- `rag02.py` mein `print(res["documents"], res["distances"])` debug line padi hai — seekhne ke liye theek hai, saaf karni ho to kar dena.
- `.gitignore` ab `chroma_*/` pattern use karta hai. Pehle naam-se-naam likhe the aur `chroma_food`/`chroma_rules` chhoot ke commit ho gaye the (10 MB). Ab tracking se hata diye, disk par bache hain — par purane commit ki history mein ab bhi pade hain.

---

## Aage kya hai (order mein, `ROADMAP.md` se)

1. Supabase / pgvector se connect (SQL ke saath, Phase 2 ka bacha hua hissa)
2. RAG ka bacha hissa — chunk size + overlap, citations, re-ranking
3. Deployment — FastAPI, Docker, hosting, env vars
4. Evaluation & Observability — Langfuse/Logfire
5. n8n automation
6. PyTorch (sabse aakhir, kam priority)

Plus: 3 portfolio projects, har ek live deployed, kisi asli insaan ki asli problem.
