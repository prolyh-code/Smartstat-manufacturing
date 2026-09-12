---
id: DOC-070
title: manufacturing-statistical-analysis-agent-progress-summary.md
type: research-note
status: active
owner: Ian
created: 2026-09-12
updated: 2026-09-12
---

# 제조 통계분석 앱 --- LLM Agent 전환 핵심 정리 및 Step 15 실행 명세

## 0. 문서 목적

이 문서는 지금까지의 대화를 장기적인 개발 기준으로 압축한 **Working
Specification**이다.

기존 「통계분석 앱 제작 기획서.md」의 핵심 개념을 유지하면서, 단순
통계분석 앱에서 **Manufacturing Statistical Analysis Agent**로
발전시키기 위한 설계 결정과 다음 개발 단계(Step 15)를 정리한다.

------------------------------------------------------------------------

# 1. 제품의 핵심 정의

### 기존 방향

> 제조 현장의 질문을 통계적 판단으로 바꿔주는 통계 의사결정 도구

기존 기획은 통계 계산 자체보다 다음을 핵심 가치로 정의했다.

-   어떤 상황에서 어떤 분석을 선택하는가
-   분석 결과를 어떻게 이해하는가
-   제조 현장에서 무엇을 판단하는가
-   추가로 무엇을 확인해야 하는가

### 현재 재정의

> **Manufacturing Statistical Analysis Agent**

**제조 현장의 질문을 이해하고, 적절한 통계 분석을 계획·실행하며, 결과를
근거 기반의 제조 판단과 다음 행동으로 연결하는 AI Agent**

핵심 변화:

``` text
기존
질문 → 분석 선택 → 계산 → 그래프 → 해석

현재
질문
 ↓
문제 이해
 ↓
Problem Model
 ↓
분석 계획
 ↓
Rule/Guardrail
 ↓
Statistical Tool
 ↓
결과 검증
 ↓
Finding/Evidence
 ↓
제조 해석
 ↓
Next Best Analysis
 ↓
Decision / Improvement
```

------------------------------------------------------------------------

# 2. 절대 유지해야 할 핵심 원칙

## 2.1 LLM은 통계 계산을 하지 않는다

LLM은 통계적 수치를 직접 계산하지 않는다.

``` text
LLM
→ 무엇을 분석해야 하는가 판단

Rule Engine
→ 분석 조건 검증

Statistical Engine
→ 실제 계산

LLM
→ 결과 해석 및 설명
```

기존 기획에서도 결정론적 Statistical Engine을 사용하고, LLM은 계산
결과를 설명하는 구조를 핵심 신뢰성 전략으로 정의했다.

## 2.2 통계적 판단과 제조적 판단을 분리한다

예:

> p \< 0.05

는 통계적 판단이다.

> 이 차이가 실제 제조 품질에 중요한 수준인가?

는 제조적 판단이다.

두 판단을 같은 것으로 취급하지 않는다.

## 2.3 연관성과 인과관계를 구분한다

예:

> M4 설비의 불량률이 높다.

→ 관찰된 현상

> M4와 불량률 사이에 통계적 연관성이 있다.

→ 통계적 근거

> M4가 불량 증가의 원인이다.

→ 관찰자료만으로는 확정할 수 없음

Agent는 근거 수준을 넘어선 인과적 표현을 하지 않는다.

## 2.4 분석 사실은 LLM Memory에만 저장하지 않는다

모든 핵심 분석 사실은 Application State에 저장한다.

``` text
AnalysisSession
 ├─ ProblemModel
 ├─ DatasetContext
 ├─ AnalysisPlan
 ├─ AnalysisHistory
 ├─ Findings
 ├─ Evidence
 ├─ Hypotheses
 ├─ Confounders
 ├─ NextActions
 └─ FinalDecision
```

------------------------------------------------------------------------

# 3. Agent의 핵심 구조

권장 구조는 **Hybrid: Single Orchestrator + Specialized Modules**이다.

