from plyer import notification

notification.notify(
    title='Yoga Zamanı!',
    message='Nefes pratiği yapmayı unutma 🧘‍♀️',
    app_name='Yoga Hatırlatıcı',
    timeout=10  # saniye cinsinden
)
import time
from plyer import notification

while True:
    notification.notify(
        title='Hadi kalk!',
        message='Omuzlarını çevir, boynunu ger, derin nefes al 😌',
        app_name='Hareket Vakti',
        timeout=10
    )
    time.sleep(3600)  # 1 saat bekle

