import ezdxf

lbp = 100 #length bp
wl_spacing = 1.53


#opens csv file and returns the offset table
def _open_file(file_path):

    print("openning file..." + file_path)
    
    # Open the file for reading
    with open(file_path, 'r') as file: # Read the file line by line and store each line as an element in a list
        file_lines = file.readlines()
    offset_table = [] #the main offset dataset
    # Now you can work with the list of lines
    for line in file_lines:
        l = line.replace("," , " ")
        offset_table.append(l.split())
    return offset_table



def get_xyz(offset):

    print("reading points...")
    
    z_axis = [i for i in offset[0]] #isolating the Z index
    z_axis.pop(0) #the first element is actually blank[we replaced with 0.00 to make the table look like a cube]; so remove
    offset.pop(0) #removing the 1st element cause we already isolated that in z-axis
    x_axis = [i[0] for i in offset] #isolating the x_axis
    for i in offset:    
        i.pop(0) #removing the x_axis from the offset table
    x_dis = float(lbp)/float(x_axis[len(x_axis)-1])
    z_dis = float(wl_spacing)

    return offset,x_axis,x_dis,z_axis,z_dis




def wl_spline(_offset ,x_axis,x_dis,z_axis,z_dis):
    wl = []
    for z in range(0, len(z_axis)): 
        wl_temp = []
        for x in range(0, len(x_axis)):
            y_point = _offset[x][z]
            points.append([float(x_axis[x])*x_dis , float(y_point) , float(z_axis[z])*z_dis])
            wl_temp.append([float(x_axis[x])*x_dis , float(y_point) , float(z_axis[z])*z_dis])
        wl.append(wl_temp)
    #mirror
    for z in range(0, len(z_axis)): 
        wl_temp = []
        for x in range(0, len(x_axis)):
            y_point = _offset[x][z]
            points.append([float(x_axis[x])*x_dis , -float(y_point) , float(z_axis[z])*z_dis])
            wl_temp.append([float(x_axis[x])*x_dis , -float(y_point) , float(z_axis[z])*z_dis])
        wl.append(wl_temp)
    print("making waterline spline...")
    return wl

def stl_spline(_offset ,x_axis,x_dis,z_axis,z_dis):
    stl = []
    for x in range(0, len(x_axis)):
        stl_temp = []
        for z in range(0, len(z_axis)):
            y_point = _offset[x][z]
            stl_temp.append([float(x_axis[x])*x_dis , float(y_point) , float(z_axis[z])*z_dis])
        stl.append(stl_temp)
    #mirror
    for x in range(0, len(x_axis)):
        stl_temp = []
        for z in range(0, len(z_axis)):
            y_point = _offset[x][z]
            stl_temp.append([float(x_axis[x])*x_dis , -float(y_point) , float(z_axis[z])*z_dis])
        stl.append(stl_temp)
    print("making station spline...")
    return stl


def _get_point(_offset ,x_axis,x_dis,z_axis,z_dis ):
    p = []
    for z in range(0, len(z_axis)): 
        for x in range(0, len(x_axis)):
            y_point = _offset[x][z]
            p.append([float(x_axis[x])*x_dis , float(y_point) , float(z_axis[z])*z_dis])
            
    #mirror
    for z in range(0, len(z_axis)): 
        for x in range(0, len(x_axis)):
            y_point = _offset[x][z]
            p.append([float(x_axis[x])*x_dis , -float(y_point) , float(z_axis[z])*z_dis])
    print("getting points...")
    return p

def save_as_dxf(pnts , wl , stl ):
    # MESH requires DXF R2000 or later
    doc = ezdxf.new("R2000")
    msp = doc.modelspace()
    for i in range(0 , len(wl)) : mesh = msp.add_spline(wl[i])
    for i in range(0 , len(stl)) : mesh = msp.add_spline(stl[i])
    for i in range(0 , len(pnts)) : mesh = msp.add_point(pnts[i])
    print("exporting DXF...")
    print("AHHULL made by Ismam Labib and Mokarrom")
    doc.saveas("hull_points.dxf")


offset = []
x_axis,x_dis,z_axis,z_dis = [[],0,[],0]
points = []


def run(csv_file_path):
    main_offset = _open_file(csv_file_path)
    offset,x_axis,x_dis,z_axis,z_dis = get_xyz(main_offset)
    points = _get_point(offset , x_axis,x_dis,z_axis,z_dis)
    _wl_point = wl_spline(offset ,x_axis,x_dis,z_axis,z_dis)
    _stl_point = stl_spline(offset ,x_axis,x_dis,z_axis,z_dis)
    save_as_dxf(points , _wl_point , _stl_point)
    return points , _wl_point , _stl_point



