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