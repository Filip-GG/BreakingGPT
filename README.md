# Топовый проект в сфере ML
Типы данных для обученя: 
- pdf 
- doc 
- docx

Папки:
- dataset_input -- входной набор данных для дообучения модели
- dataset -- обработанный наброр данных

# Описание исполняемых файлов
- pdf_convector -- набор функций конвертации файлов в pdf для дльнейшей работы
- localEmbeddings -- класс emebeddings для работы с lm studio
- file_message -- набор функций для работы с патками

# Инструкция для запуска
1. Установите Lm Studio (https://lmstudio.ai/) 
    a. Скачайте модель для Embeddings: nomic-embed-text-v1.5-GGUF/nomic-embed-text-v1.5.f32.gguf
    b. Скачайте модель для Обработки текста: Hermes-3-Llama-3.1-8B-GGUF/Hermes-3-Llama-3.1-8B.Q4_K_M.gguf
    PS: модель для обработки можно использывать ЛЮБУЮ, НО для Embeddings не получиться
    Запустрите локальный ссервер и подключите скаченные модели
2. Установите библиоткеи для python
3. В файле конфигурации:
    - base_url_* -- это ip полученные в ходе запуска локального сервера
    - model_* -- это название моделей

# Доп. ссылки:
- https://soshnikov.com/ai/creating-problem-domain-specific-chat-assistant-with-yandex-gpt-and-langchain-ru/