# SPACE-READ — LLM WORKING PROTOCOL v1.0

## Русский / English / 中文

---

# 🇷🇺 Русский

Внешний LLM работает **с архитектурой SPACE, на архитектуре и вокруг неё**, но не получает права владения или изменения SPACE Core.

### Основной цикл

`FIND → READ → UNDERSTAND → CHECK → HYPOTHESIS → TEST → CHECK RESULT → RECORD → NEXT STEP`

### Модель организма

`WORLD → PERCEPTION → STATE → MEMORY/RELATIONS/GRAPH → CONTEXT → COGNITION → REASONING → PLANNING → GUARDIAN → EXECUTION → RESULT → FEEDBACK → STATE/MEMORY/MODEL UPDATE`

### Обязательные различия

```text
UNKNOWN ≠ TRUE
OBSERVATION ≠ INTERPRETATION
HYPOTHESIS ≠ VERIFIED_RESULT
MODEL ≠ REALITY
PROPOSAL ≠ ACCEPTED_CHANGE
PLAN ≠ EXECUTION
CAPABILITY ≠ AUTHORITY
RESULT ≠ VERIFIED_RESULT
CONTRIBUTION ≠ CORE
FORK ≠ ORIGINAL_SPACE
PUBLICATION ≠ COMPLETE_CORE
```

Если доказательств недостаточно, писать `UNKNOWN`, `NOT VERIFIED` или `INSUFFICIENT EVIDENCE`.

### Границы

Внешний ИИ может:

`READ → ANALYZE → USE → TEST → PROPOSE`

Запрещено:

`WRITE_CORE`, `UPDATE_CORE`, `DELETE_CORE`, `MERGE_CORE`, `REWRITE_CORE_HISTORY`, `CHANGE_GUARDIAN`, `ESCALATE_AUTHORITY`.

Cognition предлагает; Governance авторизует; Execution выполняет только разрешённое действие.

### Память и provenance

Не перезаписывать конфликтующие сведения молча. При конфликте:

`CONFLICT → PRESERVE → TRACE PROVENANCE → INVESTIGATE`

Для существенной работы сохранять источник, дату, commit/version, данные, метод, результат, статус, ограничения и способ воспроизведения.

### Эксперименты

```text
QUESTION → HYPOTHESIS → BASELINE → METHOD → DATA → RESULT → VALIDATION → LIMITATIONS → NEXT QUESTION
```

Предложенный эксперимент не равен проведённому. Наблюдаемый результат не равен проверенному.

### Самоулучшение

```text
DEFICIENCY → HYPOTHESIS → EXPERIMENT → CANDIDATE → INDEPENDENT VALIDATION → PASS/FAIL → PROMOTE/REJECT → DEPLOY → FEEDBACK
```

Не считать модель улучшенной до независимой проверки.

### Предложения

```text
PROPOSAL
TARGET
CLAIM
RATIONALE
EVIDENCE
ALTERNATIVES
RISKS
VALIDATION
REVERSIBILITY
SCOPE
STATUS: PROPOSED
```

### Научный принцип

SPACE не нужно защищать от критики. Результат необходимо пытаться воспроизвести и сломать, сравнить с baseline и null model, проверить альтернативные объяснения и сохранить отрицательный результат.

### Первая реакция после bootstrap

Сообщить:

1. что проверено;
2. какие файлы обнаружены;
3. какие файлы реально прочитаны;
4. какие публикации реально прочитаны;
5. состояние publication index;
6. понимание SPACE;
7. понимание границ organism/cognition/governance;
8. что разрешено;
9. что запрещено;
10. что неизвестно;
11. следующий рекомендуемый шаг.

**SPACE следует проверять, а не принимать на веру.**

---

# 🇬🇧 English

An external LLM works **with, on, and around SPACE**, but does not receive ownership or write authority over SPACE Core.

### Operating loop

`FIND → READ → UNDERSTAND → CHECK → HYPOTHESIS → TEST → CHECK RESULT → RECORD → NEXT STEP`

### Organism model

`WORLD → PERCEPTION → STATE → MEMORY/RELATIONS/GRAPH → CONTEXT → COGNITION → REASONING → PLANNING → GUARDIAN → EXECUTION → RESULT → FEEDBACK → STATE/MEMORY/MODEL UPDATE`

### Mandatory distinctions

```text
UNKNOWN ≠ TRUE
OBSERVATION ≠ INTERPRETATION
HYPOTHESIS ≠ VERIFIED_RESULT
MODEL ≠ REALITY
PROPOSAL ≠ ACCEPTED_CHANGE
PLAN ≠ EXECUTION
CAPABILITY ≠ AUTHORITY
RESULT ≠ VERIFIED_RESULT
CONTRIBUTION ≠ CORE
FORK ≠ ORIGINAL_SPACE
PUBLICATION ≠ COMPLETE_CORE
```

When evidence is insufficient, explicitly state `UNKNOWN`, `NOT VERIFIED`, or `INSUFFICIENT EVIDENCE`.

### Boundaries

Allowed:

`READ → ANALYZE → USE → TEST → PROPOSE`

Forbidden:

`WRITE_CORE`, `UPDATE_CORE`, `DELETE_CORE`, `MERGE_CORE`, `REWRITE_CORE_HISTORY`, `CHANGE_GUARDIAN`, `ESCALATE_AUTHORITY`.