``` text
User
 ↓
Agent Orchestrator
 ├─ Intent / Problem Reasoning
 ├─ Analysis Planner
 ├─ Manufacturing Reasoner
 └─ Interpreter
 ↓
Rule / Guardrail
 ↓
Tool Layer
 ↓
Deterministic Statistical Engine
 ↓
Result Validation
 ↓
Analysis State
 ↓
Finding / Evidence
 ↓
Next Best Analysis
```

Multi-Agent 구조는 MVP에서 사용하지 않는다.

------------------------------------------------------------------------

# 4. Agent의 핵심 역할

Agent의 역할은 다음 4개로 압축한다.

### Understand

사용자의 제조 질문을 이해하고 문제를 구조화한다.

### Plan

필요한 데이터와 분석 순서를 계획한다.

### Explain

통계 결과를 이해하기 쉬운 언어와 제조 관점으로 설명한다.

### Explore

추가 분석, 원인 후보, 다음 행동을 탐색한다.

통계적 신뢰성은 별도의 구조가 담당한다.

``` text
Validate → Calculate → Verify
```

------------------------------------------------------------------------

# 5. 제조 통계 질문 Taxonomy

8개 문제 유형:

1.  CURRENT_STATE_DIAGNOSIS --- 현상 파악
2.  TARGET_COMPARISON --- 기준/목표 대비 판단
3.  GROUP_COMPARISON --- 두 그룹 비교
4.  MULTI_GROUP_COMPARISON --- 다중 그룹 비교
5.  IMPROVEMENT_VERIFICATION --- 개선 전후 검증
6.  RELATIONSHIP_ANALYSIS --- 관계/영향 분석
7.  ROOT_CAUSE_EXPLORATION --- 이상/원인 탐색
8.  PROCESS_JUDGMENT --- 공정 판단/개선

통계 방법을 사용자에게 먼저 노출하지 않는다.

``` text
제조 질문
→ 문제 유형
→ 분석 계획
→ 통계 방법
```

------------------------------------------------------------------------

# 6. 핵심 Use Case

MVP 및 Agent 검증용 대표 사례:

-   UC-01 공정 상태 진단
-   UC-03 두 공정 비교
-   UC-05 다중 설비 비교
-   UC-07 개선 전후 검증
-   UC-11 불량 증가 원인 탐색

특히 Agent의 대표 시나리오는:

> **"최근 토크 불량이 증가한 원인을 찾아줘."**

이며, 이 사례에서 다음 능력을 검증한다.

-   불량률 계산
-   시간 추세
-   설비 비교
-   Model 비교
-   Shift/Operator 비교
-   연관성 검정
-   Confounding 탐색
-   가설 갱신
-   추가 분석 추천
-   인과관계 과장 방지

------------------------------------------------------------------------

# 7. Agent State 핵심 객체

## AnalysisSession

``` text
session_id
status
user_question
problem_model
dataset_context
analysis_plan
analysis_history
findings
hypotheses
confounders
evidence
next_actions
final_decision
```

## ProblemModel

``` text
problem_type
response
quality_event
objective
candidate_factors
time_scope
relationship
```

## DatasetContext

``` text
dataset_id
dataset_version
rows
variables
variable_types
quality_status
missing_rate
scope
```

원본 데이터 전체를 LLM Context에 넣지 않는다.

## Finding

관찰/분석 결과의 의미.

``` text
finding_id
statement
type
evidence_level
source_analysis
direction
confidence
```

## Evidence

근거의 강도를 관리한다.

``` text
E0 No evidence
E1 Observed pattern
E2 Statistical association/difference
E3 Repeated / cross-validated candidate
E4 Experimental / improvement verification
```

## Hypothesis

``` text
UNTESTED
SUPPORTED
STRENGTHENED
WEAKENED
REJECTED
CONFIRMED
```

단, 관찰자료의 단순 통계적 유의성만으로 CONFIRMED를 부여하지 않는다.

------------------------------------------------------------------------

# 8. Tool Architecture

LLM이 직접 Python 함수를 자유롭게 실행하지 않는다.

``` text
LLM
 ↓
Tool Registry
 ↓
Rule Engine
 ↓
Tool
 ↓
Statistical Engine
```

## MVP Tool

### Data

