<p align="center" style="font-weight: bold !important;">
    <span>بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ</span>
</p>

All praise belongs to Allāh, Lord of all the worlds. May peace and blessings be
upon our Prophet Muḥammad, upon his family, his companions and all those who
follow his guidance until the Day of Judgment.

# Introduction

TODO

# Plan

To convert current macros in `pp.old` to GPP format.

# Dependencies

1. [GPP](https://github.com/logological/gpp)
2. Python 3.x (Not necessary if not expecting to use #exec)

# Honorifics

Honorific macros (should) include the following:

1. (سبحانه وتعالىٰ)
2. (صلى الله عليه وسلم)
3. (رضي الله عنه)
4. (رضي الله عنهما)
5. (رضي الله عنهم)
6. (رضي الله عنها)
7. (رضي الله عنهن)


Their Latin equivalents should be flexible;
they should be definable in different transliterations.

TODO

# Conditional Macros

TODO

# Programming

TODO

# Notes

- `#define p(x) (May Allāh be pleased with x)`

    This doesn't work as it also affects page markers (e.g. p. 45).

# License

The GPP manual in the `reference` folder is from the GPP project.
It has been put there purely for convenience.
