run:
	mumax3 test1.mx3

image:
	feh test1.out/*.jpg
	mumax3-convert -png test1.out/*.ovf
	feh test1.out/*.png

%.npy: %.ovf
	mumax3-convert -numpy $^

clean:
	rm -r test1.out

v1:
	mumax3 B_field/v1.mx3
	mumax3-convert -numpy B_field/v1.out/*.ovf

v2:
	mumax3 B_field/v2.mx3
	mumax3-convert -numpy B_field/v2.out/*.ovf

h1:
	mumax3 B_field/h1.mx3
	mumax3-convert -numpy B_field/h1.out/*.ovf

h2:
	mumax3 B_field/h2.mx3
	mumax3-convert -numpy B_field/h2.out/*.ovf

h3:
	mumax3 B_field/h3.mx3
	mumax3-convert -numpy B_field/h3.out/*.ovf
