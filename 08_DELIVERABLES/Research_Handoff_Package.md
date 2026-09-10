---
id: DELIV-HANDOFF-001
title: Research Handoff Package — PRISM 통계분석 Add-on
status: 최종(G7 Translation 완료, 지속 갱신 중)
version: v2.0 (2026-09-10, PRISM Add-on/무AI/분석패키지/모듈화 프레이밍 전면 반영 — v1.0의 "SmartStat Manufacturing 독립 앱" 프레이밍을 대체)
---

# Research Handoff Package — PRISM 통계분석 Add-on

> 이전(v1.0) 중간 스냅샷을 대체합니다. 연구를 이어받거나 Claude Code로 개발에 착수할 때 이 문서에서 시작하십시오.

## 범위, 버전, 수신자, 승인 상태

scope_version v0.2. 수신자: Ian(단독). 승인 상태: **G0(헌장) in_review — 여전히 리뷰어 미지정, Ian 승인 필요**. G6(Adjudication)·G7(Translation)은 본 세션에서 self-adjudicated로 완료(누적 갱신 중).

**핵심 전제(개발 착수 전 반드시 확인)**: (1) 이 산출물은 독립 앱이 아니라 **PRISM에 추가할 Add-on**입니다. (2) **Add-on 런타임에는 AI/LLM이 없습니다** — 모든 해석은 사전 설계된 결정론적 규칙/템플릿입니다. (3) PRISM의 기술 스택·데이터 스키마·API 연동 방식(GAP-08)은 이 연구에서 의도적으로 다루지 않았으며, Claude Code 개발 착수 시 Ian이 최종 지침서·앱 폴더와 함께 직접 전달할 예정입니다(DEC-009).

## 산출물 목록 (2026-09-10, RUN-022 기준)

```
README.md
통계분석 앱 제작 기획서.md (SRC-000)
00_GOVERNANCE/Research_Charter.md(G1~G11), Project_Status.csv, Decision_Log.csv(DEC-001~013), Change_Log.md
01_SCOPE/Research_Questions.md (RQ-01~12, H1~H6)
02_EVIDENCE/Source_Register.csv(SRC-000~152), Claim_Evidence_Matrix.csv(CLM-01~46),
           Evidence_Gaps.md(GAP-01~11), Case_Library_Register.csv(CASE-001~008)
03_DATA/Data_Dictionary.csv, Lineage_Register.csv, 00_Raw_ReadOnly/README.md (실데이터 없음)
04_METHODS/Research_Protocol.md, Analysis_Plan.md, Field_Case_Library_Protocol.md,
           Navigator_Logic_Statistical_Audit.md (3단계 자체검토)
05_EXECUTION/Gate_Dashboard.csv, Execution_Log.csv(RUN-001~022)
06_ANALYSIS/navigator_risk_simulation.py, navigator_risk_simulation_results.json
07_RESULTS/Findings_Register.csv(FND-01~11), Limitations_and_Open_Questions.md(갱신 필요)
08_DELIVERABLES/
   Executive_Brief.md, Final_Report.md, MVP_Coverage_Matrix.md(갱신 필요),
   Navigator_Design_Requirements.md(NAV-REQ-01~08),
   Navigator_Question_Flow.md(v2 — 스무고개 결정트리 + §8 드라이런 검증),
   Analysis_Module_Library_and_Composition_Rules.md(모듈 카탈로그 ~29개, §2.1~2.9 + 조합규칙),
   Analysis_Package_Spec_{ResultVerification,RootCause,KeyFactor,MSA,Maintenance,
                          ProactiveComparison,Reliability,SafetyStock}.md (분석 패키지 8종),
   GAP09_Interpretation_Template_Coverage_Matrix.md,
   Research_Handoff_Package.md(본 문서)
99_ARCHIVE/README.md
```

## 데이터 스냅샷과 접근/보존 규칙

실 CTQ 데이터 없음. `06_ANALYSIS/`의 시뮬레이션 데이터는 합성(synthetic)이며 seed=20260909로 재현 가능. 향후 실 데이터 확보 시 `03_DATA/00_Raw_ReadOnly/`에 익명화 후 보관.

## 방법, 코드, 설정, 환경, 실행 지침

