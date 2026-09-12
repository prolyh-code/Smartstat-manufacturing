---
title: LLM_extention 추가 검토(Step 8~25) 점검 결과 — 1차 검토(A-1~A-4) 후속확인
scope: "LLM_extention/8.md ~ 25.(3건) + progress-summary.md — Step1-7 검토 이후 새로 추가된 18개 파일"
reviewer: Claude (Cowork)
reviewed_at: 2026-09-12
status: Ian 검토 대기
based_on: Gap_Analysis_Step1-7_검토.md의 A-1~A-4, B-2를 기준으로 후속 확인
---

# 점검 결론 (요약)

새로 추가된 18개 파일은 1차 검토(Step1-7)에서 지적한 **A-1(데이터 기밀성)을 실질적으로, 그리고 상당히 잘 해결**했습니다. "앱은 LLM 없이도 완전히 동작해야 한다"는 것을 아예 **필수 요구사항(Architecture Requirement)**으로 못박고, Manual/AI 이중모드·AI Gateway·데이터 전송 정책(원본 데이터 전송 금지 기본값)까지 구체화한 것은 원래 PRISM의 "런타임 무-AI" 철학과 이번 LLM 확장을 정합성 있게 연결한 좋은 결정입니다[추론: 이 결정이 제 1차 검토의 A-1을 직접 참고한 것인지는 확인할 수 없으나, 지적한 문제의 핵심을 정확히 짚었습니다].

반면 A-2(다중비교), A-3(불량률 비교 Tool), A-4(교란요인 통제 일반화), B-2(MSA 게이트)는 이번 확장에서도 **해결되지 않았거나, 부분적으로만 진전**되었습니다. 특히 A-3는 흥미로운 상태입니다 — 서술과 다이어그램에는 `chi_square_test()`가 이미 여러 번 등장하지만, 공식 Tool 목록에는 끝내 등재되지 않은 **내부 불일치**가 새로 발견되었습니다. 아래에 근거와 함께 정리합니다.

---

# 1. A-1 (데이터 기밀성) — 실질적으로 해결됨

`25. 중간점검 LLM 통계 분석 앱 구조_수동 전환 기능.md`에서 다음을 명시적으로 확정했습니다.

- **Core App = 100% Local, AI Layer = Optional.** LLM이 없어도 Excel/CSV 업로드부터 t-test, ANOVA, 그래프, Report까지 전부 동작해야 한다는 것을 요구사항으로 고정.
- **AI Gateway**를 신설해 Authentication/Context Filter/Privacy Control을 별도 계층으로 분리.
- **데이터 전송 정책**을 "분석 결과만 전송 / 필요한 데이터 일부 전송 / 원본 데이터 전송 금지" 3단계로 정의하고, **원본 데이터 전송 금지를 기본값**으로 권장 — 100만 행 Excel을 통째로 LLM에 보내지 않고, 구조화된 분석 결과(집계 통계량)만 전달하는 구체적 JSON 예시까지 제시.
- **LLM 연결 실패가 앱 실패로 번지지 않는다**(Optional Dependency)는 원칙과, AI ON/OFF·Manual↔AI 전환 UX까지 설계.

이 문서 자체의 자기평가표(§28)가 정직합니다 — "데이터 전송 정책"을 "원칙만 존재, 추가 설계 필요"로 스스로 표시해 두었습니다. 즉 **원칙은 확정되었으나 세부 메커니즘(식별정보 마스킹, 온프레미스/사내 LLM의 구체적 채택 여부 등)은 아직 Step 26~30에서 다뤄야 할 과제로 남아 있습니다.** 이 정도면 다음 단계로 넘어가기 충분한 진전입니다[추론].

---

# 2. A-3 (불량률 비교 통계 Tool) — 서술은 앞서가고 Tool 목록은 뒤처진 불일치

1차 검토에서 "불량여부(이분형) 비교에 proportion test/chi-square가 필요하다고 서술은 하면서 실제 Tool 목록에는 없다"고 지적했는데, 이번 확장에서도 **똑같은 패턴이 반복**되고 있습니다. 다만 구체적인 증거가 더 늘었습니다.

- `11. 실제 Agent 작동 시나리오 설계.md` §11-9에서: "불량률이라는 범주형/비율 데이터이므로 단순히 평균을 비교하는 것과 다른 접근이 필요하다"며 `chi_square_test()`를 Tool로 명시하고, 실제 Agent 실행 구조 다이어그램(§11 후반부)에도 `defect_rate()` / `chi_square_test()` / `group_defect_rate()`를 나란히 그려 넣었습니다.
- `13. Agent Data Contract and Interface 설계.md`의 Evidence Schema 예시에도 `"basis": ["chi_square_test", "group_defect_rate"]`가 등장합니다.
- 그런데 **공식 "Tool Registry / MVP Tool 목록"을 선언하는 4곳** — `8. Brain Architecture` §8-17, `13.` §13-15, `18. Tool Registry and Rule Engine` §18-3, 그리고 `manufacturing-statistical-analysis-agent-progress-summary.md` §8 — **어디에도 `chi_square_test`가 실제로 등재되어 있지 않습니다.** 네 곳 모두 Comparison 카테고리는 t-test/ANOVA 계열만, Manufacturing 카테고리는 `defect_rate()`/`group_defect_rate()`(비율 계산만, 검정 아님)만 있습니다.

