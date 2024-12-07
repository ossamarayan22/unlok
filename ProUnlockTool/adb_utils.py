import subprocess

def execute_adb_command(command):
    """
    تشغيل أمر ADB وتنفيذ النتيجة.
    :param command: قائمة تحتوي على الأمر وأي معاملات إضافية.
    :return: مخرجات الأمر كنص.
    """
    try:
        result = subprocess.run(
            ["adb"] + command, capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def get_connected_devices():
    """
    الحصول على قائمة بالأجهزة المتصلة عبر ADB.
    :return: قائمة بالأجهزة المتصلة.
    """
    output = execute_adb_command(["devices"])
    devices = []
    for line in output.splitlines()[1:]:  # تجاوز السطر الأول الذي يحتوي على العنوان
        if line.strip():
            device_info = line.split("\t")
            if len(device_info) == 2 and device_info[1] == "device":
                devices.append(device_info[0])
    return devices

def reboot_device(device_id):
    """
    إعادة تشغيل الجهاز باستخدام ADB.
    :param device_id: معرف الجهاز (serial number).
    :return: رسالة النجاح أو الخطأ.
    """
    return execute_adb_command(["-s", device_id, "reboot"])
