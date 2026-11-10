# Meri Learning Beginner TO AI Engineer

## shape method batata hai ki rows aur column kitne hain array me aur reshape method change karta hai rows aur column ko

## axis =0 vertically chun ta hai numbers ko aur axis = 1 horizontally

## .mean() method average nikalta hai aur std hamesha nikal sakte ho, aur wahi batata hai ki difference hai ya nahi. Chhota std aaya matlab sab paas-paas, bada aaya matlab bikhre hue. Wo naapne ka auzaar hai, sirf bikhre data ke liye nahi.

## np.median(array) ye hamesha beech ka point dhundhta hai jaise [50, 55, 60, 65, 70] inke beech ka median hoga 60 lekin jab koi bada numbar ho baaki numbero se to use koi itna jyada fark nahi padta jaise 100 add kar diya [50, 55, 60, 65, 70, 100] ab bhi median 60 ke aas pass hoga 62.5

## Sabse chhota/bada dhoondhne wale loop mein dono dabbe — value aur naam — pehle item se shuru karo. Zero ya koi apna number mat daalo. Aur test karte waqt list ka order badal ke dekho

## f string ke andar string pass karni ho variable me to single quote use karo 

## .sum() and np.dot har cheez ka apna wazan ho aur kul jod chahiye example kirana bill quantity se price ko multiply karke uski addition karke total nikalna        ex. (qty x price).sum() ya np.dot(qty, price)

## corelation matlab do variables ke beech ka rishta kaisa hai 0 kuch nahi, 1 dono sath sath chalte hai, -1 ek upar ek niche

## Mode matlab sabse zyada baar aane wala value ex. kapde ki dukan me sabse zyada bikne wala size jaise L,M,S number nahi jab number na ho to mode use hota hai code me np.unique se count karte hai argmax() se position aur vals[position] se jawab

## Variance hai std() ka square aur .var() se milta hai Variance ye formulas me dikhta hai

## probability shakyata mapak ya confidence 0 se 1 ke beech 0 matlab kuch nahi 1 matlab pakka ex. is email ke spam hone ka chance 0.92 hai, jo chahiye / kul or total ex. class mein 20 students 12 pass koi ek uthao - pass hone ka chance 12/20 = 0.6  filtering + len + divide, probability jab jawab pakka na ho, fraud catching, ye customer wapas ayega ya nahi yaha apply ho sakta hai

## pandas: Dataframe - excel ki sheet code mein
## read_csv() and to_csv() file se table ko bulana , table se file ko bhejna ek line me, compared to normal python with open() many lines

## head() deta hai selective rows jitni rows head me utna output  info() deta hai file ke tables ka type ex int64, object

## describe() data ke columns ka mean/std/min/max/median nikal ke deta hai

## loc(row, column) me column ka naam likhte hain number nahi

## df[df['marks'] > 80] NumPy jaisa hai par full row deta hai sirf number nahi

## groupby('city')['marks'].mean() teen hisse kiss se dher, konsa column, kya hisaab

## sort_values() ek order me lagana ABCD ya BCDA ascending=false ulta

## missing data NaN = khali. isnull.sum() dikhata hai ex. poore table me kaha data matlab object ya int missing hai

## dropna() wo rows hata deta hai jaha kuch na kuch missing hai aur wo dikhata jo rows poori bhari hui hai

## fillna() missing data bhar deta hai numbers ke liye .median() laga ke aur text ke liye fillna('unknown') likh kar

## pd.merge() do tables ko jodne ke liye. on='naam' se milao. bina how='left' ke jo dono me common nahi hai wo gayab ho jata hai

## astype('Int64') bada I Nan ke saath bhi int rakh sakta hai

## SQL: SELECT -> FROM -> WHERE -> GROUP BY -> ORDERBY -> LIMIT ye sequence fixed ise aise hi karna hota hai

## SELECT/FROM/WHERE kya chahiye, kahan se, kis shart par WHERE me barabari ek = se. values case sensitive hain

## GROUP BY pandas ka groupby() . SELECT city AVG(marks) ... GROUP by city.

## ORDER BY ... DESC + LIMIT -- sort_values() + head. Top nums ke liye

## JOIN/LEFT JOIN -- merge() from pandas ka SQL roop ON s.naam = a.naam se milate hain

## LEFT JOIN sab rows rakhta hai, JOIN sirf matching

## SELECT * ye pura table de dega isse bacho agar 2 columns chahiye to sirf wahi mango * ye nahi

## LLM API call setup -- kese kare - pehle model ke platform se API key le phir us model ki library pip se install karo. new terminal ex. setx GEMINI_API_KEY "yaha api key dalo" wo environment variable me chali gayi safe key kabhi bhi code me mat likhna. 

## LLM API ko call kese kare -- from google import genai - se librarary ko aur module ko bulao. har ai model ke librarary ka thoda sa alag syntax hota hai. wo syntax ya code model ke documentations se mil jata hai. uske code me pehle model ko bulane ke liye connection banana hota hai, phir model ka id ya naam likhna padta hai, phir ek jagah apna message ya question likhna hota hai "hi" ais quotes me. phir print karke aur program karne par model ka response ya message dikhata hain

## Classifier - model ka output control karne ki koshish - system instruction = guzarish ya vinanti Ek shabd dena." Model zyadatar maanta hai, kabhi Positive likh deta hai, kabhi full stop laga deta hai,
## Schema = pabandi. Tum API ko pehle hi keh dete ho: "jawab in teen mein se ek hona chahiye, aur kuch ho hi nahi sakta." Ab model ke paas chauthi cheez likhne ka rasta hi nahi bacha. 

## Kya jawab hoga (positive ya negative) — ye model khud tay karta hai. Humne kahin nahi likha ki "thanda matlab naraz". Usne training mein karodon reviews padhe hain aur naraz-khush ka farak khud seekh liya hai. Ismein hamara koi haath nahi.

## Kis shakl mein jawab aayega (ek shabd, chhote akshar) — ye humne kaabu kiya. Yahi system instruction aur .strip().lower() ka kaam tha.

## Yaani: faisla uska, format hamara.

## Dhundhla sawal, dhundhla jawab. System instruction se jawab ka shape kaabu mein aata hai.

## AI ka jawab hamesha saaf karo. .strip().lower() — shape bharosemand hota hai, akshar nahi

## Streaming - jab user se ko wait karna padta hai answer ke liye ex. 20 seconds. tab streaming wait nahi karwata jaise jaise answer banta hai wo answer tukdo me aate jata hai

## ClientError vs ServerError - 400-499 code matlab clienterror hamari taraf ki baat ex 429 limit khatm 404 wrong model or name, servererror 500-599 unki taraf ki baat 503 server busy

## Token counting : estimated token counts karna count_tokens().total_tokens se, actual tokens ka total nikalne ke liye r = usage_metadata.total_token_count se prompt + answer ka total milta hai agar sare ab tak ke prompts + answer ka total chahiye total + r se milta hai

## Token counting me sabhi data ko count kiya jata hai ausatan 4 characters = 1 token jaise system_instructions, prompt ya data and answer

## Embeddings aur Semantic search: embeddings ka use shabdon ka ek dusre se kitna acha sambandh hai ya kitne milte julte hai ye numbers me dekhna aur konsa shabd sabse zyada milta julta hai use dhundhna. embeddings ek text ko numbers me badalta hai. np.dot() se do cheezon me kitna gehra sambandh hai ye numbero me nikala phir sabse bade number ko dhund ne ke liye np.argmax() ka istemal kiya jo us number se connected shabd tha use print kiya

