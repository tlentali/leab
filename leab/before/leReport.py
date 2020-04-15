import plotly.graph_objects as go
from jinja2 import Template, Environment, FileSystemLoader
from plotly.offline import plot
from plotly.graph_objs import Scatter
from IPython.display import IFrame


def plot_baseline_conversion_rate(
    baseline_conversion_rate: float = 20, minimum_detectable_effect: float = 5
):
    """
    plot_baseline_conversion_rate(34, 6)
    """
    minimum_detectable_effect_inf = baseline_conversion_rate - minimum_detectable_effect
    minimum_detectable_effect_sup = baseline_conversion_rate + minimum_detectable_effect

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            y=["Minimum Detectable Effect ", "Baseline conversion rate "],
            x=[minimum_detectable_effect_inf, baseline_conversion_rate],
            text=[
                str(minimum_detectable_effect_inf)
                + "%"
                + "<br>"
                + "Conversion rates in the gray area<br>will not be distinguishable from the baseline.",
                str(baseline_conversion_rate) + "%",
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

    fig.add_trace(
        go.Bar(
            y=["Minimum Detectable Effect "],
            x=[minimum_detectable_effect * 2],
            text=str(minimum_detectable_effect_sup)
            + "%"
            + "<br>"
            + "Conversion rates in the gray area<br>will not be distinguishable from the baseline.",
            hoverinfo="text",
            name="",
            orientation="h",
            marker=dict(
                color="rgba(58, 71, 80, 0.6)",
                line=dict(color="rgba(58, 71, 80, 1.0)", width=1),
            ),
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

    return fig


def plot_sample_size(sample_size):
    """
    plot_sample_size(2300)
    """
    if sample_size > 9999:
        font_size = 28
    else:
        font_size = 35

    colors = ["gold"]

    fig = go.Figure(
        data=[go.Pie(labels=["sample size<br>per variation."], values=[sample_size])]
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
    return fig


def build_leReport(baseline_conversion_rate, minimum_detectable_effect, sample_size, path):
    """
    """
    message_baseline_conversion_rate = (
        f"Baseline conversion rate: {baseline_conversion_rate}%"
    )
    message_minimum_detectable_effect = (
        f"Minimum Detectable Effect: {minimum_detectable_effect}%"
    )
    html_plot_sample_size = plot(
        plot_sample_size(sample_size), output_type="div", config=dict(displayModeBar=False)
    )
    html_plot_baseline_conversion_rate = plot(
        plot_baseline_conversion_rate(34, 6),
        output_type="div",
        config=dict(displayModeBar=False),
    )

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template/leTemplate.html")
    template_vars = {
        "title": "le Report",
        "html_plot_sample_size": html_plot_sample_size,
        "html_plot_baseline_conversion_rate": html_plot_baseline_conversion_rate,
        "message_baseline_conversion_rate": message_baseline_conversion_rate,
        "message_minimum_detectable_effect": message_minimum_detectable_effect,
    }

    html_out = template.render(template_vars)

    with open(path, "w") as f:
        f.write(html_out)

    IFrame(src=path, width=1000, height=600)

