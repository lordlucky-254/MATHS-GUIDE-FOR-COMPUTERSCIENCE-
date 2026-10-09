# Contributing

Thanks for helping make this a better resource for CS students. All kinds of
contributions are welcome: fixing a typo, clarifying an explanation, adding a
worked example, or suggesting a resource.

## Ways to contribute

- **Fix an error** — a wrong formula, broken link, or confusing sentence.
- **Improve clarity** — rewrite a paragraph so it's easier to follow.
- **Add examples** — concrete examples make abstract math click.
- **Add resources** — good textbooks, lectures, or interactive sites.
- **Add a topic** — a math area commonly used in CS that's missing here.

## Guidelines

1. **Keep it student-friendly.** Write for someone seeing the topic for the first
   time. Prefer plain language over jargon, and define terms when you introduce them.
2. **Show why it matters.** Every concept should connect to a real CS application.
3. **Be concise.** This is a reference, not a textbook. Favor short, scannable
   sections over long prose.
4. **Follow the existing structure.** Each topic file uses the same sections:
   *Overview*, *Why it matters for CS*, *Core concepts*, *Key formulas & notation*,
   *CS applications*, *Resources*.
5. **Use Markdown correctly.** Fenced code blocks for formulas or pseudocode, tables
   for reference material, and relative links between files.
6. **Keep formulas readable.** Use inline code (`` `O(n log n)` ``) or fenced
   blocks. Avoid LaTeX in raw form unless the file already uses it consistently.

## Adding a new topic

1. Pick a number that fits the existing ordering (e.g. `10-...`).
2. Create `topics/NN-topic-name.md` using the standard section structure.
3. Add a row to the topic index in `README.md`.
4. If it fits a learning path, mention it in the *Recommended learning path* section.

## Style notes

- Headings: `#` for the title, `##` for major sections, `###` for subsections.
- Keep lines reasonably short where practical; one sentence per line is fine.
- Prefer American English spelling for consistency.

## Submitting changes

1. Fork the repository (or create a branch if you have write access).
2. Make your changes in a focused commit with a clear message, e.g.
   `docs: clarify Big-O definition in discrete math`.
3. Open a pull request describing what you changed and why.

## Code of conduct

Be kind and constructive. This is a learning resource; assume good faith and help
others understand.
