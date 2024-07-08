"""
This module contains unit tests for the resource_monitor module.
"""

import pytest
from math_sim.resource_monitor import ResourceMonitor, aliquot_sequence, sieve_of_eratosthenes, factorize

@pytest.fixture(scope="module")
def resource_monitor():
    return ResourceMonitor()

def test_resource_monitor_init(resource_monitor):
    assert resource_monitor.max_memory_percent == 90
    assert resource_monitor.max_cpu_percent == 95
    assert not resource_monitor.memory_usage
    assert not resource_monitor.cpu_usage
    assert not resource_monitor.time_points

@pytest.mark.timeout(5)
def test_check_resources(resource_monitor):
    memory_usage, cpu_usage = resource_monitor.check_resources()
    assert isinstance(memory_usage, float)
    assert isinstance(cpu_usage, float)
    assert 0 <= memory_usage <= 100
    assert 0 <= cpu_usage <= 100
    assert len(resource_monitor.memory_usage) == 1
    assert len(resource_monitor.cpu_usage) == 1
    assert len(resource_monitor.time_points) == 1

@pytest.mark.timeout(10)
@pytest.mark.parametrize("start_num, expected", [
    (220, [220, 284]),
    (10, [10, 8, 7, 1, 0]),
    (12, [12, 16, 15, 9, 4, 3, 1, 0])
])
def test_aliquot_sequence(start_num, expected):
    result, _ = aliquot_sequence(start_num, max_steps=10)
    assert result == expected

@pytest.mark.timeout(10)
def test_sieve_of_eratosthenes():
    primes, _ = sieve_of_eratosthenes(30)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

@pytest.mark.timeout(10)
@pytest.mark.parametrize("num, expected", [
    (84, [2, 2, 3, 7]),
    (17, [17]),
    (100, [2, 2, 5, 5])
])
def test_factorize(num, expected):
    factors, _ = factorize(num)
    assert factors == expected

@pytest.mark.timeout(5)
def test_resource_limits():
    with pytest.raises(MemoryError):
        ResourceMonitor(max_memory_percent=0).check_resources()
    with pytest.raises(RuntimeError):
        monitor = ResourceMonitor(max_cpu_percent=0)
        monitor.check_resources()

@pytest.mark.timeout(30)
def test_aliquot_sequence_long():
    result, _ = aliquot_sequence(276, max_steps=50)
    assert len(result) > 10
    assert result[:5] == [276, 396, 696, 1104, 1872]

@pytest.mark.timeout(30)
def test_sieve_of_eratosthenes_large():
    primes, _ = sieve_of_eratosthenes(1000)
    assert len(primes) == 168
    assert primes[-1] == 997

@pytest.mark.timeout(30)
def test_factorize_large():
    factors, _ = factorize(123456)
    assert factors == [2, 2, 2, 2, 2, 2, 3, 643]

if __name__ == "__main__":
    pytest.main(["-v", "--tb=short"])