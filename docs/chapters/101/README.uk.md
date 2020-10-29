<table>
  <tr>
    <td width="70%"><h1>Jina 101: Перше, що варто вивчити про Jina</h1>
    <a href="https://twitter.com/intent/tweet?text=%F0%9F%91%8DCheck+out+Jina%3A+the+New+Open-Source+Solution+for+Neural+Information+Retrieval+%F0%9F%94%8D%40JinaAI_&url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina&hashtags=JinaSearch&original_referer=http%3A%2F%2Fgithub.com%2F&tw_p=tweetbutton" target="_blank">
  <img src="../../../.github/badges/twitter-share101.svg?raw=true"
       alt="tweet button" title="👍Спробуйте Jina: нове Open-Source рішення для нейропошуку інформації 🔍@JinaAI_"></img>
</a>
  <a href="../../../README.uk.md#jina-привіт-світе-👋🌍">
    <img src="../../../.github/badges/jina-hello-world-badge.svg?raw=true" alt="Запустити Jina Hello World">
</a>

<a href="https://docs.jina.ai">
    <img src="../../../.github/badges/docs-badge.svg?raw=true" alt="Читати документацію">
</a>
<a href="https://github.com/jina-ai/jina/">
    <img src="../../../.github/badges/jina-badge.svg?raw=true" alt="Відвідати Jina на Github">
</a>
<a href="https://jobs.jina.ai">
    <img src="../../../.github/badges/jina-corp-badge-hiring.svg?raw=true" alt="Переглянути jobs@Jina AI">
</a>
    <a href="#">
    <img src="../../../.github/badges/pdf-badge.svg?raw=true" alt="Завантажити PDF-версію Jina 101">
    </a>
     <br>
<a href="README.md">English</a> •
  <a href="README.ja.md">日本語</a> •
  <a href="README.fr.md">Français</a> •
  <a href="README.pt.md">Português</a> •
  <a href="README.de.md">Deutsch</a> •
  <a href="README.ru.md">Русский язык</a> •
  <a href="README.zh.md">中文</a> •
  <a href="README.ar.md">عربية</a> •
  <a href="README.uk.md">Українська</a>
    </td>
    <td>
      <img src="img/ILLUS12.png?raw=true" alt="Jina 101 концепт книги з ілюстраціями, Авторські права Jina AI Limited" title="Jina 101 концепт книги з ілюстраціями, Авторські права Jina AI Limited"/>
    </td>
  </tr>
</table>

