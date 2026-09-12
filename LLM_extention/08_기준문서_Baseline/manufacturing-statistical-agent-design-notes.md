> ## ⚠ 이 문서의 현재 상태 (2026-09-12 기준)
>
> **이 문서는 Step 1~25까지의 맥락 요약이며, 최신 설계가 아닙니다.**
>
> - **맥락 파악용으로는 유효합니다** — 프로젝트의 철학, 4-역할 분리, Evidence 체계, Use Case, Golden Case 개념을 이해하려면 이 문서가 가장 빠른 경로입니다.
> - **구현 근거로는 사용하지 마십시오.** Step 26~31에서 다음이 바뀌었습니다.
>   - 제품 형태: 데스크톱 전제 → **웹앱(다중 사용자 동시접속)**
>   - LLM 인증: 미정 → **개인 계정 + 개인별 승인 한도**
>   - LLM 호출 위치: 미정/서버 → **사용자 개인 PC(브라우저)**
>   - §10 Statistical Engine의 Phase 구분: **chi-square·proportion test가 MVP로 이동**(DD-086)
>   - §33 Open Design Decisions: **전부 해소됨**(O-1~O-13)
>   - §24 Information Architecture: Step 26 §4의 화면 목록(S-00~S-13, S-90)으로 대체
>   - §30 Security/Privacy/Reliability: Step 28·28-1·29로 전면 대체
>   - §32 Revised Development Sequence: Step 29 신설로 번호 이동(Schema→30, Final MVP→31)
> - **현재 설계의 진입점은 루트의 `CLAUDE.md`입니다.** 설계결정의 유효·폐기 여부는 `DD_Register.md`에서 확인하십시오.
>
> 이 문서를 v1.4로 갱신하는 작업은 미실행 상태이며, 갱신 대신 **`CLAUDE.md` + `DD_Register.md` + Step 31 계열**이 현재 기준 역할을 합니다.

---

# Manufacturing Statistical Agent
# Design Notes — Baseline v1.0

**작성일:** 2026-09-12  
**목적:** 기존 `통계분석 앱 제작 기획서.md`와 이후 설계 대화를 하나의 기준점(Baseline)으로 압축하여, 이후 기획·설계 단계에서 맥락이 끊기지 않도록 한다.

---

## 1. Project Definition

본 프로젝트는 제조 현장의 생산·품질·설비·공정 데이터를 대상으로 통계 분석을 수행하고, 분석 결과를 제조적 판단과 다음 행동으로 연결하는 **Manufacturing Statistical Analysis Platform**을 구축하는 것이다.

핵심은 통계 계산 기능 자체가 아니다.

> **“통계를 계산하는 프로그램이 아니라, 제조 현장의 질문을 통계적 판단으로 바꿔주는 프로그램.”**

기존 제품 철학:

**현장 문제 → 질문 → 분석 선택 → 결과 → 그래프 → 쉬운 해석 → 현장 판단**

LLM Agent 통합 후:

**Easy Access → Easy Understanding → Easy Analysis → Easy Interpretation → Evidence-based Decision → Next Action**

---

## 2. Original Product Concept

가칭:

> **SmartStat Manufacturing**

핵심 포지션:

> **Manufacturing Statistical Assistant**

Minitab, JMP, Excel, Python/R과 통계 계산 능력으로 경쟁하지 않는다. 제조 현장 사용자가 통계 전문지식 없이도 적절한 분석을 선택하고 결과를 이해하며 현장 판단을 할 수 있도록 하는 것이 핵심 경쟁력이다.

기존 차별화:
- 제조 현장 중심 분석
- 현장 문제 중심 메뉴
- 분석 선택 지원
- 쉬운 결과 해석
- 직관적 고품질 SVG
- 제조 사례
- 자동 보고서
- 비전문가 접근성

---

## 3. Why LLM Integration

LLM은 통계 계산기를 대체하기 위해 도입하지 않는다.

### LLM이 담당
- 자연어 질문 이해
- 문제 정의
- 분석 방법 추천
- 다단계 분석 계획
- 결과 해석
- 제조 현장 의미 해석
- 추가 분석 제안
- 원인 후보/가설 탐색
- Next Best Analysis 선택
- 사용자와의 대화형 분석

### LLM이 담당하지 않음
- 원시 통계 계산
- p-value/CI/test statistic 직접 계산
- Statistical Engine 결과 임의 수정
- 관찰자료만으로 인과관계 확정
- Rule Engine 우회
- 실행되지 않은 결과 생성

핵심 분리:

> **LLM = Reasoning / Language / Planning**  
> **Statistical Engine = Deterministic Computation**  
> **Rule Engine = Hard Constraint**  
> **State = Facts**  
> **Knowledge/RAG = Domain Context**

