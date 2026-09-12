---
id: DOC-038
title: 1147-prism-mindmap-llmextention-gap-review.md
type: research-note
status: active
owner: Ian
created: 2026-09-12
updated: 2026-09-12
---

# 통계분석 앱(PRISM/SmartStat) — 계층 마인드맵 제작 + LLM_extention 기획 Step1~7 검토 + 대화메모 저장 지침 재정비

**세션 날짜**: 2026-09-11 ~ 2026-09-12 (Cowork, "제조 현장용 통계분석 앱 개발" 프로젝트)
**이전 메모**: [00_GOVERNANCE/Change_Log.md](../00_GOVERNANCE/Change_Log.md) — 이 메모는 SecureVault(PWW Manager) 앱 작업과는 별개로, 제조현장 CTQ 통계분석 앱 PRISM/SmartStat 프로젝트에 대한 세션 전환 기록으로 재정리했다. 지난 9/8 이후 이 프로젝트 볼트에는 RUN-019~030까지 다수의 작업이 쌓였는데, 이 메모에서는 그중 **아직 개인 메모로 남기지 않은 최근 두 건(마인드맵, LLM_extention 검토)과 이번에 새로 발견·정비한 메모 저장 문제**만 기록함. RUN-019~028의 세부내용은 볼트의 `00_GOVERNANCE/Change_Log.md`가 원본.

## 이번 세션에서 한 일

1. 통계분석 계층 마인드맵 제작 (RUN-029, 2026-09-11)
2. LLM_extention 기획(LLM 확장 Agent 설계) Step 1~7 전체 통독 및 갭 분석 (RUN-030, 2026-09-12)
3. "대화 내용 자동 메모" 최상위 지침이 9/8 이후 실행되지 않은 원인 진단 및 재정비 (이 폴더 자체의 문제)

## 1. 통계분석 계층 마인드맵 (RUN-029)

- Ian이 작성한 `Development_Guide_for_Claude_Code.md`(§3~6: 아키텍처, 원자 모듈 카탈로그, 8개 분석 패키지, Navigator 질문흐름)를 근거로 3갈래 계층 마인드맵을 제작.
- 구조: ① Navigator(스무고개 Q1-A~D + 6개 핵심 패키지 경로), ② 분석 패키지(품질/공정 표준 6개 vs 도메인 확장 2개), ③ 원자 모듈 카탈로그(§2.1~2.9).
- **형식 결정**: 새 연구·근거를 생성하지 않는 순수 시각화 산출물이라 볼트에 md로 추가하지 않고 **Claude Artifact(HTML, 자체 tidy-tree 레이아웃 + SVG)로 발행** — `https://claude.ai/code/artifact/521edf29-012c-438d-a1cf-43356f73c097` (비공개, Ian 계정).
- **버그 발견·수정**: 발행 전 Playwright로 로컬 스크린샷(라이트/다크/모바일) 1회 검수 중 리프 노드 pill 높이(`LEAF_H`)가 실제 pill 높이보다 작아 인접 노드가 겹치는 레이아웃 버그 발견 → `LEAF_H` 30→44, 그룹/브랜치 간격도 비례 조정 후 재검증 완료.
- Navigator 가지에는 이전 세션(RUN-028)에서 발견한 DBT-09(신뢰성·안전재고 패키지가 Navigator에 라우팅되지 않는 격차)을 경고색 노드로 시각화해, 지침서의 텍스트 경고가 다이어그램에서도 드러나도록 함.
- 볼트 반영: Execution_Log.csv RUN-029, Change_Log.md, claude.ai Project 문서(`claude/research-workspace-status.md`) 모두 갱신 완료.

## 2. LLM_extention 기획 Step 1~7 검토 (RUN-030)

**배경**: `LLM_extention/` 폴더는 현재의(런타임에 AI 없는) PRISM Add-on을 향후 "제조 통계 LLM Agent"로 확장하기 위한 별도 기획 문서군(1, 2, 3, 3.1~3.9, 4, 4.1~4.5, 5, 6, 7 계열, 총 18개 파일 통독). Ian의 요청: "7. Manufacturing Statistical Agent Prompt Architecture까지 읽고 누락/보완 필요 사항을 점검해달라."

**전체 평가**: 설계 철학(LLM은 계산하지 않는다, 교란요인 인식, Evidence Level E0~E4, Stop Condition)은 일관되고 견고함.

