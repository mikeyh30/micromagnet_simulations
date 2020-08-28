run:
	mumax3 test1.mx3

image:
	feh test1.out/*.jpg
	mumax3-convert -png test1.out/*.ovf
	feh test1.out/*.png

clean:
	rm -r test1.mx3