## API call ko hamesha loop ke bahar kare nahi to jyada bill aa sakta hai

## Vector DB - persistentClient() data disk me save hota hai file me vs Client() no file but add() har baar karna padta hai

## add() vs upsert() vs update() - add() naya dalta hai purani mile to chhod deta hai - update() jo pehle se hai usko badalta hai nayi id do to kuch nahi karta error bhi nahi deta ex. fruit_dishes wali list me jo items pehle se hai unme badlao agar hota hai to update kar dega naa ki nayi item ko update wo ignore karta hai nayi item ko   - upsert() ye nayi items ko bhi save karta hai or show karta hai agar koi change ho purani items mein wo bhi change karke save karta hai show karta hai

## delete_collection() - ek baar run phir comment kar do agar galat data chala jaye use remove karne ke liye hai

## if collection.count() == 0 is condition ke andar sirf jo sirf ek baar run karna jaruri hai ye gemini ki call bachata hai

## 'distances' chromadb me use hota hai ye numpy ke np.dot() se ulta hai chroma me distance me chota wo acha

## metadatas - dicts me likha hua hota hai jaise 'cold' : true/false ki dict hoti hai query() me where'cold' : True puch kar hum saari cold items show kar sakte hai

## Threshold - items ke beech agar jyada distance ho ya query ka items ya list andar ki info se koi sambandh na hone par model ko call karne se pehle hi rok dena ex. if res['distances'][0][0] > 0.8: else: model call

## Gounding instruction - agar model ko items ya list se related kuch milta hai par usse related info nahi hai list me to system_instruction me kuch aisa prompt dala jaye jo use extra ya unrelated info dene se roke ex.agar list me nahi hai to 'pata nahi' bolo

## chunking       →  bade text ko tukdon mein todo
## embed + store  →  har tukda Chroma mein
## retrieve       →  sawal se milte-julte tukde nikaalo
## threshold      →  bilkul alag sawal ho to yahin rok do
## prompt         →  tukde + sawal ek saath, saaf label ke saath
## grounding      →  rules mein na ho to "nahi pata" bolo

<!-- 1. RAG kya hai. Do cheezein jodna — Chroma se sahi tukde dhoondho, Gemini se un tukdon par jawab banwao. Retrieval = dhoondhna, Generation = jawab banana.

2. Kis kaam aata hai. Model ko tumhare data ka pata nahi hota. Poora document har baar bhejna mehenga aur token limit se bahar. RAG sirf zaroori do-teen tukde bhejta hai.

3. Teen kadam. Sawal embed karo → Chroma se tukde nikaalo → wo tukde + sawal prompt mein daal ke Gemini ko bhejo. Tarteeb yahi rahegi — dhoondho pehle, poochho baad mein.

4. Threshold. res["distances"][0][0] sabse kam doori hai (Chroma sorted deta hai). Wo hadd se zyada ho to Gemini call karo hi mat — sawal topic se bahar hai. API call bhi bachi.

5. Distance ki hadd. Distance batata hai ki tukda sawal se milta-julta hai. Ye nahi batata ki usme jawab hai. "samosa kitne baje tak" par samosa wala tukda 0.472 par aaya — ekdum paas, par usme timing likhi hi nahi thi.

6. Grounding instruction. "Sirf diye gaye data se jawab do, na mile to nahi pata bolo." Isse hallucination kam hoti hai, khatam nahi — kyunki system instruction guzarish hai, pabandi nahi. Wahi baat jo llm01.py mein seekhi thi.

7. Instruction ka santulan. Bahut dheeli — jhooth bolega. Bahut kadi — sahi jawab bhi rok dega. "100 rupaye mein kya kha sakta hu" par "I don't know" aa gaya tha, kyunki "don't add additional information" ne hisaab lagane se bhi rok diya. "calculation is allowed" jodne se theek hua.

8. Data ek jagah rakho. Sabse badi galti — rules contents mein aur "list di hai" system_instruction mein. Model bola "please provide the list". Jawab kabhi aata kabhi nahi. Sab kuch ek prompt mein, saaf label ke saath — "rules ye hain / sawal ye hai" — tab har baar sahi chala.

9. Chunking. Bade text ko tukdon mein todo (text.split("\n\n")), har tukda alag embed karo, alag id se Chroma mein daalo. Poore akhbaar ka ek embedding banaoge to sab matlab ghul-mil jayenge.

10. n_results ek se zyada rakho. "College kitne ghante khula hai" ka jawab do alag rules mein tha — 11am aur 5pm. Ek tukda laate to jawab kabhi nahi banta.

11. join. "\n".join(list) — gond par lagta hai, list par nahi. list.join("\n") error deta hai. Aur res["documents"] ek parat andar hoti hai, isliye res["documents"][0] par lagta hai.

Chunk size aur overlap. Koi jaadui number nahi hota. Chhota tukda — matlab adhoora ("50 rupaye" mila par "delivery" gayab, Gemini ne "jaankari nahi hai" bola). Bada tukda — matlab ghul-mil jaata hai aur tokens zyada. Sochne ka tarika: ek tukda = ek poori baat. Shuruat 300-500 akshar, overlap uska 10-20%.

Overlap kaise lagta hai. range(0, len(text), size - overlap) — tukda size ka, par har baar sirf size - overlap aage kudo. Isse har naye tukde mein pichhle ka aakhri hissa dobara aa jaata hai. Poster ki photocopy jaisa — kinare thoda overlap rakho warna seemā ka shabd kahin poora nahi milega.

RAG kharab jawab de to sabse pehle chunking dekho. Wahi sawal, wahi model, sirf overlap laga — "ye jaankari nahi hai" se "Delhi mein 50 rupaye" ho gaya.

Chhote tukde chhaan do. if len(chunk) > 40: — kachra tukde ("agte hain.") Chroma mein jaake kisi din kisi sawal ka "sabse paas" ban sakte hain. Aur hadd itni kasi mat rakho ki ek akshar se bache — > 10 sirf isliye chala kyunki kachra theek 10 ka tha.

enumerate(list, 1) — har item ke saath uska number deta hai, aur 1 se ginti shuru karta hai.

Citations. Tukdon ko [1] [2] number ke saath prompt mein bhejo aur instruction mein maango ki jawab ke saath number likhe. Isse user khud check kar sakta hai aur tum debug kar sakte ho. Bina maange model kabhi karta hai kabhi nahi — teen mein se ek jawab mein chhoot gaya tha.

Citation ka number dhoondhe hue tukdon ka hai, asli document ka nahi. Sawal badla to kram badal jayega. Asli app mein tukde ki pakki id bhejte hain.


Re-ranking kya hai. Do parat mein dhoondhna. Chroma se zyada tukde nikalo (8), phir Gemini se poocho kaunse 2-3 sach mein jawab dete hain, sirf wahi aage bhejo. Clerk 500 CV mein se 20 chhaanta hai, manager un 20 mein se 3 chunta hai.

Kyun zaroori hai. Embedding dekhta hai "baat isi bare mein hai", ye nahi dekhta "jawab isme hai". "kis baat par kanooni karyavahi" par embedding ne "fighting will not be tolerated" ko top-3 mein daal diya — usme kanoon ka zikr hi nahi tha. Manager ne nikaal diya.

response.text hamesha string hoti hai. "1,2,3" numbers jaisa dikhta hai par hai text — len() 5 deta hai, aur rules["1,2,3"] error deta hai. strip() → split(",") → int() karke asli numbers banane padte hain.

