---
id: DOC-006
title: Change_Log.md
type: research-note
status: active
owner: Ian
created: 2026-09-12
updated: 2026-09-12
---

# Change Log

## 2026-09-09 — 워크스페이스 초기화 및 P0~P2 착수

- engineer-research-lifecycle 스킬 기반 연구 워크스페이스(00_GOVERNANCE~99_ARCHIVE) 생성.
- 기획서(SRC-000)를 소스로 등록하고 연구 헌장(Research_Charter.md) 초안 작성.
- 연구질문 10건, 가설 4건 초안(Research_Questions.md) 작성.
- 1차 웹 문헌 스캔 8건 수행, Source_Register/Claim_Evidence_Matrix 작성.
- 사용자 지시(세션 중 추가)에 따라 "실제 가전 조립 현장 적용사례 조사"를 헌장 목표 G7로 추가하고, 조립라인 SPC 사례 문헌 2건(SRC-109, SRC-110)을 추가 조사.
- 실제 현장조사(관찰·인터뷰) 실행을 위한 `Field_Case_Library_Protocol.md` 작성(미실행, 프로토콜만 존재).
- 아직 승인·검증된 empirical finding은 없음 — 모든 claim은 draft/hypothesis 단계이며, 특히 실제 현장 니즈(CLM-09)는 `missing` 상태.

## 2026-09-09 (계속) — 현장 인터뷰 착수 준비

- 사용자 지시에 따라 GAP-06(실제 조립현장 조사)을 Ian-Claude 1:1 대화형 인터뷰로 실행하기로 확정(DEC-003).
- 인터뷰 착수 전 요구공학 인터뷰 기법 문헌 2건(SRC-111, SRC-112) 조사, critical incident/laddering/probing 원칙을 `Field_Case_Library_Protocol.md`에 반영해 질문 가이드를 확정판으로 개정.
- CLM-09 상태를 `missing` → `in_progress`로, G1b 게이트를 `planned` → `in_progress`로 갱신.
- 본 세션에서 Round 1부터 인터뷰 질문을 시작함.

## 2026-09-09 (계속) — 인터뷰 세션1 완료 및 방향 전환

- Ian과의 1:1 인터뷰(에어컨 전체공정 담당)로 CASE-001 확보: CTQ(냉매충전량·체결토크)의 관리도/공정능력분석은 이미 사내 웹앱으로 자동화되어 있음(baseline 갱신, FND-06); 실제 pain point는 "상황인식 부재"와 "습관적 판단의 편의성"(FND-07), "사후 반응적 비교만 존재"(FND-08)로 확인됨.
- 사용자가 추가 인터뷰의 한계효용이 낮다고 판단(DEC-004)하여, 소모성 부품 수명/교체주기(Weibull 신뢰성분석), 안전재고 관리 등 인접 통계영역의 외부 사례를 조사(SRC-114~116)하고 `Case_Library_Register.csv`(신규 파일)에 CASE-002~003으로 기록.
- `Case_Library_Register.csv` 신규 생성 — CASE-001(1차 현장), CASE-002~003(문헌 기반 후보) 수록.
- Research_Questions.md에 RQ-11, H5(적응 마찰 가설), H6(가치인식 확장 가설) 추가.
- G1b 게이트 상태를 `planned`→`in_progress`로, CLM-09를 `missing`→`observed(1건)`으로 갱신했으나, 표본이 1건·1인이므로 일반화는 여전히 금지.

## 2026-09-09 (계속) — 산업공통 Case Library 확장 (헌장목표 G8 신설)

- 사용자가 타 제품군 추가 인터뷰 대신, 산업 공통으로 잘 알려진 통계활용 사례를 5대 주제(MSA, 원인분석 방법론, 핵심요인분석, 결과검증 방법, 유지관리 방안)로 조사할 것을 명시적으로 지시(DEC-005).
- 문헌 스캔 9건(SRC-117~125) 수행, `Case_Library_Register.csv`에 CASE-004~008 추가 — 각각 CASE-001(에어컨 툴교환/파라미터조정 사례)과의 정성적 대응관계를 함께 기록.
- Claim_Evidence_Matrix에 CLM-16~20 추가(모두 문헌수준 지지, 사내 정량검증 전).
- Research_Charter.md에 목표 G8 신설, 목표번호(G1~G8)와 실행게이트번호(Gate_Dashboard.csv의 G0~G8)가 별개 체계임을 명시하는 주의문 추가(표기 혼동 방지).
- Research_Questions.md에 RQ-12 추가.
- 핵심 시사점: CASE-005(원인분석)·CASE-006(핵심요인분석)·CASE-007(결과검증)·CASE-008(유지관리)이 모두 CASE-001의 개별 요소(툴교환=비정형 원인분석, 파라미터 조정=OFAT 핵심요인탐색, "괜찮아 보임"=검증생략, 재발=유지관리 부재)와 대응되어, 5대 주제가 서로 분리된 게 아니라 CASE-001 하나의 사례 안에 이미 다 들어있던 하나의 흐름(원인분석→핵심요인규명→개선→검증→유지관리)이라는 것이 드러남. 이는 Analysis Navigator를 단일 검정 선택 도구가 아니라 이 흐름 전체를 안내하는 구조로 설계해야 함을 시사(향후 헌장/Navigator 설계 리뷰 시 반영 필요).

## 2026-09-09 (계속) — Navigator 결정로직 통계이론 자체감사 (헌장목표 G2 진전)

- 사용자의 "연구를 계속 진행해달라"는 요청에 따라, 지금까지 가장 진척이 더뎠던 헌장목표 G2(Navigator 로직의 통계이론적 검증)를 진행.
- `04_METHODS/Navigator_Logic_Statistical_Audit.md` 신규 작성 — 기획서 §7·§28의 결정트리를 표준 t-test/ANOVA 전제조건과 대조해 6개 오매핑 위험구간 식별: (1) 정규성·등분산 확인이 검정선택보다 나중에 배치된 순서역전, (2) 표본수 하한 부재, (3) 등분산 위반 시 Welch's t-test 자동전환 로직 불명확, (4) ANOVA 트리도 동일한 순서 문제, (5) 다중비교 보정 안내 부재, (6) 비모수 대안이 전부 Phase2로 밀려 MVP에서 정규성 위반 시 대안 없음.
- 이 감사는 **Claude 자신의 이론적 추론([추론] 표기)이며 통계 전문가의 독립 검증을 거치지 않았다** — GAP-07로 별도 등록, RQ-02·FND-09·CLM-21·G4(Method freeze) 게이트에 반영하되 모두 `observed(자체감사)` 상태로만 표시하고 `reviewed`/`accepted`로 승격하지 않음.
- CASE-001(에어컨 인터뷰)의 "몇 개 조립해보고 유사하면 종료"가 위험 1·2(순서역전·표본수 부재)의 실제 발현 사례임을 연결.

## 2026-09-09 (계속) — 독립 전문가 리뷰 waived, Claude 2차 자기비판적 재검토 수행

