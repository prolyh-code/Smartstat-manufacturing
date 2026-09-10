---
id: DELIV-DEVGUIDE-001
title: PRISM 통계분석 Add-on — 프로그램 제작 지침서 (Claude Code 전달용)
type: development-specification
status: 배포용 최종본 — Ian이 PRISM 앱 폴더·기술 스택 문서와 함께 Claude Code에게 직접 전달 예정
version: v1.0 (2026-09-10)
owner: Ian(연구책임자/제품오너), Claude(Cowork)(연구·설계 수행)
related: Final_Report.md(v2.1), Analysis_Module_Library_and_Composition_Rules.md(v1.2), Navigator_Question_Flow.md(v2), Analysis_Package_Spec_*.md(8종), GAP09_Interpretation_Template_Coverage_Matrix.md, Research_Handoff_Package.md
---

# PRISM 통계분석 Add-on — 프로그램 제작 지침서

> 이 문서는 "제조 현장용 통계분석 앱 개발" 연구(F:\obsidian\vault\통계분석앱\)의 최종 산출물을 **Claude Code가 실제로 코드를 작성하는 데 바로 쓸 수 있는 형태**로 압축·재구성한 지침서입니다. Ian이 PRISM 앱 폴더 및 기술 스택 문서와 함께 Claude Code에게 전달할 예정이며, 이 문서 자체가 연구 결과와 개발 착수 사이를 잇는 다리 역할을 합니다.

---

## 0. 이 문서 사용법

**읽는 순서**: 이 문서를 먼저 통독한 뒤, 실제 구현 시 §5의 각 패키지 레시피와 함께 `Analysis_Package_Spec_*.md`(패키지당 1개, 해석 템플릿 전체 문구 포함) 및 `Analysis_Module_Library_and_Composition_Rules.md`(모듈 전체 카탈로그)를 상세 스펙으로 참조하십시오. 이 지침서는 **요약·재구성본**이며, 정확한 해석 문구·결정 임계값·근거 출처는 원본 스펙 파일이 최종 권위를 갖습니다(불일치 시 원본 스펙 우선).

**이 문서에 없는 것**: PRISM의 기술 스택, 데이터베이스 스키마, API/DB 연동 방식, 인증 체계는 이 연구범위에서 의도적으로 다루지 않았습니다(§8 참조). 이는 Ian이 PRISM 앱 폴더와 함께 별도로 전달합니다.

| 이 문서에서 다루는 것 | 상세 스펙이 있는 원본 파일 |
|---|---|
| 제품 정의·핵심 제약·아키텍처 개요 | 이 문서 §1~4 |
| 8개 분석 패키지 레시피(모듈 흐름) | 이 문서 §5, 상세는 `Analysis_Package_Spec_*.md` |
| Navigator 질문 흐름 | 이 문서 §6, 상세는 `Navigator_Question_Flow.md` |
| 해석 템플릿 설계 원칙 | 이 문서 §7, 상세는 `GAP09_Interpretation_Template_Coverage_Matrix.md` |
| 알려진 한계·[추론] 항목 | 이 문서 §9 |
| 전체 근거(출처·주장·의사결정) | `02_EVIDENCE/`, `00_GOVERNANCE/Decision_Log.csv` |

---

## 1. 무엇을 만드는가 — 제품 정의

**PRISM 통계분석 Add-on**은 기존 사내 CTQ 자동분석 앱인 **PRISM에 추가되는 기능 모듈**입니다. 독립 앱이 아닙니다. 대상 사용자는 국내 중소형 가전(냉장고·세탁기·에어컨·조리기기) 제조업의 품질/공정 엔지니어로, 통계 기초교육은 받았으나 실무에서 통계 소프트웨어(Minitab·JMP 등)를 쓰지 않는 비전문가입니다. 제품의 핵심가치는 "현장에서 벌어진 상황을 통계적으로 판단 가능한 질문으로 전환해주고, 그 판단을 비전문가도 이해할 수 있는 말로 설명해주는 것"입니다.

CTQ 관리도·공정능력분석은 PRISM이 이미 자동화하고 있으므로, 이 Add-on의 차별화 지점은 **원인분석·개선검증·상황인식·예방적 비교·유지관리·측정시스템분석(MSA)·(도메인 확장으로) 신뢰성·안전재고**입니다.

---

## 2. 절대 지켜야 할 제약 (Non-negotiable)