---

## 4. Final Product Architecture

```text
                         User
                          │
                          ▼
                Manufacturing Statistical UI
                          │
             ┌────────────┴────────────┐
             │                         │
        Manual Analysis            AI / Agent
             │                         │
             └────────────┬────────────┘
                          ▼
                   Analysis State
                          │
                          ▼
                    Data Engine
                          │
                          ▼
                 Rule / Guardrail
                          │
                          ▼
                   Tool Registry
                          │
                          ▼
                 Statistical Engine
                          │
                          ▼
                  Result Validator
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
          Result       Finding      Evidence
             │            │            │
             └────────────┼────────────┘
                          ▼
                 Interpretation
                          │
                          ▼
                Manufacturing Judgment
                          │
                          ▼
                  Next Best Analysis
                          │
                          ▼
                    Next Action
```

### 핵심 원칙

Manual과 AI는 별개의 분석 시스템이 아니다.

**동일한 Deterministic Statistical Engine을 공유한다.**

따라서:
- Manual → AI 전환 가능
- AI → Manual 전환 가능
- AI OFF에서도 핵심 기능 사용 가능
- LLM 장애가 통계 분석을 중단시키지 않음
- 동일 데이터/조건에서 통계 결과 재현 가능

---

## 5. Operating Modes

### Level 0 — Manual Mode
**LLM OFF**

사용자가 직접:
1. 데이터 업로드
2. 분석 메뉴 선택
3. 변수 선택
4. 조건 확인
5. 분석 실행
6. 그래프 확인
7. 결과 확인
8. 보고서 생성

기존 Wizard와 Analysis Navigator가 이 역할을 담당한다.

> **LLM이 없어도 앱은 완전한 통계 분석 도구로 독립 동작해야 한다.**

### Level 1 — Guided / Assisted Mode
**LLM ON**

AI가 질문을 이해하고 분석 방법을 추천한다. 필요한 데이터/조건을 확인하고 분석 계획을 제시한다. 필요하면 사용자 승인 후 실행한다.

### Level 2 — AI Analysis Mode
사용자가 목적을 주면 AI가 여러 분석을 계획하고 실행한다.

예:
> “A라인과 B라인의 토크 차이가 왜 발생하는지 확인해줘.”

가능한 흐름:
데이터 구조 → Line 비교 → 분산 비교 → Model 구성 → Model별 비교 → 추가 변수 → 통제 분석 후보 → Finding → Evidence → 다음 분석.

### Level 3 — Agentic Analysis
목표를 주면 Agent가 반복적으로 분석한다.

**Question → Problem → Data → Plan → Tool → Result → Finding → Evidence → Hypothesis → Confounder → Next Analysis → Decision**

자율성은 Rule Engine과 데이터 조건에 의해 제한한다.

---

## 6. Manual ↔ AI Interoperability

### Manual → AI
사용자가 먼저 Welch t-test 등을 수행한 뒤 **[AI에게 원인 분석 요청]**을 선택하면 기존 Analysis State를 이어받는다.

AI는 기존:
- dataset
- selected variables
- analysis result
- findings
- evidence
- analysis history

를 이용한다.

### AI → Manual
AI가 다음 분석을 제안하면 **[이 분석 실행]**을 통해 Manual 분석 화면에서 deterministic engine으로 실행한다.

### AI OFF
중간에 AI를 끌 수 있으며:
- Analysis State 유지
- 통계 결과 유지
- Finding/Evidence 유지
- 수동 분석 계속 가능

AI는 필수 실행 기반이 아니라 **선택적 Intelligence Layer**다.

---

## 7. App ↔ LLM Architecture

앱 내부에 **AI Gateway**를 둔다.

```text
UI
 │
 ▼
AI Gateway
 ├─ Authentication
 ├─ Provider Selection
 ├─ Model Selection
 ├─ Prompt Assembly
 ├─ Context Filtering
 ├─ Tool Calling
 ├─ Timeout
 ├─ Retry
 ├─ Error Handling
 ├─ Privacy Control
 └─ Audit / Logging
 │
 ▼
LLM Provider
 ├─ OpenAI
 ├─ Anthropic
 ├─ Company / Private LLM
 └─ Future Local LLM
```

Provider는 추상화하여 특정 LLM 공급자에 종속되지 않게 한다.

### AI Activation Policy
- 단순 계산 → LLM OFF
- 방법 선택 → LLM Optional
- 복합 분석 → LLM ON
- 원인 탐색 → Agentic Analysis

---

## 8. LLM UI / UX

