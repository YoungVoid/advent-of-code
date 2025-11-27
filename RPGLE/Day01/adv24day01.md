## adv24day01 (SQLRPGLE)

**Summary:**
- **Purpose:** Reads a small puzzle input file from the IFS, parses pairs of numbers on each line, and computes the sum of absolute differences between each pair (used as Part 1 answer for an Advent of Code Day 1 puzzle).
- **Main entry:** `ADV24DAY03` (declared with `Ctl-Opt Main(ADV24DAY03)` in the source).

**Files / Location:**
- Source: `adv24day01.sqlrpgle` (SQLRPGLE)
- Documentation: this file `adv24day01.md` in the same folder.

**Important constants and settings (in source):**
- `PUZZLE_INPUT_LINE_COUNT` = 6 — the code expects up to 6 lines of puzzle input.
- `PUZZLE_INPUT_FILE_PATH` = `/home/VOID/AdventOfCode/2024/Day1Test.txt` — path in the IFS where input is read from.

**Data structures:**
- `input_t` (qualified) — contains two packed(5) fields: `left_number` and `right_number`.
- `puzzleInput` — an array of `input_t` with dimension `PUZZLE_INPUT_LINE_COUNT`.

**High-level flow:**
- Program entry: `ADV24DAY03` (no parameters).
- It calls `getDataFromFile()` to read the entire input file contents into a large character buffer.
- The raw file data is passed to `FormatData()` which splits it into lines and maps each line into `left_number` and `right_number` fields.
- `GetAnswerPart1()` iterates the formatted data, sums the absolute differences between left and right values, and returns the total.
- The program sends the answer back via `snd-msg` (so it will appear in job log or caller messages depending on environment).

**Key procedures (what they do):**
- `ADV24DAY03` — top-level procedure that coordinates reading, formatting, computing the answer, and sending the message.

- `getDataFromFile(filePath)` — uses external C runtime procedures (`open`, `read`, `close`) declared via `dcl-pr` to open the IFS path, read up to a fixed buffer (`Data char(13000)`), and return the raw data as a character string.
  - Uses constants: `O_RDONLY`, `O_TEXTDATA`, `O_CCSID`, `S_IRGRP`, and `sysCCSID`.
  - If open fails (file descriptor < 0) it currently returns blanks and does not raise an explicit error.

- `FormatData(rawData)` — splits `rawData` by a configured `endOfLine` byte (`dcl-c endOfLine x'25'`) and for each split line extracts two single-character substrings:
  - `formattedData(i).left_number = %int(%trim(%subst(line:1:1)));`
  - `formattedData(i).right_number = %int(%trim(%subst(line:5:1)));`
  - Returns an array of `input_t` sized by `PUZZLE_INPUT_LINE_COUNT`.

- `GetAnswerPart1(puzzleInput)` — loops each `line` in the passed array and does:
  - `totalDistance += %abs(line.left_number - line.right_number);`
  - Sends diagnostic messages for each line and the running total using `snd-msg`.
  - Returns `totalDistance` (integer).

**Notes / Observations (things to confirm or improve):**
- The `endOfLine` constant is `x'25'` (hex 25) — make sure input file indeed uses that byte as a separator. Typical newline is `x'0A'` (LF) or `x'0D'` (CR) or `x'0D0A'` for CRLF. If the file actually uses standard newlines, change `endOfLine` accordingly.
- `FormatData` uses `%subst(line:1:1)` and `%subst(line:5:1)` — these extract single characters at positions 1 and 5. If the input numbers can be multiple digits or are in different columns, adjust these offsets and lengths.
- `PUZZLE_INPUT_LINE_COUNT` is fixed at 6. If input length varies, consider resizing dynamically or detecting the number of lines after splitting and only processing those.
- Error handling in `getDataFromFile` is minimal — open/read errors are not surfaced clearly. Consider returning an error code or raising message to caller.

**Compile / Run (IBM i guidance)**
- Ensure the input file exists in the IFS at the path set by `PUZZLE_INPUT_FILE_PATH`.
- To compile SQLRPGLE on IBM i you can use a compile command such as (replace `<LIB>` and source file parameters appropriately):

```powershell
CRTSQLRPGI OBJ(<LIB>/ADV24DAY01) SRCFILE(<LIB>/QRPGLESRC) COMMIT(*NONE)
```

- After compiling, call the program (replace `<LIB>` with your library):

```powershell
CALL PGM(<LIB>/ADV24DAY01)
```

- Note: the source sets `Ctl-Opt Main(ADV24DAY03)` so the entrypoint inside the module is `ADV24DAY03`. You may choose to name the program object differently; the example `CRTSQLRPGI` above uses `ADV24DAY01` as an object name — ensure you use the names consistent with your build process.

**Example input format (inferred from code):**
- The code expects each 'line' to contain at least 5 bytes; it reads a single character at position 1 and a single character at position 5 and converts them to integers. Example raw line (positions shown):

  1 _ _ _ 2

This would be parsed as left=1 and right=2. If your actual input is `"12 34"` or `"1,2"` you must adapt `FormatData` accordingly.

**Recommended improvements (next steps):**
- Replace `endOfLine x'25'` with a newline constant (LF) or detect line breaks automatically.
- Update `FormatData` to parse numbers with `%scan` or field delimiters so multi-digit numbers are supported.
- Add robust error handling and propagate file-read errors to the caller.
- Make `PUZZLE_INPUT_LINE_COUNT` dynamic or compute number of lines found after splitting.

**Key excerpts (quick reference):**
```rpgle
Ctl-Opt Main(ADV24DAY03);

dcl-c PUZZLE_INPUT_LINE_COUNT 6;
dcl-c PUZZLE_INPUT_FILE_PATH '/home/VOID/AdventOfCode/2024/Day1Test.txt';

// Top-level
Dcl-Proc ADV24DAY03;
  puzzleInput = FormatData(getDataFromFile(PUZZLE_INPUT_FILE_PATH));
  answer = GetAnswerPart1(puzzleInput);
  snd-msg *INFO %char(answer) %target(*CALLER);
  return;
End-Proc;
```

If you'd like, I can:
- update `FormatData` to use a standard newline separator and support multi-digit numbers,
- add better error reporting for `getDataFromFile`, or
- create a `README.md` that includes actual compile commands specific to your target library.

---
Generated from `adv24day01.sqlrpgle` — review the "Notes" section above and tell me which improvements you'd like me to implement next.