즉 이 프로젝트는 스스로 "불량률 비교에는 카이제곱검정이 필요하다"는 것을 이미 여러 번 인지하고 실행 예시에 써 왔으면서도, 그것을 **공식 스펙(Tool Registry)에 반영하는 절차만 누락**된 상태입니다. 이건 원칙의 문제가 아니라 **문서 동기화(spec drift)의 문제**이므로 수정 비용이 낮습니다 — Step 18(Tool Registry) 재정리 시 `chi_square_test()` 또는 `proportion_test()`를 Comparison/Manufacturing 카테고리에 정식으로 추가하기만 하면 해결됩니다.

---

# 3. A-2 (다중비교 보정) — 사후검정용은 이미 있음, 후보요인 스크리닝용은 여전히 없음

1차 검토보다 정확하게 구분하겠습니다. 이번 확인에서 보니 이 프로젝트가 다중비교를 **완전히 놓친 것은 아닙니다.**

- `3.5`, `4.3` 등 기존 파일에 `tukey_posthoc()`, `games_howell()`, `bonferroni_posthoc()`가 있고, 이는 **하나의 ANOVA에서 유의한 차이가 나온 뒤 그룹 쌍(pairwise)들을 사후비교할 때의 다중비교 보정**으로, 통계적으로 올바르게 설계되어 있습니다.
- 하지만 제가 원래 지적한 것은 **다른 종류의 다중비교**입니다 — UC-11의 "Candidate Factor Screening" 단계에서 Machine, Model, Shift, Operator, Temperature 등 **서로 다른 여러 변수를 각각 독립적인 검정으로 동시에 훑어보는 것**(`11-9`, `12`, `20` 등 여러 신규 파일에서 여전히 이 패턴 그대로 반복)에는 다중비교 보정이라는 개념 자체가 등장하지 않습니다. 전체 46개 파일을 검색해도 "Bonferroni/FDR/다중비교"라는 단어가 **사후검정 맥락 외에는 한 번도 나오지 않습니다.**

두 가지는 통계적으로 다른 문제이므로, Rule Engine의 "Method Rules"에 후보요인 스크리닝 단계 전용 보정 규칙을 별도로 추가하는 것을 권합니다.

---

# 4. A-4 (교란요인 통제 일반화) — 여전히 미해결

`13. Agent Data Contract and Interface 설계.md`의 Confounder Schema(§13-11)에도 `"recommended_analysis": "MODEL_CONTROLLED_MACHINE_COMPARISON"`이라는 필드가 있는데, 이는 1차 검토에서 지적한 것과 **동일한 "동일 조건 내 재비교"(수동 층화) 패턴**입니다. `18. Tool Registry`에도 ANCOVA·다중회귀 기반 교란변수 통제·Mantel-Haenszel류의 **일반화된 Tool은 여전히 없습니다.** 교란요인이 1개·범주형일 때는 잘 작동하지만, 2개 이상이거나 연속형(Temperature 등)일 때는 이 구조로 대응이 어렵다는 원래 지적이 그대로 유효합니다.

---

# 5. B-2 (측정시스템분석 MSA 게이트) — 여전히 캡션 수준

`4.4`에 "측정 시스템이 달라지면 Before/After 차이가 공정 변화인지 측정 오차인지 구분하기 어렵다"는 주의문이 있는 것 외에, 신규 파일들에서도 MSA를 실행 흐름의 선행 게이트로 넣지는 않았습니다(검색 결과 `MSA`, `Gauge R&R`, `측정시스템` 키워드는 새 파일 어디에도 없음).

---

# 6. 새로 발견된 문서 관리상의 사소한 문제

- **"25."로 시작하는 파일이 3개**(`25. 중간점검 LLM 통계 분석 앱 구조_수동 전환 기능.md`, `25. 중간점검2.md`, `25. First Vertical Slice Technical Implementation.md`) 존재합니다. 서로 다른 내용인데 번호가 충돌하고 있어, 나중에 참조하거나 검색할 때 혼동될 수 있습니다.
- `25. 중간점검2.md`에서 스스로 제안했던 **통합 baseline 문서**(`manufacturing-statistical-agent-design-notes.md`, 20개 섹션 구조, "Design Decision Log" 포함)는 실제로 생성되지 않았습니다 — 대신 그보다 앞서 만들어진 `manufacturing-statistical-analysis-agent-progress-summary.md`(Step 15까지만 다룸)가 사실상 그 역할을 대신하고 있는데, 이 파일은 Step 16 이후( Tool Registry, Data Contract, Vertical Slice 등)의 내용을 포함하지 않아 **현재는 낡은 baseline**입니다.

---

# 종합 제안

A-1(데이터 기밀성)은 이제 원칙 수준에서 확정되었으니, Step 26(Product UX & Operating Architecture) 이전에 **A-3의 Tool Registry 동기화(공식 목록에 chi_square_test 추가)만 먼저 5분짜리로 정리**하고 넘어가는 것을 권합니다[추론] — 이건 원칙 논쟁이 아니라 이미 3~4곳에서 합의된 내용을 목록에 반영만 하면 되는 작업이라 우선순위가 높으면서도 비용이 낮습니다. A-2(후보요인 스크리닝 다중비교)와 A-4(교란요인 통제 일반화)는 Step 17/18에서 Statistical Engine·Rule Engine을 실제로 구현할 때(현재 진행 중인 방향) 함께 반영하는 것이 자연스럽습니다. B-2(MSA)는 우선순위가 낮아 보이나, 원래 PRISM 카탈로그에 MSA 모듈이 있었던 점을 고려하면 Phase 2에서는 반드시 짚어야 합니다. 문서 관리 문제("25." 중복, 낡은 baseline)는 지금 정리해두면 이후 Claude Code 전달 시 혼동을 줄일 수 있습니다.
