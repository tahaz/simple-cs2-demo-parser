import os
import argparse
from helpful_demo_functions import filter_by_tick
from demo_parser import parse_demos


def load_dataframes_list(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataframe list file not found: {file_path}")
    with open(file_path, 'r') as f:
        content = f.read().replace("\n", ",")
        return [df.strip() for df in content.split(",") if df.strip()]

def main():
    parser = argparse.ArgumentParser(description="Parse and filter CS2 demos.")
    parser.add_argument("--demos_folder", type=str, required=True, help="Folder with .dem files")
    parser.add_argument("--output_folder", type=str, required=True, help="Folder to save parsed demos as CSVs")
    parser.add_argument("--dataframe_typelist", type=str, required=True, help="Path to comma-separated dataframe list (txt file)")
    parser.add_argument("--df_to_filter_name", type=str, default="grenades", help="Keyword for which dataframes to shorten (e.g., 'grenades')")
    parser.add_argument("--num_tick_saved", type=int, default=8, help="Keep every n-th tick where input is n")
    parser.add_argument("--no-filter", action="store_true", help="Skip the filter step if size not important")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    os.makedirs(args.output_folder, exist_ok=True)

    demo_type_list = load_dataframes_list(args.dataframe_typelist)

    parse_demos(args.demos_folder, args.output_folder, demo_type_list, verbose=args.verbose)

    if not args.no_filter:
        filter_by_tick(args.output_folder, args.df_to_filter_name, args.num_tick_saved, verbose=args.verbose)

if __name__ == '__main__':
    main()