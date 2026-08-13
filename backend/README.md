# Backend Testing

Run the calculator unit tests from this directory with:

```bash
python -m unittest test_calculator.py -v
```

## Test Cases

| Test | Expected result |
|---|---|
| `10 + 5` | `15` |
| `10 - 5` | `5` |
| `10 × 5` | `50` |
| `10 ÷ 5` | `2` |
| `7 ÷ 2` | `3.5` |
| `10 ÷ 0` | Raises `ZeroDivisionError` |
| Unsupported operation | Raises `ValueError` |
