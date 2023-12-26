# Reusable Python Functions

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Dependencies](#dependencies)
- [Author](#author)

## Description

A collection of reusable Python functions designed for formatting data from the platform or Microsoft Lists.

## Features

- `delete_top_rows`: Uses openpyxl to remove specified rows from the top of an Excel file based on a given condition.
- `save_csv_as_xlsx`: Saves a CSV file as an Excel file to display UTF-8 characters correctly on macOS.

## Installation

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/Karl-Horning/reusable_python_functions.git`
2. Navigate to the project directory: `cd reusable_python_functions`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

### `delete_top_rows`

```python
from reusablefunctions import delete_top_rows

# Example usage
delete_top_rows('example.xlsx')
```

### `save_csv_as_xlsx`

```python
from reusablefunctions import save_csv_as_xlsx

# Example usage
save_csv_as_xlsx('example.csv')
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure that the project still works.
4. Create a pull request with a clear description of your changes.

## License

This project is licensed under the [MIT License](./LICENSE).

## Dependencies

- [openpyxl](https://openpyxl.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)

## Author

Karl Horning: [GitHub](https://github.com/Karl-Horning/) | [LinkedIn](https://www.linkedin.com/in/karl-horning/) | [CodePen](https://codepen.io/karlhorning)