**최우선 보완 필요(A) 4건**:
1. **A-1 (가장 심각)** — LLM에 전달되는 제조 데이터(불량률, 설비명, 생산량 등)의 기밀성 문제. 기존 PRISM이 "런타임에 AI 없음"으로 설계된 이유가 바로 이 리스크 차단이었을 가능성이 높은데, 이번 확장 기획은 그 전제를 뒤집으면서도 대안(온프레미스 LLM, 데이터 마스킹 등)을 전혀 논의하지 않음.
2. **A-2** — 여러 후보 요인(Machine/Model/Shift/Operator 등)을 동시에 스크리닝할 때 다중비교(multiple comparison) 보정이 없어 우연한 유의성(false positive) 위험.
3. **A-3** — 불량여부(이분형) 반응변수 비교에 필요한 proportion test/chi-square가 서술(4.5, 7장)에서는 명시적으로 요구되지만, 실제 Tool Architecture 목록(5-6, 5-19 MVP 범위)에는 빠져 있는 **문서 내 사실 확인 가능한 불일치**.
4. **A-4** — 교란요인 통제가 일반화된 Tool(ANCOVA, 층화분석 등) 없이 UC-11처럼 사례별 임시방편(수동으로 "동일 Model 내 재비교")에만 의존.

**중요 보완(B)**: Statistical Engine 자체 검증/회귀테스트 전략 부재, 측정시스템분석(MSA) 게이트 미통합, 시계열 자기상관/변화점탐지 방법론 미정의, Evidence 하향조정 정책 부재, Data Guard 구체 판단기준(결측률 임계값 등) 부재.

**운영·거버넌스 보완(C)**: LLM API 비용/지연/장애 대응 정책, 사용자 실시간 정정이 세션 Evidence에 반영되는 절차, 모델 교체 시 Golden Case 재검증 연결, 고위험 판단의 human-in-the-loop 승인체계.

**산출물**: `LLM_extention/Gap_Analysis_Step1-7_검토.md`(신규, 볼트 커밋 완료), Ian에게 파일로 전달. Execution_Log.csv RUN-030, Change_Log.md, Project 문서 모두 갱신.

**다음 결정 필요**: Ian이 Step 8(Multi-Agent 구조 검토)로 계속 진행하길 원하면, **A-1(데이터 기밀성) 문제에 대한 결론을 먼저 내리는 것을 권장**해둔 상태(아직 Ian의 판단 대기).

## 3. Claude_chat_Memo 자동저장 지침 재정비

**증상**: Ian이 "대화 내용을 노트해달라고 최상위 지침으로 설정했는데 이 폴더(`N:\개인\AI\Claude_chat_Memo\`)에 9/8까지 내용만 저장되어 있다"고 문의.

**진단**: 확인해보니 이 지침이 실제로 지속(durable)되는 곳이 어디에도 없었음 — (1) claude.ai Project의 custom instructions는 비어 있음, (2) 연결된 볼트 폴더들에 CLAUDE.md류 설정파일 없음, (3) 계정 전체 메모리(memory)에도 해당 지침 없음. **결론: "최상위 지침"이 아니라 9/8 무렵의 어느 대화에서 1회 요청 → 그 세션이 그때 한 번 실행 → 이후 새 세션들은 그 요청을 알 방법이 전혀 없어 자연히 중단된 것으로 추정.**

**조치**: Claude의 계정 전체 memory(모든 Claude 세션/surface에서 공유되는 유일한 지속 저장소)에 이 지침을 기록 — "매 대화 후 주요 내용을 `N:\개인\AI\Claude_chat_Memo\` 하위 월/일 폴더에 저장할 것"(이 프로젝트가 bound된 Project 하위 경로에 저장되어, 이 프로젝트 관련 세션에서는 자동 참조됨. 단, 다른 프로젝트/세션에서는 별도로 기억되지 않을 수 있음 — 필요시 재확인).

**남은 제약**: 폴더 접근은 매 세션·매 기기연결마다 재승인이 필요한 구조. 이번 세션에서는 Ian이 방금 이 폴더를 직접 연결해줘서 이 메모 작성이 가능했음.

**기존 메모 폴더 구조 확인**: `2026/09/07/`, `2026/09/08/`에 파일명 `HHMM-주제슬러그.md` 형식으로 3~4건씩 저장되어 있던 것을 확인 — 이번 메모도 동일 형식 유지.

## 다음에 이어갈 것

1. Ian의 A-1(LLM_extention 데이터 기밀성) 판단 확인 후 Step 8 검토 여부 결정
2. Execution_Log.csv 기존 행 5개(RUN-005/008/010/011/012) CSV 컬럼정합성 수정 (PRISM 트랙 잔여과제, 오래전부터 미해결)
3. Navigator의 신뢰성/안전재고 라우팅 공백(DBT-09) 처리 방식 확정 — 개발착수 시 Ian과 결정 필요
4. 이 메모 저장 지침이 실제로 "다음 세션에서도" 잘 이어지는지 한 번 더 확인 (memory 기록이 project-scoped라 다른 세션/프로젝트에서 인식되는지 검증 필요)

## 참고

- 이 프로젝트(PRISM/SmartStat)의 원본 작업이력은 Obsidian 볼트 `00_GOVERNANCE/Change_Log.md`, `05_EXECUTION/Execution_Log.csv`가 1차 자료이며, 이 메모는 Ian 개인용 요약본.
- claude.ai Project 문서 `claude/research-workspace-status.md`에도 동일 취지의 현황 요약이 있음(세션 간 연속성용, 이 메모보다 더 상세).
