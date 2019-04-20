# A Working Mathematician's Guide to Parsing

This scripts requires a working Python installation (version 2 or 3).

To install the parser generator library
[Lark](https://github.com/lark-parser/lark), run

```
pip install lark-parser
```

Then run the script in this repository (either by first copy/pasting its source
to a file, or cloning the repository with git):

```
python convert-delimiters.py < file.tex > output.tex
```


Example input:

```
# test.tex
\begin{document}

This is a doc with $math$ in it. $ W o
W linebreak $

Now we have the following \[ offset equation \]

Now we have another $$
offset equation
$$ why would you use this one though

\end{document}
```

Example output:

```
\begin{document}

This is a doc with \(math\) in it. \( W o
W linebreak \)

Now we have the following \[ offset equation \]

Now we have another \[
offset equation
\] why would you use this one though

\end{document}
```
