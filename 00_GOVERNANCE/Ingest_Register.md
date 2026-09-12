---
id: DOC-007
title: Ingest_Register.md
type: research-note
status: active
owner: Ian
created: 2026-09-12
updated: 2026-09-12
---

# Ingest Register

- 처리 일시: 2026-09-12
- 기준: `git status --short --untracked-files=all`
- 상태: 새로 추가된 Vault 하위 파일을 로컬 인제스트 레지스트리에 반영 완료

## 처리 범위

다음은 현재 마운트된 워크스페이스에서 확인된 수정 파일과 신규/미추적 파일을 기준으로 한 인제스트 등록 목록입니다. 기준 명령은 `git status --short --untracked-files=all` 입니다.

### 1) 수정된 파일 (tracked changes)

#### Governance / Scope / Evidence / Data / Methods / Analysis / Results / Deliverables
- `00_GOVERNANCE/Change_Log.md`
- `01_SCOPE/Research_Questions.md`
- `02_EVIDENCE/Evidence_Gaps.md`
- `03_DATA/00_Raw_ReadOnly/README.md`
- `04_METHODS/Analysis_Plan.md`
- `04_METHODS/Field_Case_Library_Protocol.md`
- `04_METHODS/Navigator_Logic_Statistical_Audit.md`
- `04_METHODS/Research_Protocol.md`
- `05_EXECUTION/Execution_Log.csv`
- `06_ANALYSIS/README.md`
- `07_RESULTS/Limitations_and_Open_Questions.md`
- `08_DELIVERABLES/Analysis_Module_Library_and_Composition_Rules.md`
- `08_DELIVERABLES/Analysis_Package_Spec_KeyFactor.md`
- `08_DELIVERABLES/Analysis_Package_Spec_MSA.md`
- `08_DELIVERABLES/Analysis_Package_Spec_Maintenance.md`
- `08_DELIVERABLES/Analysis_Package_Spec_ProactiveComparison.md`
- `08_DELIVERABLES/Analysis_Package_Spec_Reliability.md`
- `08_DELIVERABLES/Analysis_Package_Spec_ResultVerification.md`
- `08_DELIVERABLES/Analysis_Package_Spec_RootCause.md`
- `08_DELIVERABLES/Analysis_Package_Spec_SafetyStock.md`
- `08_DELIVERABLES/Development_Guide_for_Claude_Code.md`
- `08_DELIVERABLES/Executive_Brief.md`
- `08_DELIVERABLES/Final_Report.md`
- `08_DELIVERABLES/GAP09_Interpretation_Template_Coverage_Matrix.md`
- `08_DELIVERABLES/MVP_Coverage_Matrix.md`
- `08_DELIVERABLES/Navigator_Design_Requirements.md`
- `08_DELIVERABLES/Navigator_Question_Flow.md`
- `08_DELIVERABLES/Research_Handoff_Package.md`
- `99_ARCHIVE/README.md`
- `Claude outputs/Development_Guide_for_Claude_Code.md`
- `통계분석 앱 제작 기획서.md`

### 2) 신규/미추적 파일 (new / untracked)

#### Root and governance docs
- `CLAUDE.md`
- `index.md`
- `LLM_wiki/index.md`
- `00_GOVERNANCE/Ingest_Register.md`
- `00_GOVERNANCE/LLM_Extension_Design_Guide.md`
- `00_GOVERNANCE/LLM_Security_Options_and_Decision.md`

#### Claude outputs
- `Claude outputs/1147-prism-mindmap-llmextention-gap-review.md`
- `Claude outputs/2210-통계분석앱-설계-검토-ClaudeCode-인터뷰-보완.md`
- `Claude outputs/_write_test.txt`

#### LLM_extention / 원본기획서
- `LLM_extention/00_원본기획서/통계분석 앱 제작 기획서.md`