LLM을 단순 Chatbot으로 만들지 않는다.

권장:

> **Chat + Analysis Workspace**

### 좌측
- 사용자 질문
- AI 응답
- 분석 진행 상황
- 추천 다음 단계

### 우측
- 데이터
- 그래프
- 통계 결과
- Finding
- Evidence
- Hypothesis
- 다음 분석

### Analysis Trace
Chain-of-Thought는 노출하지 않는다. 대신 사용자가 검증 가능한 수준의 실행 요약을 표시한다.

예:

```text
✓ 데이터 구조 확인
✓ Group 변수 확인
✓ Sample size 확인
✓ 분산 차이 확인
✓ Welch t-test 수행
✓ Effect Size 계산
✓ Model 구성 차이 확인
● 결과 해석 중
○ 다음 분석 후보 탐색
```

---

## 9. Result UX

### ① Statistical Result
Deterministic Statistical Engine의 사실:
- N
- Mean
- SD
- Difference
- Test Statistic
- df
- P-value
- CI
- Effect Size
- Diagnostics
- Warnings

### ② AI Interpretation
LLM이 결과를 자연어로 설명한다.

### ③ Manufacturing Judgment
통계 결과 + Rule + Manufacturing Knowledge를 이용해 제조적 의미를 판단한다.

반드시 다음을 구분한다.

> **통계적 유의성 ≠ 제조적 유의성 ≠ 인과관계**

---

## 10. Statistical Engine

통계 계산은 검증된 deterministic library 기반으로 수행한다. 외부 API에 pandas/SciPy 등의 내부 구현을 직접 노출하지 않는다.

### MVP
- Descriptive Statistics
- Histogram
- Box Plot
- Scatter Plot
- 1-Sample t-test
- 2-Sample t-test
- Paired t-test
- One-way ANOVA
- Post-hoc
- Pearson Correlation
- Simple Regression

### Phase 2
- Welch t-test
- Welch ANOVA
- Non-parametric tests
- Multiple Regression
- Chi-square
- Proportion tests
- Normality tests
- Variance tests
- Residual analysis

### Phase 3
- SPC
- Capability
- Pareto
- Defect Analysis
- Yield / FPY / RTY
- Anomaly Detection
- Multivariate
- PCA
- DOE
- Optimization

---

## 11. Tool Architecture

Agent는 Statistical Engine 내부 함수를 직접 호출하지 않고 **Tool Registry**를 사용한다.

Tool contract:
- name
- version
- description
- category
- input_schema
- output_schema
- execute()

### Tool categories
**Data:** profile_data, check_data_quality, summarize_variables, detect_missing, detect_duplicates, detect_outliers

**EDA:** descriptive_statistics, distribution_analysis, trend_analysis, outlier_analysis

**Comparison:** one_sample_t_test, two_sample_t_test, welch_t_test, paired_t_test, anova, welch_anova, tukey_posthoc, games_howell

**Relationship:** pearson_correlation, spearman_correlation, simple_regression

**Manufacturing:** defect_rate, group_defect_rate

**Visualization:** histogram, box_plot, scatter_plot, comparison_plot, trend_chart

거대한 `analyze_manufacturing_data()` 하나로 모든 기능을 감싸는 방식은 지양한다.

---

## 12. Rule & Guardrail

```text
LLM Proposal
    ↓
Schema Validation
    ↓
Rule Engine
    ↓
APPROVE / REJECT / REPAIR
    ↓
Tool Execution
```

Rule domains:
1. Data Rules
2. Method Rules
3. Assumption Rules
4. Result Rules
5. Interpretation Rules
6. Causal Rules

주요 원칙:
- 데이터 구조 확인 후 분석
- paired/independent 구분
- 조건 위반 시 경고/차단
- 중복 분석 방지
- 실행되지 않은 결과 주장 금지
- correlation → causation 금지
- 관찰자료만으로 root cause 확정 금지
- 중요한 데이터 품질 문제는 분석 차단 가능

Severity:
INFO / WARNING / ERROR / BLOCKER

---

## 13. Analysis State

LLM Memory만으로 분석 사실을 관리하지 않는다. Application State에 명시적으로 저장한다.

### 4가지 Memory
1. Conversation Memory
2. Analysis State
3. Evidence Memory
4. Knowledge Memory

### AnalysisSession
- session_id
- status
- user_question
- problem_model
- dataset_context
- analysis_plan
- analysis_history
- findings
- evidence
- hypotheses
- confounders
- next_actions
- final_decision

### ProblemModel
- problem_type
- response
- factor
- groups
- objective
- relationship
- candidate_confounders

