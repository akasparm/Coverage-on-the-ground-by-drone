#------------------------------------ Importing the required libraries ----------------------------------------
from math import *
from numpy import *

#---------------------------------- Defining the function to find the area ------------------------------------
def area_covered(psi, theta, phi, dx, dy, dz):

    #--------------------------- Creating the variables for matrix calculations -------------------------------
    a = cos(2*theta)
    b = sin(2*theta)*sin(psi)
    c = cos(psi)**2 + (sin(psi)**2)*(-cos(2*theta))
    d = cos(theta)*(cos(phi)*dx + sin(phi)*dy) + sin(theta)*dz
    e = cos(psi)*(cos(phi)*dy - sin(phi)*dx) + sin(theta)*sin(psi)*(cos(phi)*dx + sin(phi)*dy) - cos(theta)*sin(psi)*dz
    f = dx**2 + dy**2 - dz**2
    area_matrix = array([[a, b, d], [b, c, e], [d, e, f]])                                                                      # Computation of the matrix for Area calculations

    #--------------------------------------- Calculating the Area ---------------------------------------------
    A = - (pi/((a*c - b*b)**(3/2)))*(linalg.det(area_matrix))

    #--------------------------------------- Returning the output ---------------------------------------------
    return A;


#---------------------------------------- Defining the main function ------------------------------------------
def main():

    #----------------------------------- Asking for the required input ----------------------------------------
    psi = radians(float(input("Enter rotation about x in degrees (psi): ")))
    theta = radians(float(input("Enter rotation about y in degrees (theta): ")))
    phi = radians(float(input("Enter rotation about z in degrees (phi): ")))
    dx = float(input("Enter final x coordinate(dx): "))
    dy = float(input("Enter final y coordinate(dy): "))
    dz = float(input("Enter final z coordinate(dz): "))

    #--------------------------------------- Printing the output ----------------------------------------------
    print("The area on covered on the XY Plane is: ", area_covered(psi, theta, phi, dx, dy, dz))

if __name__ == "__main__":
    
    main()