Хочете отримати загальне уявлення про нейропошук та наскільки він відрізняється від звичайного символьного пошуку? [Ознайомтесь із нашим пояснюючим постом у блозі](https://medium.com/@jina_ai/what-is-jina-and-neural-search-7a9e166608ab) щоб дізнатися більше!

<h2 align="center">Документ та Чанк</h2>

<img align="left" src="img/ILLUS1.png?raw=true" alt="Jina 101 концепція Документу та Чанку, Авторські права Jina AI Limited" title="Jina 101 концепція Документу та Чанку, Авторські права Jina AI Limited" hspace="10" width="30%"/>


Коли більшість людей думає про пошук, вони думають про рядок, у який вводять слова, наприклад Google. Але пошук - це значно більше за це, так само як тест, вам, можливо, захочеться шукати пісню, рецепт, відео, генетичну послідовність, наукову працю або місцезнаходження.

У Jina, ми називаємо усі ці речі **Документами**. Коротко кажучи, Документ - це все, що ви можете хотіти шукати і вхідний запит, який ви використовуєте коли шукаєте.

Документи можуть бути величезними, хоча як ми можемо шукати правильну частину? Ми робимо це розбиваючи Документ на **Чанки**. Чанк - це невеличка семантична одиниця Документу, як речення, 64x64 піксельне зображення або пара координат. 

Уявіть Документ у вигляді плитки шоколаду. Документи мають різні формати та інгредієнти, але ви можете розділити їх на чанки як завгодно. Зрештою, те, що ви купуєте та зберігаєте є плитками шоколаду, а те, що ви їсте та перетравлюєте - чанки. Вам не хочеться проковтувати цілу плитку, але ви і не бажаєте розкришуквати її у порошок; Роблячи так, ви втрачаєте смак (тобто семантику).

<br/><br/><br/>

<h2 align="center">Налаштування YAML</h2>

<img align="right" src="img/ILLUS2.png?raw=true" alt="Jina 101 YAML, Авторські права Jina AI Limited" title="Jina 101 YAML Concept, Авторські права Jina AI Limited" hspace="10" width="30%"/>

Кожна частина Jina налаштовується за допомогою **файлів YAML**. Файли YAML пропонують налаштування, які дозволяють змінювати поведінку об'єкту, не змінюючи його коду. Jina може побудувати дуже складний об'єкт безпосередньо з YAML-файлу або зберегти об'єкт у YAML-файл.

<br/><br/><br/><br/><br/><br/>

<h2 align="center">Executor-и</h2>

<img align="left" src="img/ILLUS3.png?raw=true" alt="Jina AI Executor, Авторські права Jina AI Limited" title="Jina AI Executor Concept, Авторські права Jina AI Limited" hspace="10" width="30%"/>

Як ми розбиваємо Документ у Чанки та що відбувається далі? **Executor-и** роблять всю цю важку роботу, а кожен з них представляє собою певну алгоритмічну одиницю. Вони роблять такі речі, як кодування зображень у вектори, зберігання векторів на диску, ранжування результатів, тощо. Кожен з них має простий інтерфейс, що дозволяє сконцентруватися на алгоритмі та не заморочуватись над дрібницями. Вони з коробки володіють неперервністю, плануванням, ланцюгуванням, групуванням та розпаралелюванням. Властивості Executor зберігаються у [YAML-файлі](#configuring-jina-with-yaml). Вони завжди розміщуються поряд один з одним.

<br/><br/><br/>

<h3 align="center">Сім'я Executor</h3>


<p align="center">
  <img src="img/ILLUS4.png?raw=true" alt="Jina 101 Сім'я Executor, Авторські права Jina AI Limited" title="Jina 101 Сім'я Executor, Авторські права Jina AI Limited" hspace="10" width="80%"/>
</p>

**Executor-и** є великою сім'єю. Кожен член сім'ї зосереджується на одному важливому аспекті пошукової системи. Давай зустрінемось з:
- **Crafter**: для створення/сегментування/перетворювання Документів та Чанків;
- **Encoder**: для представлення Чанку, як вектора;
- **Indexer**: для збереження та отримання векторів та ключ-значення даних зі сховища;
- **Ranker**: для сортування результатів;

Маєте на думці новий алгоритм? Не біда, ця сім’я завжди приймає нових членів!

<br/><br/>

<h2 align="center">Driver-и</h2>

<img align="right" src="img/ILLUS5.png?raw=true" alt="Jina 101 Driver, Авторські права Jina AI Limited" title="Jina 101 Driver, Авторські права Jina AI Limited" hspace="10" width="30%"/>

Executor-и роблять всю важку роботу, але вони не є дуже вправними у спілкуванні між собою. **Driver** допомагає їм робити це визначаючи як Executor реагує на мережеві запити. Він інтерпретує мережевий трафік у форматі, який Executor може розуміти, наприклад, перекладаючи Protobuf у масив Numpy.

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>



<h2 align="center">Peas</h2>

<img align="left" src="img/ILLUS6.png?raw=true" alt="Jina 101 Pea, Авторські права Jina AI Limited" title="Jina 101 Pea, Авторські права Jina AI Limited" hspace="10" width="30%"/>

Всім здоровим сім'ям потрібно спілкуватися і родина Executor не відрізняється у цьому. Вони говорять між собою за допомогою **Peas**.

Поки Driver перекладає дані для Executor, Pea обгортає Executor та дозволяє йому обмінюватися даними через мережу або з іншими Peas. Peas також можуть працювати у Docker, вміщуючи всі залежності та контекст в одному місці.

<img align="right" src="img/ILLUS7.png?raw=true" alt="Jina 101 Pea, Авторські права Jina AI Limited" title="Jina 101 Pea, Авторські права Jina AI Limited" hspace="10" width="30%"/>

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>



<h2 align="center">Pod-и</h2>

<img align="left" src="img/ILLUS8.png?raw=true" alt="Jina 101 Pod, Авторські права Jina AI Limited" title="Jina 101 Pod, Авторські права Jina AI Limited" hspace="10" width="30%"/>

Отже, тепер ви маєте чимало Peas, які спілкуються між собою та повсюди обертаються. Як ви можете їх організувати? Природа використовує **Pod-и** і ми також.

Pod - це група Peas з однаковими властивостями, і працюють паралельно на локальному пристрої або по мережі. Pod забезпечує єдиний мережевий інтерфейс для своїх Peas, роблячи їх ззовні схожими на одну Pea. Крім цього, Pod додає додатковий контроль, планування та управління контекстром для Peas.

<img align="right" src="img/ILLUS9.png?raw=true" alt="Jina 101 Pod Remote, Авторські права Jina AI Limited" title="Jina 101 Pod Remote, Авторські права Jina AI Limited" hspace="10" width="30%"/>

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

<h2 align="center">Flow</h2>


<img align="left" src="img/ILLUS10.png?raw=true" alt="Jina 101 Flow, Авторські права Jina AI Limited" title="Jina 101 Flow, Авторські права Jina AI Limited" hspace="10" width="30%"/>


Тепер ми маємо наповнений Pod-ами сад, з кожним Pod повним Peas. Це дуже багато, щоб управляти! Привітайтесь з **Flow**! Flow - це як рослина Гороху. Подібно до того, як рослина керує потоком кориних речовин та швидкістю росту свої відгалужень, Flow керує станами та контекстом групи Pods, організовуючи їх для виконання одного завдання. Незалежно від того, чи Pod є віддаленим, чи працює у Docker, один Flow керує ними усіма!

<br/><br/><br/><br/><br/><br/>



<h2 align="center">Від Мікро до Макро</h2>


Jina є щасливою родиною. Ви можете відчути гармонію використовуючи Jina.

Ви можете проєктувати на мікрорівні та масштабуватись до макрорівня. YAML стають алгоритмами, потоки стають процесами, Pods стають Flows. Патерни та логіка завжди залишаються незмінними. У цьому й краса Jina.


<p align="center">
  <img src="img/ILLUS11.png?raw=true" alt="Всі персонажі Jina 101, Авторські права Jina AI Limited" title="Всі персонажі Jina 101, Авторські права Jina AI Limited" hspace="10" width="80%"/>
</p>

<br/><br/><br/><br/>

<p align="center">
<a href="../../../README.uk.md#jina-привіт-світе-👋🌍">
    ✨<b>Заінтриговані? Спробуйте наш "Привіт, світе!" та побудуйте власний нейропошук зображень за 1 хвилину. </b>
</a>
</p>
<br><br><br>
<p align="center">
    ✨<b>Дайте волю вашій цікавості та щасливого пошуку! </b>🔍
</p>
<br><br><br>
<p align="center">
    <a href="https://twitter.com/intent/tweet?text=%F0%9F%91%8DCheck+out+Jina%3A+the+New+Open-Source+Solution+for+Neural+Information+Retrieval+%F0%9F%94%8D%40JinaAI_&url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina&hashtags=JinaSearch&original_referer=http%3A%2F%2Fgithub.com%2F&tw_p=tweetbutton" target="_blank">
  <img src="../../../.github/badges/twitter-share101.svg?raw=true"
       alt="tweet button" title="👍Спробуйте Jina: нове Open-Source рішення для нейропошуку інформації 🔍@JinaAI_"></img>
</a>
  <a href="../../../README.uk.md#jina-привіт-світе-👋🌍">
    <img src="../../../.github/badges/jina-hello-world-badge.svg?raw=true" alt="Запустити Jina Hello World">
</a>

<a href="https://docs.jina.ai">
    <img src="../../../.github/badges/docs-badge.svg?raw=true" alt="Читати документацію">
</a>
<a href="https://github.com/jina-ai/jina/">
    <img src="../../../.github/badges/jina-badge.svg?raw=true" alt="Відвідати Jina на Github">
</a>
<a href="https://jobs.jina.ai">
    <img src="../../../.github/badges/jina-corp-badge-hiring.svg?raw=true" alt="Переглянути jobs@Jina AI">
</a>
    <a href="#">
    <img src="../../../.github/badges/pdf-badge.svg?raw=true" alt="Завантажити PDF-версію Jina 101">
    </a>
</p>
<br><br><br>



Зовнішній вигляд цього документа ("Jina 101: Перше, що варто вивчити про Jina") є авторським правом © Jina AI Limited. Всі права захищені. Клієнт не може копіювати, копіювати чи використовувати повторно будь-яку частину елементів візуального дизайну або концепції без письмового дозволу Jina AI Limited.

