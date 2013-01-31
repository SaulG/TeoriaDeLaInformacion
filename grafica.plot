set term postscript eps color 24

set size 2, 1
                                                                                                                                                                                                 
set xlabel "Iteracion"

set ylabel "Objetivo"

set key off

set pointsize 1.2

set output "grafica.eps"

   plot sin(1/x) axis x1y1, 100*cos(x-1) axis x2y2
