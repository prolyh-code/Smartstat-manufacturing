---
id: CLAUDE-001
title: Claude Project Guide
type: research-note
status: active
owner: Ian
created: 2026-09-12
updated: 2026-09-12
---

# Claude Project Guide

## 목적

이 프로젝트는 제조 현장용 통계 분석 앱의 연구, 설계, 검증, 개발 지침을 Obsidian Vault 기반으로 관리하기 위한 최상위 개발 규칙 문서입니다.

## 핵심 원칙

1. 원천 자료는 불변으로 유지한다.
2. Wiki와 Runtime 지식 계층을 구분한다.
3. 파일은 메타데이터와 링크를 가지고 관리한다.
4. 분석 로직은 결정론적 엔진을 우선한다.
5. LLM은 계산 대신 이해, 계획, 해석, 경로 제안을 담당한다.
6. 데이터 보안과 기밀성을 우선한다.

## 메타데이터 규칙

모든 문서는 다음 정보를 포함한다.

- id
- title
- type
- status
- owner
- created
- updated

권장 형식:

```yaml
---
id: DOC-001
title: 문서 제목
type: research-note
status: draft
owner: Ian
created: 2026-09-12
updated: 2026-09-12
---
```

## 링크 규칙

- 문서 간 연계는 상대 경로 링크를 사용한다.
- 원천 문서와 해석 문서를 분리한다.
- 인덱스 문서가 최상위 탐색 경로 역할을 수행한다.
- 파일명은 의미를 담아 짓고, 필요 시 디렉터리별 카테고리를 유지한다.

## 주요 탐색 경로

- 프로젝트 인덱스: [index.md](index.md)
- 거버넌스: [00_GOVERNANCE/Change_Log.md](00_GOVERNANCE/Change_Log.md)
- 근거: [02_EVIDENCE/Source_Register.csv](02_EVIDENCE/Source_Register.csv)
- 산출물: [08_DELIVERABLES/Development_Guide_for_Claude_Code.md](08_DELIVERABLES/Development_Guide_for_Claude_Code.md)
- LLM Wiki: [LLM_wiki/index.md](LLM_wiki/index.md)

## LLM 확장 정책

- LLM은 계산을 대신하지 않는다.
- 사용자 질문을 구조화하고, 분석 계획을 수립한다.
- 통계 검정과 결과 산출은 deterministic engine이 수행한다.
- 민감 데이터는 외부 API에 그대로 전달하지 않는다.
- 사내 격리형 또는 온프레미스 모델을 우선한다.

## 프로젝트 참고 문서

- [README.md](README.md)
- [08_DELIVERABLES/Development_Guide_for_Claude_Code.md](08_DELIVERABLES/Development_Guide_for_Claude_Code.md)
- [00_GOVERNANCE/LLM_Extension_Design_Guide.md](00_GOVERNANCE/LLM_Extension_Design_Guide.md)
- [00_GOVERNANCE/LLM_Security_Options_and_Decision.md](00_GOVERNANCE/LLM_Security_Options_and_Decision.md)
- [00_GOVERNANCE/Ingest_Register.md](00_GOVERNANCE/Ingest_Register.md)