for X in Y mein Y tokri hai. for n in rules[n-1] likhne se string par loop chala aur akshar nikle. Tokri wo hai jisme se ek-ek nikalna hai — yahan nums. rules[n-1] loop ke andar aata hai.

Loop variable ka naam gaddi wala mat rakho. for nums in nums likhne se poori list mit jaati hai.

Gemini se numbers maango to ginti 1 se hoti hai, list 0 se. rules[n - 1] likhna padta hai.

Do call ka kharcha. Ab har sawal par do Gemini call jaati hain — ek chunne ki, ek jawab ki. Faayda ye ki doosri call mein kam tukde jaate hain. Chhote data par ye ghaate ka sauda hai, bade data par faayde ka.

FastAPI kya hai. Python code ko ek darwaza (URL) de deta hai taaki koi aur use kar sake. Script sirf tum chala sakte the, wo bhi file edit karke.

@app.get("/pata") — upar wali ye line neeche wale function ko ek pata deti hai. Koi us pate par aaya to function chalta hai.

Chalane ka tarika alag hai — python main.py nahi, uvicorn main:app --reload. main = file, app = us file ka variable. --reload matlab save karte hi server khud restart.

/docs khud ban jaata hai. Ek line likhe bina. Client ya frontend wale ko dene ke liye ready documentation — freelance mein seedha faayda.

Sabse bada farak: print vs return. Script mein print user tak pahunchta tha kyunki user aur programmer ek hi the. Server mein user kisi aur shehar mein hai — print sirf tumhare terminal mein jaata hai, user tak sirf return pahunchta hai. Threshold wale raste par return bhool gaya tha to user ko null mila.

Setup function ke bahar. Chroma aur Gemini client server chalu hote waqt ek baar banao. Function ke andar rakhoge to har sawal par dobara banega. Wahi "API call loop ke bahar" wali baat, naye bhes mein.

Class = design, object = bhara hua form. class Question ek khaali form ka naksha hai. body wo form jo kisi ne bharke bheja. Question.query galat hai (naksha khaali hai), body.query sahi.

GET vs POST. GET mein sawal URL mein jaata hai — chhoti cheezon ke liye theek, par lambe text ya &/# jaise akshar par tootta hai. POST mein sawal body mein jaata hai, JSON ki shakl mein. Bade input ke liye POST.

response_model shape pakka karta hai. Answer mein rules_used dena bhool gaye the — Pydantic ne rok diya, Field required bola. Bina iske wo bug chup-chaap nikal jaata.

Docker kya hai. Code, Python, aur saari libraries ek dabbe mein band. Wo dabba kahin bhi chalao, andar sab waisa hi rehta hai. Ilaaj ek hi jumle ka — "mere laptop par to chal raha tha."

requirements.txt — libraries ki list, har line par ek. Package ka naam aur import ka naam alag ho sakta hai: install google-genai, import google. Version likhna behtar (fastapi==0.141.1) warna kal koi nayi version aa gayi to dabba toot sakta hai.

Dockerfile ke kadam — FROM (kis dabbe se shuru), WORKDIR (andar kaunsa folder), COPY (kya andar bhejo), RUN (build ke waqt kya chalao), CMD (dabba chalte hi kya chalao).

requirements.txt alag se pehle copy karte hain. Docker har kadam yaad rakhta hai. Sirf code badla to wo dekhta hai requirements.txt to wahi hai, aur install skip kar deta hai. Sab ek saath copy karte to har chhoti si change par saari libraries dobara install hoti — 3 minute vs 5 second.

--host 0.0.0.0 — bina iske dabba chalega par tum baat nahi kar paoge. Default 127.0.0.1 ka matlab "sirf isi machine se", aur dabbe ke liye wo "sirf isi dabbe ke andar se" ban jaata hai. 0.0.0.0 matlab bahar walon ko bhi andar aane do.

-p 8000:8000 — dabbe mein khidki. Baayan laptop ka port, daayan dabbe ka. Bina iske dabba andar-andar chalta rahega.

Image vs container. Image = bana hua packet. Container = wo packet jo abhi chal raha hai. Ek image se kai container.

.dockerignore — .gitignore jaisa. COPY . . sab kuch andar bhej deta hai; bade folder (chroma) rok do.

Key Dockerfile mein kabhi mat likhna. Image GitHub par jaati hai, hosting par jaati hai, doosron ko milti hai — key uske saath chali jayegi. Aur image ki har parat save rehti hai, line hata bhi do to purani parat mein padi rehti hai.

Key chalte waqt bahar se do. .env file banao, docker run --env-file .env se chalao. .env ko .gitignore aur .dockerignore dono mein daalo — ye sabse aam galti hai, log key GitHub par daal dete hain aur bot dhoondh lete hain.

Dabbe ka data dabbe ke saath mit jaata hai. Container band kiya to andar ki almirah gayab. Restart par phir se embed. Chaar rules par koi baat nahi, 500-page PDF par der bhi aur paisa bhi. Iska hal — volume (bahar ka folder jodna) ya hosted vector DB (Supabase/pgvector).

Project 1 : is project me humne Procedural RAG  chunking ka use kiya kyuki data ya documents koi paragraph nahi tha wo instructions the isliye alag line banane ke bajaye poore steps ko ek chunk me "/n".join me dala gaya. streamlit ka istemal waqt bachane ke liye kiya kyuki streamlit python me hi likha jata hai frontend ke liye koi dusri language nahi sikhni padi jaise HTML, streamlit khud ek frondend ki tarah kam karta hai st.session_state aur st.chat_message ne ek chatbox bana diya. gemini-embedding-2 7 documents list leta hai lekin ek hi vector nikalta hai jab ki gemini-embedding-001 ye 7 documents ko 7 alag embeddings deta hai jo hame is project me chahiye tha wo tha gemini-embedding-001.

## Tool Calling - AI ke paas haath-pair nahi hote. Wo sirf message bhejta hai ki "ye function chalao". Asli execution Python karta hai. (Manual tarike mein humein khud chalana padta hai, jabki Chats ke saath Automatic tarike mein SDK pichhe se khud sambhal leta hai).

## Agent Loop (ReAct pattern) - Reason + Act + Observe. AI pehle sochta hai (mujhe price chahiye), phir tool chalata hai (Act), phir result dekhta hai (Observe), aur tab tak ye loop chalta hai jab tak final answer na mil jaye. Isme tools ek ke baad ek sequence mein chalte hain.

## RAG vs Agent - RAG ek padhne wala bachha hai (Read-Only) jo fast, sasta aur safe hai. Agent ek action-taker robot hai jo database update ya email bhej sakta hai (Tools ke zariye). Agent mehenga, slow hota hai aur hallucinate karke galat action lene ka darr hota hai.

## Hybrid/Router Architecture - Jab RAG (knowledge) aur Agent (action) dono chahiye, toh RAG ko hi ek "Tool" (jaise search_db) bana kar Agent ko de do. Ye industry ka best tarika hai.

## Tool Schema Design (Docstring & Type Hints) - AI ko function ka andar ka code nahi dikhta. Use sirf function ka naam, type (str, int) aur docstring ("""...""") samajh aati hai. Swiggy menu jaisa: bina details ke AI confuse hoke galat data daal dega (hallucinate). Har tool par type hints aur docstring likhna compulsory hai.