1. **Add-on 런타임에는 AI/LLM이 없습니다.** 배포된 앱이 사용자에게 보여주는 모든 해석 문장은 이 연구에서 사전에 설계한 **결정론적 규칙과 슬롯 기반 템플릿**에서만 나옵니다. 구현 시 해석 문구 생성 경로에 LLM API 호출이 들어가서는 안 됩니다 — 이는 이 프로젝트의 존재 이유이자 유일한 아키텍처 제약입니다.
2. **모든 분석 흐름(레시피)은 데이터 인식(M-DATA-PROFILE)으로 시작하고, 안전 폴백(M-SAFETY-FALLBACK)으로 끝납니다.** 예외 없음. 폴백이 없는 패키지는 미완성으로 간주합니다.
3. **자동판별 결과를 침묵 처리(silent skip)하지 않습니다.** 데이터에서 자동으로 알아낸 것(대응표본 여부, 시계열 여부, 변수 타입 등)은 반드시 기본값이 미리 선택된 확인질문("이렇게 이해했는데 맞나요? — 맞아요(추천) / 아니에요")으로 사용자에게 되물어야 합니다. 이것이 AI 없는 환경에서 오판별을 잡아내는 유일한 안전장치입니다(DEC-011).
4. **패키지 체이닝(NEXT)은 추천만 하고 자동 실행하지 않습니다.** 한 패키지 결과가 다른 패키지 실행을 제안할 수 있지만, 항상 사용자 확인을 거쳐야 합니다.
5. **해석 템플릿이 매칭되지 않는 슬롯 조합이 발생하면 절대 빈 화면을 보여주지 않습니다.** 반드시 M-SAFETY-FALLBACK 문구("표준 해석 문구가 아직 준비되지 않았습니다. 수치를 직접 확인하시거나 담당자에게 문의하십시오")로 대체합니다.
6. **통계 용어·패키지 이름을 사용자 화면에 노출하지 않습니다.** "원인분석", "MSA" 같은 내부 명칭은 개발 문서와 라우팅 로직에서만 쓰고, 사용자에게는 상황 중심의 일상어 질문만 보여줍니다.

---

## 3. 아키텍처 개요 — 모듈과 레시피의 2계층 구조

이 Add-on의 통계 로직은 두 계층으로 설계되어 있습니다.

- **원자 모듈(Atomic Module, M-*)**: 입력→처리(결정로직)→출력 구조를 가진 최소 재사용 단위. 예: 정규성검정, 효과크기 산출, 해석문 조립. 여러 패키지에서 재사용됩니다.
- **분석 패키지(레시피, RECIPE)**: 사용자가 트리거하는 하나의 현장 목적에 대해 여러 모듈을 결정론적으로 연결한 end-to-end 흐름. 총 8개.

**구현 매핑 권장**: 모듈(M-*)은 재사용 가능한 함수/클래스로 1회 구현하고, 패키지(레시피)는 모듈을 순서대로 호출하는 선언적 설정(예: YAML/JSON)으로 구현할 것을 권장합니다. 이렇게 하면 새 패키지 추가 시 코드를 새로 짜는 대신 설정 파일만 추가하면 되고, 공통 로직(해석 조립·안전 폴백)의 버그를 한 곳에서만 고치면 전체에 반영됩니다. 참고자료: *Industrial Statistics: A Computer-Based Approach with Python*(SRC-146, Python 기반 산업통계 Case Study 40건 이상)이 모듈별 코드 패턴 참고에 유용할 수 있습니다.

레시피 표기법(그대로 선언적 설정으로 옮길 수 있도록 설계됨):

```
RECIPE <패키지ID>
TRIGGER: <사용자가 이 패키지를 트리거하는 조건>
INPUT: <필수/선택 입력 필드>
FLOW:
  <모듈ID>
  → <모듈ID>
  → BRANCH(<분기조건>)
      <조건A> → <모듈ID 또는 skip>
      <조건B> → <모듈ID 또는 skip>
  → M-INTERP-ASSEMBLE
  → M-SAFETY-FALLBACK   ※ 모든 레시피의 마지막 단계는 항상 이것
NEXT: <조건> → <다른 레시피ID>(추천만, 자동실행 금지)   ※ 선택
```

신규 패키지가 필요해지면(§5의 8개 범위 밖), `Analysis_Module_Library_and_Composition_Rules.md` §5의 절차(목적 정의 → 표준 골격 적용 → 카탈로그 매칭 → 빈 구멍만 신규 모듈화 → 해석 슬롯 유형 판정 → 레시피 문서화 → 폴백 확인 → 전수 커버리지 자체점검)를 그대로 따르십시오.

---

## 4. 원자 모듈 카탈로그 요약 (9개 카테고리, 약 29개)

전체 모듈의 입력/출력/결정로직 상세는 `Analysis_Module_Library_and_Composition_Rules.md` §2를 참조하십시오. 아래는 카테고리별 요약입니다.