### DatasetContext
- dataset ID/version
- rows
- columns
- variables
- quality status
- missing rate
- scope

대용량 raw dataset 전체를 LLM context에 넣지 않는다.

---

## 14. Data Quality

분석 전 Data Quality Check를 수행한다.

핵심 원칙:
- Completeness
- Uniqueness
- Validity
- Consistency
- Accuracy

검토:
- 결측
- 중복
- 형식 오류
- 변수 유형
- 표본 수
- 그룹 불균형
- 이상값
- 규격/단위

Data Quality Layer가 **Analysis Dataset**을 정의하고 Statistical Engine은 이 dataset을 대상으로 계산한다.

---

## 15. Finding / Evidence / Hypothesis

### Result
수치/검정 결과.

### Finding
관찰된 의미.

### Hypothesis
가능한 설명 또는 원인 후보.

### Evidence
발견/가설을 뒷받침하는 수준.

Evidence:
- E0: No evidence
- E1: Observed pattern
- E2: Statistical difference / association
- E3: Repeated / cross-validated candidate
- E4: Experimental / improvement verification

Evidence level은 p-value 크기 자체를 의미하지 않는다.

### Causal strength
- NONE
- ASSOCIATION
- CANDIDATE
- SUPPORTED
- EXPERIMENTALLY_SUPPORTED

Hypothesis lifecycle:

**UNTESTED → SUPPORTED → STRENGTHENED / WEAKENED / REJECTED → CONFIRMED**

CONFIRMED는 엄격하게 제한한다.

---

## 16. Confounder

제조 데이터에서는 Model, Machine, Shift, Operator 등의 교란변수가 중요하다.

MVP에서 대표적인 confounding risk:
1. Factor–Outcome association
2. Factor–Confounder imbalance
3. Confounder–Outcome association

세 조건이 함께 나타나면 HIGH confounding risk로 표시할 수 있다.

---

## 17. Next Best Analysis

Agent는 한 번 분석하고 끝나지 않는다.

개념적 scoring:

> **Relevance × Information Gain × Data Availability × Statistical Validity × Manufacturing Impact**

LLM이 후보를 만들고 Rule Engine이 부적절한 후보를 제거한 후 우선순위를 결정한다.

### Stop Conditions
- 질문이 충분히 답변됨
- 추가 분석의 정보 가치가 낮음
- 필요한 데이터가 없음
- 인과 검증에 실험/DOE 필요
- 데이터 간 충돌

> **Stop은 실패가 아니라 분석 결과다.**

---

## 18. Manufacturing Judgment

통계적 유의성과 제조적 유의성을 분리한다.

판단에 사용할 수 있는 정보:
- Target
- LSL / USL
- Historical baseline
- CTQ 중요도
- Defect relationship
- Capability
- Customer requirement
- Cost / impact

MVP 우선:
- Target
- LSL
- USL
- Historical baseline

핵심:

> **“통계적으로 다른가?”뿐 아니라 “제조적으로 얼마나 중요한가?”**

---

## 19. Knowledge / RAG

### 3개 Knowledge Domain

1. **Statistical Knowledge**
2. **Manufacturing Knowledge**
3. **Company Knowledge**

기존 Raw-Wiki / LLM-Wiki 구조를 기반으로 확장한다.

원칙:
- Raw source immutable
- Structured LLM-Wiki
- Agent Knowledge
- Runtime에서 전체 Wiki를 prompt에 넣지 않음
- 필요한 지식만 RAG

Retrieval은:
- Planning Retrieval
- Interpretation Retrieval

로 분리할 수 있다.

---

## 20. Manufacturing Knowledge Graph 방향

향후:

```text
Torque
  ↓ measured_by
Torque Tool
  ↓
Fastening Process
  ↓
CTQ
  ↓ affected_by
Machine / Model / Operator / Shift
  ↓
Defect
```

통계 분석과 제조 지식을 연결하는 기반으로 활용한다.

---

## 21. Prompt Architecture

Prompt layers:
1. Core System
2. Statistical Policy
3. Manufacturing Reasoning
4. Tool Use Policy
5. Knowledge Retrieval Policy
6. Agent State Context
7. Current Task
8. User Message

역할 분리:

> Prompt = Behavior  
> Tool Schema = Capability  
> Rule Engine = Hard Constraint  
> State = Facts  
> RAG = Knowledge

데이터 cell은 신뢰되지 않은 입력으로 취급하여 prompt injection 방어를 고려한다.

`CLAUDE.md`는 개발 Agent governance 문서이고 runtime prompt와 동일한 개념이 아니다.

`LLM-Wiki`는 지식 구조이지 runtime system prompt가 아니다.

---

## 22. Evaluation / Golden Case