## Literal (typing) - Agar AI ko kisi ek variable ke liye strictly 2-3 options hi dene hain (jaise sirf "AM" ya "PM") toh `am_pm: Literal["AM", "PM"]` use karte hain. Isse AI ko option list mil jati hai aur wo apne mann se "Morning" nahi bhej sakta.

## Tool Validation - Schema sirf format (int, str) check karta hai. Validation tool ke andar asliyat check karta hai (jaise amount < 0 toh nahi). Agar data illogical hai, toh return mein error string bhejo taaki AI apni galti sudhar sake. Isse fatal action (bank crash) hone se bachta hai.

## Tool Error Handling (`try...except`) - Jab internet ya server down ho, toh Python crash hoke laal error phekta hai. Ise rokne ke liye tool ka main logic `try` block mein rakhein aur error aane par `except` block se user-friendly string return karein. Isse AI bina crash hue user ko politely sorry bol pata hai.

## Retries & Timeouts - Agar API atak (hang) jaye, toh `timeout=5` (5 seconds) ka rule lagate hain jisse Python `TimeoutError` de. Haar manne se pehle, ek `for` ya `while` loop (max 3 attempts) banakar retry karte hain taaki chote network glitches handle ho jayein.

## Exponential Backoff - Retries mein har baar fix 2 second rukne se server par DDoS jaisa asar (load) padta hai. Isliye har attempt ke baad wait time double karte hain (`time.sleep(2)`, phir 4, phir 8). Ise Exponential Backoff kehte hain jisse struggling server ko recovery ka time milta hai.

## Maximum Agent Steps - AI (ReAct pattern) ziddi hota hai. Agar koi jawab dhoondhne mein error aaye toh wo alag tareeqe se naye tool chala kar infinite loop mein fass sakta hai (jisse API calls ka bill bohot bada aa sakta hai). Isliye Manual Agent loop mein hum `steps` counter lagate hain (jaise max 5 steps). Python strict hota hai, 5 steps poore hote hi wo fauran AI ko rok kar loop tod (break) dega.

## State Management & Agent Memory Basics - AI by default 'Ghajini' (stateless) hota hai, use pichle kisi request ki yaad nahi hoti. Memory banaye rakhne ke liye humein message history maintain karni padti hai jisme har message ke do roles hote hain: 'user' (insan) aur 'model' (AI). Python list (RAM) program band hone par khali ho jati hai, isliye permanent memory ke liye Database/File ka use karte hain. Boht lambi chat (hazaron messages) bhejne par token bill aur latency bohot zyada ho jati hai; isliye smart engineer context ko compact (summarize) karta hai, sliding window (recent messages) rakhta hai ya RAG/ChromaDB se sirf relevant purani yaadein retrieve karke model ko bhejta hai.

## Human-in-the-loop (HITL) Approval - Critical, financial ya destructive actions (paise bhejna, data delete karna, emails) lene se pehle AI ko insaan se confirmation lena padta hai. Read-only actions (balance dekhna, attendance) bina approval ke chal sakte hain. Approval maangte waqt action ke saare zaroori arguments (kisiko, kitna, kahan) saaf dikhane chahiye taaki user blind approval na kare. Agar user reject kare toh tool crash (`raise Exception`) karne ke bajaye clean cancellation string return karta hai taaki AI polite reply de sake. Approval fatigue se bachne ke liye threshold lagate hain (jaise <= 500 auto-approve, > 500 ask approval) aur daily cumulative limits rakhte hain.

## Agent Evaluation - Agent sirf text nahi banata balki actions leta hai, isliye evaluation mein Text Response ke alawa Tool Selection (sahi tool chuna ya nahi) aur Tool Arguments (parameters sahi pass kiye ya nahi) test karna sabse zaroori hota hai (fake refund problem). Trajectory length (step count) test karne se pata chalta hai ki agent bina bhatke kitne kam steps mein kaam karta hai taaki latency aur token bill kam rahe. Text evaluation exact match (`==`) se nahi ho sakta; iske liye keyword matching (`in`), embedding cosine similarity ya LLM-as-a-judge ka use karte hain. Naye prompt ya tool change ke baad Regression Testing zaroori hai taaki purane features kharab na hon.

## Deterministic Workflow vs Autonomous Agent - Deterministic (Python code) fixed patri ki tarah 100% predictable, sub-millisecond fast, aur ₹0 cost ka hota hai; isko payments, invoices, authentication aur structured loops mein use karte hain. Autonomous Agent (LLM) aazaad dimaag ki tarah open-ended, complex aur unstructured queries (fuzzy research, complaint reasoning) solve karta hai. Production mein best architecture 'Hybrid / Router' hoti hai jahan gatekeeper simple queries ko Python rules se nipatata hai aur complex problems ko Agent ke paas bhejta hai. AI ek sher hai aur Python rules uska pinjra (guardrails) — dono ka santulan hi software ko safe aur powerful banata hai.

## LangGraph Fundamentals (State, Nodes, Edges) - Complex agentic workflows ko visual flowchart (graph) mein baandhne ka framework. 1) State: Ek central bahi-khata (`TypedDict`) jo poore workflow ka data aur memory hold karta hai; TypedDict se autocomplete milti hai aur spelling mistakes/type errors rukte hain. 2) Nodes: Normal Python functions jo state input mein lete hain aur sirf naya update (`dict`) return karte hain jo LangGraph state mein merge kar deta hai. 3) Edges: Ek node se doosre node tak jane ka raasta; Normal Edge seedha rasta hai, jabki Conditional Edge chouraha hai jahan router function condition check karke rasta tay karta hai. 4) START aur END: Graph ke entry aur finish point.

## Conditional Edges & Routing in LangGraph - `builder.add_conditional_edges(source_node, router_func, path_map_dict)` ke zariye workflow mein branching ki jaati hai. Router function state ko check karke agle node ka label (string) return karta hai aur dictionary map (`{"pass": "next_node", "fail": END}`) us string ko sahi node ya exit point se jodti hai. Agar koi error ya fraud ho, toh conditional edge seedha `END` par bhej kar baaki nodes ko bypass kar sakti hai. Iske alawa conditional edges se loops (chakkar) bante hain jahan `tools` wapas `agent` node par cycle karta hai jab tak final answer na mile, jisse lambe `while True` loop likhne se chhutkara milta hai.

## Tool Integration Inside LangGraph (ReAct Loop) - Graph ke andar LLM aur Python tools ko autonomous loop mein jodna. 1) Flow: START -> agent -> (conditional edge) -> agar tool manga toh 'tools' node, agar final text toh END. 2) Loop cycle: tools node execution ke baad wapas agent node par result bhejta hai taaki AI final answer bana sake. 3) ToolNode: LangGraph ka prebuilt component `ToolNode(tools_list)` jo bina kisi manual `if/else` ke AI ke maange hue tool ko auto-execute karta hai aur result state mein merge karta hai. 4) tools_condition: Prebuilt conditional router jo check karta hai ki AI ke aakhiri message mein `tool_calls` hain (toh 'tools' bhejta hai) ya nahi (toh 'END' bhejta hai).

## Checkpointing & Memory Persistence in LangGraph - Multi-turn conversations aur state ko bachaye rakhne ke liye checkpointers use hote hain. 1) MemorySaver RAM mein state save karta hai (test/dev ke liye), jabki SqliteSaver/PostgresSaver disk/database par persistent store karte hain (production ke liye). 2) thread_id: Har user/conversation ka unique session ID (`config={"configurable": {"thread_id": "..."}}`); same thread_id par purana context auto-load hota hai, alag thread_id nayi fresh chat shuru karti hai. 3) Time Travel: Checkpointer har step ka snapshot save karta hai, jisse hum pichle step par rewind karke state edit kar sakte hain ya galti sudhar sakte hain. 4) Human-in-the-loop: Checkpointer ki madad se graph critical steps par pause hokar safely sleep ho jata hai aur ghanton baad human approval milne par wahin se resume hota hai bina server resources block kiye.