- Ian이 "통계 전문가가 없어 곤란하니 그 부분은 클로드가 대신하라"고 명시적으로 지시(DEC-006).
- GAP-07(Navigator 감사 독립검증)을 `waived`로 전환하고, 대체 통제수단으로 Claude가 RUN-007 감사 결과를 스스로 비판적으로 재검토(Review Pass 2)하는 방식을 채택 — engineer-research-lifecycle 스킬의 `waived`(시한부 예외 + 대체통제) 정의에 따름.
- 재검토로 보강된 내용: (1) 표본수 위험에 중심극한정리(CLT)의 완화효과 반영, (2) 등분산 위반 대응을 "감지 후 분기"에서 "Welch's t-test 기본값화"로 더 단순하고 강한 권고로 수정(SRC-127), (3) 효과크기(Cohen's d)가 등분산을 가정한다는 정합성 문제 명시, (4) **신규 위험 7 — 독립성(자기상관) 가정이 1차 감사에서 누락되었음을 발견**: 시간순으로 연속 수집되는 조립라인 데이터는 자기상관이 흔해(SRC-128,129) 표준 t-test/ANOVA의 유효표본수를 부풀릴 위험이 있으며, 이는 spc-profile.md의 V5(시간/드리프트)와 연결됨.
- **중요한 원칙 유지**: 이 재검토는 `reviewed(self-reviewed)` 수준까지만 인정되며, `accepted`(오너 승인)로 스스로 승격하지 않았다 — 이는 Ian의 몫으로 명시적으로 남겨둠. 모든 관련 파일(Findings_Register, Claim_Evidence_Matrix, Gate_Dashboard, Evidence_Gaps)에 "독립검증이 아니다"라는 한계를 반복 명시.

## 2026-09-09 (계속) — Navigator 위험 몬테카를로 시뮬레이션 정량검증 (RUN-009) 및 설계요구사항 초안

- 사용자 지시("남아 있는 연구 과제는 순차적으로 연속해서 진행, 자동 승인")에 따라, Review Pass 2에서 식별된 7개 위험 중 수치로 검증 가능한 4개를 합성데이터 기반 몬테카를로 시뮬레이션(numpy/scipy 벡터화, seed=20260909, 반복 20,000회)으로 정량화했다: `06_ANALYSIS/navigator_risk_simulation.py`.
- **Scenario A(등분산위반)**: worst-case(소표본n=5·큰분산 vs 대표본n=15·작은분산)에서 Student's t 1종오류율 22.3%(명목5%의 약4.5배) vs Welch's t 5.6% — Welch 기본값화(CLM-22)를 정량적으로 뒷받침. 최초 설계는 반대 방향(보수적 결과)으로 배치되어 있었음을 자체 검토로 발견하고 수정 후 재실행(RUN-009 deviation 필드에 기록) — 이 자기수정 과정을 시뮬레이션 재현성·투명성의 근거로 보존.
- **Scenario B(CLT견고성)**: 지수분포(우측왜도) 데이터에서 n=5~50 전 구간에서 1종오류율 4.06~5.12%로 명목값 근접 — 놓쳤던 점1을 지지하되 이 특정 왜도수준에 한정된 결과임을 명시.
- **Scenario C(다중비교)**: 3그룹 반복 pairwise t-test의 familywise 오류율 12.5% vs ANOVA 5.0% — 위험5를 정량적으로 확인.
- **Scenario D(자기상관, 신규위험7)**: AR(1) rho 0→0.9 증가 시 1종오류율 4.7%→63.8% — 4개 시나리오 중 가장 큰 효과크기로, 자기상관을 Navigator의 최우선 위험으로 재분류할 것을 제안.
- `Navigator_Logic_Statistical_Audit.md`에 "Review Pass 3 — 몬테카를로 시뮬레이션 정량검증" 섹션 추가, frontmatter status를 self-reviewed+simulation-quantified로 갱신.
- 시뮬레이션 결과를 `Source_Register.csv`(SRC-130), `Claim_Evidence_Matrix.csv`(CLM-24~27), `Findings_Register.csv`(FND-10), `Execution_Log.csv`(RUN-009), `Gate_Dashboard.csv`(G4), `Project_Status.csv`(WP4), `Evidence_Gaps.md`(GAP-03), `Research_Questions.md`(RQ-02)에 반영.
- 7개 위험(및 시뮬레이션 정량화 결과)을 실행 가능한 설계 요구사항으로 번역한 `08_DELIVERABLES/Navigator_Design_Requirements.md`(NAV-REQ-01~08) 신규 작성 — 최우선 3건: 순서역전 수정, Welch 기본값화, 자기상관 체크 질문 추가.
- **한계 재확인**: 이 모든 결과는 합성데이터 기반이며 실제 CTQ 데이터가 아니다. 여전히 `reviewed(self-reviewed)` 수준이며 `accepted`는 Ian의 몫이다.

## 2026-09-10 — MVP(Phase1) 커버리지 매트릭스 (RQ-07 답변) 및 구조적 공백 2건 발견

- 사용자 지시("다음 연구를 진행해 주세요")에 따라 RQ-07(Phase1 MVP 범위가 실제 현장 커버리지에 충분한가)을 진행. 기획서(SRC-000) §32(Case Library)·§34(Phase1)·§35(Phase2)·§45(개발우선순위) 원문을 `Case_Library_Register.csv`의 CASE-001~008과 1:1 대조하여 `08_DELIVERABLES/MVP_Coverage_Matrix.md` 작성(RUN-010).
- **결과**: 8개 사례 중 완전커버 0건, 부분커버 3건(CASE-001/005/007 — 검정 도구는 Phase1에 있으나 Navigator가 "언제 이 검정을 쓰는지" 안내하지 않음), 미커버 5건(CASE-002/003/004/006/008 — 필요 기법이 Phase2~3).
- **신규 구조적 발견(FND-11)**: (1) CLM-28 — 기획서 §35에서 정규성·등분산 검정 자체가 Phase2로 분류되어 있어, Phase1의 t-test/ANOVA가 애초에 가정 확인 수단 없이 설계됨(Navigator 위험1의 순서 문제보다 근본적). (2) CLM-29 — MSA(Gauge R&R)가 Phase1·2 어디에도 없어, Phase1의 모든 CTQ 검정이 측정시스템 신뢰성 미확인 상태로 이루어짐(spc-profile.md V0 원칙과 충돌).
- Research_Questions.md(RQ-07 상태 갱신), Claim_Evidence_Matrix.csv(CLM-28~29), Findings_Register.csv(FND-11), Execution_Log.csv(RUN-010), Gate_Dashboard.csv(G2), Project_Status.csv(WP2)에 반영.
- **주의**: 이 발견은 "Phase1 범위가 잘못됐다"는 결론이 아니라 기획서 원문 대조에 기반한 사실 확인 + Claude의 해석([추론])이며, 의도된 단계적 축소(Phase1→2→3)일 가능성을 배제하지 않는다. Ian의 최종 판단이 필요하다.

## 2026-09-10 (계속) — 연구 완료: G6 Adjudication·G7 Translation (RUN-011, DEC-007)

- 사용자 지시("연구를 먼저 완료해 주세요")에 따라 연구를 종합판정(G6)하고 최종 산출물(G7)을 작성했다. **G3(실데이터)·G5(실사용자검증)는 자원 제약(실 CTQ 데이터 없음, 추가 인터뷰 한계효용 소진, 독립전문가 부재)으로 완료할 수 없어 명시적으로 프로토타입 단계로 이관한다(DEC-007)** — 이는 실패가 아니라 헌장 자체가 예견한 경계다.
- RQ-01~12(12건) 전체 상태를 재확인하고, FND-01~11(11건)·CLM-01~29(29건)·CASE-001~008(8건)을 종합해 하나의 서사로 정리: **"현장 실무자는 도구를 몰라서가 아니라 '이 상황이 분석 대상'이라는 인식 자체에서 막힌다"(FND-07)**는 것이 가장 중요한 통합 발견이며, Navigator 위험 4건 정량화(FND-10)와 MVP 구조적 공백 2건(FND-11)이 이를 뒷받침한다.
- 학습 결정: **`adapt`(조건부 채택)**. "본 앱이 우수하다/효과성이 입증되었다/현장 전반의 니즈를 파악했다"는 주장은 여전히 `hold`.
- `08_DELIVERABLES/Final_Report.md`(v1.0, 종합판정), `Executive_Brief.md`(v1.0, 의사결정용 요약), `Research_Handoff_Package.md`(v1.0, 산출물 인벤토리+다음 액션) 전면 재작성 — 이전 2026-09-09 버전(P0~P2 중간 스냅샷)을 대체.
- `Limitations_and_Open_Questions.md`에 신규 결정부채 2건 추가: DBT-04(시뮬레이션이 합성데이터 기준), DBT-05(Phase1 구조적 공백이 의도된 설계인지 미확인).
- `Decision_Log.csv`(DEC-007), `Gate_Dashboard.csv`(G3/G5 이관 명시, G6/G7 completed), `Project_Status.csv`(WP6/WP7 신설), `Execution_Log.csv`(RUN-011)에 반영.
- **거버넌스 원칙 재확인**: G6/G7은 `self-adjudicated`이며 Ian의 `accepted` 최종 승인은 아직 없다. G0(헌장 승인) 역시 여전히 대기 상태다. "프로젝트가 종료되었다"는 주장은 하지 않는다 — 연구 단계가 마무리되었을 뿐, 제품 개발 단계의 결정은 Ian의 몫으로 남아 있다.

## 2026-09-10 (계속) — 주요 정정: 독립 앱 → PRISM Add-on, AI 미탑재, 분석 패키지 개념 도입 (DEC-008)

- Ian이 연구 프레이밍의 근본 오류를 정정: (1) **CTQ 데이터는 이미 PRISM**(사내 서버 등록 앱)이 자동분석·보고서·대시보드·CTQ표준관리·트렌드분석·비교분석으로 커버하고 있다. (2) 본 연구의 목적은 독립 앱이 아니라 **PRISM에 추가할 통계분석 Add-on 모듈**의 Claude Code 협업개발용 **지침서** 작성이다. (3) Add-on의 대상은 PRISM 밖의 제조 개선·관리 활동(원인분석·핵심요인분석·결과검증·유지관리 등 — 헌장목표 G8 5대주제와 정확히 일치, 재조사 불필요). (4) **Add-on에는 AI가 탑재되지 않는다** — 모든 해석은 런타임 LLM 호출 없이 사전 설계된 결정론적 규칙·템플릿으로 제공되어야 한다. (5) 사용자가 개별 통계기법을 요청하지 않아도 목적 하나로 여러 분석을 연계 실행하는 **"분석 패키지"**(예: 결과검증 패키지 = 히스토그램→정규성검정→검정방법 자동선택→실행→효과크기→해석까지 E2E 자동제공) 설계가 핵심 요구사항으로 추가됨.
- **기존 통계적 발견은 폐기되지 않는다** — Navigator 7위험 감사·시뮬레이션 정량화·Case Library 8건·MVP 커버리지 매트릭스·산업공통 5대주제 연구는 "독립 앱"이든 "PRISM Add-on"이든 통계적으로 동일하게 유효하다. 정정 대상은 (a) 제품 프레이밍(독립앱→Add-on), (b) 해석엔진 설계 전제(LLM→결정론적 규칙/템플릿) 2가지뿐이다.
- 보강 조사 3건 수행(RUN-012): 비-AI 규칙기반 가이드형 통계도구의 실재 사례 — Minitab Assistant(결정트리+Report Card 자동 가정확인, SRC-131), QI Macros Stats Wizard(기술통계→검정 자동연계+해석, SRC-132); 템플릿 기반 NLG의 학술적 근거 — 구조화된 수치를 규칙으로 분류해 슬롯 템플릿에 채우는 방식이 의료 도메인에서 AI 없이 이해도 96.5%·자연스러움 97.5%를 달성한 사례(SRC-133). 세 사례 모두 "AI 없이도 가이드형+연계형+해석포함 도구가 실현 가능하다"는 설계 방향의 실증적 뒷받침이 됨(CLM-30~32).
- `00_GOVERNANCE/Research_Charter.md` 전면 개정: 문제/baseline(PRISM 기준으로 재정의), 목표(G5 재정의: LLM 리스크 조사→결정론적 해석 설계; **G9 신설**: 분석 패키지 설계), 비목표(AI 런타임 탑재 명시적 배제), 범위(PRISM 밖 활동으로 재정의), 성공기준(G9 최소 1건 명세, 안전한 실패 템플릿 필수), 최종산출물(연구보고서→Claude Code 개발지침서로 확장).
- `Evidence_Gaps.md`: **GAP-08(신규, 최우선)** — PRISM의 기술스택·데이터스키마·API/통합방식이 전혀 조사되지 않음, Ian의 자료 제공 필요. **GAP-09(신규)** — AI 없이 모든 해석 분기를 사전에 커버해야 하는 템플릿 라이브러리의 전수 설계 필요. 기존 GAP-04(LLM 안전장치)는 superseded → GAP-09로 통합.
- `Findings_Register.csv`(FND-12, 이번 정정 자체를 발견으로 기록), `Decision_Log.csv`(DEC-008), `Gate_Dashboard.csv`(G6 reopened→completed 재확인, G7에 신규 산출물 추가) 반영.
- **신규 핵심 산출물**: `08_DELIVERABLES/Analysis_Package_Spec_ResultVerification.md`(RUN-013) — "개선 결과 검증 패키지"의 1차 개발 명세. E2E 처리흐름, 검정방법 자동선택 결정표(NAV-REQ-01/02 반영), 자기상관 체크(NAV-REQ-04 반영), 슬롯 기반 해석 템플릿 예시, 안전장치(템플릿 미매칭 시 기본값), 향후 다른 패키지(원인분석·핵심요인분석·MSA·유지관리)가 따를 재사용 패턴을 포함. **PRISM 기술 통합 세부사항은 GAP-08 해소 전까지 placeholder임을 명시.**
- **다음 세션 최우선 과제**: GAP-08(PRISM 기술정보) 확보, 추가 분석 패키지 3~4건 명세 작성, Final_Report의 PRISM Add-on 프레이밍 전면 보강.

## 2026-09-10 (계속) — GAP-08 범위 밖 확정(DEC-009) 및 분석 패키지 명세 4건 추가 작성(RUN-014)

- Ian의 명시적 지시("PRISM 앱의 기술 스택과 데이터 스키마 등은 최종 지침서와 앱 폴더를 클로드 코드에게 전달할 예정이므로 그 부분에 대해서는 미결사항으로 남겨주세요. 다음 연구로 넘어가 주세요")에 따라 DEC-009를 기록: GAP-08(PRISM 기술정보)은 본 연구 단계에서 더 이상 추적조사하지 않고, Claude Code 개발 착수 시점에 최종 지침서·앱 폴더와 함께 직접 전달받는 것으로 확정. Evidence_Gaps.md GAP-08 행과 우선순위 메모를 이에 맞게 갱신(상태는 `open`이나 "본 연구 To-Do"가 아닌 "개발단계 인수 항목"으로 성격 전환).
- 이에 따라 시급도 1위가 GAP-09(해석 템플릿 커버리지)로 이동했음을 명시.
- Analysis_Package_Spec_ResultVerification.md(RUN-013)와 동일한 구조(목적/트리거→입력요구사항→E2E흐름+결정표→해석템플릿 라이브러리→PRISM 연동 미확정사항[placeholder]→재사용패턴→근거)로 신규 패키지 명세 4건 작성, Case_Library_Register.csv의 남은 4대 주제를 전부 커버:
  - `Analysis_Package_Spec_RootCause.md` — 원인분석 패키지(CASE-005): 후보원인(범주형/연속형) 자동판별→시각화→검정 자동선택(2그룹/3+그룹/연속형 분기)→효과크기 기준 우선순위화→다중비교 경고.
  - `Analysis_Package_Spec_KeyFactor.md` — 핵심요인분석 패키지(CASE-006): 다중회귀 기반 vital few 식별, VIF 다중공선성 체크, 표준화계수 기준 요인순위, 저설명력(R²) 경고.
  - `Analysis_Package_Spec_MSA.md` — MSA 패키지(CASE-004): Gauge R&R 분산성분 분해, %GRR/NDC 자동판정(AIAG 기준), 불량 판정 시 다른 모든 패키지 결과의 신뢰성 저하를 경고하는 구조로 설계 — spc-profile.md V0 원칙과 직결.
  - `Analysis_Package_Spec_Maintenance.md` — 유지관리 패키지(CASE-008): 개선 후 I-MR 관리도 자동생성, Western Electric Rules 4종으로 급격한 이상값과 완만한 재발 조짐(drift)을 구분 탐지.
- 보강 웹조사 4건(SRC-134~137)을 Source_Register.csv에, 관련 claim(CLM-33~36)을 Claim_Evidence_Matrix.csv에 추가. 특히 CLM-34(원인분석 패키지의 검정+효과크기 기반 우선순위화)는 원 출처(Pareto 문헌)에 없는 Claude의 설계 확장이므로 [추론]으로 명시.
- Gate_Dashboard.csv G7을 "분석 패키지 명세 5종(G9의 5대 Case Library 주제 전체 커버 완료)"으로 갱신. Execution_Log.csv에 RUN-014 기록.
- 다음 세션 우선과제: (1) Final_Report.md·Executive_Brief.md의 PRISM Add-on 프레이밍 보강 갱신(RUN-012 이후 미착수 상태 지속), (2) GAP-09 — 5개 패키지 해석템플릿의 전수 조합 매트릭스 작성, (3) Ian의 G0(헌장)·G6/G7(self-adjudicated 판정) 최종 accepted 승인.

## 2026-09-10 (계속) — 패키지→모듈 라이브러리+조합규칙 전환(DEC-010, RUN-015)

- Ian의 재정정: "통계 분석은 하나의 툴만 사용하는 것이 아니라 연속으로 분석이 이어지는 것이 일반적이며, 조합단위의 분석 그룹을 클로드가 조합작업을 할 수 있도록" 연구를 진행할 것을 명시적으로 지시. 이전에 작성한 5개 패키지 명세는 "예시(샘플)"였을 뿐, 각 패키지를 매번 처음부터 프로즈로 새로 기술하는 방식은 지속가능하지 않다는 지적.
- DEC-010 기록: G9의 산출물을 "개별 패키지 프로즈 명세"에서 "재사용 가능한 원자 모듈(Atomic Module) 라이브러리 + 조합 규칙(Composition Rule)"으로 전환. 기존 5개 패키지 명세는 폐기하지 않고, 이 모듈 카탈로그로 전부 재구성 가능함을 검증하는 근거로 재활용.
- 보강 웹조사 2건(SRC-138 KNIME/Alteryx 재사용노드 체이닝, SRC-139 조립형 데이터분석 building-block 아키텍처) — CLM-37~38로 등록. 모듈 조합 자체에는 AI가 불필요함을 뒷받침(무AI 제약과 정합).
- 신규 산출물 `08_DELIVERABLES/Analysis_Module_Library_and_Composition_Rules.md` 작성: 기존 5개 패키지에서 반복 사용된 하위요소를 원자모듈 약 20개로 추출·카탈로그화(모듈ID·기능·입출력·사용패키지·근거), 모듈을 연결하는 조합 표기법(RECIPE/TRIGGER/FLOW/BRANCH) 정의, 기존 5개 패키지 전부를 이 표기법으로 재구성해 카탈로그 완전성 검증, 신규 패키지를 조합으로 만드는 절차(알고리즘) 명시, Claude Code 구현 권고(모듈=재사용 함수/클래스, 패키지=선언적 레시피) 포함.
- Research_Charter.md G9 재보강(모듈 라이브러리+조합규칙을 산출물로 명시), 성공기준에 "카탈로그가 기존 5개 패키지를 전부 재구성 가능해야 함" 추가.
- Gate_Dashboard.csv G7, Execution_Log.csv RUN-015 갱신.
- 다음 세션 우선과제: (1) 모듈 카탈로그를 이용해 신규 패키지(예: 공정능력·수율분석 등) 조합 시범사례 작성 — 카탈로그의 실전 검증, (2) GAP-09 해석템플릿 전수 매트릭스, (3) Final_Report/Executive_Brief PRISM 프레이밍 갱신, (4) Ian의 G0/G6/G7 최종 accepted 승인.

## 2026-09-10 (계속) — 객관식 질문 흐름 설계 + 신규 패키지 조합 시범사례 + 추가 후보 점검(RUN-016)

- Ian의 지시: "사용자가 제시한 데이터와 어떤 분석을 원하는지 객관식 답변을 받아 내장된 분석 툴을 조합하는 과정을 통해 종합적인 분석 작업이 가능하게 하는 작업을 고민"하고, "새 패키지 1건도 조합해보고 가능한 추가 조합 패키지를 점검"할 것.
- `08_DELIVERABLES/Navigator_Question_Flow.md` 신규 작성: 자유텍스트 없이 객관식으로만 답하는 2단계 질문흐름(Level1: 목적 선택 7지선다 → 레시피 매핑, Level2: 데이터로 자동감지 안 되는 것만 조건부 질문 — paired 여부/시계열 여부/원인변수 타입) + 결정론적 라우팅표 + "잘 모르겠음" 폴백(추측 대신 데이터 프로파일링 후 가능한 선택지만 재제시). G2(Navigator)와 G9(분석 패키지)를 잇는 문서로 자리매김.
- `08_DELIVERABLES/Analysis_Package_Spec_ProactiveComparison.md`(DELIV-PKG-SPEC-006, 예방적 비교 패키지) 신규 작성 — 모듈 카탈로그를 실제로 사용한 조합 시범사례. FND-08(예방적 비교 부재) 대응. **신규 모듈 0개**로 조합됨(결과검증 패키지와 통계로직 동일, 트리거·해석문구만 다름) — 카탈로그의 재사용 가치를 실증. 이 패키지에서 "패키지 체이닝"(NEXT 필드 — 유의한 차이 발견 시 원인분석 패키지 실행을 추천, 자동실행 아님) 개념을 처음 도입, `Analysis_Module_Library_and_Composition_Rules.md` §3에 반영.
- `Analysis_Module_Library_and_Composition_Rules.md`에 신규 §8 "추가 조합 패키지 후보 점검" 작성 — 6개 후보(예방적비교/다중그룹확장/MSA연동/다변량모니터링/신뢰성분석/안전재고/KeyFactor다중비교보정)를 카탈로그 재사용도·신규모듈 필요여부·비목표 충돌여부로 점검. 다변량 모니터링(PRISM 비목표 충돌 소지)·신뢰성(Weibull)·안전재고는 대량의 신규 모듈이 필요하거나 범위 밖 소지가 있어 Ian의 명시적 확인 없이는 착수하지 않는 것으로 판단.
- Gate_Dashboard.csv G7, Execution_Log.csv RUN-016 갱신.
- 다음 세션 우선과제 갱신: (1) 다변량모니터링·신뢰성·안전재고 착수 여부 Ian 결정, (2) GAP-09 해석템플릿 전수 매트릭스, (3) Final_Report/Executive_Brief PRISM 프레이밍 갱신, (4) Ian의 G0/G6/G7 최종 accepted 승인.

## 2026-09-10 (계속) — Navigator 질문흐름 UX 재설계(DEC-011, RUN-017)

- Ian의 정정: (1) 데이터에서 자동식별된 내용을 질문 없이 넘기지 말고 "이 내용으로 분석할까요?" 확인질문을 반드시 거칠 것. (2) 분석 선택지에 통계 기술용어가 많아 일반인에게 부담스러우니, 일상어로 질문하고 앱이 답변을 종합해 분석방향을 스스로 결정하는 "스무고개" 방식으로 바꿀 것.
- DEC-011 기록. `Navigator_Question_Flow.md`를 v1(6~7지선다 단일 메뉴+자동감지 시 질문 생략)에서 **v2**(Q1→Q2/Q3→Q4/Q5의 3단 이내 상황질문 결정트리, 전부 일상어, 통계 카테고리명 비노출)로 전면 재작성. 자동판별 항목(대응여부/측정순서/원인후보 종류)은 전부 "맞나요?" 확인질문(기본값 미리 선택)으로 전환 — 침묵 스킵 없음.
- `Analysis_Module_Library_and_Composition_Rules.md`의 M-DATA-PROFILE 모듈 정의에 "자동판별 시 확인질문 전환"을 기본 동작으로 명시(이 동작은 M-DATA-PROFILE을 쓰는 모든 패키지에 공통 적용).
- 라우팅 결정표(§4)의 최종 매핑(6개 레시피)은 변경되지 않음 — 이번 재설계는 사용자 접점(질문 UX)에 한정되며 기존 6개 패키지 명세 자체는 수정 불필요.
- 다음 세션 우선과제 갱신(변동 없음): (1) 보류된 추가후보(다변량모니터링·신뢰성·안전재고) 착수 여부 Ian 결정, (2) GAP-09 해석템플릿 전수 매트릭스, (3) Final_Report/Executive_Brief PRISM 프레이밍 갱신, (4) Ian의 G0/G6/G7 최종 accepted 승인.

## 2026-09-10 (계속) — 산업통계 사례집 문헌 보강 (RUN-018)

- Ian이 제조현장 사례 중심 통계학 도서 추천 목록(외부 조사자료)을 제공: *Statistical Case Studies for Industrial Process Improvement*(Czitrom & Spagon, SIAM), *Statistical Methods for Quality Improvement*(Ryan, Wiley), *Introduction to Engineering Statistics and Six Sigma*(Allen, Springer), 『통계적 품질관리 4.0』(양희정), 『통계적 품질관리』(윤원영 외), 『Montgomery 통계적 품질관리』(번역판), *Industrial Statistics: A Computer-Based Approach with Python*(Springer, 2023).
- 상위 2건(SIAM/Wiley)은 WebSearch로 서지사항(저자·출판사·실재 여부)을 독립 재검증. 나머지 5건은 Ian 제공 2차자료를 그대로 등록하되 verification_status에 "Claude 미재검증"을 명시(정직한 근거등급 유지 원칙).
- Source_Register SRC-140~146, Claim_Evidence_Matrix CLM-39~40 등록. CLM-39: SIAM 사례집이 Gauge R&R→DOE→SPC→신뢰성→개선의 연계 흐름을 실제 산업사례로 보여줌 — '분석 패키지' 개념을 소프트웨어 아키텍처(CLM-37/38)와 별개로 통계학 도메인 콘텐츠 관점에서도 뒷받침. CLM-40: Ryan의 저서가 DOE·Taguchi를 통합 다룸 — 모듈 카탈로그의 장기 확장 후보(문헌적 정당성)로 기록하되, 헌장 비목표 변경은 Ian의 결정 사항임을 명시.
- `Analysis_Module_Library_and_Composition_Rules.md` §8(추가후보 점검)에 "DOE·Taguchi 패키지" 행을 신규 추가(장기 후보, 현재는 비목표), 신뢰성 후보 행에 문헌 근거 보강 내용 추가. §6에 Python 기반 사례집(SRC-146)을 향후 Claude Code 구현 참고자료로 flag.
- 헌장 범위(비목표) 자체는 변경하지 않음 — 이번 작업은 근거 등록과 향후 후보 문서화에 한정.

## 2026-09-10 (계속) — 스무고개 질문흐름 셀프 드라이런 검증(RUN-019)

- Ian의 지시("(1) 이 스무고개 트리를 Ian이 직접 한번 시뮬레이션해보며 검토, (2) 보류해둔 추가 후보 범위 결정, (3) GAP-09 해석템플릿 전수화, 순서대로 진행") 중 항목 (1) 수행.
- 작동하는 프로토타입이 없으므로, Ian을 대신해 Claude가 `Navigator_Question_Flow.md` v2 결정트리를 9개 시나리오(S1~S9)로 셀프 드라이런: Case_Library_Register.csv의 실사례(CASE-001~008) 기반 시나리오 + 의도적으로 구성한 경계사례(데이터 극빈약, 시점 모호 등) 조합. GAP-07 waiver 때와 동일한 방법론(독립전문가 부재 시 Claude 자기비판적 재검토를 대체통제로 사용)을 재사용.
- 실제 설계결함 2건 발견 및 수정:
  - **S8**: Q2("최근에 조치를 했다" 이후 분기)가 "방금 한 조치"라는 시점 기준으로 짜여 있어, "오래전에 조치했지만 그 효과를 아직 한 번도 확인해보지 않은" 사용자를 제대로 못 걸렀음(결과검증/유지관리 어느 쪽에도 깔끔히 안 들어맞음). Q2를 시점이 아니라 "그 조치 효과를 확인한 적이 있는지"로 재작성해 해결(A=미확인→결과검증, B=확인했고 유지 여부 확인 원함→유지관리).
  - **S9**: 데이터가 단일 열·단일 그룹·시간정보 없음 수준으로 극히 빈약한 경우에도 §5 폴백 로직이 억지로 패키지 하나를 추천하려 했음. "이 데이터만으로는 어떤 분석이 맞을지 추천하기 어렵다"고 솔직히 안내하고 추가 정보를 요청하는 분기를 신설.
- 비이슈 확인 2건: MSA·유지관리 패키지 내부 경고 문구가 Navigator 확인질문과 중복되지 않음; 핵심요인분석 경로에서 원인후보종류 질문이 (다변량 회귀이므로 불필요해) 정상적으로 생략됨.
- `Navigator_Question_Flow.md`에 신규 §8 "검증: 시나리오 드라이런" 절 추가(9개 시나리오 전체표+수정내역+한계 명시: 이 드라이런은 Claude의 자기검토이며 GAP-07과 같은 근거등급 한계를 가지므로 Ian의 실제 스팟체크를 권고).
- **부차 발견(이월 결정)**: 드라이런 도중 해석템플릿 커버리지 갭 2건을 추가로 발견함 — (a) ResultVerification·ProactiveComparison·RootCause 3개 패키지 모두 "유의함+효과크기 중간" 조합의 해석템플릿이 누락(현재는 "큼/작음" 양극단만 있음), (b) Maintenance 패키지의 Western Electric Rule2 템플릿이 누락되어 있고, 여러 규칙이 동시에 위반된 경우를 단일 배타적 분류가 아니라 목록형으로 함께 보여줘야 하는데 현재 로직은 그렇지 않음. 두 갭 모두 성격상 GAP-09(해석템플릿 전수 커버리지) 본작업 범위이므로, 이번 항목(1)에서 즉시 패치하지 않고 항목(3) GAP-09 작업으로 명시적으로 이월(방치 아님 — Execution_Log RUN-019 deviation 필드에 기록).
- Execution_Log.csv RUN-019, Gate_Dashboard.csv G7 갱신.
- 다음: (2) 다변량모니터링·신뢰성·안전재고 3건 범위결정을 Ian에게 직접 질의, (3) GAP-09 해석템플릿 전수 매트릭스 작업(위 이월된 갭 2건 포함) 착수.

## 2026-09-10 (계속) — 보류 후보 3건 범위 결정(DEC-012, RUN-020)

- Ian의 지시 항목 (2) 수행: 이 결정은 Research_Charter.md의 "이해관계자·오너" 조항에 따라 Ian의 고유 권한이므로, Claude가 자체 판단으로 확정하지 않고 AskUserQuestion으로 3건을 각각 개별 질의(조사근거 기반 권장안 동봉).
- 결과: **다변량 CTQ 동시 모니터링** → 보류 유지(Claude 권장 채택, PRISM 기존기능과 중복 위험). **신뢰성/수명분석(Weibull)** → 지금 착수(Ian이 Claude의 "보류" 권장을 채택하지 않고 문헌근거(SRC-140/142, CLM-39)를 이유로 직접 착수 선택). **안전재고 산정** → 지금 착수(Ian이 Claude가 고지한 도메인 불일치 위험을 인지한 상태에서 직접 착수 선택).
- Research_Charter.md에 G10(신뢰성)·G11(안전재고)을 신규 목표로 추가. 단, 이 두 건은 기존 6개 패키지처럼 "설계 완료·근거 보강만 필요"한 상태가 아니라 **모듈 설계를 시작하기 전에 선행 문헌조사가 필요한 상태**이므로, Evidence_Gaps.md에 GAP-10(신뢰성 심화조사)·GAP-11(안전재고 신규조사, 이 프로젝트 내 도메인 근거 0건)을 신설하고, 이 프로젝트가 지금까지 일관되게 지켜온 "선 근거조사 → 후 설계" 순서를 그대로 적용하기로 함(Ian의 착수 지시가 근거조사 생략을 의미하지 않음을 명시).
- `Analysis_Module_Library_and_Composition_Rules.md` §8 후보 점검표를 확정 결과로 갱신.
- Decision_Log.csv DEC-012, Execution_Log.csv RUN-020, Evidence_Gaps.md, Research_Charter.md 갱신.
- 다음: (3) GAP-09 해석템플릿 전수 매트릭스 작업(기존 6개 패키지 대상, RUN-019에서 이월된 갭 2건 포함) 착수. G10/G11(신뢰성·안전재고)의 선행 문헌조사는 GAP-09 완료 후 순서대로 진행 예정.

## 2026-09-10 (계속) — GAP-09 해석템플릿 전수 커버리지 매트릭스(DEC-013, RUN-021)

- Ian의 지시 항목 (3) 수행: 기존 6개 분석 패키지(결과검증·예방적비교·원인분석·핵심요인분석·MSA·유지관리)의 해석 템플릿 §4를 전부 재검토.
- 신규 방법론 수립: 해석 슬롯을 (a) 배타적 핵심분류(동시에 두 값일 수 없음, 예: 유의/비유의) (b) 접두 경고(핵심분류와 독립, 있으면 항상 최우선 표시, 예: 자기상관경고) (c) 목록형 조립(동시에 여러 항목이 발생 가능, 예: Western Electric Rules 4종) 3유형으로 분류하는 규칙을 `Analysis_Module_Library_and_Composition_Rules.md` §2.7에 일반 규칙으로 등재하고, 신규 패키지 설계 절차(§5)에도 "해석 슬롯 유형 판정" 단계를 추가.
- 실제 발견·수정: (1) 결과검증·예방적비교·원인분석 3개 패키지 모두 "유의+효과크기 중간" 템플릿이 누락되어 있었음(RUN-019에서 이월된 갭) → 3개 파일 §4에 직접 추가. (2) 유지관리 패키지는 Western Electric Rule2 템플릿이 누락되어 있었을 뿐 아니라, "위반규칙" 슬롯 자체를 배타적 단일분류로 잘못 설계되어 있었음(실제로는 여러 규칙이 동시에 위반될 수 있음) → §3(E2E 흐름)과 §4(템플릿)를 함께 재설계해 목록형 조립 방식으로 전환(규칙별 템플릿 5개+동시위반 안내문 1개+데이터부족 접두경고 1개만으로 이론상 32가지 조합을 전부 커버).
- 핵심요인분석·MSA 2개 패키지는 재검토 결과 이미 완전한 커버리지를 갖추고 있음을 확인(수정 불필요).
- 신규 산출물 `08_DELIVERABLES/GAP09_Interpretation_Template_Coverage_Matrix.md` 작성 — 6개 패키지 전부의 "이론상 조합 수 vs 준비된 템플릿/규칙 수"를 표로 정리하고 전부 "완전" 판정.
- **DEC-013**: GAP-09를 "구조적 완전성"(모든 슬롯 조합에 템플릿/조립규칙이 존재하는가) 기준으로 6개 기존 패키지에 대해 closed 처리. 단 "문구가 실사용자에게 오해석을 유발하지 않는가"는 별도 검증(GAP-02/05, 프로토타입 필요)으로 명시적으로 분리해 이관 — 완전 종결이 아님을 분명히 함. G10(신뢰성)·G11(안전재고) 패키지는 아직 설계 전이므로 이 매트릭스에 포함되지 않으며, 각 패키지가 설계될 때 별도로 작성해야 함.
- Decision_Log.csv DEC-013, Execution_Log.csv RUN-021, Evidence_Gaps.md GAP-09(closed로 갱신) 반영.
- **Ian이 지시한 3건(스무고개 드라이런/보류후보 범위결정/GAP-09 전수화)이 순서대로 모두 완료됨.** 다음 세션 우선과제: (1) G10(신뢰성)·G11(안전재고) 착수 전 선행 문헌조사(GAP-10/11), (2) Final_Report/Executive_Brief PRISM·모듈화·G10/G11 프레이밍 갱신(누적 스테일 상태), (3) Ian의 G0/G6/G7 최종 accepted 승인, (4) 실사용자 검증(GAP-02/05) 경로 확보 시 Navigator 드라이런·해석템플릿 문구를 함께 검증.

## 2026-09-10 (계속) — G10(신뢰성)·G11(안전재고) 선행 문헌조사 및 1차 패키지 명세(RUN-022)

- Ian의 "진행해 주세요" 지시에 따라 직전 세션 우선과제 1순위(GAP-10/11 선행 문헌조사)를 착수.
- **GAP-10(신뢰성)**: WebSearch·WebFetch로 문헌 4건 확보 — Machine Design(SRC-147, β/η 해석·중도절단 데이터 처리·비용비 기반 교체시점 실사례), ScienceDirect 논문(SRC-148, 제목·초록만 확인), Ellistat(SRC-149, 신뢰도함수 R(t) 공식), nomtbf.com(SRC-150, MTBF=η×Γ(1+1/β) 공식과 한계). CLM-41~44로 등록. `Analysis_Module_Library_and_Composition_Rules.md` §2.8에 M-RELY-DATAPROFILE/WEIBULLFIT/STRATEGY/RELFUNC/MTBF 5개 모듈 신설.
- **GAP-11(안전재고)**: WebSearch·WebFetch로 문헌 2건 확보 — ABC Supply Chain(SRC-151, 안전재고 계산 6방식 체계), Wikipedia(SRC-152, 재주문점=리드타임중 평균수요+안전재고). CLM-45/46으로 등록. §2.9에 M-INVENTORY-DEMANDSTATS/METHODSELECT/SAFETYSTOCK/REORDERPOINT 4개 모듈 신설. 재고관리 전문 교과서 수준 검증은 아직 없어 근거등급을 medium/low-medium으로 낮게 표시.
- 신규 패키지 명세 2건 작성: `Analysis_Package_Spec_Reliability.md`(DELIV-PKG-SPEC-007)·`Analysis_Package_Spec_SafetyStock.md`(DELIV-PKG-SPEC-008) — GAP-09에서 수립한 "배타적 핵심분류/접두경고/목록형 조립" 슬롯 유형 분류 방법론을 그대로 적용해 해석 템플릿의 전수 커버리지를 처음부터 구조화(§4 "전수화 확인" 문단 포함).
- **미해결로 명시적으로 남긴 항목**: 신뢰성 패키지의 비용비 기반 교체주기 최적화(M-RELY-REPLACEINTERVAL, SRC-148 본문 미열람으로 결정로직 미확정); 안전재고 패키지의 재고관리 전문 교과서 근거 보강. 두 GAP 모두 "open(부분)"으로 조정 — 패키지 1차 명세 완료를 성급하게 "closed"로 표시하지 않음(GAP-09에서 세운 "구조 완전성과 근거 충분성은 별개" 원칙을 일관 적용).
- Research_Charter.md G10/G11 완료 표시, Evidence_Gaps.md GAP-10/11 부분해소 갱신, Execution_Log.csv RUN-022 갱신.
- 다음 세션 우선과제 갱신: (1) SRC-148 본문 확보(가능하면) 또는 대체 문헌으로 M-RELY-REPLACEINTERVAL 완성, (2) 재고관리 전문 교과서 조사로 안전재고 패키지 근거 보강, (3) Final_Report/Executive_Brief 전면 갱신(PRISM·모듈화·G10/G11까지 반영, 8개 패키지로 누적된 스테일 상태 해소), (4) Ian의 G0/G6/G7 최종 accepted 승인, (5) 실사용자 검증(GAP-02/05) 경로 확보 시 8개 패키지 전체의 해석템플릿 문구를 함께 검증.

## 2026-09-10 (계속) — Final_Report/Executive_Brief/Research_Handoff_Package 전면 갱신(RUN-023)

- Ian의 "다음 진행해 주세요" 지시에 따라 직전 우선과제 3순위(Final_Report/Executive_Brief 갱신)를 착수. 세 문서 모두 v1.0("SmartStat Manufacturing" 독립 앱 프레이밍, DEC-008 이전)에 머물러 있던 것을 v2.0으로 전면 갱신.
- `Final_Report.md`: 제목·전제를 PRISM Add-on/무AI로 교체, 요약(Executive Conclusion)에 모듈화·분석패키지·GAP-09 방법론(구조적 완전성 vs 문구품질 구분)을 신규 단락으로 추가, RQ 결과표·핵심발견·권고사항·금지된 결론에 각각 신규 항목([신규] 표기) 추가, Claim-to-evidence 색인을 CLM-46/SRC-152/RUN-022/DEC-013까지 확장. 기존 발견(FND-05~11, Navigator 7위험·시뮬레이션 수치)은 DEC-008 원칙에 따라 폐기하지 않고 재프레이밍만 수행.
- `Executive_Brief.md`: 동일한 방향으로 축약 갱신 — "지금 내릴 수 있는 결정"에 8개 패키지 Phase 배치 항목 추가, "금지된 결론"에 PRISM 통합·근거등급 혼동·문구검증 관련 3개 항목 신규 추가.
- `Research_Handoff_Package.md`: 산출물 목록을 8개 패키지+모듈 카탈로그+Navigator v2+GAP09 매트릭스로 갱신, 결정 이력에 DEC-008~013 요약 추가, 다음 액션에 GAP-08(Claude Code 개발착수 시 최우선)·GAP-10/11 잔여·미갱신 문서 목록을 명시.
- **의도적으로 범위에서 제외한 것**: `MVP_Coverage_Matrix.md`·`Limitations_and_Open_Questions.md`·`07_RESULTS/Findings_Register.csv`는 이번 갱신에 포함하지 않음 — 8개 패키지 기준 재작성은 별도의 상당한 작업이므로, 성급하게 완료로 표시하는 대신 Research_Handoff_Package.md의 "다음 액션"에 명시적으로 남겨둠.
- Execution_Log.csv RUN-023 갱신.
- 다음 세션 우선과제: (1) MVP_Coverage_Matrix.md·Limitations_and_Open_Questions.md·Findings_Register.csv를 8개 패키지 기준으로 갱신, (2) GAP-10/11 잔여 해소, (3) Ian의 G0/G6/G7 최종 accepted 승인, (4) 실사용자 검증 경로 확보 시 전체 문구 검증.

## 2026-09-10 (계속) — MVP_Coverage_Matrix/Limitations/Findings_Register 갱신(RUN-024)

- Ian의 "계속 진행해 주세요" 지시에 따라 RUN-023에서 의도적으로 미룬 3개 파일을 갱신.
- `MVP_Coverage_Matrix.md`(v2.0): 기획서 Phase1/2/3 기준 대조에서 8개 분석 패키지 기준 대조로 전면 재작성. **결론이 크게 바뀜** — v1.0 "완전커버 0/8"에서 "8개 사례 전부 대응 패키지 보유"로. v1.0이 지적한 구조적 공백 2건(가정확인 도구 부재, MSA 부재)이 8개 패키지 완성으로 실제 해소되었음을 확인 — 남은 질문은 "무엇을 만들 것인가"에서 "어떻게 검증·배포할 것인가"로 이동했다고 평가.
- `Limitations_and_Open_Questions.md`(v2.0): DBT-05(Phase1 가정확인·MSA 제외)를 "open(축소)"로 조정(기능 공백은 해소, 로드맵 배치만 미정). 신규 DBT-06(PRISM 연동 가정, GAP-08 의도적 이관)·DBT-07(해석템플릿 구조완전성≠문구품질)·DBT-08(안전재고 도메인 불일치 위험, Ian이 인지하고 착수) 추가.
- `Findings_Register.csv`: FND-13(모듈화가 실제 조합비용을 낮춤 — 예방적비교 신규모듈 0개, 신뢰성/안전재고 각 4~5개)·FND-14(GAP-09의 핵심 방법론적 통찰 — 구조적 완전성과 문구품질은 별개 검증)·FND-15(Navigator v2 드라이런 실제 결함 2건)·FND-16(DEC-012 거버넌스 사실관계 — Ian이 Claude 권장안을 2/3 기각) 4건 신규 등록.
- **부수 발견**: Findings_Register.csv의 기존 행 5개(FND-07/09/10/11/12)에서 CSV 컬럼 수 불일치(따옴표 처리 오류로 추정)를 발견 — 이전 세션에서 발생한 것으로 보이며 이번 작업 범위가 아니므로 수정하지 않음. 신규 추가한 FND-13~16은 컬럼 정합성 확인 완료. **다음 세션에서 기존 행 5개의 CSV 정합성 점검·수정을 별도 과제로 고려할 것.**
- Execution_Log.csv RUN-024 갱신.
- **이로써 Final_Report/Executive_Brief/Research_Handoff_Package/MVP_Coverage_Matrix/Limitations/Findings_Register 전부 8개 패키지·PRISM Add-on 프레이밍으로 최신화됨.** 다음 세션 우선과제: (1) Findings_Register.csv 기존 행 CSV 정합성 점검, (2) GAP-10/11 잔여 해소, (3) Ian의 G0/G6/G7 최종 accepted 승인, (4) 실사용자 검증 경로 확보 시 8개 패키지 전체 문구 검증.

## 2026-09-10 (계속) — Findings_Register.csv 데이터 정합성 수정(RUN-025)

- Ian의 "진행해 주세요" 지시에 따라 RUN-024에서 발견만 하고 보류했던 CSV 컬럼 정합성 오류를 수정.
- **원인**: FND-07/09/10/11/12 5개 행의 텍스트 필드(claim·uncertainty·assumptions·prohibited_overreach 등) 안에 쉼표가 따옴표 없이 그대로 들어가 있어, CSV 파서가 그 쉼표를 필드 구분자로 오인 — 결과적으로 각 행이 17개가 아닌 18~25개 컬럼으로 쪼개져 있었음(이전 세션에서 CSV 작성 시 발생한 것으로 추정).
- **수정 방법**: 각 행을 헤더 스키마(17개 컬럼)와 항목 수로 대조해, 쪼개진 조각들을 원래 필드로 재결합(쉼표로 다시 합침)한 뒤 전체를 올바르게 따옴표 처리해 재작성. 4개 행(FND-07/09/10/11)은 항목 수가 정확히 맞아떨어져 재구성에 모호함이 없었음.
- **FND-12만 예외**: 재구성 과정에서 필드 1개(contradicting_artifacts)가 분실된 것으로 보여(원본에 아예 빈 상태로 저장되었던 것으로 추정) 위치·의미 추론을 통해 빈 문자열로 복원 — 이 부분만 완전한 확실성은 아님을 명시.
- 수정 후 전체 16개 데이터 행 모두 17개 컬럼으로 정상 파싱됨을 확인.
- Execution_Log.csv RUN-025 갱신.
- 다음 세션 우선과제: (1) GAP-10/11 잔여 해소(우선순위 낮음), (2) Ian의 G0/G6/G7 최종 accepted 승인, (3) 실사용자 검증 경로 확보 시 8개 패키지 전체 문구 검증.

## 2026-09-10 (계속) — GAP-10/11 잔여 해소(RUN-026)

- 직전 세션 우선과제 1순위(GAP-10/11 잔여 해소)를 이어서 수행. 별도 Ian 지시 없이 스스로 우선과제 목록에서 다음 항목을 선택해 진행(기존 "진행해 주세요" 패턴과 동일한 자기주도 방식).
- WebFetch로 문헌 2건 추가 확보: SRC-153(ReliaSoft, 예방교체 비용률(CPUT) 방정식) — GAP-10의 M-RELY-REPLACEINTERVAL 결정로직 근거; SRC-154(NC State SCM, 안전재고 튜토리얼) — GAP-11의 Z값 환산표 교차검증 근거. CLM-47/48로 등록.
- **GAP-10 완전 해소**: M-RELY-REPLACEINTERVAL(비용비 기반 최적 교체주기)을 "β>1일 때만 적용, CP·CU·R(t)로 구성된 CPUT 함수를 그리드 탐색으로 최소화"하는 결정로직으로 확정 — `Analysis_Module_Library_and_Composition_Rules.md` §2.8, `Analysis_Package_Spec_Reliability.md`(Step 5 신설, §4 템플릿에 "교체주기안내" 목록형 조립 슬롯 추가, §6 갱신)에 반영. **원문(SRC-153)의 해석적(미분) 최적화를 결정론적 규칙엔진 제약 하에서 그리드 탐색으로 단순화한 부분은 [추론]/설계 확장으로 명시** — 개발단계 수치검증을 권장사항으로 남김. `Evidence_Gaps.md` GAP-10을 `open(부분)` → `closed`로 갱신.
- **GAP-11은 부분 진전만**: SRC-154로 Z값 환산표(90% 서비스수준)를 교차검증한 결과 SRC-151(1.28)과 SRC-154(1.29)가 소수점 둘째자리에서 다르나 동일한 표준정규분포 0.90분위수의 반올림 차이로 판단 — 기존 1.28값을 유지하고 `Analysis_Package_Spec_SafetyStock.md`에 각주로 설명. 재고관리 전문교과서 수준 근거는 여전히 확보하지 못해 **GAP-11은 `open(부분)`을 그대로 유지**(성급하게 closed로 표시하지 않음 — GAP-09/10에서 일관되게 지켜온 "실무자료 상호검증 ≠ 교과서 수준 검증" 구분 원칙 적용).
- `MVP_Coverage_Matrix.md` CASE-002/003 행 갱신(GAP-10 해소·GAP-11 부분진전 반영). `Analysis_Module_Library_and_Composition_Rules.md` 프런트매터 v1.1→v1.2, §8 후보점검 표의 신뢰성·안전재고 행 갱신.
- Execution_Log.csv RUN-026 갱신 — **작성 도중 RUN-026 자체의 status 필드(`completed(GAP-10 closed, GAP-11 open(부분)으로 잔여 축소)`)에 쉼표가 따옴표 없이 들어간 것을 즉시 발견하고 수정** — RUN-025에서 고쳤던 것과 동일한 유형의 실수를 스스로 재발시킬 뻔한 것이므로, CSV 필드 작성 시 쉼표 포함 여부를 항상 따옴표 처리 전에 재확인하는 습관을 다음 세션에도 유지할 필요.
- **남은 항목**: (1) GAP-11 재고관리 전문교과서 근거 보강(우선순위 낮음), (2) β임계값(1.2/0.8)·그리드탐색 단순화 등 [추론] 표시된 설계확장 전반에 대한 통계 담당자 검토, (3) Ian의 G0/G6/G7 최종 accepted 승인, (4) 실사용자 검증 경로 확보 시 8개 패키지 전체 문구 검증. 이 시점에서 GAP-10/11 관련 실질적 "다음 조사 과제"는 사실상 소진되었으며, 다음 세션은 Ian의 게이트 승인이나 실사용자 검증 경로 확보 등 **Claude가 단독으로 더 진전시키기 어려운 항목**이 우선순위 상위를 차지하는 상태로 전환됨을 명시적으로 기록해둔다.

## 2026-09-10 (계속) — 최종 보고서(Word) 생성 및 Final_Report.md 정정(RUN-027)

- Ian의 "최종 보고서를 생성해주세요" 지시에 따라 배포용 최종 보고서를 작성.
- **먼저 `Final_Report.md`의 스테일 항목을 v2.1로 정정**: (1) MVP 범위 충분성(RQ-07/FND-11) 서술이 RUN-024에서 이미 "완료(8개 사례 전부 대응 패키지 보유)"로 해소되었음에도 "재검토 필요(미반영)"로 남아있던 것을 정정, (2) GAP-10을 RUN-026에서 closed로 갱신한 것을 요약·결론·한계 섹션에 반영, (3) 핵심 발견에 FND-14~16 상당 항목(구조완전성/근거충분성 구분, 거버넌스 사실관계) 2건 추가, (4) Claim-to-evidence 색인을 CLM-48/SRC-154/FND-16/RUN-026까지 확장. 성급하게 "갱신 필요"로만 남겨두지 않고 실제 내용을 정정했다는 점이 중요 — 최종 보고서가 이미 해소된 항목을 "미해결"로 잘못 전달하는 것은 이 프로젝트의 정직성 원칙에 어긋나므로 우선 수정.
- **docx 스킬로 Word 배포본 생성**: `PRISM_통계분석_Addon_최종보고서.docx` — 표지, 갱신고지, 요약(강조박스), 연구범위, RQ표, 8개 패키지 현황표, 핵심발견 10건, 권고사항, 금지된 결론, 한계, Claim-to-evidence 색인으로 구성(A4, 7쪽). LibreOffice로 PDF 변환 후 페이지 이미지를 직접 확인해 표·글머리기호·번호매기기 렌더링을 검증 — 번호목록이 "연구범위" 섹션과 "핵심발견" 섹션에 걸쳐 이어지는 오류(8번부터 시작)를 발견해 별도 numbering 참조로 분리·수정. Word본은 md 원본(source of truth)의 배포용 파생본이며, md가 갱신될 때마다 Word본도 재생성이 필요함을 명시.
- Final_Report.md와 신규 Word본을 모두 볼트에 커밋.
- **[부수 발견, 미해결로 명시적으로 남김]** Execution_Log.csv 전체를 Python csv 모듈로 재검증하던 중, RUN-027과 무관한 기존 행 5개(RUN-005, RUN-008, RUN-010, RUN-011, RUN-012)에서 컬럼 수 불일치(14개가 아닌 15개)를 발견했다 — Findings_Register.csv에서 이미 고쳤던 것과 같은 유형(텍스트 필드 내 쉼표 미따옴치 처리)으로 추정된다. **이번 작업 범위가 아니므로 이번 세션에서는 수정하지 않고 발견 사실만 기록** — Findings_Register.csv 때와 동일하게, 다음 "진행해 주세요" 지시가 있으면 우선순위 상위 후보로 다룬다.
- Execution_Log.csv RUN-027 갱신.
- 다음 세션 우선과제 갱신: (1) **[신규]** Execution_Log.csv 기존 행 5개(RUN-005/008/010/011/012) CSV 정합성 점검·수정, (2) GAP-11 재고관리 전문교과서 근거보강(우선순위 낮음), (3) Ian의 G0/G6/G7 최종 accepted 승인, (4) 실사용자 검증 경로 확보 시 8개 패키지 전체 문구 검증.

## 2026-09-10 (계속) — Claude Code 전달용 개발 지침서 신규 작성(RUN-028)

- Ian의 "클로드 코드에게 전달할 프로그램 제작 지침서를 .md 형식으로 생성해 달라"는 지시에 따라 `08_DELIVERABLES/Development_Guide_for_Claude_Code.md`(신규, DELIV-DEVGUIDE-001)를 작성. Ian이 이전부터 예고한 "PRISM 앱 폴더·기술 스택 문서와 함께 Claude Code에게 전달할 최종 지침서"가 바로 이 문서다.
- 기존에 흩어져 있던 연구 산출물(모듈 라이브러리, 8개 패키지 스펙, Navigator 흐름, GAP-09 방법론, 의사결정 이력)을 **개발 착수 시 바로 실행 가능한 형태**로 압축·재구성: (1) 절대 지켜야 할 제약(무AI·표준 골격·확인질문 원칙·체이닝 비자동실행 등) 6개조, (2) 모듈-레시피 2계층 아키텍처와 표기법, (3) 9개 카테고리 모듈 요약표, (4) 8개 패키지 전체를 RECIPE 표기법으로 재작성(신뢰성·안전재고는 기존에 프로즈로만 서술되어 있던 것을 이번에 레시피 표기로 신규 변환), (5) Navigator 질문트리 압축본, (6) GAP-09 해석템플릿 3유형 방법론, (7) GAP-08 관련 패키지별 데이터 요구사항 확인 목록, (8) [추론] 설계확장 전체 목록, (9) 의사결정 이력 요약, (10) 개발착수 체크리스트, (11) 참고문서 색인. 정확한 해석 문구·임계값은 원본 스펙 파일이 최종 권위를 갖는다는 점을 서두에 명시해 이중 유지보수 위험을 낮췄다.
- **[신규 발견]** 지침서를 작성하며 Navigator 질문 트리(`Navigator_Question_Flow.md` §2)를 다시 대조한 결과, **6개 핵심 패키지까지만 라우팅하고 신뢰성·안전재고(G10/G11) 패키지로 가는 경로가 설계되어 있지 않다는 구조적 공백**을 발견했다 — Navigator v2가 G10/G11 추가 이전(RUN-019)에 드라이런 검증되었기 때문으로 추정된다. 이 자리에서 임의로 Navigator를 확장하지 않고, 지침서 §6에 "⚠ 구현 시 반드시 확인할 격차"로 명시해 Ian과 Claude Code가 개발 착수 시 결정(질문트리 확장 vs 별도 메뉴)하도록 이관했다.
- Execution_Log.csv RUN-028 갱신. Development_Guide_for_Claude_Code.md 볼트 커밋 완료.
- 다음 세션 우선과제(변동 없음, 재확인): (1) Execution_Log.csv 기존 행 5개(RUN-005/008/010/011/012) CSV 정합성 점검·수정, (2) Navigator의 신뢰성/안전재고 라우팅 공백 처리 방식 결정, (3) GAP-11 재고관리 전문교과서 근거보강(우선순위 낮음), (4) Ian의 G0/G6/G7 최종 accepted 승인, (5) 실사용자 검증 경로 확보 시 8개 패키지 전체 문구 검증.

## 2026-09-11 — 통계분석 계층 마인드맵 생성(RUN-029)

- Ian의 "클로드 코드에게 분석 툴 제작에 필요한 지침서를 작성했는데 통계분석의 계층 구조를 마인드 맵 형태로 생성해 주세요" 지시에 따라, `Development_Guide_for_Claude_Code.md` §3~6(아키텍처, 원자 모듈 카탈로그, 8개 분석 패키지, Navigator 질문흐름)을 근거로 계층 마인드맵을 제작.
- **구조**: 루트(PRISM 통계분석 Add-on)에서 3갈래로 분기 — ① Navigator(스무고개, Q1-A~D 4개 상황분기 + 6개 핵심 패키지로의 경로), ② 분석 패키지(품질/공정 표준 6개 + 도메인 확장 2개, 근거등급 차이를 그룹 라벨로 구분), ③ 원자 모듈 카탈로그(§2.1~2.9, §2.7은 "★전 패키지 공통"으로 강조). Navigator 가지에는 RUN-028에서 발견한 DBT-09(신뢰성·안전재고 미라우팅 격차)를 별도의 경고색(rust) 노드로 명시적으로 시각화해, 지침서의 텍스트 경고가 다이어그램에서도 누락되지 않도록 함.
- **형식**: 새 연구·근거를 생성하지 않는 순수 시각화 산출물이므로, 볼트에 md 파일로 추가하지 않고 Claude Artifact(HTML, 자체 tidy-tree 레이아웃+SVG 렌더링, 라이트/다크 테마 대응)로 발행 — `https://claude.ai/code/artifact/521edf29-012c-438d-a1cf-43356f73c097`. 발행 전 로컬 스크린샷(라이트/다크/모바일)으로 1회 검수해 리프 노드 pill이 서로 겹치는 레이아웃 버그를 발견·수정한 뒤 발행함.
- Execution_Log.csv RUN-029 갱신(output_locator에 Artifact URL 기록).
- 다음 세션 우선과제(변동 없음, 재확인): (1) Execution_Log.csv 기존 행 5개(RUN-005/008/010/011/012) CSV 정합성 점검·수정, (2) Navigator의 신뢰성/안전재고 라우팅 공백 처리 방식 결정, (3) GAP-11 재고관리 전문교과서 근거보강(우선순위 낮음), (4) Ian의 G0/G6/G7 최종 accepted 승인, (5) 실사용자 검증 경로 확보 시 8개 패키지 전체 문구 검증.

## 2026-09-12 — LLM_extention 기획 Step 1~7 검토(RUN-030)

- Ian의 "LLM_extention 폴더는 현재 앱에 LLM을 추가해 확장된 개념의 완성도 높은 분석앱으로 발전시키기 위한 기획이다. 내용을 읽고 7. Manufacturing Statistical Agent Prompt Architecture 까지 누락 또는 보완이 필요한 사항을 점검해달라"는 지시에 따라, `LLM_extention/` 폴더(총 21개 파일 중 1, 2, 3, 3.1~3.9, 4, 4.1~4.5, 5, 6, 7 계열 18개 파일)를 전문 통독하고 비판적 검토(gap analysis)를 수행.
- **이 작업은 기존 PRISM Add-on 연구 트랙(위 RUN-001~029)과는 별개의 신규 트랙**이다 — LLM_extention은 "런타임에 AI 없는" 기존 PRISM을 향후 LLM 기반 Agent로 확장하기 위한 별도의 기획 문서군이며, 이번 RUN-030은 그 기획 자체를 검토한 것으로, 기존 PRISM 연구의 잔여과제(Execution_Log.csv 컬럼 정합성 등)와는 무관함.
- **검토 결과 요약**: 전체 설계 철학(LLM은 계산하지 않는다, 교란요인 인식, Evidence Level E0~E4, Stop Condition)은 일관되고 견고하다고 평가. 다만 4건을 최우선 보완사항(A)으로 식별: (A-1) LLM에 전달되는 제조 데이터의 기밀성 문제가 기존 PRISM의 "런타임 무-AI" 설계원칙과 충돌하는데 이 충돌 자체가 검토되지 않은 점(가장 심각), (A-2) Candidate Factor를 여러 개 동시 스크리닝할 때 다중비교(multiple comparison) 보정이 없는 점, (A-3) 불량여부(이분형) 반응변수 비교에 필요한 proportion test/chi-square가 서술(4.5, 7장)과 실제 Tool 목록(5-6, 5-19) 사이에서 불일치하는 점(문서 내 사실 확인 가능한 결함), (A-4) 교란요인 통제가 일반화된 Tool 없이 사례별 임시방편(수동 층화분석)에만 의존하는 점. 그 외 중요 보완사항(B: Statistical Engine 자체 검증전략, MSA 게이트 미통합, 시계열 자기상관/변화점탐지, Evidence 하향조정 정책, Data Guard 구체기준 부재)과 운영·거버넌스 보완사항(C: LLM API 비용/지연/장애 대응, 사용자 실시간 정정 반영 절차, 모델교체 시 Golden Case 재검증 연결, 고위험 판단의 human-in-the-loop)을 구분해 정리.
- 산출물 `LLM_extention/Gap_Analysis_Step1-7_검토.md`(신규)를 볼트에 커밋하고 Ian에게 파일로 전달. 종합 제안 섹션의 우선순위 판단(A항목을 Step 8 이전에, B/C는 이후 구현설계 단계에서 처리)은 [추론]으로 명시.
- Execution_Log.csv RUN-030 갱신.
- 다음 검토 시 참고: Ian이 이후 "Step 8" 이후 문서(Multi-Agent 구조 검토 등)를 이어서 검토해달라고 하면, 이번 RUN-030에서 식별한 A-1(데이터 기밀성)이 해소되었는지 여부를 먼저 확인하고 진행하는 것이 좋다.

## 2026-09-12 (계속) — LLM_extention 추가 파일(Step 8~25) 후속 점검(RUN-031)

- Ian의 "추가 검토가 진행되었습니다. 추가로 생성한 파일을 점검해 주세요" 지시에 따라, RUN-030 검토 이후 `LLM_extention/` 폴더에 새로 추가된 18개 파일(Step 8 Brain Architecture ~ Step 25 First Vertical Slice, "25." 번호가 중복된 파일 3건 포함, `manufacturing-statistical-analysis-agent-progress-summary.md`)을 점검. RUN-030에서 식별한 A-1~A-4/B-2가 이번 확장에서 어떻게 처리되었는지 후속 확인하는 성격의 작업.
- **A-1(데이터 기밀성) — 실질적으로 해결 확인**: `25. 중간점검 LLM 통계 분석 앱 구조_수동 전환 기능.md`에서 "Core App은 100% Local, AI Layer는 Optional"을 아키텍처 요구사항으로 명문화하고, Manual/AI 이중모드·AI Gateway·데이터 전송 정책(원본 데이터 전송 금지를 기본값으로)까지 구체화했음을 확인. 문서 자체의 자기평가표가 "데이터 전송 정책 세부 메커니즘은 추가 설계 필요"로 정직하게 표시해 두어, 원칙은 확정, 세부는 Step 26~30 과제로 이관된 상태로 판단.
- **A-3(불량률 비교 Tool) — 신규 발견: 문서 동기화(spec drift) 불일치**: `11. 실제 Agent 작동 시나리오 설계.md`와 `13. Agent Data Contract and Interface 설계.md`의 서술·다이어그램·Evidence 예시에는 `chi_square_test()`가 이미 여러 차례 등장하는데, 공식 "Tool Registry/MVP Tool 목록"을 선언하는 4곳(파일 8 §8-17, 13 §13-15, 18 §18-3, progress-summary §8) 어디에도 실제로 등재되어 있지 않음을 grep으로 확인. 원칙은 이미 합의되었고 목록 반영만 누락된 것이므로 수정 비용이 낮은 실무적 결함으로 평가.
- **A-2(다중비교 보정) — 재구분**: 사후검정(post-hoc)용 다중비교 보정(Tukey/Games-Howell/Bonferroni posthoc)은 기존 파일(3.5, 4.3)에 이미 올바르게 존재함을 재확인. 다만 원래 지적한 "후보요인(Machine/Model/Shift/Operator/Temperature 등)을 동시에 각각 독립 검정으로 스크리닝할 때의 다중비교"는 46개 파일 전체를 재검색해도 여전히 다뤄지지 않음을 확인 — 두 문제가 서로 다른 종류의 다중비교임을 명확히 구분해 기록.
- **A-4(교란요인 통제 일반화)**: `13.`의 Confounder Schema에도 `recommended_analysis: MODEL_CONTROLLED_MACHINE_COMPARISON`처럼 여전히 "동일조건 재비교"(수동 층화) 패턴만 있고, ANCOVA/다중회귀 기반 일반화 Tool은 신규 파일에도 추가되지 않음을 확인 — 미해결 유지.
- **B-2(MSA 게이트)**: 신규 파일 전체에서 MSA/Gauge R&R/측정시스템 키워드가 전혀 발견되지 않아 — 미해결 유지.
- **[부수 발견, 문서관리]** "25."로 시작하는 파일이 3개(`25. 중간점검 LLM 통계 분석 앱 구조_수동 전환 기능.md`, `25. 중간점검2.md`, `25. First Vertical Slice Technical Implementation.md`) 존재해 번호가 충돌함을 발견. 또한 `25. 중간점검2.md`에서 자체 제안했던 통합 baseline 문서(`manufacturing-statistical-agent-design-notes.md`, Design Decision Log 포함 20개 섹션 구조)가 실제로는 생성되지 않았고, 그보다 앞서 만들어진 `manufacturing-statistical-analysis-agent-progress-summary.md`(Step 15까지만 다룸)가 대신 baseline 역할을 하고 있으나 Step 16 이후 내용(Tool Registry, Data Contract, Vertical Slice 등)이 반영되지 않아 낡은 상태임을 기록.
- 산출물 `LLM_extention/Gap_Analysis_Step8-25_후속검토.md`(신규)를 볼트에 커밋하고 Ian에게 파일로 전달.
- Execution_Log.csv RUN-031 갱신.
- 다음 검토 시 참고: A-3(Tool Registry에 chi_square_test 정식 등재)은 비용이 낮으면서도 이미 3곳 이상에서 합의된 내용이라 우선순위 상위 후보. Step 26(Product UX & Operating Architecture) 진행 여부는 Ian의 판단 대기.

## 2026-09-12 (계속) — LLM_extention 1차·2차 검토 통합 및 AI 전달용 제안 문서 작성(RUN-032)

- Ian 요청: "전체 점검 내용을 ai에게 전달하여 개선할 수 있도록 내용을 다시 정리해 주세요. 확정하여 언급할 것이 아니라 제안을 하는 방식으로 작성해 주세요. 전체 맥락을 유지해야 하고 step간 연계성과 전체 구조의 일관성이 확보되어야 합니다." + 신규 요구사항: "LLM을 연결할 때 API가 아닌 계정 로그인 방식으로 진행하는 것이 좋겠습니다. 통합 API Key로 인증할 경우 사용 토큰을 부담할 부서가 없으므로 개인 계정으로 인증받는 형식이 되어야 합니다."
- RUN-030(Step1-7 검토)과 RUN-031(Step8-25 후속검토)을 하나의 문서로 통합. 모든 항목을 "확정된 결함"이 아니라 "확인·검토 제안"으로 재작성했고, 각 항목에 관련 Step 번호와 파일명을 함께 표기해 Step 간 연계성과 근거를 추적할 수 있도록 구성.
- **원본 기획서 동기화 상태 점검(신규 확인 항목)**: 볼트 루트의 `통계분석 앱 제작 기획서.md`와 `LLM_extention/통계분석 앱 제작 기획서.md`를 diff한 결과, frontmatter(메타데이터)를 제외한 본문이 완전히 동일함을 확인 — 즉 Step 1 대화 시작 이후 Step 25까지 이 파일의 본문이 전혀 갱신되지 않았음을 확인. `25. 중간점검2.md`에서 자체 제안했던 baseline 문서(`manufacturing-statistical-agent-design-notes.md`)도 생성되지 않았고, 대신 역할을 하고 있는 `progress-summary.md`는 Step 15까지만 다뤄 낡은 상태임을 재확인. 문서에는 (A)원본 기획서 직접 갱신 또는 (B)별도 baseline 문서를 Step마다 실제로 갱신하는 두 방향을 제시하고, 어느 쪽이든 "현재 확정 상태"를 보여주는 문서 하나는 계속 최신으로 유지해 줄 것을 제안 형태로 요청.
- **LLM 인증 방식 신규 요구사항 반영**: Ian이 제시한 "공용 API Key 대신 개인 계정 로그인" 요구사항을 Step 26/27(AI Gateway·LLM Provider 구조) 검토 항목으로 편입. 과금모델의 실제 지원 여부, 현장 사용자 개별 계정 보유 부담, 부서단위 계정/chargeback 대안, `AnalysisSession`에 과금 계정 정보를 기록할지 여부 등을 모두 제안형 검토 포인트로 정리(확정 아님).
- RUN-030/031의 A-1~A-4, B-2 및 부수 발견사항(25.번호 중복, 낡은 baseline, MSA 게이트, 다중비교 재구분, 교란요인 통제 일반화, Evidence 재검증 정책 부재, Data Guard 수치기준 미정, 시계열 자기상관/변화점 탐지, 운영·거버넌스 항목 등)을 Step 번호·파일명 태그와 함께 §3-1~3-11로 재구성.
- 산출물 `LLM_extention/AI전달용_통합제안.md`(신규)를 볼트에 커밋하고 Ian에게 파일로 전달. 이 문서는 Ian이 LLM_extention 기획을 진행 중인 별도 AI 대화창에 붙여넣어 전달할 목적으로 작성됨(내부 기록용이 아님).
- Execution_Log.csv RUN-032 갱신.
- 다음 검토 시 참고: 문서 자체가 최우선 항목으로 (1)원본 기획서/baseline 동기화 방향 결정, (2)LLM 인증 방식 결정을 지목함. 나머지 §3 항목들은 Step 26 이후 자연스럽게 다뤄질 수 있는 낮은 우선순위 참고사항으로 명시.


## 2026-09-12 (계속) — LLM_extention 폴더 구조 재정리(RUN-033)

- Ian 요청: "지금부터 ChatGPT가 진행해온 앱 개발 기획서 작업을 클로드가 이어서 진행하겠습니다. 먼저 F:\obsidian\vault\통계분석앱\LLM_extention\ 폴더를 파일 내용을 참고하여 폴더 구조를 만들고 파일을 각 폴더에 이동시켜 주세요." — 이 시점부터 LLM_extention 트랙의 기획 작업 주체가 ChatGPT에서 Claude(Cowork)로 전환됨.
- 이동 전 안전성 확인: LLM_extention 폴더 전체를 대상으로 Obsidian wikilink(`[[ ]]`) 사용 여부를 검색 — 실제 파일 간 상호참조 링크는 없음을 확인(유일하게 발견된 `[[`는 `6. Manufacturing Knowledge Architecture.md` 안에서 지식문서 연결 형식을 보여주는 예시 템플릿 문구였음). 따라서 파일을 폴더 간 이동해도 기존 문서 간 링크가 깨지지 않음을 사전에 확인하고 진행.
- **[장애 발견 및 우회]** 이동 작업 착수 시 이 세션의 `device_bash`(로컬 Linux VM)가 "9월 8일자 Windows 업데이트로 인해 Claude의 워크스페이스가 파일에 접근하지 못하는 알려진 이슈"로 작동하지 않음을 확인(Anthropic 측에서 추적 중인 이슈로 안내됨). 대신 로컬에 연결되어 있던 Desktop Commander MCP(로컬 파일시스템에 직접 접근하는 별도 서버)로 전환하여 폴더 생성·파일 이동·로그 기록을 모두 수행함 — 산출물이나 파일 무결성에는 영향 없음.
- 내용을 기준으로 LLM_extention 폴더 내 전체 47개 파일을 9개 하위 폴더로 재구성:
  - `00_원본기획서` — 통계분석 앱 제작 기획서.md(1건)
  - `01_개념정의_UseCase(Step1-4)` — Step 1~4 계열(1, 2, 3, 3.1~3.9, 4, 4.1~4.5, 총 18건)
  - `02_Agent아키텍처(Step5-9)` — Step 5~9(5건)
  - `03_MVP설계_실행엔진(Step10-15)` — Step 10~15(6건)
  - `04_StatisticalEngine_Tool(Step16-20)` — Step 16~20(5건)
  - `05_GoldenCase_평가체계(Step21-24)` — Step 21~24(4건)
  - `06_제품운영설계(Step25)` — Step 25 계열 3건(파일명 중복 해소를 위해 25-1/25-2/25-3 접미사 부여, 내용은 변경하지 않음)
  - `07_검토및제안` — Gap_Analysis_Step1-7_검토.md, Gap_Analysis_Step8-25_후속검토.md, AI전달용_통합제안.md(RUN-030~032 산출물, 3건)
  - `08_기준문서_Baseline` — manufacturing-statistical-analysis-agent-progress-summary.md, manufacturing-statistical-agent-design-notes.md(2건 — 후자는 RUN-032에서 미생성 상태로 보고했던 파일인데, 그 사이 ChatGPT 세션에서 실제로 생성된 것을 이번 확인 중 발견함)
- **[발견]** 폴더 재조회 중 `통계분석 앱 제작 기획서.md`의 수정시각과 `manufacturing-statistical-agent-design-notes.md`의 신규 생성을 확인 — RUN-032에서 지적했던 "원본 기획서 미갱신·baseline 문서 미생성" 문제가 그 사이(ChatGPT 세션에서) 일부 해소된 것으로 보임. 실제 반영 내용은 다음 세션에서 파일을 직접 열어 확인 필요.
- 파일 내용 자체는 전혀 수정하지 않았으며, 이동/이름 정리만 수행함. 이동 결과는 재조회로 검증(47개 파일 전량 확인, 누락 없음).
- Execution_Log.csv RUN-033 갱신.
- 다음 세션 참고: `manufacturing-statistical-agent-design-notes.md`(신규 확인)와 갱신된 원본 기획서 내용을 읽고, RUN-032(AI전달용_통합제안.md)에서 제안했던 항목들이 실제로 반영되었는지 확인 필요.


## 2026-09-12 (계속) — Step 26 Product UX & Operating Architecture 신규 집필(RUN-034)

- Ian 요청: "ChatGPT가 진행하던 기획서 작성을 클로드가 지금부터 이어서 진행하도록 하겠습니다. 전달하려고 했던 내용과, 지금까지 진행된 내용을 기초로 다음 단계를 진행해 주세요." — LLM_extention 트랙의 기획 집필 주체가 정식으로 Claude(Cowork)로 인계된 첫 실작업.
- 먼저 ChatGPT가 생성해 둔 Baseline 문서 `manufacturing-statistical-agent-design-notes.md`(v1.0, 1,429행, 37개 절)를 통독. 이 문서가 §32 Revised Development Sequence와 말미 Next Step에서 **Step 26 — Product UX & Operating Architecture**를 명시적으로 다음 단계로 지정하고 있어, 이를 그대로 이어받아 집필함(임의로 다른 단계를 선택하지 않음).
- **Baseline에 RUN-032 제안이 일부 반영된 정황 확인**: Baseline §33 Open Design Decisions의 Statistics 항목에 "multiple testing 정책", "outlier 처리", "missing data 처리"가 미결 항목으로 들어가 있고, §10 Statistical Engine의 Phase 2 목록에 Chi-square·Proportion tests가 포함됨 — RUN-030~032에서 제기한 A-2·A-3·Data Guard 기준 항목이 로드맵에 흡수된 것으로 판단. 반면 **LLM 인증 방식(개인 계정)은 Baseline 어디에도 반영되어 있지 않아** 이번 Step 26에서 정면으로 다룸.
- 산출물 `LLM_extention/06_제품운영설계(Step25-30)/26. Product UX and Operating Architecture.md`(신규, 20개 절). 주요 내용:
  - Baseline §36의 End-to-End 18단계 시나리오를 화면·운영모드·Analysis State 변화 단위로 분해하고, 여기서 3개의 구조적 요구(AI는 세션을 새로 시작하지 않는다 / AI 경계선에 인증과 전송승인이 동시에 걸린다 / Manual↔AI 양방향성이 optional layer 주장의 전제다)를 도출.
  - 화면 13종(S-01~S-13) 정의표. 각 화면의 **AI OFF 시 동작**을 필수 항목으로 명시해 DD-001(LLM 없이도 완전 동작)을 화면 레벨에서 보증.
  - 운영모드 Level 0~3 전이도 및 전이 규칙 — 상향 전이는 사용자 명시 행동으로만 발생(DD-013), 하향 전이 시 Analysis State 전량 보존(DD-014).
  - **Ian의 개인계정 인증 요구에 대한 설계 답변**: 요구를 "비용 귀속(진짜 요구사항)"과 "계정 로그인이라는 구현 수단"으로 분리하고, 개인별 API Key(BYOK)도 비용 귀속 요구를 완전히 충족함을 설명. 모델 A(BYOK) / B(사내 SSO + 사내 LLM Gateway) / C(공용키+할당량) 3안을 비용귀속·현장사용자 부담·구현난이도·조직통제·데이터경로 5개 축으로 비교하고, **MVP는 A, 확장지점으로 B**를 권고(O-1로 Ian 결정 대기). 모델 B는 사내 LLM 사용 시 A-1 데이터 기밀성 문제까지 근본 해결된다는 점을 명시.
  - **[주의 환기]** 주요 LLM 공급자의 개인 구독 상품 계정으로 제3자 앱이 로그인해 그 구독 사용량으로 프로그래밍 호출하는 방식은 일반적으로 제공되지 않으며 약관상 허용되지 않는 경우가 많다는 점을 [추론]으로 명시하고, O-1 결정 전 실제 공급자 약관·상품 구조 확인을 권고함.
  - S-08 AI 연결설정 화면 목업 — 인증과 데이터 전송범위를 한 화면에서 처리하고, 전송되는 항목/전송되지 않는 항목을 구체적 항목명으로 표시.
  - S-07 Chat + Analysis Workspace 목업 — 좌측=시간순 로그, 우측=현재 상태(덮어쓰기)로 책임 경계 확정. 모든 서술에 출처(Statistical Engine/LLM/Rule+제조지식) 표기 의무화(DD-020).
  - Analysis Trace 5가지 상태(완료/진행중/대기/경고/차단) 정의. Rule Engine 차단을 사용자에게 그대로 노출해야 한다는 원칙 포함.
  - 승인 필요행위 매트릭스(Level별) — 데이터 전송범위 확대는 자율성 수준과 무관하게 항상 승인(DD-024).
  - 오류·저하 UX 8종. LLM 오류는 모달이 아닌 배너로 처리하고 기존 분석 결과를 화면에서 지우지 않음(DD-025).
  - 화면↔상태 매핑표 및 Step 29(Schema Contract)에 추가 요청할 8개 필드(llm_config.auth_mode, transfer_scope, usage, approval_log, mode_history, evidence 생성시점/데이터버전, multiplicity_correction, measurement_system_confirmed).
- **RUN-030~032 검토항목의 UX 연계(Step 간 연결성 확보)**: A-2 다중비교 → DD-022(후보요인 동시 스크리닝 시 Trace에 보정 적용 여부와 보정 전/후 유의 개수 표시), B-2 MSA → DD-023(개선 전후 비교 진입 시 "측정 방법이 동일한가" 선행 질문 — 완전한 Gauge R&R 대신 저비용 게이트로 제안), A-1 데이터기밀성 → DD-024, Evidence 재검증 → §11-2에서 화면 표시만 정의하고 규칙은 Step 29로 이관.
- DD-013~DD-025 13건을 확정 제안으로, O-1~O-6 6건을 Ian 결정 대기로 명확히 분리. Baseline §34 Design Decision Log의 DD-012 다음 번호를 연속 부여해 문서 간 연속성 유지.
- §20에 **Baseline 갱신 요청** 절을 두어, 이 문서의 결정이 승인되면 design-notes.md를 v1.1로 갱신해야 할 5개 항목을 명시 — RUN-032에서 지적했던 "기준문서가 갱신되지 않아 낡은 baseline을 참조하는" 문제의 재발 방지 장치.
- 폴더명 `06_제품운영설계(Step25)` → `06_제품운영설계(Step25-30)`으로 갱신(Baseline §32가 Step 26~30을 제품·운영 아키텍처 계열로 규정한 데 따름).
- Execution_Log.csv RUN-034 갱신.
- 다음 단계: O-1(인증 모델) 결정 후 Step 27(App↔LLM / AI Gateway Architecture) 진행.


## 2026-09-12 (계속) — Step 27 App↔LLM / AI Gateway Architecture 집필(RUN-035)

- Ian 요청: "step 27로 넘어가 주세요." (Step 26의 O-1 인증모델 결정은 아직 회신되지 않은 상태)
- **선행 작업 — 계층 경계 확정**: 기존 `19. LLM Tool Calling and Agent Orchestrator.md`(1,343행)를 먼저 통독. Step 19가 이미 Orchestrator 실행 루프, ContextBuilder, Action Schema, 3단계 Tool 검증(Schema→Rule→Execute), Rule reject 후 Agent Repair, MAX_RETRY_PER_DECISION=2, 중복분석 방지, LLMProvider 인터페이스를 정의해 두었음을 확인. 따라서 Step 27은 이를 다시 쓰지 않고 **"Agent 내부 판단 루프(Step 19)" vs "앱과 외부 LLM 사이의 경계 계층(Step 27)"**으로 책임을 6개 항목에 걸쳐 명시적으로 분리했다.
- **[중요 발견] Step 19 루프에 승인 게이트가 없음**: `19-5`의 실행 루프는 `decision → rule_engine.validate → tool_registry.execute`로 직행하여, Step 26 §12-1에서 정의한 승인 매트릭스(Level 2/3의 계획단위 승인, 전송범위 확대 시 항상 승인)를 강제하는 지점이 코드 어디에도 없다. 이대로 구현하면 Step 26의 승인 설계가 소실된다. Step 27 §7에서 `ApprovalGrant` 객체(allowed_tools / max_executions / transfer_scope / max_analysis_loops와 consumed 소비량 추적)를 도입하고 보완된 루프를 제시했으며, §15-2에 Step 19 갱신 요청으로 명시했다.
- **O-1 미결 상태에서의 진행 방법**: 인증을 `LLMProvider`에서 분리해 별도 `AuthProvider`로 캡슐화하고, Gateway는 "누구의 자격으로 호출하는가"를 `Principal`(mode / subject_id / department / display_name) 한 가지 개념으로만 인식하도록 설계(DD-029). 이로써 O-1이 A(BYOK)로 결정되든 B(사내 SSO)로 결정되든 Gateway·Orchestrator·UI 본체는 수정되지 않으며, `AuthProvider` 구현체만 교체하면 된다. **Ian의 요구(비용 귀속 주체의 명확화)를 아키텍처의 1급 개념으로 승격시킨 것이 이번 Step의 핵심 구조적 결정.**
- 산출물 `LLM_extention/06_제품운영설계(Step25-30)/27. App-LLM AI Gateway Architecture.md`(신규, 16개 절). 주요 내용:
  - Gateway 10단계 처리 파이프라인(가용성→승인강제→Context Filter→Prompt 조립→모델선택→인증바인딩→전송→응답검증→사용량집계→감사로그)과 단일진입점 원칙(DD-026).
  - LLM 호출 트리거 표 13종. 변수유형 판별·중복분석 판정·규격 비교 등 결정론적 판단에는 LLM을 호출하지 않는다(DD-027) — 비용·지연뿐 아니라 **재현성** 확보가 주된 근거.
  - 전송범위 S1(결과만·기본)/S2(익명화 표본 최대 200행)/S3(원본·정책상 차단)의 실제 JSON payload를 정의 — Step 26이 화면에서만 정의했던 3단계를 직렬화 규칙으로 확정. S1 예시로 UC-03 데이터를 사용해 개별 관측치 없이도 Agent 판단이 가능함을 보임.
  - Context Filter를 Gateway 내부에 두고 우회경로를 금지(DD-032). 근거: Step 19의 ContextBuilder는 "필요한 것을 고르는" 최적화 장치, Context Filter는 "나가면 안 되는 것을 막는" 보안 장치로 목적이 다르며, 겸하면 판단품질 개선 압력이 보안경계를 침식한다.
  - **결정 재시도(Step 19)와 전송 재시도(Step 27)의 카운터 분리(DD-034)** — 합치면 네트워크 장애로 인한 재전송이 "Agent 판단 실패"로 기록되어 Golden Case 평가와 Analysis Trace를 동시에 왜곡한다.
  - 오류 9종 분류표(재시도 가부·백오프·fallback·사용자 표시), 호출유형별 timeout 기본값, fallback 3단계(하위모델→대체Provider→**LLM 없는 저하 모드**, DD-035), circuit breaker 상태전이.
  - 대체 Provider 전환이 `Principal`을 바꾸는 경우 사용자 동의 없이 전환 금지(DD-036) — fallback이 비용 귀속 원칙을 조용히 무너뜨리지 못하게 하는 장치.
  - 토큰 집계 키의 첫 축을 `principal`로 두어 개인·부서 귀속을 데이터 구조로 구현. 단가는 외부 설정 파일로 두고 미확보 시 금액 미표시(DD-037).
  - 감사 로그 기록 항목(요청ID·principal·call_type·provider·model·transfer_scope·filter 제거내역·grant_id·tool args_hash·usage·latency·retries)과 미기록 항목(자격증명 원문·원본데이터·개인식별정보·프롬프트 전문).
  - Prompt Injection 4중 방어. 핵심 논지는 언어 수준 방어가 완전할 수 없으므로 **주입이 성공하더라도 실행 가능한 행동 집합이 Action Schema·Rule Engine·ApprovalGrant로 이미 제한되어 있어야 한다**는 것.
- 검토항목 연계: 모델 교체 시 Golden Case 재검증(RUN-030 지적사항)을 DD-031 후단에 "Golden Case 평가는 실제 배포 모델 조합 그대로 수행"으로 강제.
- DD-026~DD-039 14건 확정 제안, O-7~O-10 4건 신규 미결(대체Provider 허용 여부·하드한도·프롬프트 전문 로깅·컨텍스트 캐싱).
- Execution_Log.csv RUN-035 갱신.
- 다음 단계: Step 28(Data Privacy / Security / Reliability). Step 27이 넘긴 항목은 마스킹 대상 필드 판별 규칙, 자격증명 저장소 구현, 감사로그 보존정책, 세션 데이터 저장 위치(O-4), 사내 LLM 구성 시 완화 가능한 정책 범위.


## 2026-09-12 (계속) — Step 28 Data Privacy / Security / Reliability 집필(RUN-036)

- Ian 요청: "네. 이어서 진행해 주세요." (Step 27 완료 직후 연속 진행)
- Step 27 §16이 넘긴 5개 인계항목과 미결 O-3(권한체계)·O-4(세션 저장위치)·O-9(프롬프트 로깅)를 해소하는 것을 목표로 집필.
- **[핵심 논점 1] 이 앱의 데이터 위험 중심은 개인정보가 아니라 영업비밀이다**: 기존 설계(Baseline §30, Step 25-1 데이터 전송정책)는 "원본 데이터 전송 금지"에 집중해 왔으나, **집계 통계량만 전송해도 공정 규격(Target/LSL/USL)·불량률·설비 구성이 그대로 노출된다**는 점이 충분히 다뤄지지 않았음을 지적. 실제로 Step 27 §6-3의 S1 payload에는 `spec:{target,lsl,usl}`과 그룹별 평균·표준편차가 포함되어 있다. 해법으로 **규격 정규화 상대값 변환**을 제시 — 상대위치=(평균-Target)/(USL-LSL), 규격폭 대비 산포=SD/(USL-LSL)로 변환하면 LLM은 "규격 내이나 목표 대비 편중, 산포는 관리 가능 수준"이라는 제조 판단을 정확히 수행하면서도 토크 규격이 150~190이라는 사실 자체는 전송되지 않는다(DD-041).
- **[핵심 논점 2] 식별자 판별 규칙 확정(Step 27 최대 인계항목)**: Step 27은 "식별자는 마스킹한다"고만 정하고 앱이 어떤 컬럼을 식별자로 판단하는지는 미정으로 남겼다. 3계층 판별(① 사용자 선언 — 데이터 업로드 시 변수 역할 지정, 신뢰도 최상 ② 컬럼명 사전 매칭 ③ 값 패턴 휴리스틱)과 **미분류 문자열 컬럼의 fail-closed 처리**를 확정(DD-042). 근거는 두 방향 오판의 비용 비대칭성 — 식별자를 일반 컬럼으로 오판하면 개인정보가 외부로 나가 복구 불가, 일반 컬럼을 식별자로 오판하면 분석 정보가 일부 줄어들 뿐이며 사용자가 정정 가능.
- **[핵심 논점 3] 가명화로 분석 가치와 식별성을 분리**: "작업자별 토크 차이가 있는가"는 반드시 분석해야 하지만 그 분석에 작업자가 누구인지는 필요 없다. 세션 단위 일관 가명(OP_01 등)으로 치환하고 매핑 테이블은 세션 메모리에만 유지, 화면에는 원문 표시(DD-043). ANOVA·교차분석·이상값 탐지·교란요인 통제가 전부 동일하게 동작함을 명시.
- **[신규 발견] 공용 PC 문제 — 개인 단위 인증의 현실적 약점**: Step 26 DD-016(사용자 단위 인증)과 Step 27의 Principal 설계는 암묵적으로 "1인 1 PC"를 가정한다. 그러나 라인 사무실 공용 PC에서 여러 작업자가 같은 Windows 계정을 쓰면 OS 자격증명 저장소의 개인 API Key가 공유되어 **Ian이 제기한 비용 귀속 요구가 현장에서 무너진다.** 대응 3안(기억하지 않음 모드 / 명시적 로그아웃 / 사내 SSO)을 제시하고, "이 PC에 저장하지 않음" 옵션을 공용 PC 설치의 기본값으로 확정(DD-047). **아울러 O-11(현장 PC의 개인전용/공용 비중)을 신규 제기하고 이를 O-1 인증모델 결정의 선행 확인 정보로 지정** — 공용 PC 비중이 높으면 모델 A(BYOK)는 운영상 취약하고 모델 B(사내 SSO)가 사실상 유일한 선택이 된다.
- 기타 확정: 요인 조합 표본수 5 미만 시 재식별 경고를 통계적 표본부족 경고와 함께 표시(DD-044, 한 번의 검사로 두 위험 동시 고지) / 정책 완화는 Provider의 `data_residency` Capability를 근거로만 허용하고 외부 클라우드에는 원본전송 옵션 자체를 미노출(DD-045) / **원본 데이터를 앱 저장소에 복제 보관하지 않고 경로·해시·버전만 기록**(DD-048, 보관하지 않는 데이터는 유출될 수 없다는 원칙으로 보안 표면 축소) / TLS 인증서 검증 비활성화 경로를 코드·설정 어디에도 제공하지 않음(DD-050) / 세션 자동저장 3시점과 직전 1버전 백업(DD-052) / 재현성 기록 세트 10항목에 **"이 분석 방법을 사람이 골랐는가 AI가 골랐는가"**를 포함(사후 검증에 필요하나 기록하지 않으면 복원 불가).
- 미결 해소: **O-3** → MVP는 OS 사용자 계정 종속, 앱 자체 로그인 미도입(DD-046). **O-4** → 세션은 로컬 저장 기본, 사내 서버는 Phase 2(DD-049). **O-9** → 프롬프트 전문 기본 미기록, 사용자 동의 시에만 30일 보존(DD-051).
- **법적 해석은 제품 설계 범위 밖임을 §0-3에 명시**하고, 개인정보 처리 근거·보유기간 적법성·국외 이전 해당 여부는 사내 법무·정보보호 부서 확인이 필요함을 고지. 보존기간 제안(감사로그 1년, 오류 프롬프트 30일, 사용량 2년)은 사내 정책 확정 시 그에 맞추도록 단서를 달았다.
- DD-040~DD-052 13건 확정 제안, O-11~O-13 3건 신규 미결.
- Execution_Log.csv RUN-036 갱신.
- 다음 단계: Step 29(Schema Contract). 입력은 Step 26 §16 화면↔상태 매핑, Step 27 §7-2 ApprovalGrant·§10-1 감사로그 스키마, Step 28 §13-2 변수역할·데이터분류·가명화·재현성 기록.


## 2026-09-12 (계속) — 운영환경 확정에 따른 미결항목 일괄 결정(RUN-037)

- Ian이 운영환경 4개 전제를 확정: **E-1** 사용자는 모두 개인 PC 사용 / **E-2** 회사가 LLM Enterprise 상품 사용 중 / **E-3** 앱은 사내 전용 / **E-4** 앱 자체 ID/PW 로그인으로 권한 부여된 인력만 접근. 아울러 "보안 문제는 크지 않다"는 판단과 함께 기획서 조정 및 미결항목 진행을 지시.
- **[가장 중요한 변경] O-1 인증 모델 결정이 뒤집혔다.** Ian이 최초에 제기한 요구("통합 API Key로 인증하면 사용 토큰을 부담할 부서가 없으므로 개인 계정 인증이 되어야 한다")를 Step 26 §7-1에서 "비용 귀속(진짜 요구)"과 "계정 로그인(구현 수단)"으로 분리해 두었는데, **E-2를 대입하면 비용 부담 주체가 회사(Enterprise 계약)로 이미 명확**하므로 원래 요구가 계약 수준에서 해소된다. 남는 요구는 "누가 얼마나 썼는지 보이는 것(가시성)"이며 이는 E-4의 앱 로그인 계정으로 달성된다. 따라서 **개인별 API Key(BYOK) 방식은 불필요할 뿐 아니라, 회사가 이미 Enterprise 비용을 지불하는 상황에서 개인 키를 병행하면 이중 비용이 발생**한다. 조직 Enterprise 연결 + 앱 로그인 계정 기반 사용자 식별로 확정(DD-053), **Step 26 DD-017 폐기**.
- **[설계 검증] Step 27의 AuthProvider 분리가 실제로 효과를 냈다.** Step 27 DD-029에서 인증을 `LLMProvider`에서 떼어내 `AuthProvider`로 캡슐화하고 Gateway가 `Principal`만 인식하도록 설계해 둔 덕분에, 인증 모델이 BYOK에서 Enterprise로 완전히 바뀌었음에도 **Gateway·Orchestrator·UI 본체는 수정되지 않는다.** `Principal.mode`에 `ENTERPRISE`를 추가하고 구현체만 교체하면 된다. 미결항목을 흡수하는 구조로 설계한 판단이 검증된 사례로 기록해 둔다.
- **O-3 재결정**: E-4에 따라 **Step 28 DD-046(앱 로그인 미도입) 폐기**. 앱 자체 ID/PW 로그인과 3등급 권한(일반 사용자/엔지니어/관리자)을 도입하고(DD-054), Step 26 §3-2에서 "화면 옵션으로만 처리"로 두었던 3개 역할을 권한 등급으로 승격. Step 26 화면 목록에 **S-00 로그인** 추가, S-08(AI 연결 설정)은 개인 자격증명 입력 화면에서 **조직 연결 상태 확인 + 전송범위 설정** 화면으로 성격 변경.
- **O-4 재결정**: 앱 로그인이 생기고 사내 전용이므로 세션을 계정에 귀속시킬 수 있게 됨. 세션은 앱 로그인 계정 귀속, **서버 저장이 가능한 스키마로 설계**하되 MVP 1차는 로컬로 시작(DD-055). 근거로 제조 현장의 실질 가치(교대조 인수인계, PC 교체 시 이력 승계, 팀 단위 분석 이력 축적)를 제시.
- **보안 정책 조정 — 완화 항목과 유지 항목을 구분**: Ian의 "보안 문제는 크지 않다"는 판단을 반영하되, 완화가 타당한 항목과 완화해도 얻는 것이 없는 항목을 나누어 제시.
  - **완화**: C3 공정기밀의 규격 **실값 전송을 기본**으로(DD-057, 상대값 변환은 옵션 — 규격 이탈 예상 개수·공정능력지수를 직접 언급할 수 있어 제조 판단 품질이 우수) / S3 원본 전송을 **관리자 설정으로 허용 가능**(DD-058, 단 기본값 S1 유지의 근거를 보안이 아니라 **토큰 비용·지연**으로 재정의 — 원본을 보내도 Agent 판단 품질은 오르지 않음) / 프롬프트 로깅을 관리자 설정 상시 수집 가능·90일 보존으로 완화(DD-059) / 공용 PC 대비 조치 철회, 자격증명 저장이 기본값(DD-056).
  - **유지 권고**: **C4 가명화(DD-043)** — 개인정보는 사내 처리라고 해서 자유로워지지 않으며(사내 시스템에도 처리 근거와 목적 제한이 적용됨), 가명화는 분석 가치를 전혀 잃지 않고 구현 비용도 낮아 **완화해서 얻는 이득이 실질적으로 없음**. 그 외 식별자 fail-closed(DD-042), 재식별 경고(DD-044), 원본 미복제 보관(DD-048, 보안이 아니라 원본-사본 동기화 문제 방지가 주목적), TLS 검증 비활성화 금지(DD-050), 재현성 기록 세트(DD-052, 보안이 아니라 품질 요건)도 유지. C5 고객·계약 정보는 기본 차단 유지하되 관리자 해제 가능.
- **나머지 미결 일괄 결정**: O-2(회사 Enterprise 공급자를 단일 기본 Provider) / O-5(최대 루프 5회) / O-7(대체 Provider 미구성 → **Step 27 fallback 체인이 3단계에서 2단계로 축소**, DD-036은 적용 상황 소멸) / O-8(하드 한도 미도입, 부서별·사용자별 사용량 리포트를 관리자 기능으로) / O-10(컨텍스트 캐싱 사용) / O-11(개인 PC 확정) / O-12(규격 실값) / O-13(재식별 임계값 5 유지).
- **문서 동기화 실행**: 결정 기록만 남기면 이후 세션이 낡은 결정을 그대로 참조하게 되므로, `26.`/`27.`/`28.` 세 문서 상단에 **개정 안내 블록을 직접 삽입**(Desktop Commander edit_block). 각 안내에는 폐기·개정된 DD와 그 대체 항목, 그대로 유효한 DD를 명시.
- 산출물 `LLM_extention/06_제품운영설계(Step25-30)/28-1. 운영환경 확정 및 미결항목 결정.md`(신규, 12개 절). DD-053~DD-059 7건 신규, 기존 DD 2건 폐기(DD-017·DD-046)·6건 개정(DD-041·045·047·049·051 및 DD-016 재해석).
- **남은 확인사항 4건**: ①회사 Enterprise 상품이 프로그래밍 호출(API)을 포함하는지(채팅 상품과 API는 별개 계약인 경우가 많음 — 경우에 따라 사용량 리포트가 가시성 목적인지 내부청구 근거인지가 갈림) ②기본 Provider·모델 지정 ③앱 로그인의 사내 인증체계(AD/SSO) 연동 여부 ④세션 저장용 사내 서버 인프라 가용 여부. **네 건 모두 Step 29 진행을 막지 않음을 확인**.
- Execution_Log.csv RUN-037 갱신.
- 다음 단계: Step 29(Schema Contract). 미결항목이 전부 해소되어 진행 가능.


## 2026-09-12 (계속) — Step 29 웹앱 운영 아키텍처 신설 집필 및 인증 결정 정정(RUN-038)

- Ian이 추가 전제를 확정: **E-5** 개인별로 승인된 금액에 한정하여 사용하므로 **모두 개인 계정으로 로그인** / **E-6** 앱은 **웹앱 형태**이며 동시 접속 고려 필요 / **E-7** 원본은 Excel(주)·CSV / **E-8** 원본 데이터는 보유기간 설정 후 삭제 / **E-9** 분석 데이터·보고서의 조회·다운로드 기간을 앱 관리자가 설정 / **E-10** PRISM은 이를 위한 '관리자 콘솔' 페이지를 이미 구현. 아울러 **에러 발생에 대한 복귀 로직**을 명시적으로 요구.
- **[중요 정정] Step 28-1의 비용 귀속 판단이 틀렸음을 확인하고 정정.** Step 28-1 §2-1에서 "회사가 Enterprise 계약 주체이므로 비용 귀속 문제가 계약 수준에서 해소되었다 → 개인별 API Key 불필요"라고 판단했으나, 실제로는 **개인별 승인 금액으로 비용이 배분·통제되고 인증도 개인 계정 단위**로 이루어지고 있음이 확인되었다. 즉 **Ian이 최초에 제시한 "개인 계정으로 인증받는 형식이 되어야 한다"는 요구가 처음부터 정확했다.** 이에 따라 DD-053(조직 Enterprise 연결)을 DD-061(개인 계정 인증)로 정정하고, O-8(하드 한도 미도입) 역시 DD-063(개인별 승인 한도 추적·경고·차단)으로 정정했다. 한도 소진 시에도 Manual 분석은 제한 없이 계속되며, 진행 중이던 Agent 분석은 현재 단계를 마치고 Finding·Evidence를 정리해 보여준 뒤 정지하도록 설계.
- **[설계 검증 재확인]** 인증 전제가 BYOK → Enterprise → 개인 계정으로 **두 차례 뒤집혔음에도** Step 27 DD-029(AuthProvider 분리, Gateway는 Principal만 인식) 덕분에 Gateway·Orchestrator·UI 본체는 매번 무수정이었다. 미결항목을 구조로 흡수한 설계 판단이 두 번 검증된 셈이다.
- **[웹앱 전환에 따른 전제 재정의]** Step 26~28은 암묵적으로 데스크톱 앱을 가정하고 있었으며, 웹앱 확정으로 다수 결정이 폐기·개정되었다. **DD-048(원본 데이터를 복제 보관하지 않는다) 폐기** — 웹앱에서는 업로드 자체가 복제이므로 성립 불가하며, Ian이 요구한 보유기간·삭제 정책으로 대체. **DD-018/DD-030(OS 자격증명 저장소) 개정** — 서버 측 암호화 저장소로 변경하되 "호출 직전 복호화·즉시 폐기" 원칙은 유지하고, **관리자를 포함한 누구도 평문 조회 불가**를 명시(DD-062, 개인 계정 비용이 개인에게 귀속되므로 자격증명 유출은 개인의 금전 손해로 직결). **DD-056 폐기**("이 PC에 저장하지 않음"은 웹앱에서 무의미). 세션은 서버 저장으로 확정.
- **[동시성] 이 앱 특유의 위험을 식별**: 일반 업무용 웹앱과 달리 사용자마다 큰 데이터를 메모리에 올려 계산하므로, 100만 행 20열 Excel을 10명이 동시 처리하면 수 GB로 서버 메모리가 고갈된다. 해법으로 **업로드 1회 파싱 → 열지향 중간 포맷 변환 → 이후 모든 분석은 필요한 열만 부분 로드**(DD-064) 전략을 제시 — 메모리·속도·재현성 3개 문제를 동시에 해결. 그 외 사용자별 작업 큐 격리와 자원 상한(DD-066, head-of-line blocking 방지), 세션 버전 기반 낙관적 잠금(DD-067), 부하 4단계 저하 전략(조회 기능은 마지막까지 유지).
- **[Excel 파싱 위험]** 제조 현장 Excel은 헤더 위치·병합셀·텍스트 저장 숫자·천단위 구분자·날짜 직렬번호·소계 행 혼입 등으로 **실사용 에러의 최대 발생원**임을 지적하고, 파싱→구조추정→**사용자 확인**→확정의 4단계를 필수화(DD-065). 소계 행이 데이터로 섞이면 그 위에서 Agent가 아무리 정교하게 추론해도 결론이 틀린다는 점이 근거.
- **[에러 복구 로직 — Ian 명시 요구사항]** 복구 4원칙(작업은 객체다 / 재시도는 안전해야 한다 / 진행분은 버리지 않는다 / 실패는 숨기지 않는다) 위에: 영속 Job 레코드와 8개 상태 머신(DD-068), 멱등 키(DD-069 — ANALYZE 멱등키를 Step 19 §19-14의 중복분석 판정과 **동일 기준**으로 설계하여 네트워크 재시도가 "중복 분석"으로 잘못 기록되지 않게 함), heartbeat 미갱신 작업의 INTERRUPTED 자동 재투입(DD-071), **Agent 재개 지점을 Analysis State 자체로 삼아 별도 체크포인트 메커니즘 불필요**(DD-070 — Baseline DD-010의 State 명시 저장 결정이 실제 값을 내는 지점), 실패 유형 13종별 복구 정책표, 부분 실패 시 성공분 유지와 미도출 결론 명시(DD-072), 승인 대기 30분 타임아웃.
- **[데이터 수명주기 — Ian 요구]** 데이터 자산 5종(A1 원본/A2 중간포맷/A3 세션·결과/A4 보고서/A5 로그)별 보유기간을 관리자 콘솔에서 설정(DD-073). **조회 기간과 다운로드 기간을 분리**하여 반출 경로는 먼저 막고 사내 조회는 더 오래 허용. **원본 삭제와 재현성의 충돌을 정면으로 다룸** — 원본이 90일 후 삭제되면 6개월 전 분석의 재현이 불가능하나 품질기록 보존 의무가 있을 수 있으므로, ①재현성 메타데이터는 A3 보유기간까지 존속(DD-074) ②결과 화면에 원본 만료 표시 ③보존 지정(Hold, DD-075) 3장치로 해소. 소프트 삭제+유예 14일+사전 통지, 보유기간 단축 시 영향 범위 미리보기(DD-076, 설정 실수로 인한 대량 소실 방지).
- **[관리자 콘솔]** PRISM 선례를 따라 9개 영역 설계(DD-077): 사용자·권한 / LLM 연결정책 / **사용한도·사용량** / **데이터 보유기간** / **보존 지정** / 전송·보안정책 / **작업·큐 운영(실패 작업 재투입)** / 감사로그 / 시스템 상태. **관리자도 볼 수 없는 것**(개인 LLM 자격증명 평문, 타인의 분석 데이터 내용)을 명시 — 관리자 계정 탈취가 전사 데이터 노출로 이어지는 구조를 만들지 않기 위함이며, 관리자는 운영 역할이지 데이터 열람 역할이 아님을 원칙으로 세움.
- DD-060~DD-077 18건 신규. 기존 DD 3건 폐기(DD-048·DD-053 정정·DD-056), 4건 개정.
- 문서 동기화: `28-1` 상단에 정정 안내 삽입. 폴더명 `06_제품운영설계(Step25-30)` → `(Step25-31)`로 갱신.
- **Step 번호 조정**: 본 Step 신설로 Schema Contract는 Step 30, Final MVP Specification은 Step 31로 이동.
- 남은 확인사항 4건 신규(개인별 승인금액의 단위·주기와 취득 경로 / PRISM 관리자 콘솔 UI 규약 재사용 범위 / 기본 보유기간이 사내 품질기록 보존규정과 정합하는지 / 예상 동시접속 규모와 최대 데이터 크기). 모두 Step 30 진행에는 지장 없음.
- Execution_Log.csv RUN-038 갱신.


## 2026-09-12 (계속) — Step 30 Schema Contract 집필(RUN-039)

- Ian 요청: "진행해 주세요." (Step 29 완료 후 연속 진행)
- **선행 확인**: 기존 `13. Agent Data Contract and Interface 설계.md`(1,286행)를 읽어 AnalysisSession·ProblemModel·DatasetContext·AnalysisPlan·ToolCall·ToolResult·Finding·Evidence·Hypothesis·Confounder·NextAction·AnalysisHistory 12종의 **정확한 필드명**을 확인한 뒤 작성. Step 27이 Step 19를 다시 쓰지 않았던 것과 동일한 원칙으로, **Step 13 필드는 하나도 삭제하지 않고 확장만** 했다 — Golden Case(Step 23·24)가 기존 필드명을 전제로 작성되어 있어 이름이 바뀌면 평가 자산이 전부 깨지기 때문.
- 계약을 **3계층으로 분리**(DD-078): L1 Agent Core(Step 13의 12종) / L2 Operations(Principal·BudgetStatus·LlmConfig·ApprovalGrant·Job·DatasetArtifact) / L3 Administration(RetentionPolicy·HoldRecord·AdminSetting·UsageRecord·AuditRecord). 근거는 **Core가 운영 사정에 오염되지 않아야 한다**는 것 — 예컨대 Finding에 보유기간 필드를 직접 넣으면 Golden Case 평가 코드가 보유기간 개념을 알아야 한다. 보유기간은 자산 수준에서 관리한다.
- Step 13 객체 확장: AnalysisSession에 owner_user_id·version(낙관적 잠금)·mode_history·approval_grants·conversation·usage·retention 추가하고 status에 WAITING_APPROVAL·PAUSED 추가 / DatasetContext의 variables에 role·data_class·pseudonymized·role_source 추가하고 parse_config(헤더 행·병합셀·제외 행)와 artifacts·small_cell_warning 추가 — **같은 Excel도 헤더 행을 다르게 잡으면 전혀 다른 데이터가 되므로 parse_config는 재현성의 필수 구성요소** / AnalysisHistory에 reproducibility 블록(재현성 10항목, method_selected_by 포함)·multiplicity_correction·measurement_system_confirmed·job 연계 추가 / Finding·Evidence에 created_at·source·revalidation 추가, EvidenceStatus에 DOWNGRADED·EXPIRED_SOURCE 추가.
- **Evidence 하향 조정 규칙 확정**(Step 26 §11-2에서 Step 29(현 30)로 미뤄둔 항목): **자동 하향은 하지 않는다.** 새 데이터가 기존 결론과 충돌하면 revalidation.required_when에 해당하는 사건으로 표시하고 사용자·Agent가 판단하게 한다. 시스템이 임의로 Evidence 등급을 내리면 그 판단 자체가 추적 불가능한 근거가 되기 때문.
- **[핵심 기여] 직렬화 제외 / LLM 전송 제외 / 로그 기록 제외가 서로 다른 3개 필터임을 논증**(DD-079). 구현에서 가장 흔한 오류가 이 셋을 하나의 exclude 목록으로 처리하는 것인데, 12개 항목 교차표로 조합이 모두 다름을 보였다 — 식별자 원문은 **저장은 해야 하고(화면에 실명 표시) 전송은 안 되며 로그에도 남으면 안 된다**, 자격증명은 암호화 저장O·전송X·로그X(지문만), ToolCall.arguments는 저장O·전송O·로그는 해시만. 하나의 목록으로는 표현 불가능.
- **불변식(Invariants) 17개를 계약의 일부로 고정**(DD-082)하고 8개 검증 주체(Schema Validator/Rule Engine/AI Gateway/Approval Enforcement/Job Scheduler/State Repository/Retention Worker/Golden Case Evaluator)에 배정. **스키마 필드 정의만으로는 계약이 절반만 완성된다**는 논지. 주요 불변식: Finding은 source_analysis 필수, Evidence는 실제 실행된 basis 필수, causal_strength=EXPERIMENTALLY_SUPPORTED는 E4에서만, Hypothesis CONFIRMED는 E4 Evidence가 있을 때만, 동일 멱등키 SUCCEEDED Job은 최대 1개, Level≥1에서 Tool 실행은 유효 Grant 요구, IDENTIFIER 변수 원문은 LLM payload에 미출현, UNCLASSIFIED 문자열 변수는 fail-closed 제외, budget EXHAUSTED면 신규 LLM Job 미생성, hold 자산은 삭제 제외. Rule Engine과 Golden Case Evaluator가 INV-01~06을 **이중 검증**하는 것은 실행시점 차단과 회귀 탐지라는 서로 다른 목적의 의도된 중복임을 명시.
- 세션 보유기간이 2년(Step 29)이므로 **그 사이 스키마는 반드시 바뀐다**는 전제 하에 schema_version과 호환성 변경 규칙 확정(DD-081): 선택 필드 추가·열거형 값 추가는 허용(minor), **필드 의미 변경과 삭제는 금지**(폐기 표시만), 읽기는 구버전 호환 보장·쓰기는 항상 현재 버전.
- PseudonymMap은 계약에 정의하되 **어떤 영속 저장소에도 기록하지 않고 원본으로부터 재생성**(DD-083) — 웹앱 전환으로 세션이 서버에 저장되므로 매핑이 함께 저장되면 가명화가 무의미해짐. reproducibility 블록은 원본 삭제 후에도 자체 완결적이어야 하며, group_summary 중복 저장은 **원본이 사라지는 것이 정상 동작인 시스템에서는 필수적인 비정규화**임을 명시(DD-084).
- 열거형 사전 20종을 한곳에 집약 — 문자열 리터럴이 흩어지면 반드시 어긋나기 때문.
- DD-078~DD-084 7건 신규.
- **잔여 항목 재기록**: `chi_square_test`가 Step 13 Evidence 예시와 본 문서 §3에 basis로 등장하나 공식 Tool Registry(Step 18 §18-3) 등재는 **RUN-030 이래 여전히 미확인**. Step 31 이전 정리를 다시 권고.
- Execution_Log.csv RUN-039 갱신.
- 다음 단계: Step 31(Final MVP Product Specification) — 새 설계가 아니라 Step 1~30을 하나의 사양서로 압축하고 MVP 범위·인수기준을 확정하여 개발 착수 가능 상태로 만드는 단계.


## 2026-09-12 (계속) — Step 31 Final MVP Product Specification 집필 / 설계 단계 완료(RUN-040)

- Ian 요청: "네 진행해 주세요." (Step 30 완료 후 연속 진행)
- Step 31은 새 설계를 하지 않고 **Step 1~30을 하나의 사양서로 압축하고 MVP 범위와 측정 가능한 인수 기준을 확정하여 개발 착수 가능 상태로 만드는 것**이 목적. 이로써 LLM_extention 트랙의 설계 단계가 완료됨.
- **[장기 미해소 항목 종결] A-3 `chi_square_test` Tool Registry 미등재 문제 해소**(DD-086). RUN-030에서 처음 지적한 이래 RUN-031·032·039까지 네 차례 기록만 반복되던 항목으로, Step 31에서 **MVP Tool Registry에 `chi_square_test`와 `proportion_test`를 정식 등재**하는 것으로 결론. 근거는 **UC-03 Golden Case(Step 23·24)가 이미 불량률 비교에 카이제곱검정을 사용하고 그 기대 결과(p≈.0507)까지 명시**하고 있고, 벤치마크 Use Case인 UC-11도 불량률 비교가 핵심이라는 것 — **Golden Case가 요구하는 Tool은 MVP에 있어야 한다**는 논리이며, Baseline §10이 Chi-square를 Phase 2로 분류한 것은 이 의존 관계를 반영하지 못한 것으로 판단.
- **변경 불가 제품 원칙 10개를 위반 예시와 함께 명시**(DD-085): LLM은 통계를 계산하지 않는다 / Manual은 LLM 없이 100% 동작 / Manual과 AI는 동일 Engine 공유 / 모든 Tool은 Rule 검증 통과 / 승인 범위 밖 실행 없음 / 모든 LLM 호출은 Gateway 통과 / 식별자 원문 미전송 / 관찰 데이터로 인과 확정 금지 / 미실행 결과 주장 금지 / 화면 서술에 출처 표기. 각 원칙에 **구현 단계에서 실제로 발생하기 쉬운 위반 예시**를 붙였다 — 예컨대 "해석 문장을 만들며 평균을 다시 계산", "문장 하나 생성하려고 Provider 직접 호출", "이미 검증된 계획이라며 Rule 우회". 개발 Agent가 성능·편의를 이유로 완화하지 못하도록 하는 장치.
- **MVP In/Out을 이유와 이관 단계까지 명시**: 제외 항목(SPC·공정능력·Pareto·수율, 다중회귀/ANCOVA 기반 교란 통제 일반화, MSA 완전 모듈, 제조·사내 Knowledge RAG, 다중 CTQ·상호작용, 사내 LLM 연동, 세션 공유, BYOK, 모바일)마다 왜 빼는지와 Phase 2/3 중 어디로 가는지를 기록.
- **인수 기준 40여 개를 7개 범주로 측정 가능하게 기술**(DD-087): AC-S 통계정확성(Golden Dataset 허용오차, welch 8개 단위테스트, Result Validator, ddof=1) / AC-A Agent행동(GC-UC03-001 90점 이상, **Critical FAIL 0건**, Forbidden Conclusion 미생성, UC-11 교란 탐지, 반복 실행 시 통계 결과 동일) / AC-F 기능(AI 미연결 상태에서 전 과정 완결, State 인계, 출처 표기, 다중비교 표시, MSA 질문, 헤더 3행·병합셀·소계 혼입 Excel 처리) / AC-P 성능(100만행 5분 이내, t-test 3초, 동시 10명에서 조회 2초) / AC-R 신뢰성(워커 강제종료 후 90초 내 감지·완료단계 미재실행, 멱등성, 서버 재시작, 부분 실패 표시, 두 탭 충돌) / AC-C 보안(식별자 원문이 payload에 **단 한 번도** 미출현, fail-closed, 가명매핑 미저장, 자격증명 관리자도 조회 불가, 한도 차단, 보존지정 자산 미삭제, 원본 삭제 후 재현성 메타데이터 조회) / AC-I 불변식(INV-01~17 강제 및 부정 테스트).
- **개발 Task를 Step 19의 13개에서 20개로 확장**하고 4개 마일스톤(M1 계약·엔진 / M2 상태·실행·운영 / M3 Vertical Slice·화면 / M4 운영·관리·검증)으로 묶어 각 Task에 인수기준을 배정(DD-088). **T-13(Manual Vertical Slice) 완료 시점에 이미 사용 가능한 제품이 존재**하므로 AI 계층 개발이 지연되어도 출시가 막히지 않는다는 일정상 의미를 명시하고, 일정 압박 시에도 M1과 T-13은 축소 대상이 아님을 못박음.
- **문서 권위 색인 신설**: 문서가 30개를 넘고 개정·정정이 반복되어(인증 모델 3회 변경, 제품 형태 데스크톱→웹앱 전환) 구현자가 낡은 결정을 참조할 위험이 실재하므로, 주제별 최종 권위 문서를 표로 고정. Step 19가 "Agent 실행 루프의 권위"이되 **승인 게이트가 미반영 상태임을 함께 표기**.
- **DD-089**: Step 19 문서에 승인 확인 단계가 반영되기 전에는 T-12(Orchestrator)를 착수하지 않는다 — 구현자가 Step 19만 보고 개발하면 Step 26의 승인 매트릭스가 코드에서 누락되기 때문.
- 위험 7종과 완화책, 개발 착수 전 체크리스트 12항목(확인 A~H는 착수를 막지 않으나 **현장 실제 Excel 샘플 확보는 T-07 착수 전 필수**).
- DD-085~DD-089 5건 신규. **LLM_extention 트랙 설계 단계(Step 1~31) 완료.**
- Execution_Log.csv RUN-040 갱신.
- 다음 행동 권고: ①현장 Excel 샘플 확보 ②Step 19 승인 게이트 반영 ③Baseline design-notes.md v1.4 갱신 ④T-01부터 순차 착수.


## 2026-09-12 (계속) — Ian 확인요청 3건 반영: 시각화·보고서 사양 및 LLM 연결 아키텍처 정정(RUN-041)

- Ian 확인·추가 요청 3건: ①그래프는 SVG로 제공, 사용자 요청 시에만 보고서 생성(선택적 버튼), 보고서 형식은 HTML ②"웹앱이라 서버 사이드 렌더링인데 LLM은 개인 계정으로 로그인하여 개인 로컬 PC에서 로딩·연동되어야 하는데 그렇게 설계되어 있는지" ③"분석 도구별로 어떤 그래프가 제공되는지 명문화되어 있는지"
- **[확인 결과] ②와 ③ 모두 실제 공백이었음.**
  - **③ Tool별 그래프 매핑 미정의 확인**: 그래프 종류 목록(Baseline §26의 11종)과 시각화 Tool 등록(Step 31 §3-2의 5종)은 있었으나 **"어느 분석에 어떤 그래프가 따라오는가"는 어디에도 정의되어 있지 않았다.** 매핑 없이 구현하면 개발자가 임의로 정하게 되어 "t-test를 했는데 그래프가 없다", "ANOVA에 히스토그램만 나온다" 같은 결과가 나오며, 이는 원 기획서의 핵심 UX 원칙("P-value보다 그래프를 먼저 보여준다")에 직결되는 공백.
  - **② LLM 호출도 서버 사이드로 설계되어 있었음**: Step 29 DD-062가 "개인 LLM 자격증명은 서버 측 암호화 저장소에 보관하며 복호화는 AI Gateway 호출 직전에" 였으므로, **서버가 개인 자격증명을 보관하고 서버가 호출**하는 구조. Ian의 의도("개인 로컬 PC에서 로딩되어 연동")와 불일치했다.
- **산출물 1 — `31-1. 분석 도구별 시각화 사양 및 보고서 사양.md`(신규)**
  - 시각화 Tool을 **5종 → 10종으로 확장**(DD-091). 신규: `bar_chart`·`mean_ci_plot`·`paired_plot`·`difference_ci_plot`·`residual_plot`·`normal_probability_plot`. 개칭: `comparison_plot`→`mean_ci_plot`(이름만으로 무엇을 그리는지 알 수 없었음), `trend_chart`→`line_chart`(통계적 의미와 그래프 형태 분리).
  - **분석 Tool 30종 전체에 기본(필수)·보조(선택) 그래프 매핑표 신설**(DD-092). 주요 판단: 사후검정(Tukey/Games-Howell)은 `difference_ci_plot`으로 **0선을 기준으로 어느 쌍이 유의한지**를 보여줌 / 대응 t-test는 `paired_plot`(개체별 변화 방향)+차이값 히스토그램 / **단순회귀는 `residual_plot`을 필수로 지정** — R²와 회귀계수만 보면 비선형 관계나 이분산을 놓치며, 잔차 그래프는 통계 비전문가에게도 "점들이 무늬 없이 흩어져 있으면 괜찮다"는 판단 기준을 줄 수 있음 / 카이제곱·비율검정은 오차막대 포함 비율 막대(표본 수가 다르면 비율 차이의 의미가 달라지므로 CI 표시가 중요).
  - 그래프 공통 필수요소(축 단위·표본수·결측 표기)와 **제조 맥락 요소(규격 상하한·목표선·규격 이탈 표시)**를 규칙화(DD-094). 규격선 표시가 이 제품을 일반 통계 도구와 구분하는 지점 — "평균이 다르다"보다 "규격 안에 있는가"가 현장의 실제 질문이기 때문.
  - **표본 수에 따른 표현 전환**(DD-095): n≥20 정상 box / 5≤n<20 box+개별점 중첩 / n<5 box 미표시·개별점만+경고. 근거는 표본 3개로 사분위수 상자를 그리면 실제보다 많은 정보를 가진 것처럼 보이며, 통계 비전문가일수록 그림을 그대로 신뢰하므로 **표본이 적다는 사실 자체가 그림에서 드러나야 한다**는 것. 임계값 5는 Step 28 DD-044(재식별 경고)와 일치해 한 번의 검사로 두 경고 표시 가능.
  - 그래프는 전부 **SVG**(DD-090) — 확대해도 깨지지 않아 규격선 근처 미세 차이 확인 가능, 텍스트가 텍스트로 남아 검색·접근성 확보, HTML 보고서에 인라인 삽입되어 **이미지 파일 없는 단일 파일** 완결, 서버 렌더링에 래스터화 엔진 불필요.
  - **보고서는 자동 생성하지 않고 사용자가 [보고서 생성] 버튼을 누른 시점에만 Job으로 생성**(DD-096) — 자동 생성은 워커 자원·보유기간 관리 대상(A4 자산)·불필요한 파일 누적 세 가지 비용을 만들며, 분석은 여러 번 반복되지만 보고서가 필요한 시점은 그중 일부.
  - **보고서 형식 HTML 단일 확정**(DD-097, Step 31의 "PDF, HTML" 개정) — PDF 생성에 필요한 headless browser 등 별도 렌더링 엔진 의존성과 장애 지점이 제거되고, 브라우저 인쇄로 PDF 저장이 가능하므로 PDF 요구가 대체됨. **T-16 작업량 감소.**
- **산출물 2 — `31-2. LLM 연결 아키텍처 정정 - 클라이언트 사이드 연동.md`(신규)**
  - **LLM 호출을 사용자 개인 PC(브라우저)로 전환**(DD-098, **Step 29 DD-062 폐기**). 전환이 타당한 핵심 이유는 **자격증명 보관 책임이 사라진다**는 것 — 개인 계정 비용이 개인에게 귀속되는 구조에서 회사 서버가 전 직원의 LLM 자격증명을 보관하는 것은 보관 자체가 위험이고 사용자 입장에서도 자기 계정 정보를 회사 서버에 맡기는 셈. 부수 효과로 속도제한·비용이 물리적으로 개인 단위 격리되고 사내 서버의 외부 트래픽이 줄어 방화벽 정책이 단순해짐.
  - **핵심 안전장치 — "브라우저는 전달자이지 작성자가 아니다"**(DD-099). 가명화·식별자 제거·전송범위 판정은 **원본 데이터에 접근 가능한 쪽에서만 수행 가능**하고 원본은 서버에 있으므로, Context Filter·Prompt 조립·승인 확인·모델 선택·감사는 전부 서버에 남는다. 서버는 **이미 여과가 끝난 요청 패키지**를 브라우저에 넘기고 브라우저는 수정 없이 전송만 한다. 브라우저에 필터를 두면 원본을 브라우저로 내려보내야 하므로 Step 28 설계가 무너진다.
  - 회송된 LLM 응답의 변조 가능성은 **새로운 위험이 아님**을 논증(DD-100) — LLM 응답은 원래부터 신뢰하지 않는 입력이었고(Structured Output 강제·Rule Engine·Prompt Injection 방어), 변조된 응답이 할 수 있는 최대치는 선언된 Tool 집합 안에서 승인된 범위의 분석을 요청하는 것뿐이며 그것은 사용자가 Manual로도 할 수 있는 일.
  - Orchestrator는 서버 유지(DD-101). State·Rule·Tool·Engine이 모두 서버에 있으므로 브라우저에는 판단 로직이 존재하지 않는다.
  - **유일한 실질 단점인 브라우저 종료 문제를 정직하게 명시**(DD-102): LLM 판단이 필요한 단계는 `PAUSED`, 파싱·통계 분석·보고서 생성·승인된 계획의 Tool 실행 구간은 서버에서 계속 진행. Agent 분석은 원래 사용자가 화면을 보며 승인하는 대화형 작업이고 승인 대기 자체가 브라우저 존재를 전제하므로(Step 26 §12), Step 29 §5-8의 승인 대기 30분 타임아웃과 자연스럽게 일치.
  - 사용량은 클라이언트 보고 기준이며 **앱 집계값은 참고치이고 최종 정산 근거가 아님**을 명시(DD-103) — 실제 과금은 공급자가 개인 계정에 부과하므로 앱 집계를 정산 근거로 제시하면 불일치 시 분쟁 발생. 앱의 역할은 한도 소진 전에 알려주는 것이지 청구서를 만드는 것이 아님.
  - **확인 I(브라우저에서 LLM API 직접 호출 가능 여부, CORS)** 가 불가할 경우의 대안으로 로컬 커넥터를 제시하되, **DD-098의 핵심은 "자격증명이 서버에 없다"이지 "브라우저가 직접 호출한다"가 아니므로 서버측 설계는 어느 쪽이든 동일**함을 확인.
- DD-090~DD-103 14건 신규. 인수기준 AC-F9~F14(그래프·보고서), AC-C11~C13(자격증명 미보관·필터 검증·변조 차단), AC-R8~R9(브라우저 종료 시 동작) 추가.
- 문서 동기화: `31. Final MVP Product Specification.md`와 `29. Web Application Operating Architecture.md` 상단에 개정 안내 블록 삽입.
- Execution_Log.csv RUN-041 갱신.
- 신규 확인 요청: I(브라우저 직접 호출 CORS 허용 여부), J(개인 계정 인증 유지 방식), K(사내망에서 사용자 PC의 외부 LLM 접근 허용 여부).


## 2026-09-12 (계속) — 전체 정리: 세션 생명주기 설계 · 진입점 문서 · 문서 아카이브(RUN-042)

- Ian 지시 3건: ①오래되어 방향성이 변경된 내용을 삭제하거나 무효화 ②Claude Code가 폴더에 접근했을 때 가장 먼저 읽을 파일을 만들어 전체 구조와 내용을 바로 이해할 수 있도록(파일 위치 변경·내용 수정 허용) ③로그온·로그아웃 시 앱 사용 및 LLM 종료를 명확히 처리할 수 있도록 구조 확인.
- **[③ 세션 생명주기 — `31-3` 신규]** Step 31-2에서 LLM 호출을 브라우저로 옮기면서 **앱 세션(서버)과 LLM 연결 세션(브라우저)이라는 두 개의 세션이 존재**하게 되었고, 두 생명주기가 어긋날 때 발생하는 5가지 문제(로그아웃 후 LLM 인증 잔존 / 세션 타임아웃 후에도 연결 표시 / 분석 진행 중 로그아웃 / 브라우저 강제종료 / 동시 로그인)를 정의하고 전부 처리.
  - **LLM 연결은 앱 세션에 종속**되며 역은 성립하지 않음(DD-104) — 앱 세션 종료 시 LLM도 반드시 종료, LLM만 해제하면 Manual로 계속 사용.
  - **로그인 직후 LLM 연결 상태는 항상 미연결**이고 이전 세션 연결을 자동 복원하지 않음(DD-105). 개인 비용 부담 구조에서는 연결이 항상 명시적 의사표시여야 하며, 자동 복원 시 사용자가 의식하지 못한 채 본인 계정에 비용이 발생할 수 있기 때문. 자격증명 기억은 편의이고 연결은 의사표시로 구분.
  - **로그아웃 순서를 LLM 해제 → 작업 정리 → 앱 세션 무효화로 고정**(DD-106) — **앱 세션을 먼저 끊으면 LLM 해제를 지시할 경로가 사라지기 때문.** 진행 중 작업이 있으면 무엇이 멈추고 무엇이 계속되는지 구분해 알림(Agent 분석은 PAUSED 저장, 보고서 생성은 서버에서 계속).
  - 브라우저 측 정리는 **best-effort**로만 취급하고 실질 보장은 서버 만료로 확보(DD-107). 사용자는 보통 로그아웃 버튼을 누르지 않고 탭을 닫기 때문.
  - **핵심 안전장치(DD-108)**: 앱 세션이 무효화되면 서버가 LLM 요청 패키지 발급을 거부한다. Step 31-2 DD-099에 따라 **브라우저는 스스로 프롬프트를 만들 수 없고 서버가 발급한 패키지만 전달**할 수 있으므로, 서버가 발급을 중단하면 브라우저에 토큰이 남아 있어도 앱을 통한 LLM 사용과 비용 발생이 원천 차단된다.
  - 유휴 60분·절대 12시간이되 **서버에서 작업이 진행 중인 동안은 유휴로 판정하지 않음**(DD-109, 분석이 10분 걸리는 동안 세션이 끊기면 안 되므로). 제조 현장의 잦은 자리 비움을 고려해 30분이 아닌 60분 채택.
  - 동시 활성 세션 1개 제한(DD-110) — 개인 PC 전제에서 동시 접속은 정상 패턴이 아니고, 개인 계정 비용이 두 곳에서 동시 발생하면 추적이 어려우며, 동시 수정 충돌 자체가 줄어듦.
  - 헤더에 앱 로그인 사용자와 LLM 연결 상태를 항상 구분 표시(DD-111). 개인 비용이 발생하는 연결이므로 상태가 숨겨져서는 안 됨.
  - AC-C14~C16(자격증명 잔존 없음·세션 무효 후 발급 거부·로그아웃 순서 검증), AC-R10~R14, AC-F15 추가.
- **[① 낡은 문서 무효화 — `09_ARCHIVE` 신설]** 삭제 대신 **이동 + 상태 접두사** 방식 채택(의사결정 이력은 "왜 이렇게 설계했는가"를 되짚는 근거이므로 보존).
  - `[폐기] progress-summary.md` — Step 15까지만 다루며 **데스크톱 전제와 구 Tool 목록**을 담고 있어 현재 설계(웹앱+클라이언트 사이드 LLM)와 정면 배치. 내용을 신뢰하지 말 것으로 표시.
  - `[완료] Gap_Analysis 2건`, `[완료] AI전달용_통합제안.md` — 지적사항이 전부 처리되었고, 특히 통합제안은 기획 주체가 Claude로 인계되며 **전달 목적 자체가 소멸**.
  - `[빈문서] 4. 제조 Use Case별 Agent Scenario 설계.md` — 제목만 있는 1줄 파일.
  - 아카이브 README에 각 문서의 폐기 사유와 대체 문서를 명시하고, 맨 위에 "이 폴더의 문서는 현재 설계를 나타내지 않는다"는 경고 배치.
  - `design-notes.md`(Baseline)와 `원본 기획서` 상단에는 **무엇이 여전히 유효하고 무엇이 바뀌었는지**를 구분한 상태 안내를 삽입. 원본 기획서는 **발전 과정과 의사결정 근거 보존을 위해 의도적으로 원형 유지**함을 명기(Step 25-2의 판단 계승).
- **[② 진입점 — `CLAUDE.md` 신규]** Claude Code가 폴더 접근 시 자동으로 읽는 파일명으로 작성. 구성: 제품 정의 한 문장 / 3단계 읽기 순서(CLAUDE.md → DD_Register.md → Step 31) / **변경 불가 제품 원칙 10개와 각각의 구현 중 위반 예시** / 시스템 구조 한 장과 핵심 4가지 / 폴더 구조와 **주제별 최종 권위 색인 16항목** / 운영 전제 E-1~E-10 / 개발 마일스톤 M1~M4와 착수 선행조건 / **"구현 시 자주 틀리는 지점" 10개**(세 가지 제외필터·두 가지 재시도·Agent 재개지점·가명매핑·대용량 Excel·보고서 생성·그래프 매핑·표본 부족 표현·로그아웃 순서·불변식) / 남은 확인사항 A~K.
- **[② 설계결정 대장 — `DD_Register.md` 신규]** 설계결정이 111건까지 누적되며 **폐기 4건·정정 2건·개정 8건**이 발생해 구현자가 각 Step 문서를 돌아다니며 유효 여부를 판정해야 하는 상태였음. 전체를 한 표로 모으고 **주의가 필요한 13건을 맨 앞에 배치**. 인증 방식이 세 번 바뀐 경위(개인 API Key → 조직 Enterprise → 개인 계정)와 제품 형태 전환(데스크톱 → 웹앱), LLM 호출 위치 전환(서버 → 클라이언트)의 경위를 참고 절로 기록해 "왜 이렇게 되어 있지?"라는 의문에 답할 수 있게 함.
- 최종 폴더 구조 확인: 루트에 `CLAUDE.md`·`DD_Register.md`, 00~06·08 설계 폴더, 09_ARCHIVE. 07_검토및제안은 비워져 아카이브로 이동.
- DD-104~DD-111 8건 신규. 누적 DD-001~DD-111.
- Execution_Log.csv RUN-042 갱신.


## 2026-09-12 (계속) — Step 31-4 다국어 지원 설계(RUN-043)

- Ian 최종 반영 요청: 앱 사용자에 **해외 생산 공장 기술자**가 포함되며, PRISM은 로그인 시 EN 토글로 모든 UX와 보고서를 영어로 전환한다. 이 Add-on 모듈도 **로그인 시 설정된 언어를 따라야 하고 에러 메시지·보고서·설명·툴팁 모두 영어를 지원**해야 한다. PRISM의 에러 메시지는 **한국어와 영어를 통합해 하나의 메시지로 출력**한다.
- **[문제 규명] 이 요구는 단순 번역 계층 추가가 아니다.** 일반 업무 앱은 버튼·메뉴 같은 정적 문구만 사전으로 처리하면 되지만, 이 앱은 **텍스트 대부분이 분석 결과에서 생성되는 문장**이다 — 통계 해석 문장(템플릿 생성), 제조 판단 문장(규칙 생성), AI 해석 문장(LLM 생성), 그래프 축·범례·규격선 라벨, 보고서 전체, 오류 메시지. 템플릿은 언어마다 문장 구조가 다르고(한국어 조사·어미 vs 영어 관사·복수·시제), LLM 출력은 언어를 지시하면서 **번역하면 안 되는 것을 보호**해야 한다.
- **[핵심 경계] 데이터 유래 문자열은 번역하지 않는다**(DD-113). `3호기`를 `Machine 3`으로 번역하면 사용자가 **원본 Excel 및 현장 설비에 붙은 이름과 대조할 수 없다.** 현장에서 "3호기 불량률이 높다"는 결론을 받아 설비 앞에 갔는데 보고서의 `Machine 3`이 다른 설비처럼 보이면 안 된다. 따라서 **영어 화면에 한국어 변수명이 섞여 나오는 것이 올바른 동작**임을 명시하고, 표시용 별칭(alias) 기능은 Phase 2 제안으로 남김.
- **[오류 메시지 한·영 통합]** PRISM 방식을 계승해 언어 설정과 무관하게 `[오류코드] + 한국어 + 영어`를 하나의 메시지로 출력(DD-115). 근거는 **오류가 소통의 대상**이라는 것 — 해외 공장 기술자가 오류 화면을 캡처해 한국 본사 담당자에게 보내는 상황이 실제로 발생하며, 이때 한 장의 화면으로 양쪽이 같은 내용을 봐야 한다. 오류 코드를 맨 앞에 두는 것도 언어와 무관한 검색·대조 식별자가 필요하기 때문. 정상 UX 문구는 개인 사용자를 위한 것이므로 언어 설정을 따르고 **오류만 이중 표기**하는 구분을 논증. 적용 범위는 Statistical Engine 오류(Step 17 표준 코드), Rule Engine 거부, Data Guard 차단, Job 실패, AI Gateway 오류, 인증·한도 오류 전부.
- **[해석 템플릿]** 언어별 별도 작성하고 **문장 조각 조립을 금지**(DD-116). "평균이"+"낮"+"습니다" 식으로 이어 붙이면 한국어는 조사·어미가, 영어는 관사·복수·시제가 반드시 깨진다. 문장 단위 템플릿이 유일하게 안전한 방법.
- **[LLM 출력]** Prompt Stack의 Core System Policy(L1)에서 출력 언어를 지시하되, **데이터 유래 문자열 번역 금지와 수치 재작성 금지를 함께 지시**(DD-117). 언어 변환 과정에서 수치 재작성 원칙(DD-085 #1)이 특히 깨지기 쉬움. 언어 불일치는 과도한 자동 검증(언어 감지 후 재요청) 대신 사용자의 [다시 생성] 경로로 처리 — 검증 비용과 지연이 더 크기 때문.
- **[숫자·날짜 형식]** 언어 설정과 무관하게 고정(DD-119). 소수점 `.`, 천단위 `,`, 지수 표기, ISO 8601 날짜. 근거는 일부 로케일이 소수점에 `,`를 쓰는데 제조 데이터에서 `3.14`와 `3,14`, `1,234`와 `1.234` 혼동은 **규격 판정을 뒤집는 치명적 오독**을 만든다는 것. 다국어는 지원하되 숫자 표기는 단일 규칙으로 고정하며, 한국·영어권 모두 같은 표기를 쓰므로 두 언어 사용자에게 자연스럽다.
- **[Finding 저장 방식]** 세션이 최대 2년 보존되는데 그 사이 사용자가 언어를 바꿀 수 있으므로 과거 Finding의 언어 처리가 쟁점. **템플릿 생성 텍스트는 `template_id`+`params`로 저장해 표시 시점에 렌더링**(언어 전환 시 자동 전환)하고, **LLM 생성 자연어는 원문+생성언어를 저장**(그대로 유지, 불일치 시 안내)하는 이원 구조로 결정(DD-120). LLM 문장을 양 언어로 미리 생성하지 않는 이유는 호출 비용이 두 배가 되고 개인별 승인 한도(DD-063)를 소모하기 때문.
- **[식별자 사전]** 언어 설정과 무관하게 한국어·영어 키워드를 모두 적용(DD-121). 해외 공장 데이터는 영어 컬럼명일 가능성이 높고, **데이터의 언어와 인터페이스 언어는 별개**다. 사전을 언어 설정에 따라 전환하면 영어 컬럼 `operator`가 한국어 설정에서 식별자로 인식되지 않아 **fail-closed 원칙(DD-042)이 무너지고 개인정보가 그대로 전송**된다. 작업자·설비 고유번호·로트·고객 4개 분류의 한·영 키워드 표 제공.
- **[Golden Case 언어 독립성]** AC-A8 신설 — 동일 Golden Case를 `ko`와 `en`으로 각각 실행했을 때 **통계 결과·Tool 선택·Finding 유형·Evidence 등급·Hypothesis 상태가 완전히 동일**해야 한다(자연어 문장만 언어에 따라 다름). LLM에게 언어를 지시하는 것이 **판단 자체에 영향을 줄 수 있으며, 영어로 사고할 때와 한국어로 사고할 때 선택하는 분석 방법이 달라진다면 그것은 결함**이라는 근거를 명시.
- 그 외: 언어 사전 키 누락 시 빌드 실패(DD-114, 실행 시점이 아니라 빌드 시점에 잡혀야 함), 보고서는 생성 시점 언어로 고정(DD-118, 이미 배포된 보고서가 나중에 다른 언어로 바뀌면 안 됨), 그래프 요소별 번역/원문 구분표, 언어 전환 시 동작 정의, 스키마 영향(AppSession.language, Finding.template_id/params/language 등), AC-L1~L10 인수기준 10건.
- **진입점 문서 동기화**: `CLAUDE.md`에 다국어 요구를 §1 제품 정의에 추가, 운영 전제 **E-11** 추가, 권위 색인에 31-4 추가, **"구현 시 자주 틀리는 지점"에 다국어 5건 추가**(문자열 하드코딩·데이터 번역 금지·오류 메시지 이중 표기·숫자 표기 고정·템플릿 조각 조립 금지). `DD_Register.md`에 DD-112~121 절 신설 및 건수 갱신.
- **작업량 영향 명시**: 해석 템플릿 양 언어 작성(T-13/T-14)과 전 화면 i18n(T-15)이 실질 증가분이나, **T-01에서 구조를 잡아두면 이후 비용이 크게 줄어든다**(나중에 얹으면 하드코딩된 문자열을 전부 찾아내야 하므로 훨씬 비쌈).
- DD-112~DD-121 10건 신규. 누적 DD-001~DD-121.
- Execution_Log.csv RUN-043 갱신.


## 2026-09-12 (계속) — 인수인계 준비도 최종 점검 및 결함 수정(RUN-044)

- Ian 요청: "최종 정리가 완료된 상태인가요? 클로드 코드에게 넘겨도 되는지 최종 확인해 주세요."
- 선언이 아니라 **실제 점검**을 수행했고, 넘기기 전에 고쳐야 할 결함 3건을 발견해 수정했다.
- **[결함 1] Step 31이 31-3·31-4를 전혀 참조하지 않음.** `31. Final MVP Product Specification.md`를 "개발 착수 기준 문서"로 지정해 두었는데, grep 결과 이 문서에 **31-3(세션 생명주기)과 31-4(다국어)에 대한 언급이 0건**이었다. 이대로 넘기면 구현자가 Step 31만 읽고 **로그인/로그아웃 설계와 다국어 요구 전체를 누락**하게 된다. 개정 안내 블록에 "추가 개정(31-3·31-4)" 절을 신설하여 ①세션 생명주기가 31-3에 신설되었고 S-00 로그인은 화면 목록에만 있었을 뿐 생명주기가 설계되지 않은 상태였음 ②다국어는 부가 기능이 아니라 T-01부터 구조에 반영해야 하는 요구이며 MVP In에 포함, AC-L1~L10·AC-A8 추가, T-13/T-14는 해석 템플릿을 양 언어로, T-19는 ko/en 판단 동일성 검증 ③데이터 유래 문자열 번역 금지·오류 한영 통합·숫자 형식 언어 무관 고정 주의사항 ④확인 I·J·K 추가를 명시했다.
- **[결함 2] DD-089로 스스로 설정한 블로커를 해소.** Step 27 §7에서 "Step 19의 Orchestrator 루프에 승인 확인 지점이 없다"는 공백을 발견하고 DD-089로 "Step 19에 승인 게이트가 반영되기 전에는 T-12를 착수하지 않는다"고 정했으나, **정작 Step 19 문서는 손대지 않은 채로 두었다.** 내가 만든 블로커를 그대로 두고 인계하는 것은 무책임하므로 Step 19 문서 상단에 개정 안내를 삽입했다 — "이 문서의 실행 루프는 불완전합니다" 경고, 보완된 루프 의사코드(`approval.check` → REQUIRES_APPROVAL 시 `WAITING_APPROVAL`로 break → `grant.consume`), ApprovalGrant의 범위와 재승인 트리거 5가지, 불변식 INV-08 연계, 그리고 `MAX_RETRY_PER_DECISION=2`가 **결정 재시도**이며 네트워크 **전송 재시도**와 별개 카운터임을 명시(합치면 네트워크 장애가 "Agent 판단 실패"로 기록되어 Golden Case 평가가 왜곡됨). LLM 호출 위치가 서버에서 브라우저로 바뀌었다는 점도 함께 안내. **DD-089 해소** — CLAUDE.md 선행조건 표도 갱신.
- **[결함 3] DD_Register 건수 표기 불일치.** "폐기·정정·개정된 13건"이라고 썼으나 §1 표에는 재해석·적용대상 소멸·의미 축소를 포함해 16개 행이 있었다. 브리틀한 숫자 대신 표 참조 방식으로 바꾸고 3개 부가 분류가 함께 실려 있음을 명시.
- **[준비도 판정] 인계 가능.**
  - 갖춰진 것: 진입점 `CLAUDE.md` / 설계결정 대장 `DD_Register.md`(DD-001~121, 상태 표기) / 설계 문서 36건(Step 1~31 + 31-1~31-4) / MVP In·Out과 제외 사유 / 측정 가능한 인수 기준 약 60건 / 개발 Task 20개와 의존 순서 / 낡은 문서 아카이브 분리 / 주제별 문서 권위 색인.
  - **착수 전 Ian이 제공해야 할 것**: 현장 실제 Excel 샘플(T-07 필수). Golden Dataset 실물은 미생성이나 사양이 Step 23·24에 있어 생성 가능.
  - 진행 중 확정 가능: 확인사항 A~K 11건(설정값·인프라), Step 18 잔여 2건(다중비교 보정 방법, Data Guard 수치 기준), 기술 스택 확정.
- Execution_Log.csv RUN-044 갱신.


## 2026-09-13 — Step 32 PRISM 확장 로드맵: 3단계 지식화의 2단계 반영 범위 결정(RUN-045)

- Ian이 PRISM의 3단계 로드맵을 설명하고 결정을 요청: **1단계**(현행 — MES CTQ 데이터로 전 법인 변동성·공정성능 분석, 대시보드, 법인별·제품별 주차 보고서, 데이터 품질 평가·피드백) → **2단계**(이번 기획 — LLM 연동 통계분석으로 근본 원인 탐색 + 제조·기술 부서 대책 검증) → **3단계**(지식화 — 검증에 사용된 데이터를 지식화하고 문제-원인-대책 순환 고리를 축적·고도화). 질문은 "2·3단계를 동시 구현할지, 순차 진행하되 3단계를 고려해 2단계 구조를 조정할지"이며 **앱 개발 스킬(app-build-lifecycle) 참조**를 명시.
- **[방법론 적용]** 스킬을 읽고 `upgrade`(브라운필드) 모드로 판정. 모드 upgrade / 규모 L(다중 사용자+개인정보·영업비밀+MES 등 다중 연동+다법인·다국어) / G2~G5는 reviewed.
- **[정직한 판정 — 가장 이른 미충족 게이트는 U0]** 스킬의 브라운필드 원칙은 *"그린필드는 인터뷰에서 시작하고 브라운필드는 실행 검증에서 시작한다. 기존 코드를 읽기 전에 새 설계를 쓰지 않는다"*인데, **Step 1~31 전체가 PRISM의 실제 스키마·코드·운영 데이터를 한 번도 확인하지 않고 작성되었음**을 지적. GAP-08로 의도된 것이었고 2단계는 비교적 독립적인 신규 모듈이라 그 판단이 크게 틀리지 않았으나, **3단계 지식화는 PRISM이 이미 무엇을 축적하고 있는지에 절대적으로 의존**하므로 사정이 다름. PRISM은 이미 주차 보고서와 데이터 품질 평가를 수행 중이므로 "문제 발견" 단계의 기록이 이미 축적되고 있을 가능성이 높음.
- **[결론 — C안 권고]** 순차 진행하되 2단계에 **기록 계층**을 반영. 원칙: **"기록(capture)은 2단계에, 활용(leverage)은 3단계에."**
  - **비대칭성 논거**: 활용 기능(검색·추천·지식 기반 제안)은 나중에 만들어도 비용이 선형이고 오히려 사례를 보고 만드는 편이 정확하다. 반면 **기록은 늦으면 그 사이의 개선 사이클을 영원히 잃는다.**
  - **가장 구체적 근거 — 보유기간 충돌**: Step 29 DD-073의 보유기간(원본 90일 / 세션 2년)을 그대로 두고 2단계를 2년 운영하면 **3단계 시작 시점에 축적된 것이 거의 없다.** DD-074·DD-075가 완충하지만 둘 다 개별 케이스 수동 적용이라 체계적이지 않음. 이는 추상적 우려가 아니라 **우리 설계에 이미 존재하는 구체적 결함**.
- **[2단계 기획서 자체의 구멍 발견]** Ian이 "대책 검증까지 제공하는 것이 이번 기획서"라고 정의했는데, 점검 결과 **Countermeasure(대책) 객체가 설계에 없음.** UC-07 개선 전후 검증 시나리오와 Evidence E4(실험/개선검증), 측정시스템 동일성 질문(DD-023), `final_decision` 필드는 있으나 **무엇을 바꿨기에 그렇게 되었는지는 기록하지 않는다.** 대책 내용·실시일·실시 부서·대상 범위·대응 Hypothesis 연결이 전무. 따라서 검증 결과가 "6월 이후 평균이 낮아졌다"는 관찰에 그침. **이는 3단계를 위한 추가가 아니라 2단계가 스스로 완결되기 위해 이미 필요했던 것**이며, 공교롭게도 3단계 지식의 핵심 원재료이기도 함.
- **[이미 3단계 대비가 된 부분]** Finding/Evidence/Hypothesis/Confounder 구조, Evidence Level E0~E4(E4가 곧 검증된 지식), 재현성 메타데이터(DD-084), **Step 6 Manufacturing Knowledge Architecture**(Raw-Wiki→LLM-Wiki→Agent Knowledge 파이프라인과 Case Library 개념이 이미 설계됨), Planning/Interpretation Retrieval 분리, 보존 지정 Hold. 즉 **3단계는 "새로 설계할 것"이 아니라 "Step 31 §4-2에서 꺼둔 것을 켜는 것"에 가깝다.**
- **[2단계 최소 반영 6항목]** ①`ImprovementCase` — 원인분석 세션과 검증 세션(몇 주~몇 달 떨어진 별개 세션)을 묶는 상위 컨테이너 ②`Countermeasure` 구조화 ③`VerificationResult` — **효과 없음·판단 보류도 반드시 기록**(실패한 대책의 기록도 지식이며 스킬 공통규칙 9와 일치) ④**검증 완료 케이스의 보유기간 자동 제외(자동 Hold)** — 다른 항목을 다 미루더라도 이것만은 반드시. 나머지는 나중에 추가 가능하지만 삭제된 데이터는 복구 불가 ⑤`ProblemSignature` 정규화 축(법인/공장/라인/설비/제품/CTQ/문제유형) — **단 코드 체계는 새로 만들지 않고 PRISM의 MES 체계를 재사용해야 함.** 새 체계를 만들면 1단계 데이터와 연결되지 않아 지식화의 의미가 없어짐 ⑥케이스 간 재발 참조.
- **[3단계 이관]** 유사 사례 검색·추천(사례 0건에서 검증 불가), Planning Retrieval, 대책 유효성 통계(수십 건 필요), Knowledge Graph, 자동 지식 추출, 제조·사내 Knowledge RAG.
- **[과잉 설계 방지 원칙]** 스킬 가드레일(*"목적·범위가 정해지기 전에 큰 구조를 만들지 않는다"*)을 적용해 **"기록은 충실히, 구조화는 나중에"**를 원칙으로 세움. 어떤 형태의 지식이 실제로 재사용되는지는 사례 30~50건이 쌓인 뒤에야 알 수 있으므로 지금 지식 스키마를 상세 설계하면 추측 기반 구조가 되고 마이그레이션 비용으로 돌아온다. **좋은 기록에서는 나중에 어떤 구조든 도출할 수 있지만 없는 기록에서는 아무것도 도출할 수 없다.**
- **[U0 확인사항 P-1~P-5]** ①PRISM에 이미 이슈·개선활동·조치이력 구조가 있는가(있으면 ImprovementCase를 신규 생성하지 않고 **기존 것을 확장** — 이 하나가 6항목 전체의 형태를 바꿈) ②MES 코드 체계의 정규화 수준과 법인 간 통일 여부(**부정적이면 코드 표준화가 3단계 선행 과제이며 이는 앱 개발이 아니라 데이터 거버넌스 과제**) ③주차 보고서 저장·재조회 가능성 ④데이터 품질 평가 이력 존속 여부 ⑤해외 법인 스키마·코드 동일성(31-4 다국어와 직결). **P-1·P-2가 결정적.**
- **[인계 시점 판단]** T-01·T-03~T-07(구조·엔진·Tool·Rule·파싱)은 PRISM 구조와 무관하므로 **U0 이전 착수 가능**. **T-02(Schema)만 U0 이후 확정** 권고 — §6 객체들의 형태가 P-1 결과에 달려 있기 때문.
- ADR 형식으로 맥락·결정·상태(조건부 수용)·긍부중립 결과·검토한 대안(A안 동시구현 기각 사유, B안 완전순차 채택불가 사유)을 기록.
- 폴더명 `06_제품운영설계(Step25-31)` → `(Step25-32)` 갱신. CLAUDE.md 권위 색인에 Step 32 추가(T-02 착수 전 필독), 선행조건에 U0 추가.
- Execution_Log.csv RUN-045 갱신.


## 2026-09-13 (계속) — Step 33 개선 사이클 기록 설계(RUN-046)

- Ian이 Step 32의 U0 질문 2건에 답변: **P-1 — PRISM에 개선 기록 구조가 없다.** 이유는 기술이 아니라 조직적인 것으로, 앱의 성격이 문제를 드러내는 것이라 제조·기술 부서의 반감이 있어 처음부터 협조를 얻기 어려웠고, 현재는 몇몇 기술 담당자로부터 문제 확정 로직 설명 요청을 받아 피드백하는 초기 상태. 그 상황에서 원인분석·대책수립·대책검증까지 요구하기 어려웠고 **그래서 다단계 로드맵을 수립**했다. **P-2 — CTQ 표준화는 진행 중**이며 PRISM이 CTQ 항목과 데이터 품질을 점검·비교 기록하므로 표준화를 전제로 검토 가능. 이어 순차 진행 전제의 2단계 구조 변경을 요청했고, 세 가지를 물었다 — 개선 내용을 어떻게 입력받고 기록할 것인가, 어떤 기술 스택으로 저장·활용할 것인가(현재 PostgreSQL 단일 DB), **귀찮아서 대충 입력하는 문제를 어떻게 해결할 것인가**.
- **[핵심 재정의] 이 설계의 진짜 제약은 기술이 아니라 채택이다.** PRISM은 지금까지 제조·기술 부서에게 문제 지적·순위 노출·데이터 품질 지적만 주는 **일방적 관계**였다. 그 상태에서 원인분석과 대책 검증 데이터 입력을 요구하면 저항은 당연하며, **입력 UX를 아무리 개선해도 이 구조는 바뀌지 않는다.** 2단계는 PRISM이 처음으로 부서에게 무언가를 주는 단계이고, 그중 **대책 효과의 통계적 증명이 킬러 기능**이다 — 개선했는데 "정말 좋아진 거냐, 우연 아니냐"에 답하지 못해 성과로 인정받지 못하던 문제를 해결하므로 부서에게 직접적 이득이 된다. 이에 따라 기록 계층의 목표를 **"완전한 기록"이 아니라 "지속되는 기록"**으로 설정(DD-122) — 완벽한 스키마를 필수 입력으로 강제하면 초기 저항 상황에서 0건이 축적되며, 불완전해도 실제로 쌓이는 기록이 완벽하지만 비어 있는 스키마보다 낫다.
- **[입력 설계 7원칙]**
  - **①부담을 가치 직전으로 옮긴다(DD-123)** — 개선 사이클에서 기록 가능 시점은 셋이고(원인분석 종료 / 대책 실시 직후 / 검증 요청), **대책 사전 등록을 요구하지 않고 검증 요청 시점에 묻는다.** 시점 B에서 물으면 사용자는 아무 대가 없이 입력만 하지만, 시점 C에서는 검증 결과를 얻기 위해 필요한 정보이므로 입력이 거래가 된다. 실시일 기억 문제는 **데이터 변화점 탐지로 후보 제시**하여 보완.
  - ②앱이 아는 것은 묻지 않는다 — 설비·기간·효과크기는 자동. 사용자에게 묻는 것은 앱이 알 수 없는 것 하나(물리적으로 무엇을 했는가)뿐. DD-027과 같은 정신.
  - ③선택형 우선, 자유서술은 "그 외 특이사항" 한 칸.
  - **④LLM을 구조화 도우미로 쓴다(DD-124) ★핵심** — 폼이 길어지면 그 자체가 부담이라는 원칙 ③의 한계를, 2단계에 LLM이 있다는 사실로 해소. 사용자가 "3호기 척킹 압력을 4.5에서 5.0으로 올렸어요, 6월 12일에"라고 한 문장만 말하면 LLM이 대책유형·대상·변경항목·전후값·실시일로 구조화하고 사용자는 확인만 한다. **"사용자는 게을러도 되고 기록은 성실해도 되는" 유일한 방법.** 원문 자유서술도 함께 보존 — LLM 구조화가 놓친 정보가 있을 수 있고 나중에 더 나은 추출로 재처리할 수 있기 때문(DD-120과 동일 원칙). 이 호출은 INTENT 등급 경량 호출이며 데이터 유래 문자열은 번역·변형하지 않는다(DD-113·117).
  - ⑤강제하지 않되 결과를 보여준다(DD-125) — 미기록 시 검증은 수행하되 "무엇을 바꾸셨는지 기록되지 않아 다른 설비·라인에서 참고 사례로 활용할 수 없습니다" 표시. 차단 대신 **무엇을 잃는지 보여주면** 자발적 입력률이 올라간다.
  - **⑥기록은 인정으로 되돌아온다(DD-126) ★채택의 핵심** — 검증된 개선을 **주차 보고서와 법인별 집계에 자동 반영**. PRISM이 "문제를 드러내는 앱"에서 **"개선을 기록해 주는 앱"**이 되는 장치이며, 입력의 대가는 편의가 아니라 **성과 인정**이다. PRISM이 이미 주차 보고서를 작성하므로 섹션 하나만 추가하면 된다.
  - ⑦입력 주체 분리(DD-127) — 분석은 품질·기술이 하지만 대책의 실제 내용은 제조가 안다. 대책 기록 요청을 담당자에게 전달하는 경로를 둔다.
- **[기록 구조]** 지식 재사용에 필요한 5축(문제정체·인과주장과 근거·개입·결과·**맥락조건과 부작용**) 중 다섯째가 가장 놓치기 쉬움을 지적 — 지식이 재사용되는 순간의 질문은 언제나 "그게 우리 상황에도 맞나"이므로 맥락 없는 기록("척킹 압력을 올려서 변동이 줄었다")은 재사용 불가. 맥락 대부분은 데이터에서 자동 수집 가능하고 사용자에게 묻는 것은 부작용뿐이며 이것도 선택형. **효과 없음·판단 보류도 동일하게 기록**(DD-128) — 실패한 대책의 기록은 같은 시도의 반복을 막으므로 성공 사례만큼 가치 있으며 스킬 공통규칙 9와 일치. ImprovementCase / Countermeasure / VerificationResult 객체 초안 제시.
- **[기술 스택] PostgreSQL 유지·확장(DD-129)** — ①브라운필드 원칙(이미 운영 중이고 팀이 익숙) ②데이터 성격이 전형적 관계형 ③**JSONB로 진화 흡수**(형태 미확정 부분을 스키마 변경 없이 수용) ④전문검색 내장으로 3단계 초기 유사사례 검색에 충분 ⑤**필요해지면 pgvector를 같은 DB에 붙이면 되므로 별도 벡터DB의 동기화 문제를 회피** ⑥CTQ·설비 마스터 조인 필요(다른 DB면 불가). 하이브리드 저장 원칙 **"검색할 것은 컬럼으로, 보존할 것은 JSONB로"**(DD-130), 파일은 스토리지. **같은 DB의 별도 스키마 `statmod`로 분리하고 PRISM 기존 테이블은 읽기만**(DD-131) — 스킬 브라운필드 금지사항 "운영 중 데이터의 마이그레이션 경로 없이 스키마를 바꾸는 것"을 준수하는 가장 안전한 확장. **3단계 초기 지식 활용은 SQL 질의로 구현**(DD-132) — 수십 건 규모에서는 SQL 조회가 의미 검색보다 정확하고 **사용자가 "왜 이 사례가 추천됐는지" 이해할 수 있다**는 점이 이 제품의 근거 추적 가능성 원칙과 부합. 예시 SQL 2건 제시.
- **[역방향 검증]** 기록 설계가 맞는지 확인하기 위해 **3단계 화면을 구체적으로 그려 8개 요소를 역산**했고 모두 2단계 구조로 충족됨을 확인. 그 과정에서 **누락을 발견 — 설비 기종 축(DD-133)**. 법인별 설비 번호는 서로 무관하므로 기종 단위로 묶이지 않으면 **지식화의 최대 가치인 법인 간 전이(A법인에서 해결한 것을 B법인이 활용)가 일어나지 않는다.**
- **[채택 전략]** Ian의 설명에 단서가 있다 — "몇몇 기술 담당자로부터 로직 설명 요청을 받아 피드백하고 있다"는 **그 사람들이 첫 사용자**다. 전사 확산이 아니라 **3~5명과 케이스 5~10건**이 2단계 실질 목표. 확산 경로 4단계 제시. **3단계 착수 기준: 검증 완료 30건 이상, 동일 기종 반복 5건 이상** — 그 이전에는 유사사례 검색을 만들어도 보여줄 것이 없다. 하지 말 것 4가지(필수입력 강제 / 입력률 지표 노출 — 감시로 인식됨 / 전사 일괄 오픈 — 첫인상 회복 불가 / 초기 입력 항목 과다).
- U0 확인사항 갱신: P-2′(CTQ 표준화 완료 시점·적용 범위) P-3~P-5 유지, **P-6 신규(설비 마스터에 기종·제조사·도입연도가 있는가 — DD-133의 전제이며 없으면 법인 간 전이 불가)**, P-7(PostgreSQL 버전·확장 가능 여부), P-8(사용자 계정·부서 정보 구조).
- Task 영향: T-02(스키마·인덱스), T-11(구조화 추출 호출), T-15(화면 3개), T-16(보고서 섹션+주차보고서 연동), T-18(자동 Hold). **추가 화면은 3개, 나머지는 스키마와 규칙.**
- 폴더명 `(Step25-32)` → `(Step25-33)`. CLAUDE.md 권위 색인에 Step 33 추가, 선행조건의 U0 항목을 P-6 강조로 갱신.
- DD-122~DD-133 12건 신규. 누적 DD-001~DD-133.
- Execution_Log.csv RUN-046 갱신.

---

## RUN-047 — 전파 감사 및 설비 마스터 이관 확정 (2026-09-13)

**요청:** Ian — "현재 설비에 대한 기록은 없습니다. 초기 거부감이 커서 요구하지 않았습니다. 이는 3단계 진행 시 업데이트하는 것으로 진행하겠습니다. 순차 진행으로 2단계 LLM 연동 통계분석 모듈 제작을 위한 기획서는 모두 업데이트되었는지 점검해 주세요."

### 감사 결과 — **아니요. 전파되지 않은 상태였습니다.**

`DD-122|ImprovementCase|improvement_case`로 `LLM_extention` 전체를 내용 검색한 결과 **15건이 모두 `32.`·`33.` 문서 안에만** 있었고, **DD_Register·Step 30·Step 31에는 0건**이었습니다.

이는 app-build-lifecycle 스킬의 **실패모드 F-02(서술은 앞서가고 목록은 뒤처진 내부 불일치)**이며, 앞서 `chi_square_test`가 서술에는 있고 Tool Registry에는 없던 것과 **정확히 같은 패턴**입니다. 방치했다면 구현자는 Step 30의 객체 목록으로 DDL을 고정하고 Step 31의 MVP 범위로 착수했을 것이고, 그 결과 **기록 계층 전체가 누락되어 3단계에 축적될 데이터가 0건**이 됩니다.

### DD-134 — 설비 마스터는 3단계로 이관

**결정:** 설비 마스터(기종·제조사·도입연도)는 3단계에서 보완한다. 2단계에서는 `ProblemSignature`에 설비 기종 필드를 두되 **비워 둔다**(nullable). 대신 설비 식별자(법인·공장·라인·설비번호)를 **원본 표기 그대로**, 마스터 조인 키로 쓸 수 있는 형태로 보존한다.

**지금 잃는 것이 없습니다.** 설비 식별자를 원형 그대로 남겨 두면, 3단계에서 설비 마스터가 만들어졌을 때 **조인만으로 과거 케이스 전체에 기종 정보를 소급 보완**할 수 있습니다.

**단 하나의 조건:** `3호기`를 `M3`으로 바꾸거나 공백·표기를 임의로 정리하면 나중에 마스터와 매칭되지 않습니다. **DD-113(데이터는 번역하지 않는다)과 같은 원칙**입니다.

DD-133은 폐기가 아니라 **적용 시점 이동**입니다.

### 전파 수정 5건

| 문서 | 수정 |
|---|---|
| `DD_Register.md` | Step 32·33 절 신설, DD-122~134 등재. 헤더를 `DD-001 ~ DD-134`·유효 119·적용시점 이동 1로 갱신 |
| `30. Schema Contract` | 상단 개정 안내 — 기록 계층 3종이 이 문서에 없음을 명시. **본문 객체 목록만 보고 DDL 고정 금지**, 설비 식별자 정규화 금지 |
| `31. Final MVP Spec` | 추가 개정 절 — MVP In에 기록 계층, 3단계 검색·추천은 MVP Out, 화면 3종, Task 영향(T-02·T-11·T-15·T-16·T-17·T-18) |
| `29. 웹앱 운영 아키텍처` | §6 보유기간 예외 — 검증 완료 시 `retention_hold` **자동** 설정, 삭제 대상 **선정 쿼리에서 선배제**(삭제 후 필터링 아님) |
| `CLAUDE.md` | 3단계 로드맵 문단, 운영 전제 **E-12~E-15**, 자주 틀리는 지점 6건, DD 건수·폴더명·선행조건 갱신 |

**자주 틀리는 지점 신규 6건:** 입력 강제 금지 / 원문 `description_raw` 보존 / 설비 식별자 정규화 금지 / 검증 완료 시 자동 Hold / 3단계 기능(유사사례 검색·추천) 제작 금지 / 검증은 인과 확정이 아님.

### Task 번호 정정

초안에서 T-11을 "보유기간", T-18을 "관리자 콘솔"로 잘못 적었습니다. Step 31 §7의 실제 목록을 확인하여 **T-11 AI Gateway · T-17 관리자 콘솔 · T-18 보유기간 워커**로 정정하고, Step 33 §9 표에도 T-17 행을 추가해 두 문서를 일치시켰습니다.

### 남은 차단 요인

- **U0 현행 검증 P-2′·P-3·P-4·P-5·P-7·P-8 미해소** → `T-02(Schema)` 확정 불가. **P-1·P-6은 확인 완료.**
- T-07 착수 전 **현장 실제 Excel 샘플** 필수.
- **T-01·T-03~T-07은 지금 착수 가능.**

DD-134 1건 신규. 누적 DD-001~DD-134. Execution_Log.csv RUN-047 기록.
