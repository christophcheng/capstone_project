# enable plotting extensions
import holoviews as hv
import panel as pn
from holoviews import opts

hv.extension('bokeh')
pn.extension('tabulator')

# configure defaults
opts.defaults(
    opts.Scatter(
        alpha=0.6,
        line_color='black',
        show_grid=True,
        height=360,
        width=450,
        default_tools=['box_zoom', 'reset']
    ),
    opts.Curve(
        show_grid=True,
        height=360,
        width=450,
        default_tools=['box_zoom', 'reset']
    )
)

from .data import get_champ_data, get_top_data, get_picks_data, get_name_data
