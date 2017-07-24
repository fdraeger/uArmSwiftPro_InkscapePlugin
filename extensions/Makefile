TESTFILE=./empty.svg


all:	
	@echo "Targets: copy, area, position, print"

copy:  
	/bin/cp ./*.py ~/.config/inkscape/extensions
	/bin/cp ./*.inx ~/.config/inkscape/extensions
	/bin/cp ../printarea/uArmSwiftPro_Max.svg ~/.config/inkscape/extensions

print:
	./uarm.py --active-tab=\"print\" --pos-root-x=210.0 --pos-root-y=210.0 --pos-root-z=0 --rotate-root=90.0 $(TESTFILE)

area:
	./uarm.py --active-tab=\"area\" --unit=mm --pos-root-x=210.0 --pos-root-y=210.0 --pos-root-z=0 --rotate-root=90.0 $(TESTFILE)


position:
	./uarm.py --active-tab=\"position\" --unit=px --pos-root-x=210.0 --pos-root-y=210.0 --pos-root-z=0 --rotate-root=90.0 $(TESTFILE)

