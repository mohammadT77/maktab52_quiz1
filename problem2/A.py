from time import sleep

import jdatetime as jdatetime


class TimestampOpen:

    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self._file = open(self.file_path, self.mode)
        self._open_timestamp = jdatetime.datetime.now()
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        self._close_timestamp = jdatetime.datetime.now()
        with open(self.file_path, 'a') as f:
            print('\nOpened at:', self._open_timestamp, file=f)
            print('Closed at:', self._close_timestamp, file=f)


# Test
with TimestampOpen('test.txt', 'w') as f:
    f.write('Test...')
    sleep(2)

with TimestampOpen('test.txt') as f:
    print(f.read())