Agent 품질은 LLM 문장 품질만 평가하지 않는다.

Golden Case:

- Question
- Dataset
- Data Dictionary
- Expected Problem Model
- Expected Data Assessment
- Expected Analysis Plan
- Expected Tool Calls
- Expected Statistical Results
- Expected Findings
- Expected Evidence
- Expected Hypotheses
- Expected Confounders
- Expected Next Analysis
- Expected Final Decision
- Forbidden Conclusions

평가 영역:
1. Statistics Accuracy
2. Method Selection
3. Assumption Validation
4. Finding
5. Evidence
6. Causal Guardrail
7. Next Best Analysis
8. Manufacturing Judgment

Critical FAIL:
- 잘못된 분석법
- 잘못된 계산
- 데이터 구조 오판
- paired/independent 오류
- 중요한 가정 무시
- p-value 오해
- correlation → causation
- 근거 없는 root cause 확정
- 존재하지 않는 결과/데이터 생성

권장 기준:
- 90+ PASS
- 80–89 REVIEW
- <80 FAIL

단, Critical Error가 있으면 점수와 무관하게 FAIL.

---

## 23. Golden Case UC-03

### 질문
> “A라인과 B라인의 토크 차이가 있는지 확인해줘.”

### Problem Model
- GROUP_COMPARISON
- Response: Torque
- Factor: Line
- Groups: A / B
- Objective: difference_detection
- Initially independent
- Candidate confounders: Model, Machine, Shift, Operator

### Dataset
컬럼:
Timestamp, Model, Line, Machine, Shift, Operator, Torque, Defect_Flag, Target, LSL, USL

- seed = 20260912
- n = 1840
- Target = 170
- LSL = 150
- USL = 190

Line:
- A = 815
- B = 1025

### Line statistics
A:
- Mean = 166.252
- SD = 5.233

B:
- Mean = 168.881
- SD = 7.119

Welch:
- Difference = -2.628 N·m
- t = -9.121
- df ≈ 1827.166
- p < 1e-18
- 95% CI ≈ [-3.194, -2.063]
- Cohen’s d ≈ -0.414

### Model별
Model A:
- A 419 / B 237
- Mean 165.077 / 166.223
- Difference -1.146
- p ≈ .0326

Model B:
- A 211 / B 249
- Mean 166.374 / 168.744
- Difference -2.370
- p ≈ .0000214

Model C:
- A 185 / B 539
- Mean 168.774 / 170.112
- Difference -1.338
- p ≈ .00541

Model별 비교 후에도 Line 차이가 유지된다. 그러나 Line의 인과효과를 확정하지 않는다.

### Defect exploratory
규칙: abs(Torque - Target) > 15
- A ≈ 1.60%
- B ≈ 3.12%
- Chi-square p ≈ .0507

5% 기준에서 명확한 유의차로 단정하지 않는다.

### Expected Findings
- F-001 A 평균이 B보다 낮음
- F-002 B 변동이 더 큼
- F-003 Model 구성과 Line이 서로 불균형
- F-004 Model 수준에 따라 Torque가 다름
- F-005 동일 Model 내에서도 A/B 차이가 유지
- F-006 Line effect는 candidate이지 causal confirmation이 아님

### Hypothesis
**UNTESTED → SUPPORTED → Confounding detected → STRENGTHENED**

CONFIRMED가 아니다.

### Recommended next analysis
1. Same-model comparison
2. Model-controlled regression / GLM
3. Machine / Shift / Operator 통제
4. 실제 process parameter 탐색
5. 인과 확인 시 controlled experiment / DOE

---

## 24. Product UX Information Architecture

기존:

```text
Home
 ↓
Analysis Navigator
 ↓
Data Input
 ↓
Analysis
 ↓
Graph
 ↓
Statistical Result
 ↓
Easy Interpretation
 ↓
Manufacturing Judgment
 ↓
Report
```

LLM 통합 후:

```text
Home
 ↓
Data
 ↓
┌──────────────────────┐
│ Manual Analysis      │
│ AI Analysis          │
└──────────────────────┘
 ↓
Shared Analysis State
 ↓
Result / Finding / Evidence
 ↓
Manufacturing Judgment
 ↓
Next Action
```

Home의 주요 진입점:
- 데이터 불러오기
- 분석 메뉴
- AI 분석

기존 problem-oriented Navigator는 유지한다.

---

## 25. Representative Use Cases

### Question taxonomy
A. 현상 파악
B. 기준 대비 판단
C. 그룹 비교
D. 다중 그룹 비교
E. 변화 효과 분석
F. 관계·영향 분석
G. 이상·원인 탐색
H. 공정 판단·개선 검증