#### LLM_extention / Use Case 정의
- `LLM_extention/01_개념정의_UseCase(Step1-4)/1. LLM 통합을 위한 개념 재정의.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/2. 제조현장 Use Case 정의 및 Agent Workflow 설계.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/3. LLM 확장 통계앱 기획을 위한 기본 설계.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/3.1 대표 Manufacturing Use Case 선정.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/3.2 Manufacturing Statistical Question Taxonomy.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/3.3 Use Case별 Agent Workflow 설계.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/3.4 Manufacturing Statistical Agent Decision Framework.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/3.5 Manufacturing Statistical Agent_Tool Architecture.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/3.6 Agent Memory and Analysis State Architecture.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/3.7 Manufacturing Statistical Agent UX Architecture.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/3.8 Manufacturing Statistical Agent Evaluation Framework.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/3.9 Manufacturing Statistical Agent 시나리오 대응 Architecture.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/4.1 Benchmark Scenario 정리.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/4.2 Use Case 02 공정 및 CTQ 분리 분석.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/4.3 Use Case-05 설비별 CTQ 분리 분석.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/4.4 Use Case-07 생산 전후 품질 영향 분석.md`
- `LLM_extention/01_개념정의_UseCase(Step1-4)/4.5 Use Case-11 불량 발생 원인 탐색 Agent.md`

#### LLM_extention / Agent Architecture
- `LLM_extention/02_Agent아키텍처(Step5-9)/5. LLM Agent 실전 구현 Architecture.md`
- `LLM_extention/02_Agent아키텍처(Step5-9)/6. Manufacturing Knowledge Architecture.md`
- `LLM_extention/02_Agent아키텍처(Step5-9)/7. Manufacturing Statistical Agent Prompt Architecture.md`
- `LLM_extention/02_Agent아키텍처(Step5-9)/8. Manufacturing Statistical Agent Brain Architecture.md`
- `LLM_extention/02_Agent아키텍처(Step5-9)/9. Golden Case 기반 Agent Evaluation Architecture.md`

#### LLM_extention / MVP 설계
- `LLM_extention/03_MVP설계_실행엔진(Step10-15)/10. 실제 MVP 개발 사항 정리.md`
- `LLM_extention/03_MVP설계_실행엔진(Step10-15)/11. 실제 Agent 실행 시나리오 설계.md`
- `LLM_extention/03_MVP설계_실행엔진(Step10-15)/12. Manufacturing Statistical Agent 실행 환경 설계.md`
- `LLM_extention/03_MVP설계_실행엔진(Step10-15)/13. Agent Data Contract and Interface 설계.md`
- `LLM_extention/03_MVP설계_실행엔진(Step10-15)/14. MVP technical Specification.md`
- `LLM_extention/03_MVP설계_실행엔진(Step10-15)/15. 실행 구조.md`

#### LLM_extention / Statistical Engine Tool
- `LLM_extention/04_StatisticalEngine_Tool(Step16-20)/16. Use Case-3 Golden Dataset and Data Contract.md`
- `LLM_extention/04_StatisticalEngine_Tool(Step16-20)/17. Statistical Engine 구현 개요.md`
- `LLM_extention/04_StatisticalEngine_Tool(Step16-20)/18. Tool Registry and Rule Engine.md`
- `LLM_extention/04_StatisticalEngine_Tool(Step16-20)/19. LLM Tool Calling and Agent Orchestrator.md`
- `LLM_extention/04_StatisticalEngine_Tool(Step16-20)/20. Next Best Analysis Engine.md`

#### LLM_extention / Golden Case
- `LLM_extention/05_GoldenCase_평가체계(Step21-24)/21. Golden Case 자동 평가 시스템.md`
- `LLM_extention/05_GoldenCase_평가체계(Step21-24)/22. Golden Case  템플릿 설계.md`
- `LLM_extention/05_GoldenCase_평가체계(Step21-24)/23. Golden Case-UC3-001 Synthetic Dataset 설계.md`
- `LLM_extention/05_GoldenCase_평가체계(Step21-24)/24. Golden Case-UC3-001 Execution Fixture.md`

