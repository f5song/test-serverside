from datetime import datetime, timedelta
from django.utils import timezone

# 1

dt1 = datetime.now()
dt1_aware = timezone.make_aware(dt1)
dt1_aware


# 2 (Monday=1)

future_date = dt1 + timedelta(days=500)
find_weekday = future_date.isoweekday()



days = ['จันทร์', 'อังคาร', 'พุธ', 'พฤหัสบดี', 'ศุกร์', 'เสาร์', 'อาทิตย์']
weekday_name = days[find_weekday - 1]

future_date.day , weekday_name
