# Ladders and Snakes
## Třída Game
- má pod kontrolou hrací desku i hráče
- vytvořením instance se načte vše potřebné
- zavoláním metody `play` se hra spustí
- hra vyvolává výjimky, především při nesprávných argumentech

## Konfigurace hrací desky
- hrací deska je jednoduše konfigurovatelná
- při vytváření instance `Game` stačí předat python slovník obsahující
  1) start -> kterým číslem má deska začínat
  2) end -> kterým číslem má deska končit 
  3) special_squares -> políčko s kterým číslem je speciální a na které políčko má být přesunut hráč, pokud na něj stoupne
- ukázková konfigurace je v souboru `board_config.py`, kde je slovník, který je výchozí konfigurací

## Rozdělení odpovědnosti
- hra řekne hráči, aby provedl svůj tah (v tuto chvíli pouze hození kostkou a posunutí své pozice)
- poté zkontroluje hráčovu pozici a podle toho, kde skončil, zareaguje
- úloha hráče a hry je tedy logicky oddělená
- do budoucna tak může být jednoduše rozšiřitelná

## Možná rozšíření
- zobrazení pro uživatele by mohlo být grafické
- z třídy Player by mohla podědit třída RealPlayer a MpcPlayer
  - mohly by implementovat jen ty metody, které budou pro MPC hráče a reálného hráče rozdílné
  - prozatím je možnost vytvoření reálného a MPC hráče závislá pouze na argumentu `wait_for_player`
- deska by mohla být pole objektů nové třídy `Square`
- ta by zajišťovala především zobrazení pro uživatele
