Projekt aplikacji webowej z interfejsem użytkownika i dostępem do bazy danych. Aplikacja uruchamiana jest za pomocą docker compose up.

Program został napisany w języku Python, we frameworku Django. Użyta została baza danych MySQL.



TEMAT PROJEKTU: Aplikacja webowa do tworzenia i zarządzania zadaniami typu To-Do List.


AUTORZY: Bańburski Sebastian 39952, Łacińska Aleksandra 40361 (grupa L1)

REPOZYTORIUM: https://github.com/sentresik/Django-App.git



WYMAGANIA:
- aplikacja Docker
System operacyjny:
- Windows (Testowano na Windows 10, Windows 11)
- Macbook (Testowano na MacOS Ventura)
 

INSTRUKCJA URUCHOMIENIA PROGRAMU:
1. Pobierz repozytorium na swoje urządzenie i przejdź do folderu z projektem.
2. Otwórz CMD/terminal na scieżce Django-App/App
3. Postaw i uruchom kontener bazy danych wpisując komendę:
	docker-compose up mysql -d --build
4. Postaw i uruchom kontener aplikacji wpisując komendę:
	docker-compose up django -d --build
5. Otwórz w dowolnej przeglądarce ścieżkę http://localhost:8000


OPIS KORZYSTANIA Z APLIKACJI:
1. Zarejestruj swojego użytkownika w aplikacji. Możesz podać fikcyjnego maila. Nie jest wysyłane drogą mailową żadne potwierdzenie rejestracji konta.
2. Zaloguj się do aplikacji za pomocą danych, które podałeś podczas rejestracji konta.
3. Aby stworzyć nową listę zadań, kliknij na przycisk "Create new list", uzupełnij nazwę listy, krótki opis (opcjonalnie) i zapisz parametry.
4. Aby edytować nazwę lub opis stworzonej listy zadań, kliknij w przycisk "Edit" i zmień swoje parametry.
5. Aby skasować utworzoną listę kliknij w przycisk "Delete".
6. Aby przejść do widoku zadań, kliknij w nazwę utworzonej listy.
7. Aby dodać nowe zadania kliknij w przycisk "Add item", uzupełnij nazwę zadania i zapisz parametry.
8. Analogicznie do widoku spisu Twoich list zadań, w widoku wybranej listy zadań również możesz edytować i usuwać wybrane pozycje.
9. Aby ukończyć wybrane zadanie, kliknij w przycisk "Complete" i pozycja zniknie z listy zadań do wykonania.