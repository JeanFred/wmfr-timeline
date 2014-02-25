png:
	inkscape --export-png=WmFr-Timeline-Preview.png --export-id=background --export-width=5000 WmFr-Timeline.svg

debug-png:
	inkscape --export-png=WmFr-Timeline-Preview-Debug.png --export-area-drawing --export-width=5000 WmFr-Timeline.svg
plots:
	python generate_plots.py