-   profile_data
-   check_data_quality
-   summarize_variables
-   detect_missing
-   detect_duplicates
-   detect_outliers

### EDA

-   descriptive_statistics
-   distribution_analysis
-   trend_analysis
-   outlier_analysis

### Comparison

-   one_sample_t_test
-   two_sample_t_test
-   welch_t_test
-   paired_t_test
-   anova
-   welch_anova
-   tukey_posthoc
-   games_howell

### Relationship

-   pearson_correlation
-   spearman_correlation
-   simple_regression

### Manufacturing

-   defect_rate
-   group_defect_rate

### Visualization

-   histogram
-   box_plot
-   scatter_plot
-   comparison_plot
-   trend_chart

------------------------------------------------------------------------

# 9. Tool Result Contract

모든 분석 Tool은 구조화된 결과를 반환한다.

``` text
Tool Metadata
 ↓
Input
 ↓
Statistical Result
 ↓
Diagnostics
 ↓
Warnings
 ↓
Validation Status
```

예:

``` json
{
  "tool_name": "welch_t_test",
  "tool_version": "1.0",
  "dataset_id": "DS001",
  "mean_a": 163.2,
  "mean_b": 166.1,
  "mean_difference": -2.9,
  "statistic": 2.41,
  "p_value": 0.018,
  "confidence_interval": [-5.3, -0.5],
  "effect_size": 0.42,
  "sample_size_a": 85,
  "sample_size_b": 92,
  "warnings": []
}
```

------------------------------------------------------------------------

# 10. Rule / Guardrail

4종류의 Guard를 둔다.

### Data Guard

-   형식
-   결측
-   중복
-   표본 수
-   단위
-   변수 유형

### Method Guard

-   문제 유형
-   변수 유형
-   그룹 수
-   독립/paired
-   분석 구조

### Assumption Guard

-   정규성
-   등분산성
-   독립성
-   선형성
-   잔차

### Interpretation Guard

-   p-value 오해 방지
-   효과크기 확인
-   통계적/실무적 유의성 분리
-   상관관계 → 인과관계 금지
-   관찰자료 → 원인 확정 금지

------------------------------------------------------------------------

# 11. Knowledge Architecture

Knowledge는 세 계층으로 분리한다.

``` text
Statistical Knowledge
→ 어떻게 분석하는가

Manufacturing Knowledge
→ 무엇을 봐야 하는가

Company Knowledge
→ 우리 회사에서는 어떻게 판단하는가
```

기존 Raw-Wiki / LLM-Wiki 구조를 Agent Knowledge의 기반으로 활용할 수
있다.

``` text
Raw Source
 ↓
Raw-Wiki
 ↓
LLM-Wiki
 ↓
Agent Knowledge
 ↓
RAG
```

Knowledge와 Tool은 역할이 다르다.

``` text
RAG
→ 지식 검색

Tool
→ 데이터 계산

State
→ 현재 분석 사실
```

------------------------------------------------------------------------

# 12. Prompt Architecture

Prompt를 하나로 만들지 않는다.

``` text
Core System Prompt
Statistical Policy
Manufacturing Reasoning
Tool Use Policy
Knowledge Retrieval Policy
Agent State
Current Task
User Message
```

중요한 통계 규칙은 Prompt에만 넣지 않고 Rule Engine으로 구현한다.

``` text
Prompt
= 행동/추론 지침

Tool Schema
= 능력

Rule Engine
= 강제 제약

State
= 사실

RAG
= 지식
```

------------------------------------------------------------------------

# 13. MVP 기술 스택 권고

소프트웨어 비전문가의 유지보수성과 통계/AI 생태계를 고려하여 **Python
중심**으로 개발한다.

  영역            권고
  --------------- -----------------------
  Backend         Python
  API             FastAPI
  Data            pandas
  Statistics      SciPy / statsmodels
  Schema          Pydantic
  LLM             API 기반 LLM
  State           SQLite → PostgreSQL
  Knowledge       Markdown + RAG
  Visualization   SVG
  Excel           pandas / openpyxl
  Test            pytest
  UI 초기         Streamlit
  개발            VS Code + Claude Code

초기부터 React + Node + Python + 여러 DB를 동시에 구성하지 않는다.

