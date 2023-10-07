# AHHULL 1.0 Doc  
Made by Ismam Labib and Mokarrom Hossain  

**What is AHHULL:**
-- AHHULL is a simple GUI program that turns a OFFSET DATA TABLE (.csv) into a 3D Autocad file (.dxf)

**How to use AHHULL:**
	BUILD/EXE:
		Step 1: RUN AHHULL.exe
		Step 2: Input Length Between Perpendicular
		Step 3: Input Waterplane Line Spacing
		Step 4: Click "Browse" and select you offset data (in .CSV) in file manager
		Step 5: Hit "Start" and boom
		Step 6: Done , just open the "hull_points.dxf" in Autocade 2007 or upper
	Source:
		Step 1: You need to have python and some python library to run through code [See Below]
		Step 2: Open main.py
		Step 3: Run the main.py
		Step 4: [Same as :step 1 to 6 of exe version]

**WHY AHHULL:**
-- m e h ^_^ idk


**I want to build from source:**
-- We used cxFreeze for the packaging. So you have to pip install it.
   We already wrote a simple setup.py if you want to change it then it's your responsibility
   check "https://stackoverflow.com/questions/9895636/how-do-i-use-cx-freeze" for details


**Third Party Libs:**
-- tkinter (for gui)
-- matplotlib (for 3d visualization)
-- numpy (for math)
-- ezdxf (for writing dxf file programmatically)

**Credit and Thoughts:**  
-- We started this project as just a simple hobby project. Who knows what will happen to this after ages. Let's see. **Open for any kind of advice and feedback or contribution**
