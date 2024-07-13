import pandas as pd
import argparse 
import json

def load_csv(file_name):
    return pd.read_csv(file_name)

def write_to_json(df, file_name):
    with open(file_name, "w") as file:
        json_fields = df.columns.tolist()
        obj_map = {}
        for field in json_fields:
            value = df.iloc[0][field]
            if isinstance(value, pd.Series):
                obj_map[field] = value.to_list()
            elif pd.api.types.is_numeric_dtype(value):
                obj_map[field] = pd.to_numeric(value).item()
            else:
                obj_map[field] = value
        json.dump(obj_map, file, indent=4)

def write_to_json_list(df, file_name):
    json_fields = df.columns.tolist()
    objs = []

    with open(file_name, "w") as file:
        for index, row in df.iterrows():
            obj_map = {}
            for field in json_fields:
                obj_map[field] = row[field]
            objs.append(obj_map)

        json.dump(objs, file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A Simple script to turn csv into json')
    parser.add_argument('input_file', type=str, help='input csv file')
    parser.add_argument('json_file', type=str, help='output json file name')
    
    args = parser.parse_args()
    intput_csv = args.input_file
    output_json = args.json_file

    csv_df = load_csv(intput_csv)
    if len(csv_df) != 1:
        write_to_json_list(csv_df, output_json)
    else:
        write_to_json(csv_df, output_json)
