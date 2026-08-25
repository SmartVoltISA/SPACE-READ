# SPACE-READ — текущий статус

**Статус:** CONTRACT v1 / INITIAL PUBLICATION / HARDENING  
**Repository:** `SmartVoltISA/SPACE-READ`  
**Visibility:** Public  
**Default branch:** `main`

## Сделано

### Граница

`SPACE Core → validation → SPACE-READ → human / research / external AI`

Обратной записи из SPACE-READ в Core нет в архитектурном контракте.

### Publication Contract v1

Определены классы публикации, статусы, обязательные metadata, provenance, versioning и promotion rules.

### Machine-readable layer

Созданы:

- `manifest.json`;
- `PUBLICATION_INDEX.json`;
- `schema/publication.schema.json`.

### External AI

Созданы:

- `LLM_START.md` — короткая точка входа для внешнего LLM;
- `AI_INTERFACE.md` — read/analyze/use/propose contract;
- `PROPOSAL_PROTOCOL.md` — безопасный путь оставлять след.

### Initial publication

Опубликован:

`space.architecture.overview`

Это публичная абстракция архитектуры SPACE, а не копия приватного Core.

### Security / CI

Созданы:

- `scripts/validate_read.py`;
- `.github/workflows/validate-read.yml`;
- обновлён `SECURITY_ARCHITECTURE.md`.

Workflow использует `contents: read` и не содержит предусмотренного write-back в Core.

### License

Добавлен `LICENSE` с MIT License для опубликованных материалов репозитория.

## Что НЕ считаем завершённым

- сетевой Read API;
- автоматическая синхронизация Core → READ;
- полный перенос SPACE Core;
- полная CI-проверка, подтверждённая фактическим workflow run;
- adversarial write-back test;
- включение branch protection для `main`;
- полная первая publication set всей архитектуры.

## Проверка текущего состояния

Текущая `main` указывает на commit:

`ef37ec392a92f92de7dbfaf983c0e52433c5458f`

Содержимое дерева проверено через GitHub API. Структура содержит LLM entrypoint, контракт, индекс, схему, первую публикацию, validator и CI workflow.

Локальный запуск validator из этого окружения выполнить не удалось: среда не имеет DNS-доступа к GitHub. Поэтому CI считается **созданным, но ещё не подтверждённым фактическим run**.

## Следующая контрольная точка

**PHASE 4 — Quality & Security:** дождаться первого CI run, исправить найденное, затем провести adversarial-проверку границы и подготовить branch protection.

## Recovery base

Стабильное состояние перед этим этапом:

`e0fc94f84ab32d7d3b6563a9cbd9f4ebc1bbca73`

История изменений сохраняется в Git; старые состояния не переписываются.

## Инвариант

**Внешний мир может читать SPACE, анализировать его и предлагать. Но публичный слой не должен иметь технической возможности непосредственно изменить, удалить или повредить эталонный SPACE Core.**
