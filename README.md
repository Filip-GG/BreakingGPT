# Топовый проект в сфере ML
Папки:
- dataset_input -- входной набор данных для дообучения модели
- dataset -- обработанный наброр данных

# Описание исполняемых файлов
- pdf_convector -- набор функций конвертации файлов в pdf для дльнейшей работы
- localEmbeddings -- класс emebeddings для работы с lm studio

# Текущий этап
## В процессе иследования дата сета (имееться пример работы в main)

# План
1. Преобразовать текст из Pdf в txt
    - ~~Открыть pdf~~
    - ~~Получить данные~~
    - ~~Разбить текст на сигменты~~

2. Реализовать класс YaGPTEmbeddings
    - Рализовать класс YaGPTEmbeddings унаследовав из langchain.embeddings.base.Embeddings
    - Разить текст на сигменты

3. Получить векторную базу данных
4. Реализовать класс YaGPT (для запросов)
5. Молиться что все заработает

# Доп. ссылки:
- https://soshnikov.com/ai/creating-problem-domain-specific-chat-assistant-with-yandex-gpt-and-langchain-ru/