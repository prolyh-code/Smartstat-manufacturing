---
id: LLM-EXT-GAP-001
title: LLM_extention Step 1~7 검토 — 누락 및 보완 필요 사항
type: review-note
status: active
owner: Ian
created: 2026-09-12
updated: 2026-09-12
---

# 검토 결론 (요약)

LLM_extention 기획은 **"LLM은 계산하지 않는다"는 원칙, 교란요인(Confounding Factor·混亂要因) 인식, Evidence Level(E0~E4) 체계, Stop Condition(분석 종료 조건)** 이라는 4가지 축을 일관되게 유지하고 있어, 통상적인 "ChatGPT에 통계를 물어보는" 수준의 기획보다 설계 완성도가 높습니다. 다만 Step 1~7 전체를 통독한 결과, 아래 4가지는 **최우선으로 보완이 필요한 사항(A)**이고, 나머지는 구현 단계 이전에 결정해두면 좋은 **중요 보완 사항(B)**과 **운영·거버넌스 관점 보완 사항(C)**입니다. 결론부터 말하면, 가장 심각한 결함은 기술적 결함이 아니라 **"기존 PRISM Add-on이 런타임에 LLM을 배제한 이유"와 이번 확장 기획이 정면으로 충돌하는데, 그 충돌 자체가 문서화되어 있지 않다는 점**(A-1)입니다.

---

# A. 최우선 보완 필요 사항

## A-1. LLM에 전달되는 제조 데이터의 기밀성(機密性) 문제 — 원래 설계원칙과의 정합성 미검토

**무엇이 빠졌는가:** Step 5~7 전체에서 LLM Context에 무엇을 담을지(Problem State, Dataset Profile, Analysis State, Tool Result 등)는 정교하게 설계되어 있지만, **그 정보가 외부 LLM Provider(OpenAI/Anthropic 등)의 API로 실제로 전송된다는 사실 자체에 대한 리스크 검토가 없습니다.** 기존 PRISM Add-on을 "런타임에 AI/LLM 없이 결정론적 규칙으로만 동작"하도록 설계했던 이유가 바로 이 문제(현장 데이터·불량률·설비명·모델명 등이 외부로 나가는 것)를 원천적으로 차단하기 위함이었을 가능성이 높은데, 이번 확장 기획은 그 전제를 뒤집으면서도 "그래서 이제는 괜찮다"는 근거나 대안(온프레미스 LLM, 데이터 마스킹, 사내 배포 모델 등)을 논의하지 않습니다.

**왜 중요한가:** 제조 현장 데이터(불량률, 설비 가동 조건, 생산량, 모델 배분 등)는 일반적으로 영업비밀·품질 클레임 대응 자료로 취급되며, 외부 API로 전송되는 순간 회사의 데이터 통제권을 벗어납니다. Statistical Result 예시에 나오는 것과 같은 수치(defect rate 3.2%, N=18,450 등)만 봐도 실제 서비스에서는 민감할 수 있는 정보입니다.

**보완 방향(제안):**
- Knowledge Context(6장)처럼 "Company Knowledge"에는 실제 회사명·라인명·CTQ 상세 규격이 들어가는데, 이 중 어떤 필드가 LLM Provider로 나가도 되는지/안 되는지 **데이터 분류(Public/Internal/Confidential) 기준**을 먼저 정의해야 합니다.
- 온프레미스 또는 VPC 격리형 LLM(Provider Adapter 구조를 이미 5-18에서 제안했으므로 확장 용이) 옵션을 최소 MVP 설계에 명시.
- 식별정보(설비명, 라인명, 작업자명 등)를 Tool 결과 → LLM Context 사이에서 코드화(pseudonymization)하는 계층을 Raw Data–LLM 분리 원칙(5-15)에 추가.

## A-2. 다중비교(Multiple Comparison) 보정 부재 — Candidate Factor Screening의 통계적 위험

