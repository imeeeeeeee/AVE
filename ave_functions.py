import numpy as np
import pandas as pd
from config import STRI_COEFFICIENTS, ELASTICITIES, SECTOR_CODES


def calculate_stri_simulated(stri_now, stri_benchmark):
    return stri_now - 0.5 * (stri_now - stri_benchmark)

def compute_ave(stri_now, stri_simulated, beta_k, sigma_k):
    return np.exp(-((stri_now - stri_simulated) * beta_k) / (sigma_k - 1)) - 1

def compute_confidence_interval(stri_now, stri_simulated, beta_k, beta_se, sigma_k):
    ave_upper = np.exp(-((stri_now - stri_simulated) * (beta_k - 1.96 * beta_se)) / (sigma_k - 1)) - 1
    ave_lower = np.exp(-((stri_now - stri_simulated) * (beta_k + 1.96 * beta_se)) / (sigma_k - 1)) - 1
    return -1*ave_lower, -1*ave_upper

def ave_simulator(stri_now_dict, stri_benchmark_dict):
    results = []
    for sector in stri_now_dict:
        stri_now = stri_now_dict[sector][1]
        stri_benchmark = stri_benchmark_dict[SECTOR_CODES[sector][0]][1]
        print(stri_benchmark)
        stri_sim = calculate_stri_simulated(stri_now, stri_benchmark)

        beta_k, beta_se = STRI_COEFFICIENTS[SECTOR_CODES[sector][1]]
        sigma_k = ELASTICITIES[SECTOR_CODES[sector][1]]

        ave = -1*compute_ave(stri_now, stri_sim, beta_k, sigma_k)
        ci_low, ci_high = compute_confidence_interval(stri_now, stri_sim, beta_k, beta_se, sigma_k)

        results.append({
            "Sector": sector,
            "STRI_now": stri_now,
            "STRI_benchmark": stri_benchmark,
            "STRI_benchmark_country": stri_benchmark_dict[SECTOR_CODES[sector][0]][0],
            "STRI_simulated": stri_sim,
            "AVE": ave,
            "AVE_CI_Lower": ci_low,
            "AVE_CI_Upper": ci_high
        })

    return pd.DataFrame(results)

# Example usage
if __name__ == "__main__":
    # Example STRI values
    stri_now_example = {
        "Communication": 0.25,
        "Business": 0.30,
        "Finance": 0.40,
        "Insurance": 0.35,
        "Transport": 0.45
    }

    stri_benchmark_example = {
        "Communication": 0.10,
        "Business": 0.15,
        "Finance": 0.20,
        "Insurance": 0.18,
        "Transport": 0.22
    }

    df_results = ave_simulator(stri_now_example, stri_benchmark_example)
    print(df_results)