| 카테고리 | 대표 모듈 | 역할 |
|---|---|---|
| §2.1 데이터 인식/프로파일링 | M-DATA-PROFILE, M-ASSUMP-DESIGNADEQUACY | 그룹수·n·paired·변수타입·시계열여부 자동판별 + 항상 확인질문으로 되묻기. 모든 레시피의 출발점. |
| §2.2 시각화 | M-VIZ-HISTBOX, M-VIZ-SCATTER, M-VIZ-CORRHEATMAP, M-VIZ-RUNCHART, M-VIZ-CONTROLCHART | 히스토그램·박스플롯·산점도·상관히트맵·런차트·관리도 |
| §2.3 가정 확인 | M-ASSUMP-NORMALITY, M-ASSUMP-AUTOCORR, M-ASSUMP-VIF | 정규성(Shapiro-Wilk)·자기상관(lag-1)·다중공선성(VIF) 확인, 위반 시 경고 |
| §2.4 검정 자동선택 | M-TESTSELECT-COMPARE, M-TESTSELECT-CORR, M-TESTSELECT-REGRESSION | 데이터 특성에 따라 적합한 검정법을 결정론적으로 확정(**가장 많이 재사용되는 핵심 모듈**) |
| §2.5 검정 실행/효과크기 | M-EFFECT-COMPARE, M-EFFECT-CORR, M-EFFECT-REGCOEF, M-STAT-VARDECOMP | 검정 실행 + p-value 단독이 아닌 효과크기 산출 |
| §2.6 후처리 | M-RANK-EFFECTSIZE, M-CORRECT-FWER, M-DECIDE-GRR, M-DECIDE-WECO, M-ASSUMP-MODELFIT | 순위화·다중비교보정·MSA 판정·관리도 이상탐지·적합도 확인 |
| §2.7 해석/안전장치(전 패키지 공통, 가장 중요) | M-INTERP-ASSEMBLE, M-SAFETY-FALLBACK | 슬롯값→템플릿 문장 조립(경고 템플릿 항상 최상단), 매칭 실패 시 안전 폴백 |
| §2.8 신뢰성(Reliability, G10) | M-RELY-DATAPROFILE, M-RELY-WEIBULLFIT, M-RELY-STRATEGY, M-RELY-RELFUNC, M-RELY-MTBF, M-RELY-REPLACEINTERVAL | Weibull 파라미터 추정(중도절단 데이터 처리 포함), β기반 정비전략 판정, 신뢰도함수·MTBF·교체주기 최적화 |
| §2.9 재고관리(SafetyStock, G11) | M-INVENTORY-DEMANDSTATS, M-INVENTORY-METHODSELECT, M-INVENTORY-SAFETYSTOCK, M-INVENTORY-REORDERPOINT | 수요/리드타임 통계, 계산방식 자동선택, 안전재고·재주문점 산출 |

**재사용성**: M-DATA-PROFILE·M-INTERP-ASSEMBLE·M-SAFETY-FALLBACK은 8개 패키지 전부에서, M-TESTSELECT-COMPARE·M-VIZ-HISTBOX·M-VIZ-SCATTER·M-ASSUMP-NORMALITY 등은 2개 이상 패키지에서 재사용됩니다. §2.8·2.9 모듈은 현재 신뢰성/안전재고 패키지 전용이지만, 카탈로그 구조상 향후 재사용 가능하도록 동일한 형식으로 문서화되어 있습니다.

---

## 5. 8개 분석 패키지 — 레시피

각 레시피의 정확한 해석 템플릿 문구·결정 임계값은 해당 `Analysis_Package_Spec_*.md`를 참조하십시오. 아래 레시피는 그 스펙을 코드로 옮기기 위한 압축 표기입니다.

### 요약표

| 패키지 | 근거등급 | 상태 | 스펙 파일 |
|---|---|---|---|
| 결과검증 (ResultVerification) | 품질/공정 표준 | 완전(GAP-09 구조적 완전성) | Analysis_Package_Spec_ResultVerification.md |
| 원인분석 (RootCause) | 품질/공정 표준 | 완전(다중비교 보정 포함) | Analysis_Package_Spec_RootCause.md |
| 핵심요인분석 (KeyFactor) | 품질/공정 표준 | 완전 | Analysis_Package_Spec_KeyFactor.md |
| MSA | 품질/공정 표준 | 완전 | Analysis_Package_Spec_MSA.md |
| 유지관리 (Maintenance) | 품질/공정 표준 | 완전(WECO 4종, 목록형 조립) | Analysis_Package_Spec_Maintenance.md |
| 예방적비교 (ProactiveComparison) | 품질/공정 표준 | 완전(신규 모듈 0개로 조합) | Analysis_Package_Spec_ProactiveComparison.md |
| 신뢰성 (Reliability/Weibull) | **낮음** — 문헌 1라운드 | 완전(교체주기 최적화 포함, GAP-10 closed) | Analysis_Package_Spec_Reliability.md |
| 안전재고 (SafetyStock) | **가장 낮음** — 도메인 이탈 | 1차 명세(GAP-11 open(부분)) | Analysis_Package_Spec_SafetyStock.md |

> **중요**: 위 8개 패키지는 근거등급이 동일하지 않습니다. 신뢰성·안전재고 2개는 Ian이 명시적으로 착수를 결정한 도메인 확장 패키지로, 다른 6개보다 문헌 검증이 얕습니다(DEC-012). 구현 우선순위를 정할 때 이 차이를 반영해, 먼저 6개 핵심 패키지를 구현·검증한 뒤 확장 2개를 이어가는 순서를 권장합니다.

