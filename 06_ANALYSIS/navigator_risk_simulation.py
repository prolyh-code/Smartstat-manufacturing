"""
Navigator_Logic_Statistical_Audit.md의 7개 위험 중 시뮬레이션으로 정량화 가능한 4개를 검증한다.
실제 사내 CTQ 데이터가 아닌 합성(synthetic) 데이터를 사용한 몬테카를로 시뮬레이션이다(벡터화 버전).
목적: '이론적으로 위험하다'는 주장을, 재현 가능한 수치(경험적 1종 오류율)로 뒷받침한다.

실행: python3 navigator_risk_simulation.py
난수 시드를 고정하여 재현성을 확보한다(engineer-research-lifecycle 스킬의 재현성 요구사항).
"""
import numpy as np
from scipy import stats
import json

RNG_SEED = 20260909
N_REPS = 20000
ALPHA = 0.05


def scenario_a_welch_vs_student():
    """가장 위험한 배치: '작은 표본이 큰 분산'을 갖는 경우(Student's t가 반자유도적/anti-conservative가
    되어 1종오류율이 부풀려지는 고전적 위험 사례). CASE-001처럼 소수 샘플만 보는 상황에서 그 소수
    샘플의 변동이 실제로는 더 클 수 있다는 현실적 가정."""
    rng = np.random.default_rng(RNG_SEED)
    n_small, n_large = 5, 15
    sd_small, sd_large = 3.0, 1.0  # 작은 표본이 큰 분산 (worst case, Student's t 반자유도적)
    a = rng.normal(0, sd_small, size=(N_REPS, n_small))
    b = rng.normal(0, sd_large, size=(N_REPS, n_large))
    _, p_student = stats.ttest_ind(a, b, axis=1, equal_var=True)
    _, p_welch = stats.ttest_ind(a, b, axis=1, equal_var=False)
    # 반대 배치(작은 표본이 작은 분산 — 보수적 방향)도 함께 계산해 비대칭성을 보여준다
    a2 = rng.normal(0, sd_large_small := 1.0, size=(N_REPS, n_small))
    b2 = rng.normal(0, sd_small_large := 3.0, size=(N_REPS, n_large))
    _, p_student_conservative = stats.ttest_ind(a2, b2, axis=1, equal_var=True)
    return {
        "scenario": "A: 등분산위반+표본불균형(작은표본n=5·큰분산sd=3 vs 큰표본n=15·작은분산sd=1), 실제 평균차이 없음",
        "nominal_alpha": ALPHA,
        "student_type1_error_worst_case": float(np.mean(p_student < ALPHA)),
        "welch_type1_error_worst_case": float(np.mean(p_welch < ALPHA)),
        "student_type1_error_opposite_pairing(작은표본·작은분산)": float(np.mean(p_student_conservative < ALPHA)),
        "interpretation": "worst_case에서 Student's t가 명목 5%보다 크게 벗어나면(반자유도적) CLM-22(Welch 기본값화)의 근거가 되고, opposite_pairing과 비교하면 '작은표본-큰분산' 배치가 특히 위험함을 보여준다",
    }


def scenario_b_clt_robustness():
    rng = np.random.default_rng(RNG_SEED + 1)
    results = {}
    for n in (5, 10, 30, 50):
        a = rng.exponential(scale=1.0, size=(N_REPS, n))
        b = rng.exponential(scale=1.0, size=(N_REPS, n))
        _, p = stats.ttest_ind(a, b, axis=1, equal_var=True)
        results[f"n={n}"] = float(np.mean(p < ALPHA))
    return {
        "scenario": "B: 우측왜도(지수분포) 데이터, 표본수별 t-test 1종오류율",
        "nominal_alpha": ALPHA,
        "type1_error_by_n": results,
        "interpretation": "n이 커질수록 5%에 수렴하면 CLT 완화효과(놓쳤던 점1) 확인; 작은 n에서만 벗어나면 표본수-조건부 경고가 타당",
    }


def scenario_c_multiple_comparisons():
    rng = np.random.default_rng(RNG_SEED + 2)
    n = 10
    a = rng.normal(0, 1, size=(N_REPS, n))
    b = rng.normal(0, 1, size=(N_REPS, n))
    c = rng.normal(0, 1, size=(N_REPS, n))
    p_ab = stats.ttest_ind(a, b, axis=1).pvalue
    p_ac = stats.ttest_ind(a, c, axis=1).pvalue
    p_bc = stats.ttest_ind(b, c, axis=1).pvalue
    fwer = np.mean((p_ab < ALPHA) | (p_ac < ALPHA) | (p_bc < ALPHA))
    _, p_anova = stats.f_oneway(a.T, b.T, c.T)  # f_oneway broadcasts over columns when given 2D (n, N_REPS)
    anova_reject = np.mean(p_anova < ALPHA)
    return {
        "scenario": "C: 3그룹 실제차이 없음 — 반복 pairwise t-test(3회) vs 단일 ANOVA",
        "nominal_alpha_per_test": ALPHA,
        "pairwise_familywise_error_rate": float(fwer),
        "anova_type1_error": float(anova_reject),
        "interpretation": "pairwise FWER이 5%를 크게 초과하고 ANOVA는 5%에 가까우면 위험5(다중비교 미보정)가 실질적임을 뒷받침",
    }


def ar1_matrix(rng, rho, n, n_reps, sigma=1.0):
    """(n_reps, n) 형태의 AR(1) 시계열을 벡터화하여 생성."""
    innov_sd = sigma * np.sqrt(1 - rho ** 2) if abs(rho) < 1 else sigma
    innovations = rng.normal(0, innov_sd, size=(n_reps, n))
    x = np.zeros((n_reps, n))
    x[:, 0] = rng.normal(0, sigma, size=n_reps)
    for i in range(1, n):
        x[:, i] = rho * x[:, i - 1] + innovations[:, i]
    return x


def scenario_d_autocorrelation():
    rng = np.random.default_rng(RNG_SEED + 3)
    n_total = 40
    results = {}
    for rho in (0.0, 0.5, 0.7, 0.9):
        series = ar1_matrix(rng, rho, n_total, N_REPS)
        first, second = series[:, : n_total // 2], series[:, n_total // 2:]
        _, p = stats.ttest_ind(first, second, axis=1, equal_var=True)
        results[f"rho={rho}"] = float(np.mean(p < ALPHA))
    return {
        "scenario": "D: 동일 AR(1) 공정을 전/후반부로 나눠 비교(실제 차이 없음), 자기상관 강도별 1종오류율",
        "nominal_alpha": ALPHA,
        "type1_error_by_rho": results,
        "interpretation": "rho가 커질수록(자기상관 강함) 1종오류율이 5%를 초과해 상승하면 위험7(독립성 미확인)이 실질적 위험임을 뒷받침",
    }


if __name__ == "__main__":
    out = {
        "run_id": "RUN-009",
        "seed": RNG_SEED,
        "n_reps": N_REPS,
        "results": [
            scenario_a_welch_vs_student(),
            scenario_b_clt_robustness(),
            scenario_c_multiple_comparisons(),
            scenario_d_autocorrelation(),
        ],
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    with open("navigator_risk_simulation_results.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