- 문헌 스캔: WebSearch/WebFetch (검색어·URL은 Execution_Log.csv 및 Source_Register.csv 참조).
- 현장 인터뷰: Claude-Ian 1:1 대화형(CASE-001), critical incident + probing 기법(Field_Case_Library_Protocol.md).
- Navigator 위험 시뮬레이션: `python3 06_ANALYSIS/navigator_risk_simulation.py` (numpy/scipy 필요, 실행시간 수 초, seed 고정으로 재현 가능).
- Navigator v2 검증: 실행 가능한 코드가 아니라 Claude의 셀프 드라이런(9개 시나리오, `Navigator_Question_Flow.md` §8)이며, 대체 통제수단임을 항상 명시.
- 분석 패키지 개발 시: `Analysis_Module_Library_and_Composition_Rules.md` §2(모듈 카탈로그)와 §3(조합 표기법)을 먼저 읽고, 각 `Analysis_Package_Spec_*.md`의 §3(E2E 흐름)·§4(해석 템플릿)를 그대로 구현 대상 스펙으로 사용. §4의 "슬롯 유형 판정"(배타적 핵심분류/접두경고/목록형 조립)을 지키면 전수 커버리지가 구조적으로 보장됨(GAP-09 방법론).

## 게이트 및 결정 이력

`05_EXECUTION/Gate_Dashboard.csv`, `00_GOVERNANCE/Decision_Log.csv` 참조. 핵심 결정: DEC-001(워크스페이스 구조) ~ DEC-007(연구 조기 완료·G6/G7 진행) ~ **DEC-008(PRISM Add-on/무AI/분석패키지로 프레이밍 전환 — 가장 중요한 정정)** ~ DEC-009(GAP-08을 개발단계로 명시적 이관) ~ DEC-010(모듈 라이브러리 방식으로 전환) ~ DEC-011(Navigator UX 재설계, 스무고개 방식) ~ DEC-012(신뢰성·안전재고 착수 결정, Ian이 Claude 권장안을 채택하지 않음) ~ DEC-013(GAP-09를 구조적 완전성 기준으로 closed).

## 발견, 한계, 실패, 미해결 가정

`07_RESULTS/Findings_Register.csv`(FND-01~11, 갱신 필요), `Limitations_and_Open_Questions.md`(갱신 필요) 참조. 가장 중요한 미해결 항목: **DBT-03 — 실제 조립현장 니즈가 CASE-001(1건)에 그쳐 일반화 불가**; **DBT-04 — Navigator 위험 시뮬레이션이 합성데이터 기준이라 실측 검증 전**; **[신규] GAP-08 — PRISM 기술통합은 의도적 미결**; **[신규] GAP-10/11 잔여 — 신뢰성 교체주기 최적화·안전재고 근거보강 미완**; **[신규] GAP-02/05 — 해석 템플릿·Navigator 문구의 실사용자 이해도 미검증**.

## 다음 액션, 담당자, 일정

1. **(제품결정, 최우선)** `08_DELIVERABLES/Navigator_Design_Requirements.md`의 NAV-REQ-01~08 채택 여부, 특히 Welch 기본값화(NAV-REQ-02)의 Phase1 편입 여부, 8개 패키지의 Phase1/2/3 배치 — Ian.
2. **(선택)** 여건이 되면 타 제품군 인터뷰 1~2건 추가로 CASE-001의 일반화 근거 보강 — Ian.
3. **(중기)** 프로토타입 제작 → 실사용자 테스트(GAP-01,02,05) → Navigator v2 문구와 8개 패키지 해석 템플릿 문구를 함께 실제 검증 → FND-07/H5(적응마찰 가설)와 대조.
4. **(중기)** 실 CTQ 데이터 확보 시 Navigator 시뮬레이션 결과(정규성/등분산/자기상관 위반 빈도)를 실측치로 재검증.
5. **(중기)** GAP-10(SRC-148 본문 확보 또는 대체문헌으로 교체주기 최적화 완성)·GAP-11(재고관리 교과서 근거보강) 해소.
6. **(장기)** 독립 통계전문가 확보 시 GAP-07(waived) 해제하고 Navigator 감사 전체 재검토.
7. **(Claude Code 개발 착수 시, 최우선)** GAP-08 해소 — Ian이 PRISM 기술 스택·데이터 스키마·API 연동방식을 최종 지침서·앱 폴더와 함께 직접 전달.
8. **(미착수)** `MVP_Coverage_Matrix.md`·`Limitations_and_Open_Questions.md`·`Findings_Register.csv`를 8개 패키지·G9~G11 기준으로 갱신 — 이번 세션에서 Final_Report/Executive_Brief/본 문서만 갱신했고, 나머지 3개 파일은 다음 세션 과제로 남음.

## 정정, 철회, 전파, 보관, 롤백

발견이 반증되면 Decision_Log.csv에 사유를 기록하고 해당 claim_status를 `contested` 또는 `rejected`로 갱신합니다(행을 삭제하지 않음). 워크스페이스 전체는 `F:\obsidian\vault\통계분석앱\`에 보관되며 Obsidian Vault의 버전 이력이 곧 보관 이력입니다.
