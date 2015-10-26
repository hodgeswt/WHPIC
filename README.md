Will Hodges Python Interpreted Calculator
==============

How to Use
--------------

1. Clone repo.
2. Be sure to `(sudo) pip install grako`
3. `cd /path/to/repo`
4. `python imp.py`
5. **OR** `python calc.py -h`
6. Have fun!

Example
-------------
Enter `3*3;4*2342;` and hit enter. It should spit out 
    3 * 3 = 9
    4 * 2342 = 9368
Enter `3*3;4*2342` and hit enter. It should spit out
    3 * 3 = 9


How it Works
--------------

The WHPIC was a simple learning experience involving EBNF grammars and the grako library. 
I used the grako library to generator an easy-to-use parser for the grammar (`calc.g`) and then used that parser in `imp.py`.
The file `imp.py` is fairly self-explanatory.
