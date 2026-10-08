import unittest
import time_series_visualizer
import matplotlib as mpl


class DataAnalystTestCase(unittest.TestCase):

  def setUp(self):
    self.fig_line = time_series_visualizer.draw_line_plot()
    self.fig_bar = time_series_visualizer.draw_bar_plot()
    self.fig_box = time_series_visualizer.draw_box_plot()

  def test_line_plot(self):
    actual = self.fig_line
    self.assertIsInstance(
        actual,
        mpl.figure.Figure,
        'Expected draw_line_plot to return a matplotlib figure instance.',
    )

  def test_bar_plot(self):
    actual = self.fig_bar
    self.assertIsInstance(
        actual,
        mpl.figure.Figure,
        'Expected draw_bar_plot to return a matplotlib figure instance.',
    )

  def test_box_plot(self):
    actual = self.fig_box
    self.assertIsInstance(
        actual,
        mpl.figure.Figure,
        'Expected draw_box_plot to return a matplotlib figure instance.',
    )


if __name__ == '__main__':
  unittest.main()