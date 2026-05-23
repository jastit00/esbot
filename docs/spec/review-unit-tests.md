# Review: Unit Testing of Models (8.1)

## Approach

To analyze the current test implementations the `models.py` file, the `test-design.md` file and the test files in the `tests/` directory were reviewed. Valid and invalid attribute combinations, boundary values and edge cases were collected.

For each model the following questions were asked:
- Are all valid attribute combinations covered?
- Are boundary values tested?
- Are invalid inputs / edge cases tested?

## Analysis

### 1. Session Model

**Are all valid attribute combinations covered?**
- No, the following are missing:
    - setting `id` to a valid value (manualy)
    - setting `session_token` to a valid value

**Are boundary values tested?**
- No, the following boundary values are not tested:
    - `id` max / min length including value 0
    - `session_token` max / min length

**Are invalid inputs / edge cases tested?**
- No, the following invalid inputs / edge cases are not tested:
    - `id` negative values
    - `session_token` null or duplicate (not unique) values
    - `created_at` empty string or future values


### 2. Message Model

**Are all valid attribute combinations covered?**
- No, the following are missing:
    - setting `id` to a valid value (manualy)

**Are boundary values tested?**
- No, the following boundary values are not tested:
    - `id` max / min length including value 0
    - `content` max / min length
    - `session_id` max / min length (including value 0)

**Are invalid inputs / edge cases tested?**
- No, the following invalid inputs / edge cases are not tested:
    - `id` negative values
    - `content` empty string
    - `created_at` empty string or future values
    - `session_id` negative values
    - `session_id` unvalid foreign key


### 3. QuizItem Model

**Are all valid attribute combinations covered?**
- No, the following are missing:
    - setting `id` to a valid value (manualy)
    - setting `quiz_request_id` to a valid value

**Are boundary values tested?**
- No, the following boundary values are not tested:
    - `id` max / min length including value 0
    - `text` max / min length
    - `session_id` max / min length (including value 0)
    - `quiz_request_id` max / min length (including value 0)

**Are invalid inputs / edge cases tested?**
- No, the following invalid inputs / edge cases are not tested:
    - `id` negative values
    - `text` empty string
    - `created_at` empty string or future values
    - `session_id` negative values
    - `session_id` unvalid foreign key
    - `quiz_request_id` unvalid foreign key


### 4. SubmittedAnswer Model

**Are all valid attribute combinations covered?**
- No, the following are missing:
    - setting `id` to a valid value (manualy)

**Are boundary values tested?**
- No, the following boundary values are not tested:
    - `id` max / min length including value 0
    - `text` max / min length
    - `session_id` max / min length (including value 0)
    - `quiz_item_id` max / min length (including value 0)

**Are invalid inputs / edge cases tested?**
- No, the following invalid inputs / edge cases are not tested:
    - `id` negative values
    - `text` empty string
    - `created_at` empty string or future values
    - `session_id` negative values
    - `session_id` unvalid foreign key
    - `quiz_item_id` unvalid foreign key


---

*Tool Used:* Windsurf Tab Completion

*Purpose:* Supporting aid for structuring the review document, taking into account all attribute constraints and writing good English
