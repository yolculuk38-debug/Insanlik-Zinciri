import pytest

from hc_trust.risk_flags import build_risk_flags


def test_build_risk_flags_empty():
    result = build_risk_flags([])

    assert result["risk_flags"] == []
    assert result["risk_flag_count"] == 0
    assert result["high_risk"] is False


def test_build_risk_flags_hash_mismatch():
    result = build_risk_flags(["hash_mismatch"])

    assert result["risk_flags"] == ["CRITICAL_INTEGRITY_FAILURE"]
    assert result["risk_flag_count"] == 1
    assert result["high_risk"] is True


def test_build_risk_flags_multiple_indicators():
    result = build_risk_flags(
        [
            "hash_mismatch",
            "duplicate_witnesses",
            "timestamp_inconsistency",
            "duplicate_witnesses",
        ]
    )

    assert result["risk_flag_count"] == 3
    assert "TIMESTAMP_ANOMALY" in result["risk_flags"]


def test_build_risk_flags_requires_list():
    with pytest.raises(ValueError, match="indicators must be a list"):
        build_risk_flags("hash_mismatch")