------------------------------------------------------------------------

# 14. MVP 기능 범위

## 포함

### Data

-   Excel
-   CSV
-   Preview
-   Data Profiling
-   Missing
-   Duplicate
-   Basic Outlier
-   Variable Type Detection

### Statistics

-   Descriptive
-   Histogram
-   Box Plot
-   Scatter Plot
-   1-sample t-test
-   2-sample t-test
-   Welch t-test
-   Paired t-test
-   ANOVA
-   Welch ANOVA
-   Tukey
-   Games-Howell
-   Pearson
-   Spearman
-   Simple Regression

### Agent

-   Intent
-   Problem Model
-   Analysis Plan
-   Tool Calling
-   Rule Validation
-   Result Validation
-   Interpretation
-   Finding
-   Evidence
-   Next Analysis
-   Stop

### Evaluation

-   Golden Dataset
-   Golden Case
-   자동 결과 검증
-   Tool-call 검증
-   Critical Error 검증

------------------------------------------------------------------------

# 15. MVP에서 제외

초기에는 다음을 제외한다.

-   실시간 MES
-   SPC
-   Capability
-   PCA
-   DOE
-   Optimization
-   Advanced ML
-   완전 자율 Root Cause Analysis
-   Multi-Agent
-   복잡한 Enterprise 권한관리
-   모바일 앱

이들은 Phase 2/3 확장 대상으로 유지한다.

------------------------------------------------------------------------

# 16. 개발 철학

최종 개발 원칙:

> **Contract First → Deterministic Engine → Rule Engine → Agent →
> Evaluation**

개발 순서:

1.  Project Skeleton
2.  Data Engine
3.  Statistical Engine
4.  Tool Contract
5.  Rule Engine
6.  State
7.  Problem Model
8.  Analysis Planner
9.  LLM Tool Calling
10. Result Validator
11. Interpretation
12. Finding / Evidence
13. Next Best Analysis
14. Visualization
15. Report
16. Golden Case
17. UI
18. Regression Test

UI보다 내부 계약과 분석 구조를 먼저 안정화한다.

------------------------------------------------------------------------

# 17. 첫 번째 Vertical Slice

첫 완성 시나리오:

> **"A라인과 B라인의 토크 차이가 있는지 확인해줘."**

전체 흐름:

``` text
Excel Upload
 ↓
Data Profile
 ↓
User Question
 ↓
Intent Recognition
 ↓
Problem Model
 ↓
Analysis Plan
 ↓
Rule Engine
 ↓
Welch/t-test
 ↓
Box Plot
 ↓
Result Validation
 ↓
Finding
 ↓
Evidence
 ↓
Manufacturing Interpretation
 ↓
Next Analysis
```

이 한 사례를 끝까지 연결하면 Agent의 핵심 골격이 검증된다.

------------------------------------------------------------------------

# 18. Step 15 --- Agent Execution Specification

## 18.1 사용자 입력

``` text
A라인과 B라인의 토크 차이가 있는지 확인해줘.
```

## 18.2 예상 Problem Model

``` json
{
  "problem_type": "GROUP_COMPARISON",
  "response": {
    "name": "Torque",
    "data_type": "continuous"
  },
  "factor": "Line",
  "groups": ["A", "B"],
  "objective": "difference_detection"
}
```

## 18.3 Agent가 먼저 확인할 것

1.  Torque가 수치형인가?
2.  Line이 그룹 변수인가?
3.  그룹이 정확히 2개인가?
4.  A/B 데이터가 독립적인가?
5.  Pair ID가 필요한 구조인가?
6.  결측이 있는가?
7.  표본 수가 충분한가?
8.  단위가 동일한가?
9.  분포 및 이상치에 문제가 있는가?
10. 등분산 여부가 어떤가?

## 18.4 Analysis Plan

``` text
Node 1: Data Quality
Node 2: Group Structure
Node 3: Descriptive Statistics
Node 4: Distribution
Node 5: Variance Assessment
Node 6: Two Group Comparison
Node 7: Effect Size
Node 8: Confidence Interval
Node 9: Manufacturing Significance
Node 10: Confounding Check
Node 11: Next Best Analysis
```

