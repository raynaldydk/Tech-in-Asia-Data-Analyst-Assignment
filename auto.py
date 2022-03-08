from tia import *

df = auto_get(url=auto_url, params=params, headers=headers)
dt = datetime.date(datetime.now())
df.to_csv(f'tia_posts - {dt}.csv', index=False)