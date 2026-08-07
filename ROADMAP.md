# Python → AI/ML Engineer Roadmap

**Goal:** Entry-level **AI/ML Engineer** — aisa model banana jo data se khud seekhe, *aur* usko chalta hua product banana.

**Rhythm:** Roz **3 ghante** (structure niche diya hai) · har teesre din revision-heavy · hafte mein 1 din chhutti
**Total estimate:** ~3.5-4.5 mahine

---

## Progress

```
Phase 0    Python core                  ████████████░  ~90%   ← ABHI YAHAN
Parallel   Git + GitHub                 ░░░░░░░░░░░░   ← AAJ SE SHURU
Phase 1    NumPy                        ░░░░░░░░░░░░
Phase 1.5  Math for ML (stats + LA)     ░░░░░░░░░░░░
Phase 2    Pandas + SQL + Matplotlib    ░░░░░░░░░░░░
Phase 3    ML basics (pehla model)      ░░░░░░░░░░░░
Phase 3.5  Deployment (FastAPI+Docker)  ░░░░░░░░░░░░   ← "Engineer" wala hissa
Phase 4    Classification               ░░░░░░░░░░░░
Phase 5    Neural Nets + PyTorch        ░░░░░░░░░░░░
Phase 6    LLM + RAG                    ░░░░░░░░░░░░
Phase 7    Portfolio projects           ░░░░░░░░░░░░
```

---

## Daily routine — 3 ghante

| Time | Kaam |
|---|---|
| 20 min | **Revision** — purana exercise, khaali file se, bina dekhe |
| 40 min | **Naya concept** — samajhna, chhote examples chalana |
| 15 min | ☕ **Break** (skip mat karna) |
| 60 min | **Problems** — naye concept ke 3-5 problems |
| 15 min | ☕ **Break** |
| 45 min | **Project work** — chal raha project ya bada problem |

**Zaroori niyam:**
- 3 ghante mein **sirf 40 min naya concept**. Baaki practice hai. 3 ghante naya seekhne se dimag jam jaata hai
- Break sach mein lena — screen se hatke
- Har **teesra din**: naya concept skip, poora time revision + project
- Hafte mein **1 din poori chhutti**. Ye recovery hai, aalas nahi

---

## Phase 0 — Python core (~2-3 din baaki)

- [x] variables, types, f-string — `day01.py`
- [x] input, type conversion, if/elif/else — `day02.py`
- [x] for, range, accumulator, while, break — `day03.py`
- [x] running best (max/min khud se) — `day04.py`
- [x] functions, parameters, return, scope — `day05.py`
- [x] lists — index, slicing, append, sorted vs sort — `day06.py`
- [x] dictionaries, list-of-dicts — `day07.py`
- [x] try / except — `day08.py`
- [x] file padhna + list comprehension — `day09.py`
- [ ] file mein likhna
- [ ] chhota project jisme sab jude

**Checkpoint:** File padho → list banao → total, average, max, min. Sab bina dekhe.

---

## Parallel Track — Git + GitHub (AAJ se, roz 15 min)

Ye phase nahi hai — **saath-saath chalega**. Har job ki pehli sharat hai.

- [ ] `git init`, `add`, `commit`, `status`, `log`
- [ ] GitHub account + repo banana, `push`
- [ ] `.gitignore`
- [ ] branch, merge
- [ ] README likhna

**Aaj hi karo:** `python-learning` folder ko git repo banao aur GitHub par daal do. Roz ka kaam commit karte jao — 4 mahine baad ye tumhara sabse bada proof hoga.

---

## Parallel Track — Python engineering (Phase 1 ke saath)

- [ ] virtual environment (`venv`)
- [ ] `requirements.txt`
- [ ] code ko alag files/modules mein baantna, `import`
- [ ] `if __name__ == "__main__":`
- [ ] basic testing (`pytest`) — thoda sa

---

## Phase 1 — NumPy (1.5-2 hafte)

- [ ] array banana, list se farak
- [ ] vectorization — poori list par ek saath hisaab, **bina loop**
- [ ] indexing, slicing, boolean masking
- [ ] broadcasting
- [ ] `mean`, `sum`, `std`, `argmax`, `reshape`

**Kis app jaisa:** Photo = numbers ka grid. Instagram filter = us grid par maths.
**Checkpoint:** NumPy array par bina loop ke hisaab.

---

## Phase 1.5 — Math for ML (1.5-2 hafte)

Ratna nahi hai — **feel** aana chahiye. Interview mein bhi aata hai.

**Statistics:**
- [ ] mean, median, mode, variance, standard deviation
- [ ] distribution, normal curve, outliers
- [ ] correlation vs causation
- [ ] probability basics

**Linear algebra (sirf itna):**
- [ ] vector, matrix
- [ ] dot product — *ye poore neural net ka dil hai*
- [ ] matrix multiplication
- [ ] "shape" ka matlab — `(100, 3)` kya kehta hai

---

## Phase 2 — Pandas + SQL + Matplotlib (2-3 hafte)

**Pandas:**
- [ ] `pip install pandas` (abhi installed nahi hai)
- [ ] DataFrame — Excel jaisi table code se
- [ ] CSV load, `head`, `info`, `describe`
- [ ] filter, `groupby`, sorting, merge
- [ ] missing data ki safai

**SQL** (90% data jobs mein poochha jata hai):
- [ ] `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`
- [ ] `GROUP BY` + aggregate (`COUNT`, `SUM`, `AVG`)
- [ ] `JOIN` (inner, left)
- [ ] subquery
- [ ] Python se database connect karna (`sqlite3`)

**Matplotlib:**
- [ ] line, bar, scatter, histogram
- [ ] labels, title, legend