### 5.1 결과검증 (ResultVerification)

```
RECIPE ResultVerification
TRIGGER: 2개 이상 그룹의 수치형 데이터 업로드 + "개선 결과 검증" 선택
INPUT: 그룹별 측정값(필수), 대응 여부(확인질문), 측정순서(확인질문)
FLOW:
  M-DATA-PROFILE
  → M-VIZ-HISTBOX
  → M-ASSUMP-NORMALITY
  → BRANCH(시계열 정보 있음?)
      YES → M-VIZ-RUNCHART → M-ASSUMP-AUTOCORR [우선순위: 최상단 경고]
      NO  → skip
  → M-TESTSELECT-COMPARE
  → M-EFFECT-COMPARE
  → M-INTERP-ASSEMBLE
  → M-SAFETY-FALLBACK
NEXT: 유의한 차이 없음 → RootCause(추천만)
```

### 5.2 원인분석 (RootCause)

```
RECIPE RootCause
TRIGGER: 결과변수 1개 + 후보원인 1개 이상 업로드 + "원인분석" 선택
INPUT: 결과변수(필수), 후보원인 1개 이상(필수, 범주형/연속형 자동판별)
FLOW:
  M-DATA-PROFILE(변수타입 판별 확장)
  → BRANCH(후보원인 타입)
      범주형 → M-VIZ-HISTBOX → M-ASSUMP-NORMALITY → M-TESTSELECT-COMPARE → M-EFFECT-COMPARE
      연속형 → M-VIZ-SCATTER → M-TESTSELECT-CORR → M-EFFECT-CORR
  → M-RANK-EFFECTSIZE
  → BRANCH(동시검정 후보원인 ≥3개?)
      YES → M-CORRECT-FWER [우선순위: 최상단 경고]
      NO  → skip
  → M-INTERP-ASSEMBLE
  → M-SAFETY-FALLBACK
```

### 5.3 핵심요인분석 (KeyFactor)

```
RECIPE KeyFactor
TRIGGER: 결과변수 1개 + 후보 설명변수 2개 이상(연속형) 업로드 + "핵심요인분석" 선택
INPUT: 결과변수(필수), 설명변수 2개 이상(필수, 연속형)
FLOW:
  M-DATA-PROFILE(n대변수비율 확장)
  → M-VIZ-SCATTER(매트릭스) → M-VIZ-CORRHEATMAP
  → M-ASSUMP-VIF [VIF≥5 시 우선순위: 최상단 경고]
  → M-TESTSELECT-REGRESSION
  → M-EFFECT-REGCOEF → M-RANK-EFFECTSIZE
  → M-ASSUMP-MODELFIT [저설명력 시 우선 경고]
  → M-INTERP-ASSEMBLE
  → M-SAFETY-FALLBACK
```

### 5.4 MSA (측정시스템분석)

```
RECIPE MSA
TRIGGER: Crossed Gauge R&R 형식 데이터(부품×작업자×반복) 업로드 + "MSA" 선택
INPUT: 부품×작업자×반복 측정값(필수, 표준설계 10부품×3작업자×2~3회 권장)
FLOW:
  M-DATA-PROFILE → M-ASSUMP-DESIGNADEQUACY [미달 시 경고]
  → M-VIZ-HISTBOX(작업자별) → M-VIZ-SCATTER(부품별)
  → M-STAT-VARDECOMP
  → M-DECIDE-GRR
  → M-INTERP-ASSEMBLE
  → M-SAFETY-FALLBACK
```

### 5.5 유지관리 (Maintenance)

```
RECIPE Maintenance
TRIGGER: 개선 후 시계열 측정값 업로드 + "유지관리/추적" 선택
INPUT: 시계열 측정값(필수, 최소 20~25점 권장), 개선시점(필수)
FLOW:
  M-DATA-PROFILE → M-ASSUMP-DESIGNADEQUACY(최소 20~25점 변형) [부족 시 경고]
  → M-VIZ-CONTROLCHART
  → M-DECIDE-WECO(Western Electric Rules 4종 동시 독립 탐지 — 목록형 조립, 배타적 분류 아님)
  → M-INTERP-ASSEMBLE
  → M-SAFETY-FALLBACK
```

> **구현 시 주의**: Rule1~4는 동시에 여러 개 위반될 수 있습니다(예: Rule2와 Rule3가 같은 시점에 동시 위반). 배타적 단일 분류로 구현하면 실제 발생 가능한 조합을 놓칩니다 — 반드시 규칙별 독립 탐지 후 "2개 이상 규칙 동시 위반" 안내를 별도로 추가하는 목록형 조립 방식으로 구현하십시오(§7 참조, RUN-019에서 실제로 발견된 설계결함).

### 5.6 예방적비교 (ProactiveComparison)

