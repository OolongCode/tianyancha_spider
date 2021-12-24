from pyecharts.charts import Pie, Map, Page, Bar, WordCloud
from pyecharts import options as opts
from pyecharts.globals import ThemeType


class my_graph:
    def __init__(self, bar_data, map_data, pie_data, wd_data=None):
        self.bar_data = bar_data
        self.map_data = map_data
        self.pie_data = pie_data
        self.wd_data = wd_data
        self.bar, self.pie, self.map, self.wd = None, None, None, None

    def bar_graph(self, title):
        self.bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
                .add_xaxis(['$<1000', '1000<$<10000', '10000<$<100000', '100000<$<1000000', '100000<$<1000000'])
                .add_yaxis("股份有限", self.bar_data['A'])
                .add_yaxis("有限责任", self.bar_data['B'])
                .add_yaxis("其他股份", self.bar_data['C'])
                .add_yaxis("其他有限", self.bar_data['D'])
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
                title_opts=opts.TitleOpts(title=title)
            )
        )

    def map_graph(self, title, item):
        self.map = (
            Map(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
                .add(item, self.map_data, "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title=title),
                legend_opts=opts.LegendOpts(is_show=False),
                visualmap_opts=opts.VisualMapOpts(max_=40, is_piecewise=True),
            )

        )

    def pie_graph(self, title):
        self.pie = (Pie(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
                    .add('', self.pie_data)
                    .set_global_opts(title_opts=opts.TitleOpts(title=title))
                    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
                    )

    def wd_graph(self, title):
        self.wd = (WordCloud(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
                   .add("", self.wd_data, word_size_range=[12, 60], shape="diamond")
                   .set_global_opts(title_opts=opts.TitleOpts(title=title))
                   )

    def page_init(self, filename):
        page = Page(layout=Page.DraggablePageLayout)
        page.add(self.pie)
        page.add(self.map)
        page.add(self.bar)
        page.add(self.wd)
        page.render(filename)

    def page_build(self, input, config, output):
        page = Page()
        page.add(self.pie)
        page.add(self.map)
        page.add(self.bar)
        page.add(self.wd)
        Page.save_resize_html(input, cfg_file=config, dest=output)
