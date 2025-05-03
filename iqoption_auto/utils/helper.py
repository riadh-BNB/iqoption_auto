import time
from datetime import datetime

def timestamp_now() -> int:
    """إرجاع الطابع الزمني الحالي بالثواني."""
    return int(time.time())

def format_datetime(timestamp: int) -> str:
    """تحويل طابع زمني إلى تنسيق تاريخ مقروء."""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def validate_amount(amount: float) -> float:
    """تحديد عدد الأرقام العشرية المقبولة للمبلغ."""
    return round(amount, 2)

def parse_duration(expiration: int) -> int:
    """تحويل مدة الصفقة إلى طابع زمني مستقبلي."""
    return timestamp_now() + expiration * 60