## Error & Retry Handling in LangGraph (RetryPolicy) - Production APIs mein temporary traffic spikes (503 ServerError) ya network drops aane par poore graph ko crash hone se bachane ke liye `RetryPolicy` ka use hota hai. 1) Node-Level Isolation: Retry poore workflow ko shuru se repeat nahi karta balki sirf usi fail hone wale node ko dobara chalata hai, jisse duplicate payments ya duplicate SMS bhejne se bachte hain. 2) Exponential Backoff: `initial_interval` (pehla wait time) aur `backoff_factor` (multiplier) struggle kar rahe server par hammering rokte hain. 3) Transient vs Permanent: `retry_on` parameter se hum sirf temporary errors (ServerError, ConnectionError) par retry trigger karte hain; syntax ya developer bugs (KeyError, ValueError) par turant stop karke error raise hota hai taaki time aur API cost waste na ho.

## MCP Concepts & Architecture (Model Context Protocol) - AI tools ko kisi bhi AI model/client se jodna ka open standard (AI ka Type-C cable). 1) Client-Server Decoupling: MCP Client (Host / AI Agent jo decide karta hai kab tool chalana hai) aur MCP Server (Independent process jo tools aur data hold karta hai) alag-alag chalte hain. Tool alag language (Node.js, Go, Python) mein ho sakta hai aur JSON-RPC se communicate karta hai. 2) Resources vs Tools: Resources read-only data/context hain (jaise historical bank statements, docs, schemas) jinka koi side-effect nahi hota; Tools active executable functions hain (jaise money transfer, delete) jo state badalte hain aur risk hold karte hain. 3) Transports: Local machine par `stdio` (fast, no network ports, zero data leak risk); Remote par `SSE/HTTP`. 4) Security & HITL: MCP Client ke paas dangerous actions par human approval (Allow/Deny) lene ki authority hoti hai taaki hallucinating AI poora database na uda sake.

## MCP Server Implementation (`mcp` SDK) - Python mein `from mcp.server.mcpserver import MCPServer` se server banta hai. 1) `@server.tool()` executable action banata hai jisme Type Hints aur Docstrings compulsory hain taaki AI model automatically schema samajh sake; structured dictionaries return karna production mein best hai taaki AI alag-alag parameters evaluate kar sake. 2) `@server.resource("uri://...")` read-only context provide karta hai; dynamic data ke liye URI Templates (jaise `order://receipt/{order_id}`) use hote hain jisse hazaron records ek function se handle hote hain. 3) Stdout Gotcha: stdio mode mein Server aur Client `stdout` par JSON-RPC se communicate karte hain. Agar tool ke andar raw `print()` use kiya toh plain text stdout ko pollute kar dega aur Client `JSONDecodeError` se crash ho jayega; debugging aur logging ke liye hamesha Python ka `logging` module use karein (jo `stderr` par safe rehta hai).

## MCP Agent Connection & Security Considerations - 1) Dynamic Tool Discovery: Agent ko tool ka Python code import ya dekhne ki zaroorat nahi hoti; runtime par Agent server se handshake karke tool schemas auto-discover karta hai, jisse server par naye tools aane par Agent code badalna nahi padta. 2) Multi-Server Pipelines: Ek Agent ek saath kai MCP servers (Database, Slack, GitHub) se connect hokar unke tools ko aapas mein chain (pipe) kar sakta hai. 3) Tool Namespacing: Do servers ke same naam wale tools (jaise `search`) mein collision rokne ke liye prefixes (`db_search`, `web_search`) lagaye jaate hain. 4) Credential Isolation: Passwords aur secret API keys ko kabhi bhi AI prompt ya tool arguments mein nahi bheja jata (prompt injection aur hallucination leaks se bachne ke liye); credentials ko hamesha Server ke environment variables (`env`) mein isolate kiya jata hai taaki LLM ko secret keys ka pata hi na chale.

## PostgreSQL & pgvector Architecture - 1) SQLite vs Postgres Concurrency: SQLite single-file lock use karta hai jisse concurrent writes mein server atak jata hai; PostgreSQL true client-server hai aur Row-level locking karta hai, jisse hazaaron users parallel transactions chala sakte hain. 2) pgvector in SQL: Postgres mein `VECTOR(dimensions)` data type se relational data aur AI embeddings ek hi table mein store hote hain; do alag databases (Chroma + SQL) ko sync rakhne ka jhanjhat aur orphan data khatam ho jata hai. 3) Single Query Filtering: SQL query mein normal `WHERE` filter (`price < 150 AND is_veg = true`) aur vector distance (`ORDER BY embedding <=> query_vector ASC LIMIT 3`) ek saath chalte hain. 4) HNSW Index: 5 lakh+ rows par slow sequential scan se bachne ke liye HNSW (Hierarchical Navigable Small World) graph index use hota hai jo seedhe nearest neighborhood par jump karta hai (sub-millisecond search). 5) Connection Pooling: Naye connection banane ke overhead (~100ms) aur database crash (`too many clients`) se bachne ke liye pre-opened connection pool (jaise PgBouncer/Supavisor) share kiya jata hai. 6) Type Casting with psycopg: Python list `[float, ...]` ko Postgres default `double precision[]` samajhta hai; vector similarity search query mein `%s::vector` explicit cast zaroori hota hai taaki `<=>` distance operator execute ho sake. Table column dimension model ke mutabiq hoti hai (`gemini-embedding-001` ke liye `VECTOR(3072)`).

## Hybrid Search & Reciprocal Rank Fusion (RRF) - 1) Failure of Pure Vectors: Dense embeddings specific model numbers, product IDs (jaise TX-9021 vs TX-9022), error codes (404), aur exact proper nouns ko blur kar dete hain; exact keyword search is zaroori requirement ko handle karta hai. 2) BM25 Advantages: Simple term frequency ke muqable BM25 term saturation lagata hai (repeated keyword spamming rukti hai) aur Inverse Document Frequency (IDF) se common words ko penalize karke rare keywords ko maximum weightage deta hai. 3) The Fusion Problem & RRF: BM25 score (0 to inf) aur Cosine Similarity (0 to 1) ke scales incompatible hote hain; Reciprocal Rank Fusion (RRF) raw scores ko ignore karke ranks use karta hai: Score = 1 / (60 + rank). Dono channels (keyword + vector) mein aane wale documents ko double boost milta hai aur wo top par aa jate hain. 4) PostgreSQL Full-Text Search (FTS): `to_tsvector` text ki grammar hata kar root/stem nikaalta hai (e.g., 'running' -> 'run') aur stopwords filter karta hai, jo dumb `LIKE '%word%'` ke muqable fast aur accurate hota hai. 5) Production RAG Pipeline: Keyword Match + Vector Similarity -> RRF rank fusion -> Top K reranked results LLM prompt mein ground hote hain.

