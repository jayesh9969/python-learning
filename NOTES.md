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

11. join. "\n".join(list) — gond par lagta hai, list par nahi. list.join("\n") error deta hai. Aur res["documents"] ek parat andar hoti hai, isliye res["documents"][0] par lagta hai. -->

