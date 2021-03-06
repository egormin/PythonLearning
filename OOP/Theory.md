## OOP Theory

**Парадигма программирования** - это совокупность идей и понятий, определяющих стиль написания компьютерных программ, подход к программированию.

Python поддерживает разные парадигмы программирования:
* Императивное программирование
* Процедурное программирование
* Структурное программирование
* Объектно-ориентированное программировани
* Функциональное программировани

Их можно разделить на 2 большие группы:
* Императивное программирование
* Декларативное программирование

**Императивное** - парадигма, при которой мы определяем не что мы хотим получить, а что нам необходимо сделать для получения данного результата. Т.е. ту последовательность действий, которую нам необходимо выполнить шаг за шагом. Сюда входят процедурное, структурное и т.д.

**Декларативное** - когда мы определяем не что нужно сделать, а что мы хотим получить. Мы описываем правила, по которым данные могут быть преобразованы. На основе этого и получаем результат. Сюда входит функциональное, логическое программирование (язык prolog).

ООП часто относят к императивному программированию. Но лучше выделить их в третью отдельную группу.

________________________________________________________________________________________________________________________________
**Объектно-ориентированное программирование (ООП)** - парадигма программирования, в которой основными концепциями являются понятия классов и объектов.

**Класс** является моделью ещё не существующей сущности (объекта). Он является составным типом данных, включающим в себя поля и методы. 

Класс - это составной тип данных. Он содержит свойства и поведение. Свойства - это поля (переменные, которые находятся внутри объектов данного класса). Поведение - задается методами (медоды - функции, принадлежащие объектам данного класса).

**Объект** - это экземпляр класса.

**Основные принципы ООП:**
* Абстракция
* Инкапсуляция
* Полиморфизм
* Наследование

**Абстракция** - означает, что мы передаём нашим объектам только те характеристики, которые четко опрелеляют его концептуальные границы и которые чётко отличают его от других объектов. Причём, если какие-то характеристики его нас не интересуют, то мы их не рассматриваем и не описываем. Кроме того, мы разделяем существенные детали реализации от несущественных, которые нужны для корректного использования использования данных объектов.

**Инкапсуляция** - обекты могут содержать различные данные и поведение, при этом каке-то из них являются публичными и доступными для использования из-вне, а какие-то являются *деталями реализации* и должны быть скрытыми для доступа из-вне. Т.о. те детали реализации, которые и не должны интересовать пользователей данного класса ему и не видны.

**Наследование** - при наследовании классов, классы наследники получают всё те же самые поведения и свойства, которые были и в базовом классе, либо же добавлять свои или же переопределять старые. Т.е. при наследовании новый класс является тем же самым, что и страрый, но при этом с какими-то дополнениями или изменениями.

___________________________________________________________________________________________________________________________

### Инкапсуляция 
**Инкапсуляция** - это свойство системы, позволяющее объединить данные и методы, работающие с ними, в классе, и *скрыть* детали реализации.

Инкапсуляцию можно разделить на 3 группы:
* Скрытие типов данных
* Скрытие членов класса
* Скрытие частей программной системы

***Инкапсуляция обеспечивается следующими средствами:***
* Контроль доступа (это обычно реализуется с помощью модификаторов доступа, таких как *private*, *protected*, *public*).
**Private** доступны только для самого класса и не доступны ни для кого другого, **protected** - доступны для данного класса и его потомков, но недоступны для других, **public** - доступны для всех. В Python как таковых модификаторов доступа нет, но модно реальзовать нечто подобное.
* Методы доступа (геттеры и сеттеры или аксессоры и мутаторы). Это обычные публичные методы, которые позволяют получить доступ к приватным переменным (приватным членам класса). Их суть в том, что мы напрямую не обращаемся к определённым полям данного класса, а используем специальные методы, которые делегируют доступ к ним и могут совершать какие-то дополнительные действия (например, проверять значение на корректность и т.д.)
* Свойства объекта - аналогичный по назначению методам доступа, но более удобный в использовании механизм, который позволяет сделать то же самое, но используя более удобный синтаксис обычного обращения к полям собветствующего класса или объекта. Для реализации этой функциональности нудна соответствующая поддержка в языке (в Python есть). Как правило, если используются свойства, то методы доступа не используются, т.к. это практически идентичные функциональности.

___________________________________________________________________________________________________________________________
## ООП в Python
В Python всё является объектами - экземпляром каких-либо классов, даже сами классы, которые являются объектами - экземплярами метаклассов. Главным метаклассом является класс type, который является абстракцией понятия типа данных.