## Production Testing, Mocking & Logging - 1) Structured Logging vs print(): Production mein `print()` data stream (stdout/stdio) ko pollute karta hai; `logging` module levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`), automatic timestamps, filename, aur line number deta hai jo files mein structured store hote hain. 2) Automated Testing (pytest): Manual testing scale nahi karti; `pytest` single command mein `assert` statements ke zariye saare modules ko secondon mein verify karke regression errors pakadta hai. 3) Mocking (unittest.mock): Real LLM/APIs ko bar-bar call karna expensive, slow (~2s per call), aur rate-limited (429) hota hai; `MagicMock` dummy object in-memory instant response dekar unit tests ko isolated, fast (~1ms), aur 100% free banata hai. 4) Pytest Fixtures: `@pytest.fixture` har test function ko fresh, isolated test state/data provide karta hai, jisse ek test ka state mutation dusre test ko break na kare. 5) Failure & Edge Case Testing: `side_effect` attribute se network timeout, 503 server error, ya malformed JSON mock karke agent ke retry loop aur fallback mechanisms ki resilience test ki jaati hai.

## OOP & Classes (Python Engineering) - 1) Class vs Object: Class ek blueprint/saancha hai (jaise BankAccount form), aur Object uska zinda roop/instance (jaise Amit ka khata). 2) `__init__` aur `self`: Naya object banate waqt `__init__` constructor auto-call hota hai; `self` usi specific object ki memory location ko point karta hai, jisse do users (`user1`, `user2`) ka data aapas mein mix nahi hota. 3) Encapsulation & Methods: Object ke data ko directly chhedne ke bajaye methods (`deposit`, `withdraw`) ke through validate karke change karte hain (e.g. insufficient balance check). 4) `__repr__`: Terminal ya logs mein object ko readable string shape deta hai (e.g. `BankAccount(name='Amit', balance=4500)`); bina iske `<__main__.BankAccount at 0x...>` jaisa unreadable memory address dikhta hai. 5) Class vs Instance Variables (Shadowing Trap): Instance variable (`self.balance`) har user ka apna alag hota hai; Class variable (`bank_name = 'State Bank'`) sabhi ke liye shared hota hai. Agar `user1.bank_name = 'ICICI'` likha jaye, toh class variable nahi badalta balki `user1` ke andar naya instance variable ban jata hai (shadowing), jabki `user2` abhi bhi 'State Bank' hi dekhta hai.

## Type Hints (`typing` module) - 1) Production Guardrails: Python dynamically typed hai; production APIs aur AI engineering (FastAPI, Pydantic, Gemini SDK) mein type hints unexpected types ke crashes rokte hain aur IDE autocomplete dete hain. 2) Contract vs Body: Type hint (`def fn(x: int) -> dict[str, Any]:`) sirf definition line par ek contract/label hai; function ke body ke andar normal Python chalti hai (`return {"key": val}`). 3) Modern Collections (3.9+): `list[str]`, `dict[str, int]` seedha lowercase likhe jaate hain bina purana `typing.List` import kiye. 4) Any (Wildcard): Dynamic JSON/API payloads jahan keys string hain aur values kuch bhi ho sakti hain, wahan `dict[str, Any]` use hota hai (`from typing import Any`). 5) Optional & Union: `Optional[str]` (ya `str | None`) ka matlab hai value string ho sakti hai ya `None`; `Union[int, float]` (ya `int | float`) dono types allow karta hai. 6) Dict vs Set Trap: `{a, b}` bina colon ke Set banata hai jo list aane par `unhashable type` crash deta hai; Dictionary ke liye hamesha `{"key": val}` colon ke sath joda banana zaroori hai.

## Dataclasses (`@dataclass` vs Pydantic) - 1) Boilerplate Remover: Normal class mein baar-baar `__init__`, `self.x = x`, aur `__repr__` likhna padta hai; `@dataclass` decorator type hints ke zariye ye saare methods background mein apne aap generate kar deta hai. 2) Value-Based Equality (`__eq__`): Normal class do objects ko compare karte waqt unke memory address dekhti hai (same data par bhi False aati hai); `@dataclass` auto-generated `__eq__` ke zariye andar ke data ki equality check karti hai (`job1 == job2` -> True). 3) Custom Methods: Dataclass sirf data container nahi hai, isme normal methods (jaise `annual_salary(self)`) bhi likhe ja sakte hain. 4) Immutability (`frozen=True`): Agar koi data read-only rakhna ho taaki galti se mutate na ho sake, toh `@dataclass(frozen=True)` lagate hain; change karne par Python `FrozenInstanceError` throw karta hai. 5) Dataclass vs Pydantic: Dataclass Python ka native lightweight tool hai jo internal data processing/in-memory logic ke liye best hai (zero runtime overhead, no data validation); Pydantic external APIs (FastAPI/JSON requests) ke liye use hota hai jahan runtime validation aur data sanitization zaroori hota hai.

## Modern File & Path Management (`pathlib`) - 1) Cross-Platform Paths: Windows (`\`) aur Linux (`/`) ke slashes ka jhanjhat khatam karta hai; `Path` object par `/` operator se clean path bante hain. 2) Base Directory Anchoring: `BASE_DIR = Path(__file__).resolve().parent` code ko terminal ke current working directory se aazaad karta hai, jisse script kahin se bhi run ho kabhi `FileNotFoundError` nahi aata. 3) Folder vs File Trap (`mkdir`): `.mkdir()` sirf folder banata hai; agar file path (`notes.txt`) par `.mkdir()` chala diya toh Windows folder bana dega aur `write_text()` par `PermissionError` aayega. Isliye pehle folder par `mkdir(parents=True, exist_ok=True)` chalayein, phir file path par `write_text()`. 4) 1-Line I/O: `with open(...)` ki jagah seedha `.read_text()` aur `.write_text("...")` se clean kaam hota hai. 5) Path Properties: `.name` (poora naam), `.stem` (bina extension ke), `.suffix` (extension), `.parent` (folder), `.exists()` (file hai ya nahi), aur `.glob("*.json")` (pattern matching).

## JSON Serialization & Deserialization (`json` module) - 1) Packaging Analogy: Serialization (`json.dumps`) Python dict ko text string mein pack karta hai taaki internet/APIs par bhej sakein; Deserialization (`json.loads`) string parcel ko unpack karke Python dict banata hai. 2) 's' Rule: String ke liye `dumps` / `loads` (Dump/Load to String); File ke liye bina 's' ke `dump` / `load`. 3) Pretty Print (`indent=2`): Compact single-line JSON ko human-readable formatted shape deta hai. 4) Non-Serializable Trap (`default=str`): JSON sirf basic primitives samajhta hai; `datetime`, `set`, ya `Path` objects aane par `TypeError: Not JSON serializable` crash hota hai. `default=str` parameter lagane se har custom type string ban kar safe serialize ho jata hai. 5) Broken JSON Guard (`json.JSONDecodeError`): LLM ya external API se aane wali tooti hui JSON string par `json.loads` crash hone se bachane ke liye hamesha specific `except json.JSONDecodeError:` lagayein.

## Asynchronous Programming & Concurrency (`asyncio`) - 1) Waiter Analogy: Sync code I/O wait ke dauran poora CPU freeze kar deta hai; Async code (`async/await`) I/O wait ke dauran doosre tasks ko CPU de deta hai (FastAPI aur LLM calls ke liye mandatory). 2) Keywords: `async def` coroutine function banata hai; `await` pause point hai jo sirf `async def` ke andar hi chal sakta hai (normal function mein `SyntaxError` dega). 3) Event Loop: `asyncio.run(main())` coroutines ko background loop mein run karta hai. 4) Concurrent Gathering: `asyncio.gather(t1, t2, t3)` sabhi tasks ko parallel execute karta hai; 3 sequential calls ka 3 second ka time घटकर 1 second reh jata hai. 5) Blocking Anti-Pattern: `async def` ke andar `time.sleep()` ya `requests.get()` chalane se poora event loop freeze ho jata hai; hamesha `await asyncio.sleep()` aur async HTTP clients (`httpx`) use karein.

