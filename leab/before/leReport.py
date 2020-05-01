import plotly.graph_objects as go
from plotly.offline import plot
from plotly.graph_objs import Scatter
from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import PackageLoader
from IPython.display import IFrame


class leReport:
    def __init__(
        self,
        baseline_conversion_rate: float = 20,
        minimum_detectable_effect: float = 2,
        sample_size: int = 3400,
        path: str = "leReport.html",
    ):
        self.baseline_conversion_rate = baseline_conversion_rate
        self.minimum_detectable_effect = minimum_detectable_effect
        self.sample_size = sample_size
        self.path = path

    def build_leReport(self):
        self.get_minimum_detectable_effect_inf()
        self.get_minimum_detectable_effect_sup()
        self.get_message_baseline_conversion_rate()
        self.get_message_minimum_detectable_effect()
        self.get_html_plot_sample_size()
        self.get_html_plot_baseline_conversion_rate()
        self.fill_template()
        self.write_html()
        return self.display_report_in_notebook()

    def get_message_baseline_conversion_rate(self):
        self.message_baseline_conversion_rate = (
            f"Baseline conversion rate: {self.baseline_conversion_rate}%"
        )

    def get_message_minimum_detectable_effect(self):
        self.message_minimum_detectable_effect = (
            f"Minimum Detectable Effect: {self.minimum_detectable_effect}%"
        )

    def get_html_plot_sample_size(self):
        self.html_plot_sample_size = plot(
            self.plot_sample_size(),
            output_type="div",
            config=dict(displayModeBar=False),
        )

    def get_html_plot_baseline_conversion_rate(self):
        self.html_plot_baseline_conversion_rate = plot(
            self.plot_baseline_conversion_rate(),
            output_type="div",
            config=dict(displayModeBar=False),
        )

    def fill_template(self):

        from pathlib import Path 
        BASE_DIR = str(Path(__file__).resolve().parent)
        templateLoader = FileSystemLoader(searchpath=BASE_DIR)

        env = Environment(loader=templateLoader)
        TEMPLATE_FILE = 'leTemplate.html'
        template = env.get_template(TEMPLATE_FILE)
        template_vars = {
            "title": "le Report",
            "html_plot_sample_size": self.html_plot_sample_size,
            "html_plot_baseline_conversion_rate": self.html_plot_baseline_conversion_rate,
            "message_baseline_conversion_rate": self.message_baseline_conversion_rate,
            "message_minimum_detectable_effect": self.message_minimum_detectable_effect,
        }
        self.html_out = template.render(template_vars)

    def write_html(self):
        with open(self.path, "w") as f:
            f.write(self.html_out)

    def display_report_in_notebook(self):
        return IFrame(src=self.path, width=1000, height=600)

    def get_minimum_detectable_effect_inf(self):
        self.minimum_detectable_effect_inf = (
            self.baseline_conversion_rate - self.minimum_detectable_effect
        )

    def get_minimum_detectable_effect_sup(self):
        self.minimum_detectable_effect_sup = (
            self.baseline_conversion_rate + self.minimum_detectable_effect
        )

    def plot_baseline_conversion_rate(self):
        """
        plot_baseline_conversion_rate(34, 6)
        """
        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                y=["Minimum Detectable Effect ", "Baseline Conversion Rate "],
                x=[self.minimum_detectable_effect_inf, self.baseline_conversion_rate],
                text=[
                    str(self.minimum_detectable_effect_inf)
                    + "%"
                    + "<br>"
                    + "Conversion rates in the gray area<br>will not be distinguishable from the baseline.",
                    str(self.baseline_conversion_rate) + "%",
                ],
                hoverinfo="text",
                name="",
                orientation="h",
                marker=dict(
                    color="rgba(246, 78, 139, 0.6)",
                    line=dict(color="rgba(246, 78, 139, 1.0)", width=1),
                ),
            )
        )

        fig.add_trace(go.Bar(
        y=['Minimum Detectable Effect '],
        x=[self.minimum_detectable_effect*2],
        text=str(self.minimum_detectable_effect_sup) + '%' + '<br>' + 'Conversion rates in the gray area<br>will not be distinguishable from the baseline.',
        hoverinfo='text',
        name='',
        orientation='h',
        marker=dict(
            color='rgba(58, 71, 80, 0.6)',
            line=dict(color='rgba(58, 71, 80, 1.0)', width=1)
                )
            )
        )

        fig.layout.template = "plotly_white"
        # ggplot2, plotly_dark, seaborn, plotly, plotly_white, presentation, or xgridoff.

        hoverlabel = {
            "bgcolor": "#ffffff",
            "font_size": 12,
            "font_color": "#211c1c",
            "font_family": "Courier New, monospace",
        }

        fig.update_layout(
            barmode="stack",
            showlegend=False,
            hoverlabel=hoverlabel,
            autosize=False,
            width=500,
            height=150,
            margin=dict(l=2, r=2, t=40, b=30),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )

        fig.update_yaxes(automargin=True, showgrid=False)  # avoid cropped labels
        fig.update_xaxes(showgrid=False, ticksuffix="%")
        self.fig_baseline_conversion_rate = fig
        return self.fig_baseline_conversion_rate

    def plot_sample_size(self):
        """
        plot_sample_size(2300)
        """
        if self.sample_size > 9999:
            font_size = 28
        else:
            font_size = 35

        colors = ["gold"]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=["sample size<br>per variation."], values=[self.sample_size]
                )
            ]
        )
        fig.update_traces(
            hoverinfo="label",
            textinfo="value",
            textfont=dict(size=font_size, color="white"),
            marker=dict(colors=colors, line=dict(color="#ffffff", width=1)),
        )
        fig.update_layout(
            showlegend=False,
            autosize=True,
            width=160,
            height=160,
            margin=dict(l=2, r=2, t=20, b=20),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        self.fig_sample_size = fig
        return self.fig_sample_size
