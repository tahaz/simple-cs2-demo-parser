import os
import polars as pl

def filter_by_tick(folder, keyword, every_n, verbose=True):
    for f in os.listdir(folder):
        if keyword in f and f.endswith(".csv"):
            path = os.path.join(folder, f)
            if verbose:
                print(f"Filtering {f}")
            df = pl.read_csv(path)
            if "tick" in df.columns:
                df = df.filter(pl.col("tick") % every_n == 0)
                df.write_csv(path)
                if verbose:
                    print(f"Saved filtered: {f}")
            else:
                if verbose:
                    print(f"No 'tick' column in {f}, skipped")