### 15 Use Cases
- UC-01 공정 상태 진단
- UC-02 목표값 비교
- UC-03 두 공정 비교
- UC-04 설비 비교
- UC-05 다중 조건 비교
- UC-06 차이 발생 조건 탐색
- UC-07 개선 전후 검증
- UC-08 변수 관계
- UC-09 영향도
- UC-10 이상 데이터
- UC-11 불량 원인
- UC-12 공정조건 영향
- UC-13 규격 대비 공정 판단
- UC-14 불량 현상
- UC-15 개선 효과 종합 판단

Autonomy:
- Guided: UC-01~04
- Assisted: UC-05~10
- Agentic: UC-11~15

Benchmark:
UC-03, UC-05, UC-07, UC-11, UC-15

---

## 26. Visualization

SVG를 핵심 출력 형식으로 한다.

주요 그래프:
- Histogram
- Box Plot
- Scatter Plot
- Bar Chart
- Line Chart
- Pareto
- Normal Probability Plot
- Residual Plot
- Interaction Plot
- Mean Plot
- Confidence Interval Plot

제조 grouping:
- Line
- Machine
- Model
- Shift
- Operator
- Date/Time
- Process Condition

---

## 27. Interpretation Architecture

```text
Statistical Result
       ↓
Decision Rule
       ↓
Interpretation Template
       ↓
Manufacturing Context
       ↓
Natural Language
```

LLM은 결과를 자연스럽고 상황에 맞게 설명하는 역할을 추가한다.

설명 수준:
- Level 1 현장 사용자
- Level 2 엔지니어
- Level 3 통계 전문가

---

## 28. Report

기본 구조:
1. 분석 목적
2. 데이터 정보
3. 분석 방법
4. 주요 통계량
5. 그래프
6. 검정 결과
7. 쉬운 해석
8. 제조 현장 해석
9. 주의사항
10. 권장 추가 분석

출력:
SVG / PNG / PDF / HTML / Excel / Markdown

---

## 29. Core UX Principles

1. 통계 용어보다 현장 용어를 먼저 보여준다.
2. 한 화면에 하나의 판단을 요구한다.
3. P-value보다 그래프를 먼저 보여준다.
4. 숫자보다 차이를 보여준다.
5. 결론과 근거를 분리한다.
6. 통계적 판단과 제조적 판단을 구분한다.
7. 모든 분석에는 실제 제조 사례를 연결한다.
8. AI가 말한 내용과 실제 통계 결과를 구분한다.
9. 사용자는 언제든 Manual Mode로 돌아갈 수 있다.
10. AI가 실패해도 분석 작업은 중단되지 않아야 한다.

---

## 30. Security / Privacy / Reliability

현재 기본 방향:

### Privacy
- 대용량 raw data를 필요 이상으로 LLM에 전송하지 않는다.
- LLM에는 구조화된 Dataset Context와 필요한 결과 metadata를 우선 전달한다.
- 민감 데이터 전송 여부를 정책으로 통제한다.
- Private/Local LLM을 사용할 수 있도록 Provider abstraction을 유지한다.

### Reliability
분리 처리:
- LLM timeout
- retry
- provider failure
- invalid response
- schema validation failure
- tool failure
- statistical engine failure

LLM failure가 발생해도:

> **Manual Analysis는 계속 사용할 수 있어야 한다.**

### Reproducibility
기록:
- dataset/version
- analysis method
- hypothesis
- assumptions
- test statistic
- p-value
- confidence interval
- effect size
- software/tool version
- timestamp

---

## 31. Development Architecture

논리 구조:

```text
manufacturing-stat-agent/
├── app/
├── agent/
├── state/
├── schemas/
├── tools/
├── statistics/
├── rules/
├── data/
├── llm/
├── knowledge/
├── evaluation/
├── tests/
└── config/
```

기본 철학:

> **Contract First → Deterministic Engine → Rule Engine → Agent → Evaluation → UI**

단, 현재 단계에서는 최종 Contract보다 먼저 **Product UX & Operating Architecture**를 확정한다.

---

## 32. Revised Development Sequence

### Step 26 — Product UX & Operating Architecture
- Home
- Manual / Guided / AI Assist / Agent Mode
- AI ON/OFF
- Manual ↔ AI 전환
- Chat + Analysis Workspace
- Analysis Trace
- Result / Evidence 화면
- AI 실행/중단/재개
- 오류 UI
- 승인/거부 UI
- 세션 재개

### Step 27 — App ↔ LLM / AI Gateway Architecture
- LLM 호출 시점
- API 구조
- Provider abstraction
- model selection
- context assembly
- tool calling
- timeout
- retry
- fallback
- token/cost control
- audit logging

