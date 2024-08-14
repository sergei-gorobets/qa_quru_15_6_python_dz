from datetime import time


def test_dark_theme_by_time():
    current_time = time(hour=5)

    if current_time.hour in range(6, 22):
        is_dark_theme = False
    else:
        is_dark_theme = True
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    current_time = time(hour=5)
    dark_theme_enabled_by_user = True
    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else:
        is_dark_theme = not (6 <= current_time.hour < 22)
    assert is_dark_theme is True


def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    suitable_user = next(user for user in users if user["name"] == "Olga")
    assert suitable_user == {"name": "Olga", "age": 45}

    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def print_readable_name_and_args(func_name, *args):
    readable_name = func_name.replace('_', ' ').title()
    args_str = ", ".join(map(str, args))
    print(f"{readable_name} [{args_str}]")


def print_readable_function_name(func_name, **kwargs):
    readable_name = func_name.replace('_', ' ').title()
    args_str = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
    print(f"{readable_name} [{args_str}]")
    return f"{readable_name} [{args_str}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    result = print_readable_function_name(open_browser.__name__, browser_name=browser_name)
    actual_result = "Open Browser [browser_name=Chrome]"
    assert result == actual_result, f"expected {actual_result}, but got {result}"


def go_to_companyname_homepage(page_url):
    result = print_readable_function_name(go_to_companyname_homepage.__name__, page_url=page_url)
    actual_result = "Go To Companyname Homepage [page_url=https://companyname.com]"
    assert result == actual_result, f"expected {actual_result}, but got {result}"


def find_registration_button_on_login_page(page_url, button_text):
    result = print_readable_function_name(find_registration_button_on_login_page.__name__, page_url=page_url, button_text=button_text)
    actual_result = "Find Registration Button On Login Page [page_url=https://companyname.com/login, " \
                    "button_text=Register]"
    assert result == actual_result, f"expected {actual_result}, but got {result}"
