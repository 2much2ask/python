import os

sum_files_100 = 0
sum_files_1000 = 0
sum_files_10000 = 0
sum_files_100000 = 0
folder_stat = {}
folder = os.path.join(os.path.dirname(__file__), 'some_data')

for root, dirs, files in os.walk(folder):
    for file in files:
        file_size = os.stat(os.path.join(folder, file)).st_size
        if 0 <= file_size < 100:
            sum_files_100 += 1
        elif 100 <= file_size < 1000:
            sum_files_1000 += 1
        elif 1000 <= file_size < 10000:
            sum_files_10000 += 1
        else:
            sum_files_100000 += 1
folder_stat['100'] = sum_files_100
folder_stat['1000'] = sum_files_1000
folder_stat['10000'] = sum_files_10000
folder_stat['100000'] = sum_files_100000

print(folder_stat)
