# Assuming label_coors is a dictionary where study_id maps to a list of series_ids
label_coors = {
    'study1': ['series1', 'series2', 'series3'],
    'study2': ['series4', 'series5']
}

def check_series_id_in_study(series_id, study_id, label_coors):
    if series_id not in label_coors.get(study_id, []):
        print(f"{series_id} does not exist in the list for {study_id}")
    else:
        print(f"{series_id} exists in the list for {study_id}")

# Example usage
check_series_id_in_study('series3', 'study1', label_coors)  # Output: series3 exists in the list for study1
check_series_id_in_study('series6', 'study2', label_coors)  # Output: series6 does not exist in the list for study2
