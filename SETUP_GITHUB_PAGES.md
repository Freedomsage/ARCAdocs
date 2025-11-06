# Инструкция по настройке GitHub Pages

## Шаг 1: Включение GitHub Pages

1. Перейдите в ваш репозиторий на GitHub
2. Откройте **Settings** → **Pages**
3. В разделе **Source** выберите **"GitHub Actions"**
4. Сохраните изменения

## Шаг 2: Проверка workflow

Workflow уже настроен в `.github/workflows/pages.yml` и будет:
- Автоматически запускаться при push в ветку `main`
- Деплоить содержимое папки `docs/` как GitHub Pages
- Использовать `docs/index.html` как стартовую страницу с ReDoc

## Шаг 3: Первый запуск

После включения GitHub Actions в настройках Pages:

1. Сделайте commit и push текущих изменений:
```bash
git add .
git commit -m "Setup GitHub Pages with ReDoc"
git push origin main
```

2. Проверьте статус workflow:
   - Перейдите в **Actions** таб вашего репозитория
   - Убедитесь, что workflow "GitHub Pages" запустился
   - Дождитесь завершения (обычно 1-2 минуты)

3. После успешного деплоя ваша документация будет доступна по адресу:
   `https://<your-username>.github.io/arcadocs/`

## Шаг 4: Использование GitHub MCP Server (опционально)

Если у вас есть GitHub Personal Access Token, вы можете использовать GitHub MCP Server для управления репозиторием:

```bash
# Установите токен (если ещё не установлен)
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token_here"

# Запустите MCP сервер в режиме только чтения
./github-mcp-server --read-only
```

## Структура после деплоя

После деплоя на GitHub Pages структура будет следующей:
- `/` → `docs/index.html` (ReDoc документация)
- `/openapi/` → OpenAPI спецификации
- `/README.md`, `/cae/`, `/caea/`, etc. → Markdown документация

## Устранение проблем

### Ошибка "Get Pages site failed"
- Убедитесь, что Pages включены в Settings → Pages
- Выбрано "GitHub Actions" как источник
- Репозиторий не является приватным (или у вас есть GitHub Pro)

### ReDoc не загружается
- Проверьте, что файлы в `docs/openapi/` существуют
- Проверьте пути в `docs/index.html` (должны быть относительные: `openapi/...`)
- Откройте консоль браузера (F12) для просмотра ошибок

### Workflow не запускается
- Проверьте, что файл `.github/workflows/pages.yml` находится в ветке `main`
- Убедитесь, что у вас есть права на запись в репозиторий
- Проверьте настройки Actions в Settings → Actions → General

## Полезные ссылки

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions for Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow)
- [ReDoc Documentation](https://github.com/Redocly/redoc)

