# Snake Case Guidelines

This project follows the **snake_case** naming convention. Below are the guidelines for using snake_case consistently throughout the project:

## What is Snake Case?

Snake case is a naming convention where words are written in lowercase and separated by underscores (`_`). For example:
- `example_variable`
- `process_data`
- `get_user_info`

## Guidelines

1. **Variables**: Use snake_case for all variable names.
   ```python
   user_name = "John Doe"
   max_value = 100
   ```

2. **Functions**: Use snake_case for function names.
   ```python
   def calculate_total_price():
       pass
   ```

3. **File Names**: Use snake_case for all file names.
   - Example: `hatchet_worker.py`

4. **Modules and Packages**: Use snake_case for module and package names.
   - Example: `src/app/services/`

5. **Constants**: Use uppercase with underscores for constants.
   ```python
   MAX_RETRIES = 5
   API_ENDPOINT = "https://api.example.com"
   ```

6. **Database Fields**: Use snake_case for database field names.
   - Example: `user_id`, `created_at`

7. **Tests**: Use snake_case for test function names.
   ```python
   def test_user_creation():
       pass
   ```

## Why Use Snake Case?

- **Readability**: Snake case improves readability, especially for longer names.
- **Consistency**: It ensures uniformity across the codebase.
- **Pythonic**: Snake case is the recommended convention in Python's PEP 8 style guide.

## Examples

### Good
```python
def get_user_data():
    user_name = "Alice"
    return user_name
```

### Bad
```python
def GetUserData():
    UserName = "Alice"
    return UserName
```

By adhering to these guidelines, we ensure a clean, consistent, and maintainable codebase.