**Kis app jaisa:** Kisi bhi company ka data dashboard.
**Checkpoint:** CSV load karke safai + SQL se wahi jawab nikalna.

---

## Phase 3 — ML basics · PEHLA MODEL (3-4 hafte)

- [ ] "seekhna" ka matlab kya — loss, gradient descent
- [ ] linear regression **scratch se** (loop + accumulator se!)
- [ ] scikit-learn se wahi cheez 3 line mein
- [ ] train / test split — kyun zaroori hai
- [ ] overfitting, underfitting
- [ ] feature engineering, scaling
- [ ] metrics — MAE, RMSE, R²
- [ ] cross-validation

**Kis app jaisa:** Ola ka fare estimate, ghar ka daam.
**Checkpoint:** Ek model train karke accuracy batana + kyun itni aayi, wo samjhana.

> Sabse bada padav yahi hai. Engine wahi hai jo pehle se aata hai — ek loop, ek accumulator, aur "sabse achha kaun" wala muqabla.

---

## Phase 3.5 — Deployment (2 hafte) ⭐ Engineer wala hissa

**Yahi cheez Data Scientist aur ML Engineer ko alag karti hai.** Notebook mein model banana kaafi nahi — chalta hua product chahiye.

- [ ] FastAPI basics — endpoint banana
- [ ] model ko `pickle`/`joblib` se save/load
- [ ] model ko API ke peeche lagana (`POST /predict`)
- [ ] input validation + error handling (`try/except` yahin kaam aayega)
- [ ] Docker basics — `Dockerfile`, image, container
- [ ] kahin deploy karna (Render / Railway / HuggingFace Spaces — free)

**Checkpoint:** Tumhara model ek **live URL** par chal raha ho jise koi bhi call kar sake.

---

## Phase 4 — Classification (2 hafte)

- [ ] logistic regression
- [ ] decision tree, random forest
- [ ] confusion matrix, precision / recall / F1
- [ ] class imbalance
- [ ] `GridSearchCV` se tuning

**Kis app jaisa:** Gmail ka spam filter, fraud detection.

---

## Phase 5 — Neural Nets + PyTorch (3-4 hafte)

- [ ] neuron kya hai, layers, activation
- [ ] neural net **numpy se scratch**
- [ ] PyTorch tensors (GPU pe chalte hain)
- [ ] `nn.Module` — apna model
- [ ] training loop, optimizer, loss
- [ ] image classification (CNN basics)
- [ ] model save / load
- [ ] transfer learning (pre-trained model use karna)

**Kis app jaisa:** Face unlock, Google Photos ka "ye tumhara dost hai".
**Note:** Laptop mein `torch 2.5.1+cu121` already hai — CUDA/GPU ready.

---

## Phase 6 — LLM + RAG (2-3 hafte) ⭐ Market edge

RAG = ChatGPT ko apni files ka gyaan dena.

- [ ] LLM API se baat karna (Claude / OpenAI)
- [ ] prompt engineering basics
- [ ] documents ko chunks mein todna ← *file handling*
- [ ] embeddings — text ko numbers mein badalna ← *NumPy*
- [ ] similarity search ← *running-best pattern*
- [ ] vector database (Chroma / FAISS)
- [ ] poora RAG pipeline
- [ ] RAG app ko deploy karna

**Kis app jaisa:** "Apni PDF se baat karo" tools, company ka internal chatbot, coding assistants.

> Abhi market mein LLM/RAG wale log kam hain aur demand zyada. Ye tumhara edge ban sakta hai.

---

## Phase 7 — Portfolio (ongoing)

Interview mein yahi dekha jata hai. **3 projects chahiye, teeno deployed:**

- [ ] **Project 1 — Regression:** data → model → API → live URL
- [ ] **Project 2 — Classification:** proper metrics + analysis
- [ ] **Project 3 — RAG app:** apne documents par chalne wala chatbot
- [ ] har project ka saaf README (problem, approach, result, live link)
- [ ] GitHub profile theek karna

---

## Job-ready checklist

- [ ] GitHub par 4+ mahine ka lagataar commit history
- [ ] 3 deployed projects live URL ke saath
- [ ] SQL queries bina dekhe likh sakta hoon
- [ ] Model ko API banake deploy kar sakta hoon
- [ ] Apne har project ko 5 minute mein samjha sakta hoon
- [ ] Resume + LinkedIn projects ke saath
- [ ] Basic DSA (lists, dicts, strings, simple algorithms) — coding round ke liye

---

## 6 patterns — ye zabani aane chahiye (~80%)

Syntax bhoolna bilkul normal hai (`.append()`, `sorted(x, reverse=True)` — dekh lo). **Pattern bhoolna** matlab ruko aur dohrao.

1. **accumulator** — `total = 0` bahar, `total = total + x` andar ✅
2. **counter** — `count = count + 1` ✅
3. **running best** — do dabbe, `if` ke andar dono saath badlein ✅
4. **filter** — loop + `if` + `append` ✅
5. **function** — parameter andar, `return` bahar ✅
6. **file padhna** — `with open` + loop + `int()` ✅

---

## Toolkit ab tak

`variables` · `loops` · `if/else` · `functions` · `file reading` · `try/except` · `comprehension`

---

## 3-din wala test

> **Kya main 3 din baad, khaali file mein, bina kuch dekhe ye likh sakta hoon?**

- **Haan** → aage badho
- **Nahi, par dekhte hi "arre haan"** → normal, ek baar aur likho
- **Dekhne ke baad bhi samajh nahi aaya** → ruko, wahi concept dobara

Pehli baar mein ~30% baithta hai. Revision ke baad ~60%. Project mein use karne par ~90%. **Sabke saath aisa hi hota hai.**
