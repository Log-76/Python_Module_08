import sys
import os
import importlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def check_deps():
    libs = ["pandas", "numpy", "matplotlib", "requests"]
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    missing = False
    for lib in libs:
        try:
            pkg = importlib.import_module(lib)
            print(f"[OK] {lib} ({getattr(pkg, '__version__', 'ready')})")
        except ImportError:
            print(f"[ERROR] {lib} is missing")
            missing = True

    if missing:
        print("\nFix with: pip install -r requirements.txt OR poetry install")
        sys.exit(1)


def run_matrix():
    # Simulation simple de données
    print("\nAnalyzing Matrix data...")
    data = np.random.rand(100)
    df = pd.DataFrame(data, columns=['Signal'])

    # Création du graphique
    print("Generating visualization...")
    df.plot()
    plt.title("Matrix Analysis")
    plt.savefig("matrix_analysis.png")

    if os.path.exists("matrix_analysis.png"):
        print("Analysis complete!")
        print(f"Results saved to: {os.path.abspath('matrix_analysis.png')}")


if __name__ == "__main__":
    check_deps()
    run_matrix()
