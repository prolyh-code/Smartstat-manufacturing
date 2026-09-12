---
id: DOC-008
title: LLM_Extension_Design_Guide.md
type: research-note
status: active
owner: Ian
created: 2026-09-12
updated: 2026-09-12
---

# LLM Extension Design Guide

- 처리 일시: 2026-09-12
- 범위: `LLM_extention/` 신규 문서군 및 기존 PRISM Add-on 설계와의 정합성 검토
- 상태: 단계적 정리 완료, 다음 액션으로 이어짐

## 1. 핵심 결론

LLM을 도입하는 방향은 기존 PRISM/SmartStat의 핵심 철학을 유지하면서 계층을 확장하는 방식이어야 합니다.

핵심 원칙은 다음과 같습니다.

1. LLM은 통계 계산을 수행하지 않는다.
2. LLM은 사용자 질문 이해, 분석 계획 수립, 결과 해석, 대화형 후속 분석을 담당한다.
3. 실제 계산, 가정 검정, 효과크기 산출, 규칙 기반 판정은 deterministic engine이 수행한다.
4. LLM 확장은 기존 App을 대체하는 것이 아니라, 기존 분석 엔진 위의 지능형 계층을 추가하는 구조로 설계한다.

## 2. 설계 구조

### 2.1 시스템 구성

- 사용자 인터페이스
- 데이터 입력/검증
- Rule Engine
- Statistical Engine
- Visualization Engine
- Interpretation Engine
- LLM Agent / Orchestrator
- Knowledge Base
- Company Knowledge

### 2.2 관계

```
사용자 질문
  ↓
LLM: intent understanding
  ↓
LLM: analysis plan proposal
  ↓
Rule Engine: feasibility check
  ↓
Statistical Engine: deterministic calculation
  ↓
Result validation
  ↓
LLM: contextual interpretation
  ↓
제조 인사이트 / 후속 분석 제안
```

## 3. Knowledge Architecture

LLM이 참조할 지식을 3계층으로 구분하는 것이 중요합니다.

### 3.1 Statistical Knowledge
- 검정 선택 조건
- 가정 검정
- 효과크기
- CI / p-value / 회귀 판정
- 통계적 한계와 사용 조건

### 3.2 Manufacturing Knowledge
- 공정/설비/모델/공정변수
- CTQ와 불량 정의
- 제품/라인별 품질 특성
- 제조 맥락 기반 원인 탐색

### 3.3 Company Knowledge
- 사내 규격/기준
- 머신/설비 일정표
- 품질 정책
- 사내 용어와 관행

이 세 가지를 섞어버리면 Agent가 통계적으로는 합리적이더라도 제조 맥락에서 부정확해질 수 있습니다.

## 4. 최소 보장 규칙

다음은 LLM 확장 설계에서 반드시 유지해야 할 최소 보장 규칙입니다.

- LLM은 계산이 아니라 조율과 설명을 담당한다.
- 모든 통계 판정은 deterministic engine에서 수행한다.
- 다중 비교 시 보정 절차를 포함한다.
- 불량 여부와 같은 이분형 응답은 적절한 categorical analysis로 처리한다.
- 교란요인 발견 시 단순 비교를 우회하고 보정 또는 층화분석을 적용한다.
- 데이터 민감 정보는 LLM context와 분리한다.
- 외부 API 사용 시 사내 보안 정책을 우선해야 한다.

## 5. 발견된 핵심 위험

다음 항목은 LLM 확장 기획에서 우선 보완해야 한다.

1. 데이터 기밀성 문제
   - 현장 데이터가 외부 LLM provider로 전송될 때의 리스크
   - 온프레미스 또는 비공개 LLM 구조를 검토해야 함

2. 다중 비교 보정 부재
   - 여러 후보 요인 동시 스크리닝 시 false positive 위험

3. 이분형 반응변수 Tool 부재
   - proportion test, chi-square, Fisher exact test 필요

4. 교란요인 통제의 일반화 부족
   - stratified analysis만으로는 한계

## 6. 다음 순차 액션

### 단계 1: 데이터 보안/기밀성 결론 확정
- 외부 LLM 허용 여부를 결정한다.
- 허용 시, 데이터 마스킹/익명화/온프레미스 옵션을 정의한다.

### 단계 2: 통계적 안전장치 강화
- 다중 비교 보정 절차를 규칙에 추가한다.
- 이분형 반응 변수를 처리할 Tool 목록을 보완한다.
- 교란요인 통제 도구를 정의한다.

### 단계 3: 구현 아키텍처 정제
- Agent, Rule Engine, Statistical Engine, Knowledge Base 간 경계 명확화
- Tool call 구조와 fallback 정책 정의

### 단계 4: 검증 및 평가
- Golden Case 검증
- 도메인 종단 테스트
- 보안 및 품질 관점 운영 정책 수립

## 7. 참고 자료

- `LLM_extention/1. LLM 통합을 위한 개념 재정의.md`
- `LLM_extention/3. LLM 확장 통계앱 기획을 위한 기본 설계.md`
- `LLM_extention/6. Manufacturing Knowledge Architecture.md`
- `LLM_extention/Gap_Analysis_Step1-7_검토.md`
- `08_DELIVERABLES/Development_Guide_for_Claude_Code.md`

## 8. 요약

LLM 확장은 “분석을 대신하는 기능”이 아니라 “분석이 더 잘 진행되도록 지원하는 지능 계층”으로 설계해야 합니다. 이 원칙을 유지하면, 기존 PRISM Add-on의 결정론적 구조와 충돌하지 않으면서도 현대적인 대화형 분석 경험을 더할 수 있습니다.
