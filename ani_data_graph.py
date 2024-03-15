from bokeh.plotting import ColumnDataSource, output_file, figure, save
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis11
from bokeh.models.tools import HoverTool
import pandas

data_frame = pandas.read_csv('anime_data_for_graph.csv')
source = ColumnDataSource(data_frame)
output_file('index.html')

anime_list = source.data['Title'].tolist()

p = figure(
    y_range = anime_list,
    x_axis_label = 'Score',
    y_axis_label = 'Anime',
    width = 1920,
    height = 3000,
    # fontsize = 8,
    title = 'Anime Scores',
    toolbar_location = None,
    tools = ""
    # tools = "pan, box_select, zoom_in, zoom_out, save, reset"
)
color_mapper = linear_cmap(field_name='Score', palette=Viridis11, low=min(data_frame['Score']), high=max(data_frame['Score']))

p.hbar(
    y = 'Title',#anime, u sure bro?
    right = 'Score',
    # left = 0,
    height = 0.4,
    fill_color = color_mapper,
    # fill_alpha = 0.9,
    source = source
    # legend_field = 'Title'#anime
)


hover = HoverTool()
hover.tooltips="""
    <div>
        <h3>@Title</h3>
        <div><strong>Score: </strong>@Score</div>
        <div><img src="@Image" alt="Cool Anime Image" height="200px"></div>
    </div>
"""

p.add_tools(hover)
p.ygrid.grid_line_color = None
save(p)