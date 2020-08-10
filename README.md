# Communication program for Pfeiffer TPG single gauge controler

## Programs
- pfeiffer.py: Python library from <https://github.com/CINF/PyExpLabSys/blob/master/PyExpLabSys/drivers/pfeiffer.py>
- rec_tpg.py:  Main program

## How to use
1. Connect the PC to the TPG module via RS232. Use a USB-RS232(female) cable.
   The connection cable is available in Amazon <https://www.amazon.co.jp/gp/product/B075YHFMC7>
2. Edit parameters 'filename' and 'waittime' in rec_tpg.py
3. Run the program by `$python rec_tpg.py`