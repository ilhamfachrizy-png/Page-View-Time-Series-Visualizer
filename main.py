import time_series_visualizer
from unittest import main

# Jalankan fungsi visualisasi
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()

# Jalankan unit test secara otomatis
main(module='test_module', exit=False)