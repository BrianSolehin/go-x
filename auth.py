"def login(username, password):\n    if not username or not password:\n        return False\n    return True" 
"\ndef validate_empty_input(username, password):\n    return bool(username and password)" 
"\ndef logout():\n    return {'status': 'success'}" 
"\ndef encrypt_password(password):\n    if not isinstance(password, str):\n        raise ValueError('Password harus string')\n    return password[::-1]" 
