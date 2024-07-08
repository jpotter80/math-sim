"""
This module contains tests for concurrent execution of mathematical simulations.
"""

import pytest
from math_sim.concurrent_math_sim import run_concurrent_simulations, parallel_aliquot_sequence, parallel_prime_factorization

@pytest.mark.timeout(30)
def test_run_concurrent_simulations():
    results = run_concurrent_simulations(220, 100, 84)
    
    assert 'aliquot' in results
    assert 'sieve' in results
    assert 'factorize' in results
    
    assert results['aliquot'] == [220, 284]
    assert results['sieve'] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert results['factorize'] == [2, 2, 3, 7]

@pytest.mark.timeout(30)
def test_parallel_aliquot_sequence():
    results = parallel_aliquot_sequence(10, 3)
    
    assert len(results) == 3
    assert 10 in results
    assert 11 in results
    assert 12 in results
    
    assert results[10] == [10, 8, 7, 1, 0]
    assert results[11] == [11, 1, 0]
    assert results[12] == [12, 16, 15, 9, 4, 3, 1, 0]

@pytest.mark.timeout(30)
def test_parallel_prime_factorization():
    results = parallel_prime_factorization([84, 100, 123])
    
    assert len(results) == 3
    assert 84 in results
    assert 100 in results
    assert 123 in results
    
    assert results[84] == [2, 2, 3, 7]
    assert results[100] == [2, 2, 5, 5]
    assert results[123] == [3, 41]

@pytest.mark.timeout(30)
def test_concurrent_error_handling():
    # Test with invalid inputs to ensure error handling works
    results = run_concurrent_simulations(-1, -1, -1)
    
    assert 'aliquot' not in results
    assert 'sieve' not in results
    assert 'factorize' not in results
    assert len(results) == 0

if __name__ == "__main__":
    pytest.main(["-v", "--tb=short"])