### Step 28 — Data Privacy / Security / Reliability
- raw data 전송
- 민감정보 처리
- local vs cloud
- private/company LLM
- encryption
- access control
- audit
- retention

### Step 29 — Schema Contract
- ProblemModel
- DatasetContext
- AnalysisPlan
- ToolCall
- ToolResult
- Finding
- Evidence
- Hypothesis
- Confounder
- NextAction
- FinalDecision

### Step 30 — Final MVP Product Specification
IA, UX, 기능, architecture, data model, LLM, rule, evaluation, security, report, MVP scope, acceptance criteria를 통합한다.

---

## 33. Current Open Design Decisions

### Product / UX
- AI ON/OFF의 정확한 위치
- AI 실행 버튼 명칭
- AI/Manual 화면 전환
- Agent 실행 중 사용자 개입 수준
- 취소/일시정지 정책
- 세션 재개
- Evidence 상세 수준

### LLM
- 기본 Provider
- Provider 선택 권한
- model selection 정책
- cloud LLM 전송 정책
- private/local LLM 지원 범위
- context window
- streaming UI

### Security
- local-first vs cloud-first
- encryption
- authentication
- authorization
- audit log
- data retention

### Agent
- 자율 실행 한계
- 사용자 승인 필수 단계
- 최대 analysis loop
- NBA scoring 상세
- stop 조건 상세

### Statistics
- MVP Welch 기본값 여부
- assumption failure 처리
- outlier 처리
- missing data 처리
- effect size 표준
- multiple testing 정책

이 항목들은 다음 단계에서 하나씩 의사결정한다.

---

## 34. Design Decision Log

### DD-001
**Decision:** LLM 없이도 앱은 완전히 사용할 수 있어야 한다.  
**Reason:** 독립성 및 통계 신뢰성 확보.  
**Status:** CONFIRMED

### DD-002
**Decision:** Manual과 AI는 동일한 deterministic Statistical Engine을 공유한다.  
**Reason:** 재현성과 결과 일관성.  
**Status:** CONFIRMED

### DD-003
**Decision:** LLM은 Statistical Calculator가 아니다.  
**Reason:** 통계 계산 신뢰성 확보.  
**Status:** CONFIRMED

### DD-004
**Decision:** LLM은 optional intelligence layer다.  
**Reason:** 단순 분석에는 AI가 불필요하고 비용/복잡도를 줄일 수 있음.  
**Status:** CONFIRMED

### DD-005
**Decision:** AI UI는 Chat-only가 아니라 Chat + Analysis Workspace로 설계한다.  
**Reason:** 대화와 분석 결과를 연결해야 함.  
**Status:** DIRECTIONALLY CONFIRMED

### DD-006
**Decision:** LLM 호출 앞에 AI Gateway를 둔다.  
**Reason:** provider, security, retry, context, tool calling을 중앙 관리.  
**Status:** DIRECTIONALLY CONFIRMED

### DD-007
**Decision:** LLM의 분석 제안은 Tool / Rule / State를 통해 검증한다.  
**Reason:** hallucination 및 잘못된 통계 판단 방지.  
**Status:** CONFIRMED

### DD-008
**Decision:** 관찰자료의 association을 causal confirmation으로 표현하지 않는다.  
**Reason:** 원인분석 신뢰성 확보.  
**Status:** CONFIRMED

### DD-009
**Decision:** Statistical significance와 Manufacturing significance를 분리한다.  
**Reason:** 통계적 유의성과 실제 공정 영향은 동일하지 않음.  
**Status:** CONFIRMED

### DD-010
**Decision:** Analysis State를 application state로 명시적으로 저장한다.  
**Reason:** 세션 재개 및 Manual/AI interoperability 확보.  
**Status:** CONFIRMED

### DD-011
**Decision:** Golden Case는 데이터뿐 아니라 Agent Behavior Specification으로 사용한다.  
**Reason:** 전체 분석 pipeline 품질 평가.  
**Status:** CONFIRMED

### DD-012
**Decision:** Product UX와 LLM operating architecture를 schema 확정보다 먼저 설계한다.  
**Reason:** 실제 사용 흐름이 확정되어야 적절한 contract를 정의할 수 있음.  
**Status:** CONFIRMED

---

## 35. What Is Already Defined vs Not Yet Defined

### 이미 상당히 구체화
**Product**
- 포지셔닝
- 사용자
- 핵심 문제
- Navigator
- Wizard
- 통계 기능
- 그래프
- 결과 해석
- 보고서
- 제조 사례
- MVP

