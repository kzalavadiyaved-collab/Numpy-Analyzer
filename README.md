## Project NumPy Analyzer

**NumPy Analyzer**

## Objective

Develop a NumPy Analyzer that integrates NumPy functionalities and Object-Oriented Programming (OOP) principles. The toolkit allows users to perform common data operations, statistical analyses, and mathematical computations on datasets using NumPy arrays.

## Features & Requirements

### Class and Object Structure
- Create a class `DataAnalytics` with methods to encapsulate all functionalities.

### Array Management
- **Creation, Indexing, and Slicing:** Allow users to create 1D, 2D, or 3D arrays and access specific elements, rows, columns, or slices of the array.
- **Combining and Splitting:** Provide functionality to concatenate multiple arrays or split an array into smaller arrays.

### Mathematical Operations
- Perform element-wise addition, subtraction, multiplication, and division on arrays.
- Calculate the dot product and matrix multiplication for 2D arrays.

### Search, Sort, and Filter
- Enable searching for specific values in an array.
- Sort arrays in ascending or descending order.
- Filter arrays based on user-defined conditions.

### Aggregating Functions
- Compute the sum, mean, median, standard deviation, and variance of the array elements.

### Statistical Functions
- Provide methods to calculate statistical properties like:
  - Minimum and maximum values.
  - Percentiles.
  - Correlation coefficients between arrays.

### Object-Oriented Programming (OOP)
- Use constructors for initializing arrays.
- Include encapsulation and define private methods for internal computations.
- Implement class-level methods (`@classmethod`) and static methods (`@staticmethod`) for additional utility.

### User Interface (UI)
- Create a menu-driven interface to let users choose from different options.
- Allow users to exit the program from the main menu.

## Getting Started

### Prerequisites
- Python 3.x
- NumPy (`pip install numpy`)

### Installation
```bash
git clone <repository-url>
cd numpy-analyzer
pip install -r requirements.txt
```
## video demo

[![Play Video](https://img.shields.io/badge/▶%20Play-Video-success?style=for-the-badge)](https://drive.google.com/file/d/1R8KoOQaT0SF0d1cjyGDrNKUo56d0MAgK/view?usp=sharing)
### Usage
```bash
python main.py
```

Follow the on-screen menu to select array creation, operations, search/sort/filter, aggregation, or statistical analysis options.

## Project Structure
```
numpy-analyzer/
├── main.py            # Entry point with menu-driven UI
├── data_analytics.py  # DataAnalytics class implementation
├── requirements.txt
└── README.md
```

## Class Overview: `DataAnalytics`

| Category | Methods |
|---|---|
| Array Management | `create_array()`, `index_array()`, `slice_array()`, `concatenate_arrays()`, `split_array()` |
| Mathematical Operations | `add()`, `subtract()`, `multiply()`, `divide()`, `dot_product()`, `matrix_multiply()` |
| Search / Sort / Filter | `search_value()`, `sort_array()`, `filter_array()` |
| Aggregating Functions | `sum()`, `mean()`, `median()`, `std_dev()`, `variance()` |
| Statistical Functions | `min_max()`, `percentile()`, `correlation()` |

## License

This project is open source and available under the MIT License.
