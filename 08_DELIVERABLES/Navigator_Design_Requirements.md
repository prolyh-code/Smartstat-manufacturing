---
id: DELIV-NAV-REQ-001
title: Analysis Navigator 설계 요구사항 (감사+시뮬레이션 기반 제안)
type: design-requirements-proposal
status: proposed — Ian 최종 승인 대기 (self-reviewed 근거, 독립검증 아님)
owner: Claude (Cowork) 제안, Ian 결정
created: 2026-09-09
updated: 2026-09-12
---

# Analysis Navigator 설계 요구사항

> **[추론]** 이 문서는 `Navigator_Logic_Statistical_Audit.md`의 3단계 자체 검토(1차 이론감사 → 2차 자기비판적 재검토 → 3차 몬테카를로 시뮬레이션)에서 나온 결론을 실행 가능한 설계 요구사항으로 번역한 제안입니다. 통계 전문가의 독립 검증을 거치지 않았으며(GAP-07 waived, DEC-006), 최종 채택 여부는 Ian의 판단입니다. MVP 범위(Phase 1) 변경을 포함하므로 제품 로드맵 결정과 별개로 다뤄야 합니다.

## 요약 (결론 먼저)

7개 위험 중 우선순위가 가장 높은 3가지는 다음과 같습니다.

1. **자기상관(독립성) 미확인 — 신규 위험7.** 시뮬레이션에서 4개 시나리오 중 가장 큰 효과(1종오류율 최대 63.8%)를 보였습니다. Navigator에 "이 데이터가 시간순 연속 수집인가?"를 묻는 질문을 최우선으로 추가할 것을 제안합니다.
2. **등분산 위반(위험3) — Welch's t-test 기본값화.** 조건부 경고보다 처음부터 Welch's t-test를 기본 알고리즘으로 쓰는 것이 문헌(SRC-127)과 시뮬레이션(Student 22.3% vs Welch 5.6%) 모두에서 뒷받침됩니다. Phase 1 범위 변경이 필요합니다.
3. **조건 확인의 순서 역전(위험1).** 정규성·등분산·독립성 확인을 검정 실행보다 먼저 배치하는 것은 위 두 가지 요구사항의 전제조건이기도 합니다.

나머지(표본수 하한, 다중비교 감지, 비모수 대안)는 Phase 1 대비 Phase 1.5~2로 단계적 반영을 제안합니다.

## 요구사항 목록

| REQ ID | 원 위험 | 요구사항 | 근거 | 제안 우선순위 | Phase | 상태 |
|---|---|---|---|---|---|---|
| NAV-REQ-01 | 위험1(순서역전) | Navigator 실행 순서를 "① 데이터 입력 → ② 정규성·등분산·독립성 자동 검정(내부 처리, 사용자 노출 최소화) → ③ 결과에 따라 검정방법 자동 선택 → ④ 검정 수행 → ⑤ 결과+신뢰도 표시"로 재배치 | Review Pass 1 위험1; engineer-research-lifecycle 원칙(사후 정당화 금지) | 최우선 | Phase 1 | proposed |
| NAV-REQ-02 | 위험3(등분산) | 2-Sample 비교의 기본 알고리즘을 Student's t-test가 아닌 **Welch's t-test**로 채택(등분산 검정으로 분기하지 않음) | CLM-22(SRC-127) + CLM-24(시뮬레이션: Student 22.3% vs Welch 5.6%) | 최우선 | Phase 1 (MVP 범위 변경 제안) | proposed — Ian 결정 필요 |
| NAV-REQ-03 | 위험3 연계 | 효과크기(Cohen's d)를 Welch's t-test와 정합적인 방식(예: Glass's delta 또는 등분산 비의존 대안)으로 재검토 | Review Pass 2 놓쳤던 점3 | 중 | Phase 1 | proposed |
| NAV-REQ-04 | 신규위험7(자기상관) | Navigator 진입 질문에 "이 데이터가 시간순으로 연속 수집되었습니까?"를 추가하고, YES인 경우 런차트/시차산점도(lag plot)로 자기상관 여부를 먼저 안내 | Review Pass 2 신규위험7(SRC-128,129) + CLM-26(시뮬레이션: rho 0→0.9 시 1종오류율 4.7%→63.8%, 4개 시나리오 중 최대 효과) | **최우선(시뮬레이션 근거상 1위)** | Phase 1(질문 추가)·Phase 2(정식 ACF/PACF는 spc-profile.md SPC 기능과 연계) | proposed |
| NAV-REQ-05 | 위험2(표본수) | 그룹당 표본수 n<10일 때 "참고용" 신뢰도 배지, n≥30일 때 정규성 위반 경고 강도를 낮추는 표본수-조건부 신뢰도 표시 | Review Pass 2 놓쳤던 점1(CLT) + CLM-27(시뮬레이션: 지수분포에서도 n=5부터 명목값 근접) | 중 | Phase 1.5 | proposed |
| NAV-REQ-06 | 위험5(다중비교) | 동일 CTQ에 대해 짧은 시간 내 2-Sample t-test가 2회 이상 반복되면 "3개 이상 그룹 비교는 ANOVA를 권장합니다" 안내 표시 | CLM-25(시뮬레이션: pairwise FWER 12.5% vs ANOVA 5.0%) | 중 | Phase 1.5 | proposed |
| NAV-REQ-07 | 위험4(ANOVA 순서) | ANOVA 트리에도 NAV-REQ-01과 동일한 순서 원칙 적용(정규성·등분산·독립성 선확인) | Review Pass 1 위험4 | 중 (NAV-REQ-01과 함께 처리) | Phase 1 | proposed |
| NAV-REQ-08 | 위험6(비모수 대안) | 정규성 위반 시 최소 Mann-Whitney U 하나만이라도 Phase 1에 포함할지, P3 실데이터로 위반 빈도를 확인한 뒤 결정 | Review Pass 1 위험6 | 낮음(데이터 의존적 결정) | Phase 1 또는 2 — 데이터 확인 후 결정 | deferred(P3 대기) |

## 검증되지 않은 가정 (반드시 표시)

- 시뮬레이션 수치(22.3%, 63.8% 등)는 합성데이터 기준이며, 실제 CTQ 데이터에서의 실제 발생 빈도가 아닙니다. **"이 정도로 위험할 수 있다"는 예시일 뿐 "이 정도로 위험하다"가 아닙니다.**
- NAV-REQ-02(Welch 기본값화)와 NAV-REQ-04(자기상관 체크)는 Phase 1 범위를 확장합니다 — 개발 리소스·일정에 영향을 줄 수 있으므로 제품 로드맵 결정은 별도입니다.
- 이 요구사항들은 통계 이론적 정합성 관점에서 도출되었으며, 실제 사용자(Ian 등)가 이를 UI에서 이해하고 신뢰할 수 있는지는 별도의 사용성 검증(GAP-02, GAP-05)이 필요합니다.

## 다음 단계

1. Ian이 NAV-REQ-01~08 중 Phase 1 채택 여부(특히 REQ-02, REQ-04)를 결정.
2. P3(Data readiness)에서 실 CTQ 데이터 확보 시, 정규성/등분산/자기상관 실제 위반 빈도를 실측하여 이 문서의 우선순위를 재검증.
3. 실 통계 전문가 확보 시 이 문서 전체를 최우선으로 재검토.