**Statistical Architecture**
- deterministic engine
- tool layer
- rule engine
- result validation
- effect size
- assumption handling 방향

**Agent**
- state machine
- problem model
- analysis plan
- findings
- evidence
- hypotheses
- confounders
- NBA
- stop conditions

**Evaluation**
- Golden Case
- evaluation domains
- critical fail
- UC-03 vertical slice

### 상세 설계 필요
가장 중요한 미확정 영역:

> **실제 사용자가 앱과 AI를 어떻게 오가며 분석하는가**

특히:
1. AI ON/OFF
2. AI 실행 방식
3. AI 실행 버튼
4. Chat + Workspace
5. Agent 진행 화면
6. 사용자 승인
7. AI 중단
8. Manual 복귀
9. 오류 처리
10. 세션 저장/복귀
11. LLM data transfer
12. provider selection
13. privacy/security
14. audit/cost

---

## 36. Recommended End-to-End Scenario

다음 단계에서 이 시나리오를 먼저 완성한다.

```text
① 앱 실행
   ↓
② 데이터 업로드
   ↓
③ 데이터 품질 확인
   ↓
④ Manual Analysis 선택
   ↓
⑤ Welch t-test 실행
   ↓
⑥ 결과 / 그래프 확인
   ↓
⑦ “AI 분석” 활성화
   ↓
⑧ AI가 기존 분석 상태 인식
   ↓
⑨ 원인 탐색 계획 제시
   ↓
⑩ 사용자 승인
   ↓
⑪ 다단계 분석 실행
   ↓
⑫ Finding / Evidence 생성
   ↓
⑬ 제조적 의미 해석
   ↓
⑭ Next Best Analysis 제안
   ↓
⑮ 사용자가 추가 분석 선택
   ↓
⑯ Manual 또는 AI로 계속 분석
   ↓
⑰ 최종 Decision
   ↓
⑱ Report
```

이 시나리오를 기준으로 UI, 상태, LLM 호출, Tool Call, Rule, Schema를 역으로 설계한다.

---

## 37. Final Product Definition

> **제조 현장용 통계분석 플랫폼**
>
> Statistical Analysis Engine을 중심으로 독립적인 수동 분석 기능을 제공하고, 필요할 때 LLM Agent를 선택적으로 연결하여 분석 방법 선택, 다단계 분석, 결과 해석, 원인 탐색, Evidence 관리 및 다음 분석을 지원하는 제조 데이터 분석 시스템.

핵심 구조:

> **Manual Statistical Analysis + Optional LLM Agent**

핵심 가치:

> **Easy Understanding + Reliable Statistics + Manufacturing Context + Evidence-based Decision**

최종 발전 방향:

```text
Manufacturing Data
        ↓
Data Quality
        ↓
Problem Understanding
        ↓
Statistical Analysis
        ↓
Visualization
        ↓
Statistical Result
        ↓
Finding
        ↓
Evidence
        ↓
Hypothesis / Confounder
        ↓
Manufacturing Judgment
        ↓
Next Best Analysis
        ↓
Improvement Action
```

---

## Appendix. Source Basis

이 노트는 사용자가 제공한 기존 `통계분석 앱 제작 기획서.md`와 2026-09-12까지의 프로젝트 설계 대화를 기준으로 작성한 **Baseline Design Note**다.

원본 기획서는 제품 포지셔닝, 현장 문제 중심 Navigator, 통계 기능, SVG Visualization, Data Quality, 결과 해석, Manufacturing Judgment, Report, Case Library, MVP, Deterministic Statistical Engine 및 Rule 기반 해석의 기반을 제공한다.

이후 설계에서는 이를 확장하여:
- Optional LLM
- Manual / Guided / Assisted / Agentic Mode
- AI Gateway
- Chat + Analysis Workspace
- Analysis Trace
- Manual ↔ AI interoperability
- Analysis State
- Finding / Evidence / Hypothesis / Confounder
- Next Best Analysis
- Causal Guardrail
- Golden Case Agent Evaluation

을 추가했다.

**이 문서는 최종 제품 사양이 아니다.** Open Design Decisions는 이후 단계에서 의사결정하기 위해 의도적으로 보존한다.

### Next Step

**Step 26 — Product UX & Operating Architecture**

우선 다음 실제 운영 경험을 상세 설계한다.

> **앱 실행 → 데이터 업로드 → 수동 분석 → AI ON → AI 대화 → AI 분석 → 사용자 승인 → 다단계 분석 → 수동 복귀 → 최종 판단 → 보고서**

그 후 App ↔ LLM Architecture, Security/Reliability, Schema Contract, Final MVP Specification 순으로 진행한다.
