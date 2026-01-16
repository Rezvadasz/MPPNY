# 

Ez a projekt egy egyszerű AMD proceszor teljesítmény listázó

## Fő funkciók

-  **Lokális adatbázisban tárolja a benchmark erdeményeket (UserBenchmark)**
-  **Összehasonlítsa a 10 legjobb erdedményét single és multicore teljesítmény alapján egy grafikon segítségével**
-  **Megjeleníti a fris amd híreket BeautifulSoup segítségével a TechPoerUp nevü oldalról**

## Telepítés és futtatás
### Virtuális környezet létrehozása
``` bash
CREATE_venv.bat
```
> [!NOTE]
> Ez a script létrehoz egy venvet majd telepíti a kelő függőségeket.

### Futtatás

1. Backend
``` bash
START_backend.bat
```
> [!NOTE]
> Elindít egy Uvicorn szervert ami a FastAPI működéséhez kell.

2. Frontend
``` bash
START_frontend.bat
```
> [!NOTE]
> Elindít egy Streamlit webes felületet.

## Használt technológiák

-   **Python 3**
-   **FastAPI** -- REST backend
-   **Uvicorn** -- ASGI szerver
-   **Streamlit** -- frontend webes felület
-   **requests + BeautifulSoup** -- web scraping



