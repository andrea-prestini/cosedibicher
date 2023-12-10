from datetime import datetime


@lambda _: _()
def func() -> str:
    time_text = f'Started ad: {datetime.now():%H:%M:%S}'
    print(time_text)
    return time_text