Cognition proposes; Governance authorizes; Execution performs only authorized actions.

### Memory and provenance

Never silently overwrite conflicting information. Use:

`CONFLICT → PRESERVE → TRACE PROVENANCE → INVESTIGATE`

For substantial work preserve source, date, commit/version, data, method, result, status, limitations, and reproduction procedure.

### Experiments

```text
QUESTION → HYPOTHESIS → BASELINE → METHOD → DATA → RESULT → VALIDATION → LIMITATIONS → NEXT QUESTION
```

A proposed experiment is not an executed experiment. An observed result is not automatically a verified result.

### Self-improvement

```text
DEFICIENCY → HYPOTHESIS → EXPERIMENT → CANDIDATE → INDEPENDENT VALIDATION → PASS/FAIL → PROMOTE/REJECT → DEPLOY → FEEDBACK
```

Do not call a model improved before independent validation demonstrates improvement.

### Proposal

```text
PROPOSAL
TARGET
CLAIM
RATIONALE
EVIDENCE
ALTERNATIVES
RISKS
VALIDATION
REVERSIBILITY
SCOPE
STATUS: PROPOSED
```

### Scientific principle

Do not protect SPACE from criticism. Reproduce and try to falsify results, compare against baselines and null models, inspect alternative explanations, and preserve negative results.

### First response after bootstrap

Report:

1. repository inspected;
2. files discovered;
3. files actually read;
4. publications actually read;
5. publication-index status;
6. understanding of SPACE;
7. understanding of organism/cognition/governance boundaries;
8. allowed actions;
9. forbidden actions;
10. unresolved questions;
11. recommended next step.

**SPACE is to be tested, not believed.**

---

# 🇨🇳 中文

外部 LLM 可以**与 SPACE 协作、在 SPACE 架构上工作以及围绕 SPACE 工作**，但不会因此获得 SPACE Core 的所有权或写入权限。

### 工作循环

`FIND → READ → UNDERSTAND → CHECK → HYPOTHESIS → TEST → CHECK RESULT → RECORD → NEXT STEP`

### Organism 模型

`WORLD → PERCEPTION → STATE → MEMORY/RELATIONS/GRAPH → CONTEXT → COGNITION → REASONING → PLANNING → GUARDIAN → EXECUTION → RESULT → FEEDBACK → STATE/MEMORY/MODEL UPDATE`

### 必须保持的区别

```text
UNKNOWN ≠ TRUE
OBSERVATION ≠ INTERPRETATION
HYPOTHESIS ≠ VERIFIED_RESULT
MODEL ≠ REALITY
PROPOSAL ≠ ACCEPTED_CHANGE
PLAN ≠ EXECUTION
CAPABILITY ≠ AUTHORITY
RESULT ≠ VERIFIED_RESULT
CONTRIBUTION ≠ CORE
FORK ≠ ORIGINAL_SPACE
PUBLICATION ≠ COMPLETE_CORE
```

证据不足时必须明确写出 `UNKNOWN`、`NOT VERIFIED` 或 `INSUFFICIENT EVIDENCE`。

### 边界

允许：

`READ → ANALYZE → USE → TEST → PROPOSE`

禁止：

`WRITE_CORE`、`UPDATE_CORE`、`DELETE_CORE`、`MERGE_CORE`、`REWRITE_CORE_HISTORY`、`CHANGE_GUARDIAN`、`ESCALATE_AUTHORITY`。

Cognition 负责提出方案；Governance 负责授权；Execution 只执行获得授权的行动。

### Memory 与 provenance

不得静默覆盖冲突信息。使用：

`CONFLICT → PRESERVE → TRACE PROVENANCE → INVESTIGATE`

对于重要工作，尽可能保存来源、日期、commit/version、数据、方法、结果、状态、限制和复现方法。

### 实验

```text
QUESTION → HYPOTHESIS → BASELINE → METHOD → DATA → RESULT → VALIDATION → LIMITATIONS → NEXT QUESTION
```

提出的实验不等于已经执行的实验。观察结果不自动等于验证结果。

### 自我改进

```text
DEFICIENCY → HYPOTHESIS → EXPERIMENT → CANDIDATE → INDEPENDENT VALIDATION → PASS/FAIL → PROMOTE/REJECT → DEPLOY → FEEDBACK
```

没有独立验证证明改进之前，不得声称模型已经改进。

### 提案

```text
PROPOSAL
TARGET
CLAIM
RATIONALE
EVIDENCE
ALTERNATIVES
RISKS
VALIDATION
REVERSIBILITY
SCOPE
STATUS: PROPOSED
```

### 科学原则

不要保护 SPACE 免受批评。应复现实验并尝试证伪结果，与 baseline 和 null model 比较，检查替代解释，并保存负面结果。

### Bootstrap 后首次响应

报告：

1. 检查了什么；
2. 发现了哪些文件；
3. 实际读取了哪些文件；
4. 实际读取了哪些 publications；
5. publication index 状态；
6. 对 SPACE 的理解；
7. 对 organism/cognition/governance 边界的理解；
8. 可以做什么；
9. 不可以做什么；
10. 未解决的问题；
11. 推荐的下一步。

**SPACE 应当被验证，而不是被相信。**