```
RECIPE ProactiveComparison
TRIGGER: 현재 데이터 + 비교 기준선(과거/스펙) 업로드 + "요즘 상태 확인" 선택
INPUT: 현재 측정값(필수), 비교 기준선(필수)
FLOW:
  (ResultVerification과 통계 로직 동일 — 신규 모듈 0개로 조합)
  M-DATA-PROFILE → M-VIZ-HISTBOX → M-ASSUMP-NORMALITY
  → BRANCH(시계열 정보 있음?) YES → M-VIZ-RUNCHART → M-ASSUMP-AUTOCORR [최상단 경고] | NO → skip
  → M-TESTSELECT-COMPARE → M-EFFECT-COMPARE
  → M-INTERP-ASSEMBLE(예방적 프레이밍 문구로 교체)
  → M-SAFETY-FALLBACK
NEXT: 유의한 차이 발견 → RootCause(추천만)
```

### 5.7 신뢰성 (Reliability / Weibull) — 근거등급 낮음

```
RECIPE Reliability
TRIGGER: 부품/설비별 사용시간+고장여부(고장/중도절단) 업로드 + "부품 수명/교체주기 파악" 선택
INPUT: 부품식별자(필수), 사용시간·사용량(필수), 고장여부(필수, 고장/중도절단 구분),
       계획교체비용 CP·현장고장비용 CU(선택, Step5용)
FLOW:
  M-RELY-DATAPROFILE [표본 15건 미만 시 경고]
  → M-RELY-WEIBULLFIT(중도절단 비중에 따라 MLE/순위회귀 자동선택)
  → M-RELY-STRATEGY(β>1 마모성/β≈1 우발고장/β<1 초기고장 3단 판정)
  → M-RELY-RELFUNC(R(t), 특성수명)
  → M-RELY-MTBF(μ=η×Γ(1+1/β), β≠1이면 한계경고)
  → BRANCH(β>1 그리고 CP·CU 입력 있음?)
      YES → M-RELY-REPLACEINTERVAL(CPUT 그리드탐색 최소화 → 권장 교체주기)
      NO  → skip(정비전략만 제공, β≈1/초기고장이면 "예방교체 비용이점 없음" 안내)
  → M-INTERP-ASSEMBLE
  → M-SAFETY-FALLBACK
```

> **[추론] 주의**: β 판정 구간(1.2/0.8)과 M-RELY-REPLACEINTERVAL의 그리드 탐색 방식(원문의 해석적 미분 최적화를 결정론적 규칙엔진 제약상 단순화한 것)은 설계 확장입니다. 통계 담당자 검토 및 개발단계 수치검증을 권장합니다(§9 참조).

### 5.8 안전재고 (SafetyStock) — 근거등급 가장 낮음, 도메인 이탈

```
RECIPE SafetyStock
TRIGGER: 자재/부품별 과거 수요(및 가능하면 리드타임) 이력 업로드 + "재고/발주 기준 설정" 선택
INPUT: 자재식별자(필수), 기간별 수요(필수, 시계열), 리드타임(권장), 목표 서비스수준(권장, 기본값 95%)
FLOW:
  M-DATA-PROFILE(수요이력·리드타임 데이터 유무 확인, 확인질문 전환)
  → M-INVENTORY-DEMANDSTATS(평균·표준편차)
  → M-INVENTORY-METHODSELECT(리드타임 변동 데이터 유무로 2종 중 자동선택)
  → M-INVENTORY-SAFETYSTOCK(Z값: 90%→1.28/95%→1.65/99%→2.33)
  → M-INVENTORY-REORDERPOINT(안전재고 + 리드타임중 평균수요)
  → M-INTERP-ASSEMBLE
  → M-SAFETY-FALLBACK
```

> **주의**: 이 패키지는 품질/CTQ 통계가 아니라 재고관리(수요·공급 불확실성) 도메인입니다. Ian이 도메인 불일치 위험을 인지하고도 착수를 직접 결정했습니다(DEC-012, DBT-08). PRISM Add-on 내에서 이 기능의 UI·메뉴 위치를 다른 7개와 분리할지는 제품 배치 판단이 필요합니다.

---

## 6. Navigator — 사용자 진입점 (스무고개 UX)

사용자는 통계 카테고리를 메뉴에서 고르지 않습니다. 쉬운 상황 질문을 순서대로 답하면 앱이 8개 패키지 중 무엇을 실행할지 결정합니다. 최대 3회 클릭(Q1→Q2 또는 Q1→Q3→Q4)으로 방향이 정해집니다.

```
Q1. "요즘 상황에 가장 가까운 것을 골라주세요."
    A. 최근에 뭔가를 바꾸거나 조치를 했다
    B. 딱히 바꾼 건 없는데, 문제가 있다
    C. 특별한 문제는 없지만, 그냥 지금 상태가 괜찮은지 확인하고 싶다
    D. 잘 모르겠다 — 데이터부터 보여줬으면 좋겠다

[Q1-A] Q2. 그 조치의 효과를 "지금 확인"하고 싶다 → ResultVerification
           이미 확인했고 "유지되는지" 보고 싶다   → Maintenance
[Q1-B] Q3. 원인 짐작 있음 → Q4. 하나씩 확인 → RootCause / 한꺼번에 비교 → KeyFactor
           원인 감이 안 잡힘 → KeyFactor(탐색적)
[Q1-C] Q5. 측정 도구가 정확한지 궁금 → MSA
           요즘 결과가 평소와 다른지 궁금 → ProactiveComparison
[Q1-D] → 폴백 처리(§5, Navigator_Question_Flow.md)
```

