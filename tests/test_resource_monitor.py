"""
This module contains unit tests for the resource_monitor module.
"""

import pytest
import time
from math_sim.resource_monitor import ResourceMonitor, aliquot_sequence, sieve_of_eratosthenes, factorize

def test_resource_monitor_init():
    """Test the initialization of ResourceMonitor."""
    monitor = ResourceMonitor(max_memory_percent=80, max_cpu_percent=90)
    assert monitor.max_memory_percent == 80
    assert monitor.max_cpu_percent == 90
    assert not monitor.memory_usage
    assert not monitor.cpu_usage
    assert not monitor.time_points

def test_check_resources():
    """Test the check_resources method of ResourceMonitor."""
    monitor = ResourceMonitor()
    memory_usage, cpu_usage = monitor.check_resources()
    assert isinstance(memory_usage, float)
    assert isinstance(cpu_usage, float)
    assert 0 <= memory_usage <= 100
    assert 0 <= cpu_usage <= 100
    assert len(monitor.memory_usage) == 1
    assert len(monitor.cpu_usage) == 1
    assert len(monitor.time_points) == 1

def test_aliquot_sequence():
    """Test the aliquot_sequence function."""
    result, monitor = aliquot_sequence(220, max_steps=10)
    assert result == [220, 284]
    assert isinstance(monitor, ResourceMonitor)
    assert monitor.memory_usage
    assert monitor.cpu_usage
    assert monitor.time_points

def test_sieve_of_eratosthenes():
    """Test the sieve_of_eratosthenes function."""
    primes, monitor = sieve_of_eratosthenes(30)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert isinstance(monitor, ResourceMonitor)
    assert monitor.memory_usage
    assert monitor.cpu_usage
    assert monitor.time_points

def test_factorize():
    """Test the factorize function."""
    factors, monitor = factorize(84)
    assert factors == [2, 2, 3, 7]
    assert isinstance(monitor, ResourceMonitor)
    assert monitor.memory_usage
    assert monitor.cpu_usage
    assert monitor.time_points

def test_resource_limits():
    """Test the resource limit functionality of ResourceMonitor."""
    with pytest.raises(MemoryError):
        monitor = ResourceMonitor(max_memory_percent=0)
        monitor.check_resources()
    
    def cpu_intensive_task():
        start_time = time.time()
        while time.time() - start_time < 0.5:  # Run for 0.5 seconds
            pass  # This will consume CPU

    with pytest.raises(RuntimeError):
        monitor = ResourceMonitor(max_cpu_percent=0)
        cpu_intensive_task()  # Increase CPU usage
        monitor.check_resources()

def test_aliquot_sequence_long():
    """Test the aliquot_sequence function with a longer sequence."""
    result, monitor = aliquot_sequence(276, max_steps=100)
    expected = [276, 396, 696, 1104, 1872, 3078, 4752, 8478, 15900, 31248, 52464, 95760, 166944, 288384, 493728, 
                817464, 1360728, 2392800, 3967920, 6542688, 10768920, 17767728, 29362752, 48442240, 79833792, 
                131817984, 217213408, 357744960, 588935040, 966840960, 1587495840, 2605829280, 4272712560]
    assert result == expected
    assert isinstance(monitor, ResourceMonitor)
    assert len(monitor.memory_usage) > 50
    assert len(monitor.cpu_usage) > 50
    assert len(monitor.time_points) > 50

def test_sieve_of_eratosthenes_large():
    """Test the sieve_of_eratosthenes function with a larger input."""
    primes, monitor = sieve_of_eratosthenes(1000)
    assert len(primes) == 168  # There are 168 primes below 1000
    assert primes[-1] == 997  # The largest prime below 1000
    assert isinstance(monitor, ResourceMonitor)
    assert len(monitor.memory_usage) > 100
    assert len(monitor.cpu_usage) > 100
    assert len(monitor.time_points) > 100

def test_factorize_large():
    """Test the factorize function with a larger input."""
    number = 123456789
    factors, monitor = factorize(number)
    assert factors == [3, 3, 3607, 3803]
    assert isinstance(monitor, ResourceMonitor)
    assert len(monitor.memory_usage) > 1000
    assert len(monitor.cpu_usage) > 1000
    assert len(monitor.time_points) > 1000

def test_resource_monitor_multiple_checks():
    """Test multiple resource checks with ResourceMonitor."""
    monitor = ResourceMonitor()
    for _ in range(10):
        monitor.check_resources()
        time.sleep(0.1)  # Short delay to simulate work
    assert len(monitor.memory_usage) == 10
    assert len(monitor.cpu_usage) == 10
    assert len(monitor.time_points) == 10
    assert all(0 <= m <= 100 for m in monitor.memory_usage)
    assert all(0 <= c <= 100 for c in monitor.cpu_usage)
    assert monitor.time_points[-1] > monitor.time_points[0]

if __name__ == "__main__":
    pytest.main()