### Классы в Python
В терминологии Python члены класса называются **атрибутами**. Эти атрибуты могут быть как переменными, так и функциями.

Классы создаются при помощи ключевого слова ***class***.

Классы как объекты поддерживают 2 вида операций: обращение к атрибутам классов и создание (инстанцирование) объектов - **экземпляров класса** (*instance objects*).

Обрещение к атрибутам какого-либо класса или объекта производится путём указания имени объекта и имени атрибута через точку. 

Для создания экземпляров класса используется синтаксис вызова функции. `obj = MyClass()`.

### Экземпляры классов в Python
Единственная доступная операция объектов-экземпляров - это доступ к их атрибутам.

Атрибуты *объектов-экземпляров* делятся на 2 типа: **атрибуты-данные** и **методы**.

Атрибуты-данные аналогичны *полям* в терминологии большинства широко распространённых языков программирования.

Атрибуты-данные не нужно описывать: как и переменные, они создаются в момент первого присвоения. Как правило, их создают в методе-конструкторе `__init__`.

**Метод** - это функция, принадлежащая объекту. Все атрибуты класса, являющиеся функциями, описывают соответствующие методы его экземпляров, однако, они не являются одним и тем же.

Особенностью методов является то, что в качестве первого аргумента им *передается данный экземпляр класса*. Таким образом, если obj - экземпляр класса MyClass, вызов метода obj.method эквивалентен вызову функции MyClass,method(obj).

Первый аргумент метода, который соответствует текущему экземпляру, принято называть `self`.

#### Разница между атрибутами класса и атрибутами данными
**Атрибуты класса** являются общими для самого класса и всех его экземпляров. Их изменение отражается на все соответствующие объекты. 

**Атрибуты данные** принадлежат конкретному экземпляру и их изменение никак не влияет на соответствующие атрибуты экземпляров данного класса. Таким образом, атрибуты класса, которые не являются функциями, примерно соответствуют статическим полям в других языках программирования, а атрибуты-данные - обычным полям.

### Статические методы и методы класса
**Декоратор** - это специальная функция, которая изменяет поведение функции или класса. Для применением декоратора следует перед соответствующим объявлением указать символ `@`, имя необходимого декоратора и список его аргументов в круглых скобках. Если передача параметров декоратору не требуется, скобки не указываются. 

Для создания **статических методов** используется декоратор `staticmethod`. Статический метод не привязан к экземпляру класса.

Для создания **методов класса** используется декоратор `classmethod`.

**Методы класса** похожи на обычные методы, но относятся к самому классу как объекту - экземпляру метакласса (в отличие от обычных методов, которые принадлежат объектам - экземплярам классов, и статических методов, которые относятся к самому классу и всем его экземплярам и не принадлежат никакому объекту экземпляру). Их первый аргумент принято называть `cls`.

### Инкапсуляция в Python
Все атрибуты по умолчанию являются **публичными**.

Атрибуты, имена которых начинаются с *одного знака подчеркивания `(_)`* говорят программисту о том, что они относятся ко внутренней реализации класса (к деталям реализации класса) и не должны использоваться из-вне, однако, никак *не защищены*. Это как protected. Они могут использоваться только изутри и в классах-наследниках. 

Атрибуты, имена которых начинаются, но не заканчиваются *двумя символами подчеркивания*, считаются **приватными**. К ним применяется механизм **"name mangling"**. Он не предполагает защиты данных от изменения из-вне, так как к ним всё равно можно обратиться, зная имя класса и то, как Python изменяет имена приватных атрибутов, однако, *позволяет защитить их от случайного переопределения в классах-потомках*.

### Специальные атрибуты и методы
Атрибуты, имена которых начинаются и заканчиваются *двумя знаками подчеркивания*, являются внутренними для Python и задают особые свойства объектов (примеры: __doc__, __class__).

Среди таких атрибутов есть методы. В документации Python подобные методы называют **методами со специальными именами**, однако в сообществе Python разработчиков очень распространено название **"магические методы"**. Также встречается и название **"специальные методы"**. Они задают особое поведение объектов и позволяют переопределять поведение встроенных функций и операторов для экземпляра данного класса.

Наиболее часто используемым из специальных методов является метод `__init__`, который автоматический вызывается после создания экземпляра класса.

Не следует объявлять свои собственные (нестандартные атрибуты) с именами, которые начинаются и заканчиваются двумя знаками подчёркивания.

```
str - строковое представление для пользователя.
repr - строковое представление для разработчика
```