라우팅이 정해진 뒤, 해당 패키지에 필요한 항목만 골라 "자동판별→확인질문" 흐름(§2 제약 3)을 거칩니다. 전체 질문 문구·라우팅 결정표·9개 시나리오 드라이런 검증 결과는 `Navigator_Question_Flow.md`(v2)를 참조하십시오.

> **⚠ 구현 시 반드시 확인할 격차**: 위 질문 트리는 **6개 핵심 패키지까지만** 라우팅합니다. 신뢰성·안전재고 2개 패키지(§5.7, 5.8)로 가는 경로가 아직 Navigator에 설계되어 있지 않습니다 — 이는 Navigator v2가 G10/G11(신뢰성·안전재고)이 추가되기 전에 설계·검증(RUN-019)되었기 때문입니다. 두 가지 선택지가 있습니다: (1) Navigator 상황 질문 트리에 신뢰성·안전재고로 가는 새 분기를 추가하거나(권장 — §2 제약 6을 지키려면 상황 질문 형태여야 함), (2) 두 패키지를 Navigator 밖의 별도 메뉴 진입점으로 배치. 이 결정은 연구범위에서 다루지 않았으므로 **개발 착수 시 Ian과 함께 확정**해야 합니다.

---

## 7. 해석 템플릿 설계 원칙 (반드시 준수) — GAP-09 방법론

AI가 없는 환경에서 "해석 템플릿이 커버하지 못하는 슬롯 조합"이 생기면 사용자는 빈 화면이나 오해석을 받게 됩니다. 이를 막기 위해, 새 패키지나 새 해석 슬롯을 추가할 때는 **반드시** 각 슬롯을 아래 3유형 중 하나로 먼저 분류한 뒤 템플릿을 작성하십시오.

1. **배타적 핵심분류(exclusive core classification)**: 동시에 두 값일 수 없는 상태. 예: 유의/비유의 × 효과크기등급(작음/중간/큼). → 조합 개수만큼 템플릿이 전부 있어야 합니다(차원의 곱).
2. **접두 경고(prefix warning)**: 핵심분류와 독립적인 이진 플래그로, 있으면 항상 다른 내용보다 먼저 표시. 예: 자기상관경고, 다중비교경고, 데이터부족경고. → 핵심분류 템플릿 앞에 조건부로 붙이는 별도 문구 1개면 충분합니다.
3. **목록형 조립(composable list)**: 여러 항목이 동시에 발생할 수 있는 경우. 예: Western Electric Rules 4종(2개 이상 동시 위반 가능). → 배타적 분류로 잘못 설계하면 실제 발생 가능한 조합을 놓칩니다(Maintenance 패키지가 실제로 이 실수를 저질렀던 사례, RUN-019에서 발견·수정). 항목별 개별 템플릿 + "2개 이상 동시 발생" 안내문 1개로 설계하면, 이론상 2ⁿ가지 조합을 항목 수+1개의 템플릿 조각만으로 전부 커버할 수 있습니다.

**구현 시 자체점검 절차**: 새 템플릿 테이블을 작성한 뒤, 배타적 핵심분류는 "차원의 곱만큼 템플릿이 다 있는가", 목록형 슬롯은 "항목별 개별 템플릿 + 동시발생 안내문이 있는가"를 표로 확인하십시오. 이 확인 없이 템플릿을 배포하면 런타임에 매칭 실패(빈 화면)가 발생할 수 있습니다 — 이 경우를 대비해 M-SAFETY-FALLBACK은 절대 생략하면 안 됩니다(§2 제약 5).

**중요한 구분**: 이 자체점검은 "구조적 완전성"(모든 슬롯 조합에 템플릿이 존재하는가)만 보장합니다. "그 문구가 실사용자에게 실제로 이해되는가"는 별개의 검증이며, 프로토타입과 실사용자 테스트 없이는 확인할 수 없습니다(GAP-02/05, 여전히 미착수). 구현 완료를 "문구까지 검증되었다"는 의미로 오해하지 마십시오.

전체 6개 패키지의 슬롯 유형 판정과 커버리지 점검 결과는 `GAP09_Interpretation_Template_Coverage_Matrix.md`를 참조하십시오(신뢰성·안전재고 2개는 각 패키지 스펙 파일 §4에 동일 방법론이 개별 적용되어 있습니다).

---

## 8. 데이터/스키마 관련 요구사항 — GAP-08 (의도적 미결, 개발 착수 시 Ian과 함께 확정)

