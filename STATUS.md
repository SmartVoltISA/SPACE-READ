# SPACE-READ — текущий статус

**Статус:** CONTRACT v1 / INITIAL PUBLICATION  
**Repository:** `SmartVoltISA/SPACE-READ`  
**Visibility:** Public  
**Default branch:** `main`

## Что сделано

### 1. Граница

Зафиксирована модель:

`SPACE Core → validation → SPACE-READ → human / research / external AI`

Обратной записи из SPACE-READ в Core нет в архитектурном контракте.

### 2. Publication Contract v1

Определены:

- классы публикации;
- статусы;
- обязательные metadata;
- provenance;
- versioning;
- promotion rules;
- правила внешних предложений.

### 3. Machine-readable layer

Созданы:

- `manifest.json`;
- `PUBLICATION_INDEX.json`;
- `schema/publication.schema.json`.

### 4. External AI contract

Создан `AI_INTERFACE.md` с разделением:

`read / analyze / use / propose`

и запретом:

`write_core / update_core / delete_core / merge_core`.

### 5. External contribution path

Создан `PROPOSAL_PROTOCOL.md`.

Внешний ИИ или исследователь может оставить след через Issue, Pull Request или fork. Это предложение, а не изменение канонического состояния.

### 6. First public publication

Опубликован:

`space.architecture.overview`

Это публичная абстракция архитектуры SPACE, а не копия приватного Core.

## Что сознательно НЕ заявляем

- сетевой Read API пока не реализован;
- автоматическая синхронизация Core → READ пока не реализована;
- полный перенос SPACE Core не выполнен;
- полная CI-проверка пока не выполнена;
- adversarial write-back test ещё не проведён;
- `verified` применяется только там, где область проверки явно определена.

## Текущая контрольная точка

**PHASE 4 — Quality & Security.**

Следующая практическая задача — автоматическая проверка структуры, схемы, provenance, ссылок и отсутствия write-back механизмов.

## Recovery base

Предыдущее стабильное состояние перед текущим этапом:

`e0fc94f84ab32d7d3b6563a9cbd9f4ebc1bbca73`

Изменения после этой точки должны сохранять историю и быть обратимыми через Git history.

## Инвариант

**Внешний мир может читать SPACE, анализировать его и предлагать изменения. Но публичный слой не должен иметь технической возможности непосредственно изменить, удалить или повредить эталонный SPACE Core.**