## Packaging, Virtual Environments & `pyproject.toml` - 1) Isolation with `venv`: Global Python mein sab packages daalne se library versions clash hote hain; `python -m venv .venv` har project ko isolated environment deta hai (Windows par `.venv\Scripts\activate` chalate hi `(.venv)` prompt dikhta hai). 2) Dependency Pinning: Bina version (`fastapi`) deploy karne par cloud updates live app crash kar sakte hain; exact versions (`==`) lock karne ke liye `pip freeze > requirements.txt` use karte hain. 3) Single Source of Truth (`pyproject.toml`): Bikhri hui config files ke badle modern PEP 621 standard `pyproject.toml` mein `[project]` metadata, python version (`requires-python`), aur `dependencies = [...]` ek jagah centralize hote hain. 4) Package Marking (`__init__.py`): Folder ke andar `__init__.py` file Python ko batati hai ki yeh importable package hai. 5) Editable Install (`pip install -e .`): Package ko dev mode mein install karta hai jisse code edits turant live reflect hote hain bina re-install kiye.

## GitHub Actions & Automated CI/CD (`.github/workflows/ci.yml`) - 1) Airport Security Analogy: Production code toote bina deploy karne ke liye CI pipeline har push/PR par cloud runner start karke automated tests verify karta hai. 2) Location & Structure: `.github/workflows/` folder ke andar `.yml` files banti hain; `name`, `on: [push, pull_request]`, `jobs:`, aur `runs-on: ubuntu-latest` iske mukhya hisse hain. 3) uses vs run: `uses: actions/checkout@v4` repo clone karta hai, `uses: actions/setup-python@v5` Python configure karta hai, aur `run:` direct terminal shell commands chalata hai. 4) YAML Dash Rule: Steps list ke har kadam ke aage `-` dash lagna compulsory hai; warna keys ek doosre ko overwrite kar deti hain. 5) Secret Isolation: Keys/passwords ko kabhi YAML mein hardcode mat karo; GitHub Secrets mein store karke `${{ secrets.MY_KEY }}` syntax se inject karo (logs mein auto-masked `***`).

## Git Branching Strategy & Lifecycle - 1) Live Pitch vs Net Practice: Production code (`main`) stable rehta hai; naye features ya bug fixes hamesha isolated branch (`git checkout -b feature/xyz`) par bante hain taaki live application safe rahe. 2) Uncommitted Files (M Flag): `git checkout` karte waqt uncommitted files (`M`) local working directory mein sath travel karti hain. 3) Flag `-b`: `git checkout <name>` sirf pehle se bani branch dhoondhta hai (nahi milne par pathspec error deta hai); nayi branch banakar switch karne ke liye `-b` (ya `git switch -c`) compulsory hai. 4) Safe Deletion: Kaam poora hone par pehle `main` par switch karo (`git checkout main`), phir `git branch -d <branch_name>` se purani branch delete karke repo clean rakho.

## Conventional Commits & Atomic Commits - 1) International Standard: `<type>: <description>` format Git itihaas ko clean, searchable aur automated changelog ke kaabil banata hai (`feat:`, `fix:`, `ci:`, `docs:`, `test:`, `refactor:`, `chore:`). 2) Atomic Commits: Ek commit mein saari files ka kachra nahi daalte; har logical task ka alag commit hota hai taaki future mein zaroorat padne par kisi ek specific bug ko rollback kiya ja sake. 3) Commit Hash & HEAD: Commit hash SHA cryptographic fingerprint hai jo code integrity aur history immutability ensure karta hai; `HEAD` active branch ke current latest commit ko point karta hai.

## Pull Requests (PR) & Merge Conflict Resolution - 1) PR & Code Review: Production `main` par direct push ke badle PR banti hai taaki team inspect kare aur CI checks pass hon. 2) Conflict Cause: Do branches same line ko modify karein toh Git bina pooche overwrite nahi karta (safety feature). 3) Conflict Markers: `<<<<<<< HEAD` (current code), `=======` (divider), `>>>>>>> incoming-branch` (aane wala code). 4) Resolution: Sahi code rakho, teeno markers delete karo, save karke `git add` + `git commit`. (Markers chhoot gaye toh Python `SyntaxError: invalid syntax` phekega). 5) Emergency Abort: Agar merge cancel karni ho toh `git merge --abort` sab kuch pehle jaisa safe kar deta hai.

## Git Rebase & Stashing (`git rebase`, `git stash`) - 1) Linear History: `git merge` do patriyon ko jodne ke liye extra merge commit banata hai; `git rebase main` feature branch ke commits ko uthakar `main` ke aakhiri commit ke aage seedhi line (linear sequence) mein re-play karta hai. 2) Golden Rule: Rebase commits ke SHA hashes badal deta hai (kyunki parent commit badal jata hai); isliye public/shared branch (`main`) par rebase kabhi nahi chalate, sirf private feature branches par chalate hain. 3) Stash Bag (`git stash`): Agar uncommitted changes hon toh Git rebase block karta hai (`error: cannot rebase: You have unstaged changes`); `git stash` uncommitted files ko temporary safe bag mein daalta hai aur rebase ke baad `git stash pop` se unhe wapas restore kar deta hai. 4) Rebase Conflicts: Conflict aane par resolve karke `git add <file>` karo aur `git rebase --continue` chalao (commit nahi karte); cancel karne ke liye `git rebase --abort`.

## GitHub Issues & Project Tracking (`gh issue`) - 1) Single Source of Truth: Har bug ya feature ek Issue banta hai jisse duplicate effort rukta hai aur team progress transparent rehti hai. 2) Auto-Close Keywords: Commit message ya PR description mein `fixes #id` ya `closes #id` likhne se branch merge hote hi issue automatically Closed mark ho jata hai (plain text jaise "fixed bug issue 1" trigger nahi hota). 3) CLI Integration: `gh issue create`, `gh issue list`, `gh issue view <id>`, aur `gh issue close <id>` se developer ko browser khole bina terminal se direct ticketing control milta hai.

## Pytest Fixtures & Test Isolation (`@pytest.fixture`) - 1) Fresh State Isolation: Har test function ko clean, isolated dummy data supply karta hai taaki ek test ka mutation (jaise list append ya balance deduction) doosre tests ko pollute na kare. 2) Auto-Injection: Test function ke parameter mein fixture ka naam likhte hi Pytest use automatically instantiate karke inject kar deta hai. 3) Global Sharing (`conftest.py`): Multi-file projects mein fixtures ko `conftest.py` mein rakhte hain jisse saari test files bina import kiye unhe use kar sakti hain. 4) Scope Management (`scope="session"`): Database connection ya AI models jaise heavy resources ke liye `scope="session"` use karte hain taaki wo har test mein baar-baar load na ho aur test suite fast rahe.

## Regression Testing & CI Gates - 1) Regression Concept: Naye code ya prompt change se puraane chalte hue features ka tootna Regression kehlata hai. 2) Automated Test Suite: Manual verification ke badle `python -m pytest` har baar saare puraane tests 1 second mein verify karta hai. 3) CI Blocker Gate: GitHub Actions mein regression suite fail hone par PR merge block ho jata hai (Red ❌), jisse toota hua code kabhi live production server ya users tak nahi pahunchta.

