---
id: DOC-SUMMARY-001
title: Documentation Summary
type: summary-note
status: active
owner: Ian
created: 2026-09-12
updated: 2026-09-12
---

# Documentation Summary

## 목적

이 문서는 원본 문서 본문을 변경하지 않고, 워크스페이스의 문서 메타데이터와 링크 관계를 요약해 탐색성과 관리 효율을 높이기 위한 보조 문서입니다.

## 문서 계층

### 1. 프로젝트 인덱스 계층
- [../index.md](../index.md) — 전체 문서 탐색용 인덱스
- [../README.md](../README.md) — 연구 목적과 프로젝트 제약
- [../CLAUDE.md](../CLAUDE.md) — 프로젝트 운영 규칙

### 2. 거버넌스 계층
- [../00_GOVERNANCE/Ingest_Register.md](../00_GOVERNANCE/Ingest_Register.md) — 로컬 인제스트 기록
- [../00_GOVERNANCE/Document_Metadata_Register.csv](../00_GOVERNANCE/Document_Metadata_Register.csv) — 본문 수정 없이 보관되는 메타데이터 레지스터
- [../00_GOVERNANCE/LLM_Extension_Design_Guide.md](../00_GOVERNANCE/LLM_Extension_Design_Guide.md) — LLM 확장 설계 원칙
- [../00_GOVERNANCE/LLM_Security_Options_and_Decision.md](../00_GOVERNANCE/LLM_Security_Options_and_Decision.md) — 보안 우선 의사결정 기록

### 3. 산출물 계층
- [Development_Guide_for_Claude_Code.md](Development_Guide_for_Claude_Code.md) — 구현용 지침서
- [Final_Report.md](Final_Report.md) — 최종 요약 보고서
- [Research_Handoff_Package.md](Research_Handoff_Package.md) — 이관용 패키지

### 4. LLM 확장 계층
- [../LLM_wiki/index.md](../LLM_wiki/index.md) — LLM 관련 지식 인덱스
- [../LLM_extention/CLAUDE.md](../LLM_extention/CLAUDE.md) — 로컬 LLM 프로젝트 안내
- [../LLM_extention/DD_Register.md](../LLM_extention/DD_Register.md) — 설계결정 유효/폐기 상태

## 링크 및 메타데이터 기준

- 원본 문서 본문은 그대로 유지한다.
- 메타데이터는 관리용 파일에 별도 기록한다.
- 링크는 실제 파일 위치를 기준으로 연결한다.
- 신규 문서 추가 시, 인덱스와 메타데이터 레지스터를 함께 정리한다.

## 요약

현재 워크스페이스는 다음 4개의 문서 계층으로 관리되고 있다.

1. 프로젝트 인덱스 계층
2. 거버넌스 및 의사결정 계층
3. 구현 산출물 계층
4. LLM 확장 및 지식 계층

이 구조는 문서 본문을 수정하지 않고도, 탐색, 메타데이터 관리, 링크 유지, 요약 문서 생성이 가능하도록 설계되어 있다.

## 다음 액션

- 신규 문서 추가 시 파일 경로와 메타데이터를 레지스터에 반영
- 문서별 링크 깨짐 여부를 정기 점검
- 요약본과 인덱스 간 중복을 줄이는 방향으로 갱신