PRISM의 기술 스택·데이터베이스 스키마·API 또는 DB 연동 방식·인증 체계는 **이 연구에서 의도적으로 조사하지 않았습니다**(DEC-009, Ian의 명시적 지시). 대신 각 패키지가 **어떤 데이터가 있어야 동작하는지**는 확정했습니다. 개발 착수 시 아래 항목을 PRISM의 실제 데이터 구조와 대조해 확정해야 합니다.

| 패키지 | 필요 데이터 | 확인 필요 사항 |
|---|---|---|
| 결과검증·원인분석·핵심요인분석·예방적비교 | 그룹별/변수별 수치형 측정값, 대응여부, 측정순서 | PRISM이 이미 CTQ 측정값을 시계열로 보관하고 있는지, 측정순서(타임스탬프)가 항상 남아있는지 |
| MSA | 부품×작업자×반복 Gauge R&R 형식 데이터 | 이런 형식의 데이터를 PRISM에서 입력/조회하는 기존 흐름이 있는지, 없다면 신규 입력 UI 필요 |
| 유지관리 | 개선 후 시계열 측정값 + 개선시점 | PRISM의 관리도·알림 체계와 어떻게 연동할지(§8-부가: MSA 불량판정의 타 패키지 자동경고 연동도 이와 같은 "패키지 간 상태공유 메커니즘"이 필요 — 현재 카탈로그에 없음, GAP-08 해소 후 설계) |
| 신뢰성 | 부품별 **누적 사용시간**+고장여부(고장/중도절단 구분) | PRISM이 부품별 누적 사용시간을 이미 추적하는지, 아니면 사용자가 별도 입력해야 하는지 — 설계에 큰 영향 |
| 안전재고 | 자재별 수요 이력(시계열)+리드타임 | PRISM이 ERP/MRP성 수요·발주 이력과 연동되어 있는지, 아니면 이 Add-on이 독립적으로 데이터를 입력받아야 하는지 |

**공통 확인사항**: (1) 사용자 인증/권한 체계, (2) 분석 결과의 저장·이력 관리 방식, (3) Navigator 진입점을 PRISM UI 어디에 배치할지, (4) §6에서 언급한 "MSA 불량판정의 타 패키지 자동경고 연동"처럼 패키지 간 상태를 공유해야 하는 기능의 저장 방식.

---

## 9. 알려진 한계 / [추론]으로 표시된 설계 확장 — 구현 전후 재검토 권장

아래 항목은 문헌에 직접 명시된 것이 아니라 이 연구에서 실무 적용 가능한 형태로 변환·단순화한 설계 확장입니다. 통계 담당자가 확보되면 우선적으로 재검토를 권장합니다. 구현 자체는 아래 값을 그대로 사용해 진행해도 무방하지만, 결과가 의심스러울 때 이 목록을 먼저 확인하십시오.

- **신뢰성 패키지 β 임계값(1.2/0.8)**: SRC-147의 "β>1/β≈1/β<1" 3단 서술을 실무 구간으로 변환한 것 — 정확한 경계값은 문헌에 없음.
- **신뢰성 패키지 M-RELY-REPLACEINTERVAL의 그리드 탐색**: 원문(SRC-153, ReliaSoft)은 미분 기반 해석적 최적화를 제시하나, 무AI·결정론적 규칙엔진 제약 하에서 그리드 탐색(수치 비교)으로 단순화. 그리드 해상도·범위는 개발단계에서 확정 필요.
- **안전재고 Z값 표(90%→1.28)**: 두 실무자료(SRC-151=1.28, SRC-154=1.29)가 소수점 둘째자리에서 다름 — 반올림 차이로 판단해 1.28 유지. 정밀도가 중요하면 표준정규분포 역함수를 직접 계산하는 방식으로 대체 가능.
- **안전재고 패키지 전반**: 재고관리 전문교과서 수준 검증 없이 실무자료 3건(SRC-151/152/154)만으로 설계됨(GAP-11 open(부분), 근거등급 medium/low-medium).
- **Navigator 표본수 임계값(15건 등)**: 통계적 최소 표본 관행을 참고한 설계 확장이며 문헌에 명시적 수치가 없음.
- **M-CORRECT-FWER의 KeyFactor 미적용**: 현재 RootCause에만 다중비교 보정이 적용되어 있고 KeyFactor에는 적용되지 않음 — 향후 보강 후보로 카탈로그에 명시되어 있음.
- **독립 통계전문가 리뷰가 waived 상태**(GAP-07, DEC-006) — Claude의 3단계 자체검토(이론감사→자기비판적 재검토→몬테카를로 시뮬레이션)가 대체 통제수단이며 진정한 독립검토는 아님.
- **실사용자 문구 검증 미착수**(GAP-02/05) — §7에서 설명한 "구조적 완전성"은 확인되었으나 문구의 실제 이해도는 프로토타입 단계에서 검증 필요.

---

## 10. 의사결정 이력 요약

전체 이력은 `00_GOVERNANCE/Decision_Log.csv`(DEC-001~013)를 참조하십시오. 개발자가 알아야 할 핵심 결정만 요약합니다.

