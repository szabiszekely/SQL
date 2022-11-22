import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()

class Adatbazis:
    def __init__(self,sor):
        AtomicNumber,Element,Symbol,*kutya = sor.strip().split(",")
        self.AtomicNumber = AtomicNumber
        self.Element = Element
        self.Symbol = Symbol
        
with open("peri.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    data = [Adatbazis(sor) for sor in f]
cur.execute("DROP TABLE IF EXISTS periodus")

cur.execute("""CREATE TABLE periodus
    (AtomicNumber TEXT,
    Element TEXT,
    Symbol TEXT)
""")
for i in data:
    lista = [(i.AtomicNumber,i.Element,i.Symbol)]
    cur.executemany("INSERT INTO periodus VALUES (?,?,?)", lista)
    
con.commit()

msg = cur.execute("SELECT * FROM periodus")

for row in cur.exe
print(row)