#!/bin/bash
# Скрипт для проверки и настройки GitHub Pages

echo "🔍 Проверка настройки GitHub Pages..."
echo ""

# Проверка наличия файлов
echo "📁 Проверка файлов:"
if [ -f "docs/index.html" ]; then
    echo "  ✓ docs/index.html существует"
else
    echo "  ✗ docs/index.html не найден"
fi

if [ -d "docs/openapi" ] && [ -f "docs/openapi/homologacion.yaml" ]; then
    echo "  ✓ OpenAPI файлы в docs/openapi/"
else
    echo "  ✗ OpenAPI файлы не найдены в docs/openapi/"
fi

if [ -f ".github/workflows/pages.yml" ]; then
    echo "  ✓ Workflow файл существует"
else
    echo "  ✗ Workflow файл не найден"
fi

echo ""
echo "📋 Следующие шаги:"
echo ""
echo "1. Включите GitHub Pages в настройках репозитория:"
echo "   https://github.com/Freedomsage/arcadocs/settings/pages"
echo ""
echo "2. Выберите 'GitHub Actions' как источник"
echo ""
echo "3. Сделайте commit и push:"
echo "   git add ."
echo "   git commit -m 'Setup GitHub Pages'"
echo "   git push origin main"
echo ""
echo "4. После push проверьте Actions:"
echo "   https://github.com/Freedomsage/arcadocs/actions"
echo ""
echo "5. После успешного деплоя ваша документация будет доступна по адресу:"
echo "   https://freedomsage.github.io/arcadocs/"
echo ""