**무엇이 빠졌는가:** UC-11(4.5)과 Step 7(7-25)에서 Agent는 Machine, Model, Shift, Operator 등 여러 후보 요인을 각각 독립적인 검정(t-test/ANOVA/proportion test 등)으로 동시에 "스크리닝"합니다. 그런데 이렇게 **후보 요인을 여러 개 동시에 검정하면 우연히 유의한(false positive) 결과가 나올 확률이 커진다는 다중비교 문제**가 전혀 언급되지 않습니다.

**왜 중요한가(기초 개념):** 하나의 가설검정에서 유의수준(α, significance level)을 0.05로 두면 "실제로는 차이가 없는데 유의하다고 잘못 판단할 확률"이 5%입니다. 그런데 요인을 5개(Machine, Model, Shift, Operator, Temperature 등) 동시에 검정하면, 그중 하나 이상이 우연히 유의하게 나올 확률은 대략 1-(0.95)^5 ≈ 23%까지 올라갑니다. 이 문서들이 그토록 강조하는 "교란요인 인식·인과 과장 방지"라는 원칙과 같은 선상에 있는 문제인데, 정작 스크리닝 단계 자체의 통계적 엄밀성은 다뤄지지 않았습니다.

**보완 방향(제안):** Bonferroni, Holm, 또는 FDR(False Discovery Rate, 위발견율) 보정을 Candidate Factor Screening 단계의 표준 절차로 Statistical Policy(7-5)에 추가하고, "다중 요인을 동시 스크리닝할 때는 반드시 보정된 p-value 또는 순위 기반 우선순위화를 사용한다"는 규칙을 Tool 계층에 명시.

## A-3. 이분형(불량 유/무) 반응변수에 대한 통계 Tool이 Tool Architecture에 정의되어 있지 않음

**무엇이 빠졌는가:** 4.5와 7장(7-25)에서는 명시적으로 "불량 여부(Binary)를 t-test로 비교하면 안 되고 proportion test/chi-square 등 categorical analysis를 써야 한다"고 서술하지만, **정작 5-6(Tool 분류)과 5-19(MVP Tool 목록)에는 proportion test, chi-square, Fisher's exact test, logistic regression 중 어느 것도 포함되어 있지 않습니다.** 문서 안에서 "이렇게 해야 한다"는 서술과 "실제로 구현할 Tool 목록"이 서로 어긋나는 셈입니다. (참고로 logistic regression은 7-13에서 한 번 예시로만 등장하고 Tool 목록에는 없습니다.)

**왜 중요한가:** 제조 현장 CTQ 분석에서 가장 흔한 반응변수는 연속형 측정값(Torque 등)이 아니라 오히려 **불량률(=이분형의 집계)** 자체인 경우가 많고, UC-01/05/07/11 예시 전부가 결국 defect rate 비교로 귀결됩니다. 이 Tool이 없으면 Agent가 스스로 강조한 "categorical analysis를 써야 한다"는 원칙을 실행할 수단이 없습니다.

**보완 방향(제안):** Category C(Comparison)에 2-proportion z-test, chi-square test of independence, Fisher's exact test(소표본용)를 추가하고, MVP Tool 목록(5-19)에 최소 chi-square test와 2-proportion test는 포함시킬 것을 권장.

## A-4. 교란요인 통제가 사례별 임시방편(ad-hoc)에 의존 — 일반화된 Tool 부재

**무엇이 빠졌는가:** UC-11에서 Machine–Model 교란(Model C가 M2에 집중 생산됨)을 발견한 뒤 Agent가 취하는 조치는 "Model C로 한정해서 Machine만 다시 비교"하는 **수동적 층화분석(stratified analysis)**입니다. 이것은 교란요인이 1개이고 범주가 단순할 때만 통하는 방법입니다. 교란요인이 2개 이상이거나 연속형(예: Temperature)일 때 쓸 수 있는 **일반화된 Tool(ANCOVA, 다중회귀에서의 교란변수 통제, Mantel-Haenszel 검정 등)**이 Tool Architecture에 별도 항목으로 정의되어 있지 않습니다.

