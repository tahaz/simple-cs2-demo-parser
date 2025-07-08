import os
import polars as pl
from awpy import Demo


def parse_demos(in_folder, out_folder, dataframes_to_save, verbose=True):
    files = [f for f in os.listdir(in_folder) if f.endswith(".dem")]

    for f in files:
        path = os.path.join(in_folder, f)
        if verbose:
            print(f"Parsing {f}")
        try:
            demo = Demo(path, verbose=verbose)
            demo.parse()
            name = os.path.splitext(f)[0]

            for df_name in dataframes_to_save:
                df = getattr(demo, df_name, None)
                if isinstance(df, pl.DataFrame) and df.height > 0:
                    out_path = os.path.join(out_folder, f"{name}_{df_name}.csv")
                    df.write_csv(out_path)
                    if verbose:
                        print(f"Saved: {out_path}")
        except Exception as e:
            print(f"Problem with {f}: {e}")