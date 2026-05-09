#### Step 1 - Identify Valid and Invalid Equivalence Classes


The relevant validation rules for a QuizRequest are:

    Topic length: The topic string must be between 3 and 100 characters (inclusive).
    Requested question count: Must be an integer between 1 and 10 (inclusive).
    Difficulty hint: Must be one of the accepted values: easy, medium, or hard. Any other value (including blank/null) is invalid.


For each of the three input parameters of `QuizRequest` (`topic`, `count`, `difficulty`),
identify all **valid** and **invalid equivalence classes**.

##### Parameter: `topic`

| Parameter | Class ID | Class Type | Partition Description | Representative Test Value |
|-----------|----------|------------|-----------------------|---------------------------|
| `topic`   | EC-T-1   | Valid      | String length between 3 and 100 characters (inclusive) | `"Java"` |
| `topic`   | EC-T-2   | Invalid    | String length less than 3 characters | `"Go"` |
| `topic`   | EC-T-3   | Invalid    | String length greater than 100 characters | `"A"` repeated 101 times |
| `topic`   | EC-T-4   | Invalid    | Empty string | `""` |
| `topic`   | EC-T-5   | Invalid    | Null / missing value | `null` |

##### Parameter: `count`

| Parameter | Class ID | Class Type | Partition Description | Representative Test Value |
|-----------|----------|------------|-----------------------|---------------------------|
| `count`   | EC-C-1   | Valid      | Integer between 1 and 10 (inclusive) | `5` |
| `count`   | EC-C-2   | Invalid    | Integer less than 1 (zero or negative) | `0` |
| `count`   | EC-C-3   | Invalid    | Integer greater than 10 | `11` |
| `count`   | EC-C-4   | Invalid    | Wrong type (non-integer, e.g. string or decimal) | `"abc"` |
| `count`   | EC-C-5   | Invalid    | Null / missing value | `null` |

##### Parameter: `difficulty`

| Parameter   | Class ID | Class Type | Partition Description | Representative Test Value |
|-------------|----------|------------|-----------------------|---------------------------|
| `difficulty`| EC-D-1   | Valid      | Accepted value `"easy"` | `"easy"` |
| `difficulty`| EC-D-2   | Valid      | Accepted value `"medium"` | `"medium"` |
| `difficulty`| EC-D-3   | Valid      | Accepted value `"hard"` | `"hard"` |
| `difficulty`| EC-D-4   | Invalid    | Any other non-empty string (incl. wrong case, typos) | `"Easy"` |
| `difficulty`| EC-D-5   | Invalid    | Empty string | `""` |
| `difficulty`| EC-D-6   | Invalid    | Null / missing value | `null` |

#### Step 2 - Justify Each Class

##### Parameter: `topic`

**EC-T-1: `"Java"`**
1. 4 characters, mid-range in [3,100], so it stands for any valid length without sitting on a boundary.
2. Contains both boundaries. Lower: **3** (`"abc"`), upper: **100** (`"A"` x 100); just outside: **2** (`"ab"`) and **101** (`"A"` x 101).

**EC-T-2: `"Go"`**
1. Length 2 violates the minimum of 3, representing all strings too short to pass.
2. Boundary-touching. Upper end of class: length **2**; just outside (back into valid): length **3**.

**EC-T-3: `"A"` x 101**
1. Length 101 exceeds the maximum of 100, representing all over-long strings.
2. Boundary-touching. Lower end of class: length **101**; just outside (back into valid): length **100**.

**EC-T-4: `""`**
1. Empty string is a separate edge case typically caught by a distinct blank-check rule.
2. Degenerate boundary at length **0**; no further bounds.

**EC-T-5: `null`**
1. Missing value, semantically different from empty string and explicitly invalid per spec.
2. No numeric boundary, type-level class.

##### Parameter: `count`

**EC-C-1: `5`**
1. Mid-range in [1,10], so it stands for any valid integer without sitting on a boundary.
2. Contains both boundaries. Lower: **1**, upper: **10**; just outside: **0** and **11**.

**EC-C-2: `0`**
1. Below the lower bound, representing all values <= 0.
2. Boundary-touching. Upper end of class: **0**; just outside (back into valid): **1**.

**EC-C-3: `11`**
1. Above the upper bound, representing all values > 10.
2. Boundary-touching. Lower end of class: **11**; just outside (back into valid): **10**.

**EC-C-4: `"abc"`**
1. Wrong type, violating the integer requirement, a distinct error category from range violations.
2. No numeric boundary, type-level class.

**EC-C-5: `null`**
1. Missing value, rejected independently of type or range.
2. No numeric boundary, type-level class.

##### Parameter: `difficulty`

**EC-D-1: `"easy"`**
1. Explicitly accepted enum value and the only member of its class.
2. No boundary analysis applicable, discrete enum point.

**EC-D-2: `"medium"`**
1. Explicitly accepted enum value, sole member of its class.
2. No boundary, discrete enum point.

**EC-D-3: `"hard"`**
1. Explicitly accepted enum value, sole member of its class.
2. No boundary, discrete enum point.

**EC-D-4: `"Easy"`**
1. Wrong casing represents all non-accepted strings (typos, case mismatches), since the spec rejects anything outside the enum.
2. No boundary, set has no ordering.

**EC-D-5: `""`**
1. Empty string is listed as explicitly invalid by the spec.
2. Degenerate boundary at length **0**.

**EC-D-6: `null`**
1. Missing value is listed as explicitly invalid by the spec.
2. No boundary, type-level class.
