"""
This module implements concurrent execution of mathematical simulations.
It utilizes the concurrent.futures module to run multiple algorithms in parallel.
"""

import concurrent.futures
from typing import Dict, Any
from .algorithms.aliquot_sequence.aliquot_sequence import aliquot_sequence
from .algorithms.sieve_of_eratosthenes.sieve_of_eratosthenes import sieve_of_eratosthenes
from .resource_monitor import factorize

def run_concurrent_simulations(aliquot_input: int, sieve_input: int, factorize_input: int) -> Dict[str, Any]:
    """
    Run multiple mathematical simulations concurrently.

    :param aliquot_input: Input for the aliquot sequence algorithm
    :param sieve_input: Input for the Sieve of Eratosthenes algorithm
    :param factorize_input: Input for the factorization algorithm
    :return: Dictionary containing the results of each algorithm
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        aliquot_future = executor.submit(aliquot_sequence, aliquot_input)
        sieve_future = executor.submit(sieve_of_eratosthenes, sieve_input)
        factorize_future = executor.submit(factorize, factorize_input)

        results = {}
        for future in concurrent.futures.as_completed([aliquot_future, sieve_future, factorize_future]):
            try:
                result = future.result()
                if future == aliquot_future:
                    results['aliquot'] = result[0]
                elif future == sieve_future:
                    results['sieve'] = result[0]
                elif future == factorize_future:
                    results['factorize'] = result[0]
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    return results

def parallel_prime_factorization(numbers: list) -> Dict[int, list]:
    """
    Perform prime factorization on multiple numbers in parallel.

    :param numbers: List of numbers to factorize
    :return: Dictionary mapping input numbers to their prime factors
    """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(factorize, num): num for num in numbers}
        results = {}
        for future in concurrent.futures.as_completed(futures):
            num = futures[future]
            try:
                factors, _ = future.result()
                results[num] = factors
            except Exception as e:
                print(f"An error occurred for {num}: {str(e)}")
    return results