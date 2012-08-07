png:
	inkscape --export-png=Timeline.png --export-area-drawing --export-width=10000 WmFr-Timeline.svg
	
plots:
	python generate_plots.py