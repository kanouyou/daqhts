# DAQ for HTS critical current measurement

---

# Author
* Ye YANG (Kyushu University)
* Email: kanouyou@kune2a.nucl.kyushu-u.ac.jp

# Overview
DAQ for HTS critical current measurement is written in Python and C++, and it depends on the libraries as follows.
- PyQt4
- HDF5
- ROOT (optional)
- PyVISA
- numpy
- matplotlib
- Cython

# Usage
The simple way to program directly:
```{r, engine='bash', count_lines}
chmod u+x main.py
main.py -m
```
Because python depends on the environment you set, `anaconda` is recommanded to set the computer environment.