**보완 방향(제안):** "confounding_check()"뿐 아니라 "adjusted_comparison()" 또는 "stratified_analysis()"류의 범용 Tool을 Category C/D에 추가하고, Analysis Plan Graph(5-8)에서 교란 발견 시 자동으로 이 Tool로 분기하도록 규칙화.

---

# B. 중요 보완 필요 사항

## B-1. Statistical Engine 자체의 정확성 검증·회귀테스트 전략 부재
Tool이 반환하는 결과의 신뢰성(각 통계량, p-value, CI)을 R/Python(SciPy, statsmodels) 등 검증된 라이브러리 또는 상용 통계 SW(Minitab 등)의 출력과 대조해 검증하는 절차, 그리고 Tool 버전이 바뀔 때 과거 결과가 재현되는지 확인하는 회귀테스트 체계가 어디에도 정의되어 있지 않습니다. 3.8(Evaluation Framework)의 Golden Case는 Agent의 "판단"을 평가하는 것이고, 이는 Tool의 "계산" 자체를 검증하는 것과는 다른 문제입니다.

## B-2. 측정시스템분석(MSA·Measurement System Analysis)의 선행 게이트 역할 미통합
기존 PRISM 카탈로그에 MSA 모듈이 존재하는데, LLM_extention에서는 "측정 시스템을 고려해야 한다"(6-18)는 주의사항으로만 언급되고, 실제 Agent Workflow(4.x, UC-01/05/07/11) 어디에도 "설비 간 CTQ를 비교하기 전에 측정 시스템의 반복성·재현성이 충분한지 먼저 확인한다"는 선행 단계로 연결되지 않습니다. 측정 오차가 크면 설비 간 차이로 보이는 것이 실제로는 계측기 오차일 수 있습니다.

## B-3. 시계열 데이터의 특성(자기상관·계절성·변화점 탐지) 처리 방법론 미정의
UC-11의 "언제부터 증가했는가"(4.5, §7)는 사실상 change point detection(변화점 탐지) 문제인데 구체적 방법(CUSUM, 구조변화 검정 등) 없이 그림으로만 표현됩니다. 또한 하루 단위로 집계된 생산 데이터를 "독립 표본"처럼 t-test/ANOVA에 넣는 것은 자기상관(autocorrelation)이 있으면 가정 위반입니다. Statistical Policy(7-5)의 "independent/paired/repeated/time-series" 구분은 나열만 되어 있고 time-series 케이스의 구체적 처리 규칙은 없습니다.

## B-4. Evidence의 하향 조정·재평가 정책 부재
E0→E4로 올라가는 방향만 설계되어 있고, **새로운 데이터가 기존의 E2~E3 결론을 반박할 때 어떻게 되돌리는지(Evidence 강도를 낮추거나 폐기하는 절차)**가 없습니다. 제조 현장은 조건이 계속 바뀌므로(공정 변경, 설비 교체 등), "8월 데이터로 확립한 E3 결론이 10월에도 유효한가"를 판단할 기준(예: Evidence에 유효기간·재검증 조건을 부여)이 필요합니다.

## B-5. Data Guard(데이터 품질 관문)의 구체적 판단 기준 미정의
`check_data_quality()`가 반복적으로 언급되지만, "결측률 몇 %부터 분석을 중단/경고하는가", "이상값을 자동 제거/표시만/유지 중 어떻게 다루는가" 같은 실제 임계값·정책은 어디에도 수치화되어 있지 않습니다. Rule Engine의 다른 구성요소(Method Guard, Assumption Guard)는 예시가 구체적인 데 비해 Data Guard는 이름만 있고 내용이 가장 빈약합니다.

---

# C. 운영·거버넌스 관점 보완 사항

