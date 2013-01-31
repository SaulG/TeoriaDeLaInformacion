from subprocess import call
def grafica():
    out = open('grafica.plot', 'w')     
    print >>out,'''set term postscript eps color 24\n
set size 2, 1\n                                                                                                                                                                                                 
set xlabel \"Iteracion\"\n
set ylabel \"Objetivo\"\n
set key off\n
set pointsize 1.2\n
set output \"grafica.eps\"\n
   plot sin(1/x) axis x1y1, 100*cos(x-1) axis x2y2'''                                                                                                                                                  
    out.close()                                                                                                                                                           
    call(['gnuplot', 'grafica.plot'])      
    return 

def main():
    grafica()
    return

main()
