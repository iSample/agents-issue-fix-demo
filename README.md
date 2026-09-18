# Agents Issue Fix Demo

Small public repository used to demonstrate a bounded `GitHub Issue -> fix -> Pull Request` workflow.

## Run

```bash
python3 -m unittest discover -s tests -v
```

## Intentional issue

`format_greeting` leaves two spaces before the name. The initial Issue describes the expected one-space greeting and has a failing regression test.
