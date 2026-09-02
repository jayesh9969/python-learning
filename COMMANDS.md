# Dev Commands Cheat Sheet

Ye file tumhare daily use ke commands ki list hai — Git, GitHub CLI (`gh`), Docker, Uvicorn (FastAPI), aur Pip. Jab bhi syntax bhool jao, yahan aao.

---

## 1. Git Commands (Code ka itihaas aur version control)

### Roz chalne wale commands
- `git status`
  - **Ye kya hai:** Batata hai konsi files nayi hain, konsi change hui hain, aur kya commit ke liye taiyar hai.
  - **Kab chalana hai:** Kisi bhi kaam se pehle aur commit karne se pehle, sabse pehla command yahi hona chahiye.

- `git diff`
  - **Ye kya hai:** File ke andar line-by-line kya badla hai (green = add, red = remove) wo dikhata hai.
  - **Kab chalana hai:** Commit karne se pehle cross-check karne ke liye.
  - **File specific:** `git diff Dockerfile` (sirf ek file ka change dekhna).

- `git add <file>` ya `git add .`
  - **Ye kya hai:** Files ko commit ki tokri (staging area) mein daalta hai.
  - **Kab chalana hai:** Jab changes check kar liye hon aur unhe save karne ke liye ready karna ho.
  - **Example:** `git add Dockerfile` ya saari files ke liye `git add .`

- `git commit -m "aapka message"`
  - **Ye kya hai:** Tokri mein rakhe changes ki pakki photo (snapshot) khinch kar history mein save karta hai.
  - **Kab chalana hai:** Ek chhota logical task khatam hone par.
  - **Example:** `git commit -m "Dockerfile: set dynamic port for cloud hosting"`

- `git push origin main`
  - **Ye kya hai:** Tumhare laptop ke local commits ko GitHub par upload karta hai.
  - **Kab chalana hai:** Jab local commit ho chuka ho aur code GitHub/cloud par bhejna ho.

- `git pull`
  - **Ye kya hai:** GitHub par agar koi naya commit hai to use laptop mein download karke merge karta hai.

### Bachav aur safai ke commands
- `git restore <file>`
  - **Ye kya hai:** Agar kisi file mein galat change ho gaya jo commit nahi hua, to use purani sahi halat mein wapas lata hai.
  - **Example:** `git restore main.py`

- `git log --oneline -n 5`
  - **Ye kya hai:** Pichhle 5 commits ki chhotisi list dikhata hai (commit id + message).

---

## 2. GitHub CLI (`gh`) Commands

Terminal se GitHub handle karne ka auzaar:

- `gh auth login`
  - **Ye kya hai:** Terminal ko tumhare GitHub account se jodta hai (browser khol ke login confirm karta hai).
  - **Kab chalana hai:** Sirf ek baar, jab pehli baar machine setup kar rahe ho.

- `gh repo view --web`
  - **Ye kya hai:** Current repository ko seedha default browser mein khol deta hai.

- `gh repo create`
  - **Ye kya hai:** Terminal se hi naya GitHub repo banata hai aur local folder se jod deta hai.

- `gh pr create`
  - **Ye kya hai:** Pull request create karne ke liye.

---

## 3. Docker Commands (Dabba banana aur chalana)

### Dabba banana aur chalana
- `docker build -t <image_name> .`
  - **Ye kya hai:** `Dockerfile` padh kar code aur libraries ka ek band packet (Image) banata hai.
  - **Dhyan:** Aakhri mein space aur dot (`.`) ka matlab hai "isi folder mein build karo".
  - **Example:** `docker build -t rag-api .`

- `docker run -p 8000:8000 --env-file .env <image_name>`
  - **Ye kya hai:** Image ka dabba (container) start karta hai.
  - `-p 8000:8000`: Khidki kholta hai (Laptop ka port 8000 : Dabbe ka port 8000).
  - `--env-file .env`: API key dabbe ke andar surakshit tarike se bhejta hai.
  - **Example:** `docker run -p 8000:8000 --env-file .env rag-api`

- `docker run -d -p 8000:8000 --env-file .env --name my-rag-container rag-api`
  - **Ye kya hai:** Dabbe ko background (detached mode `-d`) mein chalata hai taaki terminal free rahe.

### Dabbe par nazar aur control
- `docker ps`
  - **Ye kya hai:** Abhi chal rahe containers (dabbe) ki list, unke ID aur ports dikhata hai.

- `docker ps -a`
  - **Ye kya hai:** Saare dabbe dikhata hai — jo chal rahe hain aur jo band ho chuke hain wo bhi.

- `docker logs <container_id_ya_name>`
  - **Ye kya hai:** Dabbe ke andar jo bhi print/log ho raha hai wo bahar terminal mein dikhata hai.
  - **Live dekhna:** `docker logs -f <container_id>`

- `docker stop <container_id_ya_name>`
  - **Ye kya hai:** Chalte hue dabbe ko rokta hai.

- `docker rm <container_id_ya_name>`
  - **Ye kya hai:** Band pade container ko delete karta hai (space bachane ke liye).

- `docker images`
  - **Ye kya hai:** Laptop mein kitni images bani hui hain unki list dikhata hai.

- `docker rmi <image_name>`
  - **Ye kya hai:** Purani image ko delete karta hai.

---

## 4. FastAPI & Uvicorn Commands (Local API testing)

- `uvicorn main:app --reload`
  - **Ye kya hai:** Local Python environment mein FastAPI server start karta hai.
  - `main`: `main.py` file ka naam.
  - `app`: `app = FastAPI()` variable ka naam.
  - `--reload`: Code save karte hi server bina restart kiye khud update ho jata hai.

- **Browser Documentation:**
  - `http://127.0.0.1:8000/docs` (Swagger UI interactive testing)
  - `http://127.0.0.1:8000/redoc`

- **cURL se API test karna (Terminal / PowerShell):**
  - PowerShell mein POST request bhejna:
    ```powershell
    curl.exe -X POST "http://127.0.0.1:8000/poocho" -H "Content-Type: application/json" -d '{\"query\": \"lunch time kya hai?\"}'
    ```

---

## 5. Pip & Python Environment

- `pip install -r requirements.txt`
  - **Ye kya hai:** `requirements.txt` mein likhi saari libraries ek sath install karta hai.

- `pip list`
  - **Ye kya hai:** Abhi environment mein kaun-kaun se packages aur unke versions installed hain wo dikhata hai.

- `pip freeze > requirements.txt`
  - **Ye kya hai:** Installed packages ki current list ko `requirements.txt` mein dump karta hai.

---

## Sunhere Niyam (Golden Rules)
1. **`.env` kabhi commit mat karo** — hamesha `.gitignore` aur `.dockerignore` mein hona chahiye.
2. **Server par `print()` nahi, `return` user tak jata hai.**
3. **Docker mein `--host 0.0.0.0` zaroori hai**, warna dabbe ke bahar se baat nahi hogi.
