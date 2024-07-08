"""
Main script for the Math-Sim project, demonstrating mathematical simulations and visualizations.
"""

import argparse
import concurrent.futures
from .concurrent_math_sim import run_concurrent_simulations, parallel_prime_factorization
from .algorithms.aliquot_sequence.aliquot_sequence import aliquot_sequence
from .algorithms.aliquot_sequence.aliquot_sequence_viz import plot_aliquot_sequence
from .algorithms.collatz_conjecture.collatz_conjecture import collatz_conjecture
from .algorithms.collatz_conjecture.collatz_conjecture_viz import plot_collatz_sequence
from .algorithms.fibonacci_sequence.fibonacci_sequence import fibonacci_sequence
from .algorithms.fibonacci_sequence.fibonacci_sequence_viz import plot_fibonacci_sequence
from .algorithms.sieve_of_eratosthenes.sieve_of_eratosthenes import sieve_of_eratosthenes
from .algorithms.sieve_of_eratosthenes.sieve_viz import plot_prime_spiral, plot_prime_distribution
from .resource_monitor import factorize

def main():
    parser = argparse.ArgumentParser(description="Run mathematical simulations and visualizations.")
    parser.add_argument("--demo", action="store_true", help="Run a demonstration of all operations")
    parser.add_argument("--aliquot", type=int, help="Starting number for aliquot sequence")
    parser.add_argument("--collatz", type=int, help="Starting number for Collatz conjecture")
    parser.add_argument("--fibonacci", type=int, help="Number of terms for Fibonacci sequence")
    parser.add_argument("--sieve", type=int, help="Upper limit for Sieve of Eratosthenes")
    parser.add_argument("--factorize", type=int, help="Number to factorize")
    parser.add_argument("--parallel-aliquot", type=int, nargs=2, metavar=("START", "COUNT"),
                        help="Generate multiple aliquot sequences: START COUNT")
    parser.add_argument("--parallel-factorize", type=int, nargs="+", 
                        help="Factorize multiple numbers")

    args = parser.parse_args()

    if args.demo:
        run_demo()
    elif args.aliquot:
        run_and_plot_aliquot(args.aliquot)
    elif args.collatz:
        run_and_plot_collatz(args.collatz)
    elif args.fibonacci:
        run_and_plot_fibonacci(args.fibonacci)
    elif args.sieve:
        run_sieve(args.sieve)
    elif args.factorize:
        run_factorization(args.factorize)
    elif args.parallel_aliquot:
        run_parallel_aliquot(args.parallel_aliquot[0], args.parallel_aliquot[1])
    elif args.parallel_factorize:
        run_parallel_factorization(args.parallel_factorize)
    else:
        parser.print_help()

def run_demo():
    print("Running demonstration of all operations:")
    run_and_plot_aliquot(220)
    run_and_plot_collatz(27)
    run_and_plot_fibonacci(20)
    run_sieve(100)
    run_factorization(84)
    run_parallel_aliquot(10, 5)
    run_parallel_factorization([84, 100, 123, 456])

def run_and_plot_aliquot(start):
    print(f"Running Aliquot Sequence starting from {start}")
    sequence, _ = aliquot_sequence(start)
    print(f"Sequence: {sequence}")
    plot_aliquot_sequence(start)
    print(f"Plots saved as 'aliquot_sequence_{start}.png' and 'aliquot_resource_usage_{start}.png'")

def run_and_plot_collatz(start):
    print(f"Running Collatz Conjecture starting from {start}")
    sequence, _ = collatz_conjecture(start)
    print(f"Sequence: {sequence}")
    plot_collatz_sequence(start)
    print(f"Plots saved as 'collatz_sequence_{start}.png' and 'collatz_resource_usage_{start}.png'")

def run_and_plot_fibonacci(terms):
    print(f"Generating Fibonacci Sequence with {terms} terms")
    sequence, _ = fibonacci_sequence(terms)
    print(f"Sequence: {sequence}")
    plot_fibonacci_sequence(terms)
    print(f"Plots saved as 'fibonacci_sequence_{terms}.png' and 'fibonacci_resource_usage_{terms}.png'")

def run_sieve(limit):
    print(f"Running Sieve of Eratosthenes up to {limit}")
    primes, _ = sieve_of_eratosthenes(limit)
    print(f"Number of primes found: {len(primes)}")
    print(f"First few primes: {primes[:10]}...")
    plot_prime_spiral(limit)
    plot_prime_distribution(limit)
    print(f"Plots saved as 'prime_spiral_{limit}.png' and 'prime_distribution_{limit}.png'")

def run_factorization(number):
    print(f"Factorizing {number}")
    factors, _ = factorize(number)
    print(f"Factors: {factors}")

def run_parallel_aliquot(start, count):
    print(f"Generating {count} aliquot sequences starting from {start}")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(aliquot_sequence, start + i): start + i for i in range(count)}
        results = {}
        for future in concurrent.futures.as_completed(futures):
            num = futures[future]
            try:
                sequence, _ = future.result()
                results[num] = sequence
                print(f"Aliquot sequence starting from {num}: {sequence}")
            except Exception as e:
                print(f"An error occurred for {num}: {str(e)}")

def run_parallel_factorization(numbers):
    print(f"Factorizing numbers: {numbers}")
    results = parallel_prime_factorization(numbers)
    for num, factors in results.items():
        print(f"Factors of {num}: {factors}")

if __name__ == "__main__":
    main()