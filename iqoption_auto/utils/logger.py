import logging

logger = logging.getLogger("iqoption_auto")
logger.setLevel(logging.DEBUG)

# إعداد التنسيق العام للرسائل
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")

# إخراج إلى الشاشة
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
