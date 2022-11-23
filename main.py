from pathlib import Path
import json
import sys

def main():
    """
    simple script to 
     1 open settings.json file
     2 reorder-the-profiles-alphabetically
     3 update the contents of the settings.json file
    """
    args = sys.argv[1:]
    if len(args) == 0:
        print( "error - path to setting.json file required")

    # 1 reeading profile data
    print('reeading profile data')
    path_to_config = Path(args[0])
    with open(path_to_config) as f:
        json_data = json.load(f)
        data_list = json_data['profiles']['list']

    # 2 reordering profile data
    print('reordering profile data')
    json_data['profiles']['list'] = sorted(data_list, key=lambda k: k['name'])

    # Serializing json
    json_object = json.dumps(json_data, indent=4)

    # 3 writing profile data
    print('writing profile data')
    with open(path_to_config, "w") as outfile:
        outfile.write(json_object)

if __name__=="__main__":
    main()