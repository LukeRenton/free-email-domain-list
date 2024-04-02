# List of free email domains
This repo is a python package that provides a comprehensive list of free email domains from around the world. This package is designed to simplify the process of checking if an email address belongs to a free email provider.

## Installation

You can install free-email-domains via pip:

```bash
pip install free-email-domains
```

## Usage

After installing the package, you can use it in your Python projects as follows:

```python
>>> from free_email_domains import whitelist
>>> 'gmail.com' in whitelist
True
```

## Example

```python
from free_email_domains import whitelist as free_domains

# Check if an email domain is free
email = "example@sample.com"
if email.split('@')[1] in free_domains:
    print("This is a free email domain.")
else:
    print("This is not a free email domain.")
```

## Contributing

Contributions are welcome! If you want to add or update any free email domains, feel free to submit a pull request.

## License

This package is licensed under the MIT License. See the [LICENSE](https://github.com/LukeRenton/free-email-domain-list/blob/master/LICENSE) file for details.

## Acknowledgements

This package utilizes data from [HubSpot](https://knowledge.hubspot.com/forms/what-domains-are-blocked-when-using-the-forms-email-domains-to-block-feature), which contains a compiled free email domain list.

## Issues

If you encounter any issues or have suggestions for improvement, please report them on the [GitHub issue tracker](https://github.com/LukeRenton/free-email-domain-list/issues).