#### LLM_extention / 제품 운영 설계
- `LLM_extention/06_제품운영설계(Step25-31)/25-1. 중간점검_LLM통합분석앱구현수립_수립전략.md`
- `LLM_extention/06_제품운영설계(Step25-31)/25-2. 중간점검2_설계서동기화Baseline제안.md`
- `LLM_extention/06_제품운영설계(Step25-31)/25-3. First Vertical Slice Technical Implementation.md`
- `LLM_extention/06_제품운영설계(Step25-31)/26. Product UX and Operating Architecture.md`
- `LLM_extention/06_제품운영설계(Step25-31)/27. App-LLM AI Gateway Architecture.md`
- `LLM_extention/06_제품운영설계(Step25-31)/28-1. 운영체제형태 및 모델선정 기준.md`
- `LLM_extention/06_제품운영설계(Step25-31)/28. Data Privacy Security Reliability.md`
- `LLM_extention/06_제품운영설계(Step25-31)/29. Web Application Operating Architecture.md`
- `LLM_extention/06_제품운영설계(Step25-31)/30. Schema Contract.md`
- `LLM_extention/06_제품운영설계(Step25-31)/31-1. 분산 구조 기준 및 보안요건.md`
- `LLM_extention/06_제품운영설계(Step25-31)/31-2. LLM 운영 아키텍처 정립 - 클라우드 사이드.md`
- `LLM_extention/06_제품운영설계(Step25-31)/31-3. 세션 관리 규칙 - 로컬 및 LLM 운영.md`
- `LLM_extention/06_제품운영설계(Step25-31)/31-4. 데이터 저장 관리 - 한국어.md`
- `LLM_extention/06_제품운영설계(Step25-31)/31. Final MVP Product Specification.md`

#### LLM_extention / Baseline and Archive
- `LLM_extention/08_기준문서_Baseline/manufacturing-statistical-agent-design-notes.md`
- `LLM_extention/09_ARCHIVE/README.md`
- `LLM_extention/09_ARCHIVE/[보류서] 4. 제조 Use Case별 Agent Scenario 설계.md`
- `LLM_extention/09_ARCHIVE/[완결] AI전문가_통합제안_요약.md`
- `LLM_extention/09_ARCHIVE/[완결] Gap_Analysis_Step1-7_검토.md`
- `LLM_extention/09_ARCHIVE/[완결] Gap_Analysis_Step8-25_검토.md`
- `LLM_extention/09_ARCHIVE/[추가] manufacturing-statistical-analysis-agent-progress-summary.md`
- `LLM_extention/CLAUDE.md`
- `LLM_extention/DD_Register.md`

## 인제스트 결과

- 분류 완료: 문서 메타데이터, 연구 문서, 설계 및 아키텍처 문서, 여정/기록 문서, 테스트 파일, 참고 자료
- 핵심 주제 확인: 제조현장 통계분석 앱의 설계 스펙, LLM 확장 구조, Agent 아키텍처, Golden Case 평가 체계, 제품 운영 설계
- 다음 단계 권장: 핵심 문서 우선 선정 → 상위 인덱스/링크 정리 → 중복 문서 숨김/분류 → 운영/보안 의사결정 문서와 연결

## 메모

- 이 레지스트리는 로컬 워크스페이스 기준의 인제스트 추적용으로 작성되었으며, 수정 파일과 신규 파일을 모두 포함합니다.
- 외부 데이터베이스나 별도 ingestion API가 이 환경에 노출되어 있지 않아, 워크스페이스 내부에서의 인제스트 처리 기록으로 남깁니다.
- 신규 문서는 인덱스 문서와 링크 연결을 함께 갱신해야 하며, 후속 검토 시 중복 문서는 아카이브 또는 기준 문서로 정리하는 것을 권장합니다.
