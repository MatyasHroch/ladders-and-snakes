# Ladders and Snakes
## Třída Game
- má pod kontrolou hrací desku i hráče
- vytvořením instance se načte vše potřebné
- je možné předat různé argumenty pro úpravu běhu hry
  - `wait_for_user` -> pokud je na True, tak se před každým tahem hráče čeká na interakci uživatele
  - `board_config` -> jde o konfuguraci hrací desky, ta je totiž modulární, podrobněji později
- zavoláním metody `play` se hra spustí
- hra vyvolává výjimky, především při nesprávných argumentech

## Konfigurace hrací desky
- hrací deska je jednoduše konfigurovatelná
- při vytváření instance `Game` stačí předat python slovník obsahující
  1) start -> kterým číslem má deska začínat
  2) end -> kterým číslem má deska končit 
  3) special_squares -> python slovník, kde klíčem je číslo speciálního políčka a hodnota je číslo políčka, na které má být hráč přesunut
- ukázková konfigurace je v souboru `board_config.py`, kde je slovník, který je zároveň výchozí konfigurací

## Rozdělení odpovědnosti
- hra řekne hráči, aby provedl svůj tah
  - v tuto chvíli pouze hození kostkou a posunutí své pozice
  - později by se mohlo jednat o něco komplexnějšího
- poté zkontroluje hráčovu pozici a podle toho, kde skončil, zareaguje
- úloha hráče a hry je tedy logicky oddělená

## Možná rozšíření, ke kterým řešení směřuje
- zobrazení pro uživatele by mohlo být grafické (vzhledem k povaze zadání jsem zůstal u jednoduchých výpisů)
- třída Player by mohla být zděděna novými třídami RealPlayer a MpcPlayer
  - ty by mohly implementovat jen ty metody, které budou pro MPC hráče a reálného hráče rozdílné
  - pro hru zůstanou hráči stále typu Player
  - prozatím je možnost vytvoření reálného a MPC hráče závislá pouze na argumentu `wait_for_player`
