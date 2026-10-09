# Math for CS

A curated, student-friendly guide to the **math foundations of computer science**.

Most CS students meet the same topics over and over — discrete math, linear algebra,
probability, and so on — but rarely see _why_ they matter or how they connect. This
repository collects the most common math-related CS topics in one place, with clear
explanations, the key formulas you actually need, and concrete links to where each
topic shows up in real computer science.

> **Goal:** give students a single, well-organized reference they can browse quickly
> before an exam, a course, or an interview.

## Why math matters for CS

Computer science is applied mathematics. A few examples:

| Topic                    | Where it shows up                                              |
| ------------------------ | -------------------------------------------------------------- |
| Discrete math            | Algorithms, data structures, program correctness               |
| Linear algebra           | Machine learning, graphics, computer vision, quantum computing |
| Probability & statistics | ML, randomized algorithms, networking, security                |
| Calculus                 | Optimization, ML training, signal processing, simulation       |
| Logic                    | Compilers, type systems, verification, databases               |
| Number theory            | Cryptography, hashing, error-correcting codes                  |
| Graph theory             | Networks, routing, social networks, compilers                  |
| Set theory               | Databases, type systems, query languages                       |
| Combinatorics            | Complexity analysis, algorithm design, scheduling              |

You don't need all of this at once. Start with **discrete math**, then add the topics
that match your interests.

## Topic index

| #   | Topic                                                           | Typical course year | Core CS applications                     |
| --- | --------------------------------------------------------------- | ------------------- | ---------------------------------------- |
| 01  | [Discrete Mathematics](topics/01-discrete-math.md)              | 1–2                 | Algorithms, proofs, recurrence relations |
| 02  | [Linear Algebra](topics/02-linear-algebra.md)                   | 2–3                 | ML, graphics, computer vision            |
| 03  | [Probability & Statistics](topics/03-probability-statistics.md) | 2–3                 | ML, randomized algorithms, networking    |
| 04  | [Calculus](topics/04-calculus.md)                               | 1–2                 | Optimization, ML, signal processing      |
| 05  | [Mathematical Logic](topics/05-logic.md)                        | 2–3                 | Compilers, type systems, verification    |
| 06  | [Number Theory](topics/06-number-theory.md)                     | 3–4                 | Cryptography, hashing, coding theory     |
| 07  | [Graph Theory](topics/07-graph-theory.md)                       | 2–3                 | Networks, routing, compilers             |
| 08  | [Set Theory](topics/08-set-theory.md)                           | 1–2                 | Databases, type systems                  |
| 09  | [Combinatorics](topics/09-combinatorics.md)                     | 2–3                 | Complexity, algorithm design             |

## How to use this repo

- **Browsing?** Open any file in [`topics/`](topics/). Each is self-contained.
- **Studying for an exam?** Read the _Core concepts_ and _Key formulas_ sections first.
- **Looking for motivation?** Read the _Why it matters for CS_ section at the top of each file.
- **Learning path below** — follow it if you want a recommended order.

Each topic file follows the same structure:

1. **Overview** — what the topic is, in plain language.
2. **Why it matters for CS** — concrete applications.
3. **Core concepts** — the ideas you must know.
4. **Key formulas & notation** — the reference sheet.
5. **CS applications** — worked connections to real systems.
6. **Resources** — books, courses, and links to go deeper.

## Recommended learning path

```
Beginner            Intermediate             Advanced / Specialized
────────            ────────────             ────────────────────────
01 Discrete Math ─► 05 Logic ────────────►   06 Number Theory (crypto)
08 Set Theory    ─► 07 Graph Theory ─────►   03 Probability & Stats (ML)
09 Combinatorics ─► 02 Linear Algebra ───►   04 Calculus (optimization)
```

Start with **01 Discrete Math** — it underpins almost everything else. Then branch
based on your track:

- **Systems / theory track:** Discrete Math → Logic → Graph Theory → Number Theory
- **AI / ML track:** Linear Algebra → Calculus → Probability & Statistics
- **Generalist track:** Discrete Math → Set Theory → Combinatorics → Graph Theory

## Contributing

Corrections, better explanations, and new resources are welcome.
See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) — use it, fork it, teach with it.
