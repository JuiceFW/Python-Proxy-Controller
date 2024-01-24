# Proxy-Controller

## Overview

Proxy-Controller is a Python script designed to filter and use only proxies that have not been used for a long time. This script helps you maintain a pool of fresh and reliable proxies for your applications, ensuring optimal performance and reliability.

## Features

- **Proxy Filtering:** Utilizes a filtering mechanism to identify and use only proxies that have not been used for a specified duration.
- **Easy Integration:** Designed for easy integration into your Python projects or applications.
- **Customization:** Offers configuration options to adjust filtering criteria and testing parameters based on your specific requirements.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JuiceFW/Python-Proxy-Controller.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Python-Proxy-Controller
   ```

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. The script will show you an example of its work.

## Abilities

You can use `ProxyLimiter` as you want to use it:

- `get_proxy`: Get a proxy checking with timeout value.
- `append_proxy`: Appends a proxy to a proxy list
- `remove proxy`: Removes a proxy from a proxy list
- `add_used_proxy`: Let script know that proxy was used by the main system

### Details of methods
- `no_limits: bool = False`: Changes between: returning a random proxy from a list or looking for a proxy with the best timeout.
- `any_if_timeout: bool = False`: Changes between: returning a random proxy if all the proxies have a bad timeout or returning None
- `proxy: str`: A proxy to append/remove/insert

## Configuration

Adjust the settings in class initialization to customize the behavior of the Proxy-Controller script:

- `proxies`: A list of all proxies you have.
- `timeout`: Timeout (in seconds) for testing the viability of each proxy

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated.

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to contributors and libraries that have been instrumental in the development of Proxy-Controller.

Happy proxy filtering!