- **DEC-008(가장 중요)**: 제품은 독립 앱이 아니라 PRISM Add-on이며, 런타임에 AI/LLM이 없다.
- **DEC-009**: PRISM 기술 스택·데이터 스키마(GAP-08)는 이 연구범위에서 의도적으로 제외 — Claude Code 개발 착수 시 Ian이 직접 전달.
- **DEC-010**: 패키지마다 프로즈를 새로 쓰지 않고, 재사용 가능한 원자 모듈+조합 규칙(카탈로그) 방식을 채택.
- **DEC-011**: 자동판별 결과는 절대 침묵 스킵하지 않고 항상 확인질문으로 되묻는다.
- **DEC-012**: 신뢰성·안전재고 2개 도메인 확장 패키지는 Ian이 Claude의 "보류/제외" 권장을 채택하지 않고 직접 착수를 결정 — 근거등급이 다른 6개보다 낮다는 점을 항상 함께 표기.
- **DEC-013**: 해석 템플릿 커버리지는 "구조적 완전성" 기준으로 closed 처리하되, "문구 품질"은 별도 검증(GAP-02/05)으로 이관.

---

## 11. 개발 착수 체크리스트

1. [ ] Ian으로부터 PRISM 기술 스택 문서·앱 폴더·데이터 스키마 전달받기(GAP-08 해소)
2. [ ] §8의 데이터 요구사항을 PRISM 실제 스키마와 대조해 각 패키지별 입력 필드 확정
3. [ ] §6에서 flag한 Navigator의 신뢰성/안전재고 라우팅 공백을 Ian과 함께 결정(질문 트리 확장 vs 별도 메뉴)
4. [ ] 원자 모듈(§4)을 재사용 함수/클래스로 구현 — 특히 M-DATA-PROFILE·M-INTERP-ASSEMBLE·M-SAFETY-FALLBACK(전 패키지 공통)을 먼저 구현
5. [ ] 8개 패키지를 레시피(선언적 설정)로 구현 — 근거등급이 높은 6개 핵심 패키지 우선, 신뢰성·안전재고는 이후
6. [ ] 해석 템플릿 매칭 엔진을 §7의 3유형 방법론(배타적 핵심분류/접두경고/목록형 조립)에 따라 구현하고, 전수 커버리지 자체점검을 코드/테스트로 자동화
7. [ ] §9의 [추론] 항목을 구현 노트에 남겨, 통계 담당자 확보 시 재검토 대상으로 추적
8. [ ] 8개 패키지 각각에 M-SAFETY-FALLBACK이 실제로 동작하는지(매칭 실패를 인위적으로 유발해) 테스트
9. [ ] Navigator 질문 흐름을 실제 UI로 구현 — 통계 용어·패키지 이름이 사용자 화면에 노출되지 않는지 확인
10. [ ] 프로토타입 완성 후 실사용자 테스트 계획 수립(GAP-02/05) — 문구 품질은 아직 검증되지 않았음을 항상 전제

---

## 12. 참고 문서 색인 (F:\obsidian\vault\통계분석앱\)

| 파일 | 내용 |
|---|---|
| `08_DELIVERABLES/Final_Report.md` | 연구 전체 결론·발견·권고 (v2.1) |
| `08_DELIVERABLES/Analysis_Module_Library_and_Composition_Rules.md` | 원자 모듈 전체 카탈로그(9개 카테고리)+조합 규칙+레시피 표기법 (v1.2) |
| `08_DELIVERABLES/Analysis_Package_Spec_{ResultVerification,RootCause,KeyFactor,MSA,Maintenance,ProactiveComparison,Reliability,SafetyStock}.md` | 패키지별 상세 스펙(입력요구사항·E2E흐름·해석 템플릿 전체 문구·근거) |
| `08_DELIVERABLES/Navigator_Question_Flow.md` | Navigator 질문 흐름 전체(v2)+9개 시나리오 드라이런 검증 |
| `08_DELIVERABLES/GAP09_Interpretation_Template_Coverage_Matrix.md` | 해석 템플릿 전수 커버리지 점검 결과 |
| `08_DELIVERABLES/MVP_Coverage_Matrix.md` | 8개 패키지 대 실제 현장 사례(Case Library) 대응관계 |
| `07_RESULTS/Limitations_and_Open_Questions.md` | 한계·미해결 가정 전체(DBT-01~08) |
| `07_RESULTS/Findings_Register.csv` | 발견(FND-01~16) 구조화 목록 |
| `02_EVIDENCE/Claim_Evidence_Matrix.csv`, `Source_Register.csv`, `Evidence_Gaps.md` | 근거·출처·남은 조사 공백 전체 |
| `00_GOVERNANCE/Decision_Log.csv`, `Change_Log.md` | 의사결정·변경 이력 전체 |
| `05_EXECUTION/Execution_Log.csv` | 전체 연구 실행 이력(RUN-001~027) |
