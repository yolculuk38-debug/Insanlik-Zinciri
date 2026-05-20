from typing import Dict, List


RISK_FLAG_RULES = {
    "hash_mismatch": "CRITICAL_INTEGRITY_FAILURE",
    "duplicate_witnesses": "WITNESS_DUPLICATION_DETECTED",
    "timestamp_inconsistency": "TIMESTAMP_ANOMALY",
    "unverified_source": "UNVERIFIED_SOURCE",
}


def build_risk_flags(indicators: List[str]) -> Dict:
    """Convert low-level indicators into standardized HC:// risk flags."""

    if indicators is None:
        indicators = []

    if not isinstance(indicators, list):
        raise ValueError("indicators must be a list")

    flags = []

    for indicator in indicators:
        if not isinstance(indicator, str):
            continue

        normalized = indicator.strip().lower()

        if normalized in RISK_FLAG_RULES:
            flags.append(RISK_FLAG_RULES[normalized])

    unique_flags = sorted(set(flags))

    return {
        "risk_flags": unique_flags,
        "risk_flag_count": len(unique_flags),
        "high_risk": "CRITICAL_INTEGRITY_FAILURE" in unique_flags,
        "experimental": True,
    }