## AI Observability & Tracing (Langfuse) - 1) Black Box Problem: Production AI apps mein multiple steps (embedding, vector search, LLM generation) hote hain; normal logs latency, token consumption, aur ₹/$ cost ka step-by-step breakdown nahi de paate. 2) Trace vs Span vs Generation: Poore user request flow ko 'Trace' kehte hain; internal non-AI steps (DB retrieval, preprocessing) ko 'Span' (`@observe()`) kehte hain; LLM model calls ko 'Generation' (`@observe(as_type="generation")`) kehte hain jo model name, input prompt, output, aur token counts capture karta hai. 3) Import Order Gotcha: `load_dotenv()` hamesha `from langfuse import observe` se pehle chalna chahiye; agar Langfuse pehle import ho gaya toh wo khali environment dekh kar disable ho jata hai. 4) Decorator Syntax:
```python
from dotenv import load_dotenv
load_dotenv()  # 1. Pehle env load karo
from langfuse import observe
from langfuse.decorators import langfuse_context

@observe()  # Root Trace
def main_flow(query):
    # Tags aur custom metadata
    langfuse_context.update_current_trace(tags=["production"], metadata={"query_len": len(query)})
    docs = search_db(query)
    return generate_answer(query, docs)

@observe()  # Child Span (Database / Logic)
def search_db(q):
    return [...]

@observe(as_type="generation")  # Child Generation (LLM Call)
def generate_answer(q, docs):
    return client.models.generate_content(...)
```
5) Background Batching & `flush()`: Langfuse SDK telemetry ko background thread mein batch karta hai; FastAPI/server mein automatic rehta hai, lekin short CLI test scripts mein program exit hone se pehle `langfuse.flush()` lagana zaroori hai taaki queued traces cloud par sync ho sakein.

## LLM-as-a-Judge & Groundedness/Faithfulness Evaluation - 1) Why assert fails: LLMs non-deterministic hote hain (har baar alag shabdon mein sahi jawab dete hain), isliye traditional `assert output == expected` tests fail ho jaate hain. 2) Judge Pattern: Ek doosre strictly-prompted model (Evaluator) ko reference context (`retrieved_jobs`), candidate profile, aur diagnosis pass karke objective quality score (1.0 ya 0.0) aur qualitative reason nikaala jata hai. 3) Context is Mandatory: Bina retrieved context ke Judge kabhi bhi Faithfulness (sachai) verify nahi kar sakta, kyunki bina syllabus/kitaab ke Judge ko pata hi nahi chalega ki candidate ne hawa mein claims (hallucination) kiye hain ya context se bole hain. 4) Guaranteed JSON with Pydantic: `types.GenerateContentConfig(response_mime_type="application/json", response_schema=EvaluationResult)` lagane se model guaranteed schema follow karta hai, aur `res.parsed` seedha Python object instantiate kar deta hai bina manual `json.loads` ke.

## Automated Batch Evaluation & Golden Dataset - 1) Single Test Trap: Ek test pass hone ka matlab model production-ready nahi hota; diverse test cases (`test_dataset.json` - Python, Data, Web, Edge cases) ka Golden Dataset zaroori hota hai. 2) Automated Pipeline Runner: Har profile par retrieval (`match_jobs`) -> generation (`generate_diagnosis`) -> evaluation (`evaluate_faithfulness`) loop chala kar aggregate metrics (Average Faithfulness %) calculate hote hain. 3) ZeroDivisionError Guard: Agar dataset khali ho (`test_cases = []`), toh loop 0 baar chalega aur `sum(scores) / len(scores)` seedha `ZeroDivisionError: division by zero` dekar crash ho jayega; isliye hamesha `if len(scores) == 0:` guard check lagana chahiye. 4) CI/CD Blocker: Benchmark fail hone par (`avg_score < 0.8`) script `sys.exit(1)` throw karti hai taaki GitHub Actions CI build fail ho jaye aur kharab prompt live deploy na ho.

## Retrieval Evaluation Metrics (Hit Rate & MRR) - 1) Garbage In, Garbage Out: Agar Vector DB ne shuruat mein hi galat documents retrieve kiye toh LLM chahe kitna bhi accha ho output galat hi hoga; isliye Retrieval accuracy ko LLM se alag measure karte hain. 2) Hit Rate (Recall@K): Top-K results mein kam se kam ek sahi document mila ya nahi (1.0 ya 0.0). 3) MRR (Mean Reciprocal Rank): Sahi document kitna upar (rank) mila: Formula = 1 / rank. Rank 1 par 1.0 (best), Rank 2 par 0.5, Rank 4 par 0.25, na milne par 0.0. 4) Zero Cost & Instant: Pure Python logic hai, koi LLM call nahi, instant (0.01s) aur ₹0 cost. 5) Enumerate Start Gotcha: Python default counting 0 se shuru karta hai; `1.0 / rank` par crash se bachne aur human 1-based rank ke liye `enumerate(retrieved_jobs, start=1)` lagana compulsory hai. Case-insensitive matching ke liye dono taraf `.lower()` zaroori hai.

## AI Security & Guardrails (Prompt Injection & PII Masking) - 1) Airport Scanner Analogy: Public internet par deploy hone wale LLMs ko seedha user input nahi diya jata; malicious attacks aur data leaks se bachne ke liye beech mein Security Checkposts (Guardrails) lagte hain. 2) Direct Prompt Injection: Attacker model ke system prompt aur private data chori karne ke liye "ignore all instructions", "reveal system prompt", "you are now DAN" jaise attacks use karta hai. Pre-LLM Regex Blocklist (`INJECTION_PATTERNS`) se request ko LLM tak jaane se pehle hi reject kar diya jata hai. 3) Lowercase Normalization Trap: Attacker capital letters (`IGNORE ALL INSTRUCTIONS`) use karke case-sensitive filters ko bypass kar sakta hai; isliye matching se pehle `text.lower()` compulsory hai. 4) PII Redaction: Privacy laws (DPDP/GDPR) ke mutabiq personal phone numbers aur emails ko model ya logs mein bhejna mana hai; `re.sub()` se unhe `[REDACTED_PHONE]` aur `[REDACTED_EMAIL]` mein sanitize kiya jata hai. 5) Gatekeeper Pattern: Request flow: User Input -> `secure_user_input()` -> Agar attack hai toh Block (HTTP 400), agar safe hai toh Sanitized Text -> Vector DB & LLM.

## Rate Limiting & Abuse Prevention (Sliding Window Log) - 1) Problem: Bots aur DoS scripts 1 second mein hazaron requests bhej kar server crash kar sakti hain aur Gemini API quota/budget exhaust kar sakti hain. 2) Sliding Window Math: Har request aane par `now = time.time()` record hota hai. Purani requests ko filter karne ka formula hai: `[t for t in history if now - t < window_seconds]`. Agar `now - t` window se bada hai (jaise 80s > 60s), toh wo timestamp expire ho chuki hai aur list se nikaal di jaati hai. 3) State Tracking Trap: Nayi request allow hone par `history.append(now)` karna mandatory hai; agar append bhool gaye toh list ka count kabhi nahi badhega aur limiter hamesha requests allow karta rahega (loophole). 4) HTTP 429 Status: Limit cross hone par REST APIs mein standard status code `429 Too Many Requests` return kiya jata hai.
















