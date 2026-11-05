from rich import print
import time


timeline_split_cache = {}


def get_data(file_path: str) -> list[str]:
    data = []
    with open(file_path, 'r') as f:
        data = f.readlines()

    return [line.strip() for line in data]

def run_timeline_and_get_splits_at_end(data: list[str], start_line, start_column) -> int:
    '''
    get map, line, column

    check in cache if value exists for this line+column combination and return if exists
        
    look for splitter
    
    if splitter found
        create left timeline
        create right timeline
        cache and return splits from above timelines

    else no splitter, return 1 (base case)
    
    '''
    cache_key = f'{start_line}, {start_column}'
    if cache_key in timeline_split_cache:
        return timeline_split_cache[cache_key]

    timeline_data = data.copy()
    total_splits_at_end = 0
    column_path = list(zip(*timeline_data))[start_column][start_line:]
    try:
        splitter_position = column_path.index('^')
    except ValueError:
        # No splitter found, means timeline reaches end - base case for recursion
        total_splits_at_end = 1

        timeline_split_cache[cache_key] = total_splits_at_end
        return total_splits_at_end
    
    splitter_line_position_in_main_data = splitter_position + start_line

    total_splits_at_end += run_timeline_and_get_splits_at_end(timeline_data, splitter_line_position_in_main_data+1, start_column-1) # left timeline
    total_splits_at_end += run_timeline_and_get_splits_at_end(timeline_data, splitter_line_position_in_main_data+1, start_column+1) # right timeline
    
    timeline_split_cache[cache_key] = total_splits_at_end
    return total_splits_at_end


def main(file_path: str):

    data = get_data(file_path)

    total_splits = 0

    start_column_position = data[0].index('S')
    start_line_position = 1

    total_splits = run_timeline_and_get_splits_at_end(data, start_line_position, start_column_position)

    print(total_splits)
    



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))

    start_time = time.perf_counter()

    main(file_path)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print(f'Run Time: {elapsed_time // 60}m {elapsed_time%60}s')
