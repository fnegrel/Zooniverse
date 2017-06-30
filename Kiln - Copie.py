# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:00:49 2017

@author: FLOLT
"""

import csv
cr = csv.reader(open("slavery-from-space-classifications.csv","r"))
List_Coord=[]
List_Coord_2=[]
List_Kiln_Number=[]
List_csv=[]
Temp_kiln_x=[]
Temp_kiln_y=[]
Coord_kiln_x=[]
Coord_kiln_y=[]
Kiln_visible_picture=[]
num_classif = 0
Size_picture_x = []
Size_picture_y = []
List_decimal_Coord = []
List_decimal_Coord2 = []

C=0
for row in cr:
    
    if C!=0:
        #Getting Esting and Northing Coordinates of the picture
        #print(row[12])
        
        #EASTING
        
        Marqueur = (row[12][-52:-3].split('","Northing_BottomRight":"')[0]).split(':')
        #print(Marqueur)
        #print(row[12])
        try:
            ((row[12][-52:-3].split('","Northing_BottomRight":"')[0] ).split(':')[0]).split('"')[1]
            #print(test)
            List_Coord.append(((row[12][-52:-3].split('","Northing_BottomRight":"')[0] ).split(':')[0]).split('"')[1])
            
            C=C+1
        except:
            try:
                List_Coord.append(((row[12][-52:-3].split('","Northing_BottomRight":"')[0] ).split(':')[1]).split('"')[1])
            except:
                
                List_Coord.append(((row[12][-52:-3].split('","Northing_BottomRight":"')[0] ).split(':')[0]).split('"')[0])
                C=C+1
        
        #NORTHING    
        #print((row[12][-52:-3].split('","Northing_BottomRight":"')))
        try:
            List_Coord_2.append(row[12][-52:-3].split('","Northing_BottomRight":"')[1])
        except:
            List_Coord_2.append(("Missing data"))
            
         
        #Converting initial Easting and Northing to decimal coordinate 
        #print(List_Coord)
        for i in range(len(List_Coord)):
            calc = List_Coord[i]
            calc2= List_Coord_2[i]
            #print(str(calc))
            temps = str(calc).split(" ")
            temps2= str(calc2).split(" ")
            #print(temps)
            #print(temps2)
            
            try:
                #print(temps[0])
                #print(temps[1])
                #print(temps[2])
                temp = float(temps[0]) + float(temps[1])/60 + float(temps[2])/3600
                temp2= float(str(calc2).split(" ")[0]) + float(str(calc2).split(" ")[1])/60 + float(str(calc2).split(" ")[2])/3600
                List_decimal_Coord.append(temp)
                List_decimal_Coord2.append(temp2)
            except:
                List_decimal_Coord.append("Could not calculate this field")
                List_decimal_Coord2.append("Could not calculate this field")
                
                
             
        #        
        #    try:
        #        temp2= float(str(calc2).split(" ")[0]) + float(str(calc2).split(" ")[1])/60 + float(str(calc2).split(" ")[2])/3600
        #        List_decimal_Coord2.append(temps2)
        #    except:
        #        List_decimal_Coord2.append("Could not calculate this field")
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        #Getting the number of kiln involved in the picture
        Chaine=row[11]
        kiln_number = Chaine.count('tool_label":"Kiln"')
        #print(kiln_number)
        List_Kiln_Number.append(kiln_number)
        #print(row[11])
        
        #Getting the coordinate of each kiln annotated
        List_csv.append(row[11].split(","))
        
        tst=0
        for i in range(2,len(row[11].split(",")),6):
                
                try:
                    row[11].split(",")[i]
                    row[11].split(",")[i+1]   
                    #print("wi")   
                    
                    if row[11].split(",")[i][0] != ('"tool_label":"Kiln"}'):
                        
                        if row[11].split(",")[i][0] != ('"details":[]') and row[11].split(",")[i+1][0] != ('"tool_label":"Kiln"}'):
                                                    
                            num_classif = row[0]
                            Temp_kiln_x.append([row[11].split(",")[i]])
                            Temp_kiln_y.append([row[11].split(",")[i+1]])
                            Kiln_visible_picture.append(num_classif)
                            #print(row[10])
                            Size_picture_x.append(row[10].split(":")[-2].split(",")[0])
                            #print((row[10].split(":")[-2].split(",")))
                            Size_picture_y.append(row[10].split(":")[-1].split("}]}")[0])
                            
                        else:
                            break
                        
        
                    else:  
                        if row[11].split(",")[i][0] != ('"details":[]') and row[11].split(",")[i+1][0] != ('"tool_label":"Kiln"}'):
                                                   
                            num_classif = row[0]
                            Temp_kiln_x.append([row[11].split(",")[i+1]])
                            Temp_kiln_y.append([row[11].split(",")[i+2]])
                            Kiln_visible_picture.append(num_classif)
                            #print(row[10])
                            Size_picture_x.append(row[10].split(":")[-2].split(",")[0]) 
                            #print((row[10].split(":")[-2].split(",")))
                            Size_picture_y.append(row[10].split(":")[-1].split("}]}")[0])
                                  
                except:
                    #print("exception")
                    pass
                else:
                    pass
                
        #Size of the picture        
        #print(row[10].split(":"))
        
        
    
    else:
        C=C+1    

    
    
    

for i in range(len(Temp_kiln_x)):
    try:
        Coord_kiln_x.append(Temp_kiln_x[i][0].split(":")[2])
    except:
        Coord_kiln_x.append(Temp_kiln_x[i][0].split(":")[1])
        
    Coord_kiln_y.append(Temp_kiln_y[i][0].split(":")[1])
    
    

    
        
        
        
#print(List_decimal_Coord)

#Wrinting coords in a csv
        
outfile = open('Kiln_Coordinate.csv', 'w',newline='')
writer = csv.writer(outfile, delimiter=';', quotechar='"')
data = [["X_Coords","Y_Coords","On the picture","X_size_picture","Y_size_picture","Esting","Northing"]]
writer.writerows(data)

for i in range(len(Coord_kiln_x)):
    data = [[Coord_kiln_x[i],Coord_kiln_y[i],Kiln_visible_picture[i],Size_picture_x[i],Size_picture_y[i],List_decimal_Coord[i],List_decimal_Coord2[i]]]
    writer.writerows(data)
    
outfile.close()




#Printing the Easting and Northing of picture        
#print(List_Coord)
#print(List_Coord_2)
#print(List_decimal_Coord2)

#print(List_csv[14])
#print(List_Kiln_Number)

#print(Temp_kiln_x[2],Temp_kiln_y[2])

#print(Coord_kiln_x,Coord_kiln_y)
#Printing the total number of kiln marqued in the csv
Kiln_total=sum(List_Kiln_Number)
print("The total number of kiln is : ",Kiln_total)