## 18.5 Method Selection

``` text
Independent + equal variance
→ Student t-test

Independent + unequal variance
→ Welch t-test

Paired
→ Paired t-test

Strong non-normality / 조건 위반
→ 적절한 비모수 검정 검토
```

## 18.6 Result Validation

Tool 결과에 대해:

-   statistic 존재
-   p-value 범위 0\~1
-   CI 논리
-   effect size 존재
-   sample size 일치
-   결측 반영
-   assumption 결과 존재
-   계산 오류 없음

을 확인한다.

## 18.7 Finding 생성

예:

``` text
A라인의 평균 토크가 B라인보다 낮다.
```

Finding에는 반드시 source analysis ID를 연결한다.

## 18.8 Evidence 생성

예:

``` text
E2 — Statistical difference
```

단순 관찰이면 E1이다.

## 18.9 Manufacturing Interpretation

최종 설명은 다음 순서로 한다.

``` text
Conclusion
Evidence
Statistical Judgment
Manufacturing Judgment
Limitation
Next Action
```

예:

> A라인과 B라인의 토크 평균에는 통계적으로 유의한 차이가 있습니다. 다만
> 이 차이가 실제 조립 품질에 중요한 수준인지는 규격, 목표값, 효과크기와
> 함께 판단해야 합니다. 또한 라인별 Model 구성 차이가 있다면 Line 효과와
> Model 효과가 혼재할 수 있으므로 동일 Model 기준의 추가 비교가
> 필요합니다.

------------------------------------------------------------------------

# 19. Step 15의 핵심 산출물

Step 15가 끝났다고 판단하려면 다음 8개가 존재해야 한다.

1.  `ProblemModel` 실제 schema
2.  `AnalysisPlan` 실제 schema
3.  `ToolCall` 실제 schema
4.  `ToolResult` 실제 schema
5.  `Finding` 실제 schema
6.  `Evidence` 실제 schema
7.  UC-03 실행 흐름
8.  UC-03 Golden Case

즉, 문서상의 Agent가 아니라 **실제로 한 번 실행 가능한 Agent
Contract**가 완성되어야 한다.

------------------------------------------------------------------------

# 20. Step 16으로 넘어갈 준비

Step 15 이후에는 다음 순서가 적절하다.

### Step 16

**UC-03 실제 데이터 계약 및 Golden Dataset 제작**

### Step 17

**Statistical Engine 실제 구현**

### Step 18

**Tool Registry + Rule Engine 구현**

### Step 19

**LLM Tool Calling + Orchestrator 구현**

### Step 20

**Finding / Evidence / Next Best Analysis 구현**

### Step 21

**Golden Case 자동평가**

### Step 22

**첫 UI 및 Agent 대화 UX**

------------------------------------------------------------------------

# 21. 최종 제품 구조

최종적으로 이 프로젝트는 다음과 같은 제품으로 발전한다.

``` text
             Manufacturing User
                     ↓
              Natural Language
                     ↓
             Manufacturing Agent
                     ↓
          Problem Understanding
                     ↓
             Analysis Planning
                     ↓
            Rule / Guardrail
                     ↓
               Tool Calling
                     ↓
          Deterministic Statistics
                     ↓
            Result Validation
                     ↓
           Finding / Evidence
                     ↓
        Manufacturing Interpretation
                     ↓
           Next Best Analysis
                     ↓
        Engineering Decision
                     ↓
          Improvement Action
```

핵심 차별화는 **LLM 자체가 아니라 제조 문제를 통계적 분석과 의사결정으로
연결하는 구조**이다.

------------------------------------------------------------------------

# 22. 프로젝트의 핵심 문장

> **"통계를 계산하는 AI가 아니라, 제조 현장의 질문을 통계적 근거와 제조
> 의사결정으로 연결하는 AI Agent."**

그리고 개발의 핵심 원칙은:

> **LLM의 유연성 + Schema의 구조화 + Rule의 강제성 + Tool의 결정론적
> 계산 + State의 지속성 + Knowledge의 제조 맥락**

이다.
