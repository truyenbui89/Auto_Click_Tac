Dưới đây là file `README.md` chi tiết hướng dẫn cách sử dụng script:

```markdown
# Auto Search and Click Script

This script automates the process of searching for keywords on Google, clicking on specific domains, and interacting with the target website. It supports multiple proxies for IP rotation and allows multiple keyword-domain pairs.

## Features

- Search for keywords on Google and click on a specified domain.
- Scroll and click a random link on the target website.
- Rotate IP addresses using multiple proxies.
- Supports multiple keyword-domain pairs.

## Requirements

- Python 3.6+
- `selenium`
- `selenium-wire`
- `webdriver-manager`
- `requests`

## Installation

1. Clone this repository or download the script files.
2. Install the required Python packages:

    ```bash
    pip install selenium selenium-wire webdriver-manager requests
    ```

## Configuration

Update the proxy information in the script:

```python
proxies = [
    {
        "proxy": "svhn12.proxyno1.com:55653",
        "username": "truyen",
        "password": "truyen",
        "api": "https://app.proxyno1.com/api/change-key-ip/RW8Djr9cDwK981mNz3bEVf1721271399"
    },
    # Add more proxies as needed
]
```

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. Enter the number of keyword-domain pairs:

    ```plaintext
    Nhập số lượng từ khóa và domain: 2
    ```

3. For each keyword-domain pair, enter the keyword and the corresponding domain:

    ```plaintext
    Nhập từ khóa tìm kiếm: example keyword 1
    Nhập domain cần tìm kiếm (bao gồm https:// hoặc http://): https://example1.com
    Nhập từ khóa tìm kiếm: example keyword 2
    Nhập domain cần tìm kiếm (bao gồm https:// hoặc http://): https://example2.com
    ```

4. Enter the number of clicks to perform:

    ```plaintext
    Nhập số lượt click: 10
    ```

The script will then perform the following actions:
- Search for the keywords on Google.
- Click on the link containing the specified domain.
- Scroll and interact with the target website.
- Change the IP address using the provided proxies.
- Repeat the process for the specified number of clicks.

## Troubleshooting

If you encounter issues with the script, ensure that:
- You have the correct version of Python installed.
- All required packages are installed.
- Proxy settings are correctly configured.

## Example Output

```plaintext
Nhập số lượng từ khóa và domain: 2
Nhập từ khóa tìm kiếm: example keyword 1
Nhập domain cần tìm kiếm (bao gồm https:// hoặc http://): https://example1.com
Nhập từ khóa tìm kiếm: example keyword 2
Nhập domain cần tìm kiếm (bao gồm https:// hoặc http://): https://example2.com
Nhập số lượt click: 10
IP đã được thay đổi thành công.
IP mới: 192.168.1.1
Click 1/10: Đã nhấp vào https://example1.com
IP đã được thay đổi thành công.
IP mới: 192.168.1.2
Click 2/10: Đã nhấp vào https://example2.com
...
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Selenium](https://www.selenium.dev/)
- [Selenium Wire](https://github.com/wkeeling/selenium-wire)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

```

### Save the content above into a file named `README.md`.

### Run the script
```bash
python main.py
```

Follow the prompts to input keywords, domains, and the number of clicks.

This should provide clear guidance on how to set up, configure, and run the script effectively. If there are additional details or customization needed, they can be added to the `README.md` as required.
