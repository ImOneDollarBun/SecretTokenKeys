
# SecretTokenKeys

Проект для безопасной передачи секретных данных по одноразовому токену с ограниченным временем жизни.


Сервис предоставляет REST API, с помощью которого можно:

- Отправить секретные данные (например, пароли, токены)
- Получить одноразовый токен для доступа
- Установить TTL (время жизни токена)
- Получить данные по токену (однократный доступ)
- Используется Redis для хранения временных секретов

Проект полностью контейнеризирован через Docker и готов к развертыванию.

## Стек технологий

- **FastAPI** — основной фреймворк
- **Redis** — временное хранилище данных
- **PostgreSQL** — для логирования/долгосрочного хранения (если используется)
- **Docker + docker-compose** — деплой
- **Pydantic** — валидация данных
- **Uvicorn** — ASGI сервер
- **Pytest / Unittest** — тестирование

## Запуск проекта

```bash
git clone https://github.com/ImOneDollarBun/SecretTokenKeys.git
cd SecretTokenKeys
docker-compose up --build