## C-1. LLM API 비용·응답지연·가용성 관리 정책 부재
UC-11 같은 시나리오는 Tool Call이 10회 이상 이어질 수 있는데, 현장 사용자가 실시간으로 기다릴 수 있는 응답시간, 세션당 예상 API 비용, LLM API 장애 시 폴백(fallback) 방안(예: 기존 규칙기반 UI로 전환)이 설계에 없습니다.

## C-2. 사용자의 실시간 정정(피드백)이 그 세션의 판단에 반영되는 절차 미정의
예를 들어 사용자가 "M2는 최근에 교체한 설비야"라고 정정하면, 이는 6-26의 "Analysis Result ≠ 영구적 지식" 원칙상 곧바로 Knowledge로 승격시키면 안 되지만, **그 세션의 Agent State(Finding/Hypothesis)에는 즉시 반영되어야 하는 정보**입니다. Knowledge 승격과 별개로, "사용자가 제공한 정보를 현재 세션 Evidence로 어떻게 편입할지"에 대한 규칙(Evidence Policy의 4번 항목 "Explicit User-provided information"은 있지만 절차가 구체화되지 않음)이 필요합니다.

## C-3. 모델(LLM Provider) 교체 시 Golden Case 회귀테스트와의 명시적 연결 부재
5-18에서 LLM Provider를 교체 가능하게 만드는 아키텍처(Adapter 패턴)는 제안했지만, "Provider를 바꾸면 3.8의 Golden Case 스위트를 반드시 재실행해 동일한 판단이 나오는지 확인한다"는 절차가 두 문서 사이에 명시적으로 연결되어 있지 않습니다.

## C-4. 고위험 판단에 대한 인간 승인(Human-in-the-loop) 체계 미정의
Agent가 "생산 중단을 검토하라" 수준의 의사결정에 영향을 줄 수 있는 결론을 낼 경우, 이를 그대로 현장에 전달하기 전에 품질관리자 등의 승인을 거치는 절차가 필요한지에 대한 논의가 없습니다. Stop Condition은 "분석을 언제 멈추는가"를 다루지만 "Agent의 결론을 언제 사람이 재확인해야 하는가"는 다른 문제입니다.

---

# D. 참고 수준 보완 사항 (구현 우선순위 낮음)

- **상호작용효과·다변량 분석 부재**: UC-01/03/05/07/11 전부 단일 CTQ·단일 요인 중심이며, 회귀분석도 덧셈모형(additive model)만 예시로 들어 요인 간 상호작용(예: Machine×Temperature)이나 여러 CTQ를 동시에 보는 다변량 분석 시나리오가 없습니다. (Capability, PCA 등은 이미 MVP 제외로 명시되어 있어 이 자체는 문제가 아니지만, "왜 제외했는지"의 연장선에서 상호작용효과도 Phase 2 항목으로 명시해두면 좋습니다.)
- **역할별(품질관리자/현장 엔지니어/경영진) 응답 차별화 미검토**: Agent UX Architecture(3.7)가 대화 UX는 다루지만, 같은 결론을 누구에게 어떤 detail 수준으로 전달할지는 별도 논의가 필요합니다.

---

# 종합 제안

문서 7편(1~7) 전체를 관통하는 설계 철학(LLM은 판단하지 않고 지휘만 한다, 근거 없이는 원인을 확정하지 않는다)은 견고합니다. 다음 Step(8, Multi-Agent 구조 검토)으로 넘어가기 전에, **A-1(데이터 기밀성)은 제품의 전제 자체를 흔드는 문제이므로 Step 8보다 먼저 결론을 내리는 것을 권장**합니다[추론]. A-2~A-4(통계적 엄밀성 항목)는 Tool Architecture(3.5, 5장)에 소규모 추가만으로 해결 가능한 실무적 보완이라 개발 착수 전에 반영하기 좋은 시점입니다[추론]. B, C 항목들은 Step 8~ 이후의 구현 설계 단계에서 순차적으로 채워도 되는 항목으로 판단됩니다[추론].
