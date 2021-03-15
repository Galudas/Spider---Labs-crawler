# Spider Labs-crawler


  ## Spider Version 1.0 - crawler pentru laboratoare
  ### *Fisiere*
   - chromedriver - necesar pentru rulare 
   - spider.py - crawler pentru cs curs
   - students 
      - fisier .txt unde se afla numele studentilor a caror laboratoare le dorim descarcate
      - **IMPORTANT** - numele studentului corespunde 1 la 1 cu _numele utilizatorului de pe teams_ sau coloana _Prenume / Nume_ de pe _cs curs_ din sectiunea de upload/
         
         
  ### *Rulare*
    python3 spider.py id username password
   - **id** - Pentru obtinerea id-ului se urmeaza urmatorii pasi
      - Se intra pe upload-ul dorit (Ex. Upload labolator 1)
      - De pe url, se selecteaza id-ul (Ex. ...curs.upb.ro/mod/assign/view.php?id=_**204760**_)
   - **username** -> nume utilizator cs curs
   - **password** -> parola utilizator
      
      
 ### *Mentiune*
   - In sectiunea de upload, **Prenumele** si **Numele** trebuie neaparat sa fie setat pe **Toate**
   - Rezultatele vor fi salvare in directorul **labs** (Se va crea automat) 
  
