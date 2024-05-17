from PyQt5.QtCore import QPropertyAnimation, QRect, QTimer


def button_animation(btn, win, f):
    animation_press = QPropertyAnimation(btn, b"geometry", win)
    animation_press.setDuration(40)
    start_rect = btn.geometry()
    end_rect = QRect(start_rect.x() + 4, start_rect.y() + 4, start_rect.width(), start_rect.height())
    animation_press.setStartValue(start_rect)
    animation_press.setEndValue(end_rect)
    animation_release = QPropertyAnimation(btn, b"geometry", win)
    animation_release.setDuration(40)
    animation_release.setStartValue(end_rect)
    animation_release.setEndValue(start_rect)
    animation_press.finished.connect(animation_release.start)
    animation_press.start()
    QTimer.singleShot(100, f)