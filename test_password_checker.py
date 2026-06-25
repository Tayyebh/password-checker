def validate_password(password):
    """Validates a password and returns (is_valid, message)"""
    if len(password) < 8:
        return False, "Password is too short (minimum 8 characters)"
    elif len(password) > 20:
        return False, "Password is too long (maximum 20 characters)"
    elif not any(c.isupper() for c in password):
        return False, "Password must include at least one uppercase letter (A-Z)"
    elif not any(not c.isalnum() for c in password):
        return False, "Password must include at least one special character"
    else:
        return True, "Password is valid!"


class TestPasswordChecker:
    """Test suite for password validator"""

    def test_valid_password(self):
        """Test that valid passwords are accepted"""
        is_valid, message = validate_password("SecurePass@123")
        assert is_valid is True
        assert "valid" in message.lower()

    def test_too_short(self):
        """Test that passwords under 8 chars are rejected"""
        is_valid, message = validate_password("Short1!")
        assert is_valid is False
        assert "too short" in message.lower()

    def test_too_long(self):
        """Test that passwords over 20 chars are rejected"""
        is_valid, message = validate_password("ThisPasswordIsMuchTooLongWithSpecial!123")
        assert is_valid is False
        assert "too long" in message.lower()

    def test_no_uppercase(self):
        """Test that passwords without uppercase are rejected"""
        is_valid, message = validate_password("nouppercase!123")
        assert is_valid is False
        assert "uppercase" in message.lower()

    def test_no_special_character(self):
        """Test that passwords without special characters are rejected"""
        is_valid, message = validate_password("NoSpecialChar123")
        assert is_valid is False
        assert "special" in message.lower()


if __name__ == "__main__":
    print("Running Password Checker Tests...\n")
    test = TestPasswordChecker()
    
    tests = [
        ("test_valid_password", test.test_valid_password),
        ("test_too_short", test.test_too_short),
        ("test_too_long", test.test_too_long),
        ("test_no_uppercase", test.test_no_uppercase),
        ("test_no_special_character", test.test_no_special_character),
    ]
    
    passed = 0
    for test_name, test_func in tests:
        try:
            test_func()
            print(f"✅ {test_name}")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name}: {e}")
    
    print(f"\n{passed}/{len(tests)} tests passed")
