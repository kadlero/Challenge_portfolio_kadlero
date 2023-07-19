# Task 1: konfiguracja oprogramowania.
## Subtask 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?
###### Zdecydowałam się wziąć udział w projekcie, ponieważ poszukuję nowych wyzwań 🙃. 
###### To dzięki DareIT znalazłam swój pierwszy staż testerski i jestem bardzo zadowolona, że wzięłam w nim udział. Mam już za sobą pierwsze szlify w ramach testowania oprogramowania, zdobyłam certyfikat ISTQB FL. 
###### Analizując oferty pracy uznałam, że automatyzacja to kierunek bardzo pożądany na rynku pracy 😉. Projekt _Testy automatyczne + Python_ pozwoli mi na zaznajomienie się z tematem w bezpieczny dla mnie sposób 😇 (pod okiem mentora) i podjęcie decyzji czy nadal chcę się rozwijać w tym kierunku. 
###### Napędza mnie chęć nauczenia się nowych rzeczy i zwiększenie atrakcyjności moich dokumentów aplikacyjnych 😊 (w czasie wakacji zamierzam aktywnie szukać pracy). 
######  Moim celem jest ukończenie wszystkich zadań w ramach projektu i zdobycie certyfikatu 😁. 
###### Moje oczekiwania względem projektu? Chciałabym stworzyć projekt, którym będę mogła się pochwalić rekruterom 🤩. Chcę być absolutnie dumna, że dokonałam nowej rzeczy 😊!

### Podsumowanie
<TABLE>

<TR> <TD><i> Dlaczego zdecydowałaś się wziąć udział w projekcie? </i></TD><TD> Dla frajdy z nauczenia się czegoś nowego </TD></TR>

<TR> <TD><i> Co Cię napędza? </i></TD><TD> Sam fakt uczenia się i podrasowanie CV-ki </TD></TR>

<TR> <TD><i> Jaki jest Twój cel? </i></TD><TD> Ukończenie projektu i zdobycie certyfikatu </TD></TR>

<TR> <TD><i> Jakie masz oczekiwania względem projektu? </i></TD><TD> Zabawa i nauka </TD></TR>

</TABLE>

## Subtask 4: Wykonania testu na stronie GET ISTQB: http://getistqb.com/quiz-purpurowy/



<h6><span style="color:green"> Udzielono odpowiedzi dobrze na:</span> <span style="color:red"> 8</span> z <span style="color:blue"> 14</span> pytań</h6>

# Task 2: Selektory
## Subtask 2: Wyszukiwanie selektorów na stronie logowania. Wymień wszystkie elementy, które znajdują się na stronie logowania

### login_field_xpath
###### //*[@id="login"]
###### //*[@name="login"]
###### //*[@id="login" or @ name="login"]
###### //*[@id="login" and @ name="login"]
###### //*[@id="__next"]/form/div/div[1]/div[1]
###### /html/body/div/form/div/div[1]/div[1]/div
### password_field_xpath
###### //*[@id="password"]
###### //*[@name="password"]
###### //*[@id="__next"]/form/div/div[1]/div[2]
###### /html/body/div/form/div/div[1]/div[2]/div/input
### remaind_password_hyperlink_xpath
###### //*[@id="__next"]/form/div/div[1]/a
###### //*[text()="Remind password"]
###### //child::div/a
###### /html/body/div/form/div/div[1]/a
### language_listbox_xpath
###### //*[@id="__next"]/form/div/div[2]/div/div
###### //*[@role="button"]
###### /html/body/div/form/div/div[2]/div/div
### sign_in_button_xpath
###### //*[@id="__next"]/form/div/div[2]/button/span[1]
###### //*[text()="Sign in"]
###### /html/body/div/form/div/div[2]/button/span[1]

# Task 3: Pierwszy test automatyczny i asserty
## Subtask 2: TestMediumPage - PASSED
## Subtask 3: Pierwszy test i assert
### 🤩 log_in_to_the_system.py - PASSED