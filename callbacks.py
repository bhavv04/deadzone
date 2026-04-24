import pandas as pd
import numpy as np
import plotly.graph_objects as go
from dash import Input, Output, callback, html

df = pd.read_csv('data/features_with_predictions.csv')

ANOMALY_NOTES = {
    1988: ("Smaller", "La Niña year, low spring river discharge"),
    1999: ("Larger", "Record nitrogen load, above average discharge"),
    2003: ("Larger", "High May discharge, warm stratification"),
    2009: ("Smaller", "La Niña, low spring river discharge"),
    2017: ("Larger", "RECORD — extreme spring flooding, record N load"),
    2022: ("Smaller", "Drought conditions in Mississippi watershed"),
}

COLORS = {
    'blue':       '#1a6b8a',
    'blue_light': '#d0e8f0',
    'red':        '#c0392b',
    'red_light':  '#f5d0cc',
    'green':      '#1a7a52',
    'orange':     '#e8a030',
    'grid':       '#f0f0eb',
    'text':       '#6b6b65',
    'bg':         'white',
}


def base_layout():
    return dict(
        paper_bgcolor=COLORS['bg'],
        plot_bgcolor=COLORS['bg'],
        font=dict(family='Manrope, sans-serif', color='#1a1a18'),
        margin=dict(l=20, r=20, t=16, b=20),
    )


@callback(Output('timeseries-chart', 'figure'), Input('timeseries-chart', 'id'))
def render_timeseries(_):
    fig = go.Figure()

    anomaly_mask = df['anomaly'] == -1

    # actual bars
    fig.add_trace(go.Bar(
        x=df['year'], y=df['area_km2'],
        name='Actual',
        marker_color=[COLORS['red'] if a else COLORS['blue_light']
                      for a in anomaly_mask],
        marker_line_width=0,
        hovertemplate='%{x}: %{y:,.0f} km²<extra>Actual</extra>',
    ))

    # predicted line
    fig.add_trace(go.Scatter(
        x=df['year'], y=df['predicted'],
        name='Predicted',
        mode='lines+markers',
        line=dict(color=COLORS['blue'], width=2, dash='dot'),
        marker=dict(size=5, color=COLORS['blue']),
        hovertemplate='%{x}: %{y:,.0f} km²<extra>Predicted</extra>',
    ))

    # mean line
    mean_val = df['area_km2'].mean()
    fig.add_hline(y=mean_val, line_color=COLORS['orange'],
                  line_dash='dash', line_width=1.5,
                  annotation_text=f"40yr mean: {mean_val:,.0f} km²",
                  annotation_font_size=10,
                  annotation_font_color=COLORS['orange'])

    layout = base_layout()
    layout.update(dict(
        xaxis=dict(showgrid=False, tickfont=dict(size=10, color=COLORS['text'])),
        yaxis=dict(showgrid=True, gridcolor=COLORS['grid'],
                   tickfont=dict(size=10, color=COLORS['text']),
                   tickformat=',.0f', zeroline=False, title=''),
        legend=dict(orientation='h', y=1.1, x=0,
                    font=dict(size=11), bgcolor='rgba(0,0,0,0)'),
        bargap=0.25,
    ))
    fig.update_layout(layout)
    return fig


@callback(Output('scatter-chart', 'figure'), Input('scatter-chart', 'id'))
def render_scatter(_):
    fig = go.Figure()

    anomaly_mask = df['anomaly'] == -1

    fig.add_trace(go.Scatter(
        x=df[~anomaly_mask]['nitrogen_load'],
        y=df[~anomaly_mask]['area_km2'],
        mode='markers+text',
        name='Normal',
        marker=dict(size=9, color=COLORS['blue'],
                    line=dict(color='white', width=1.5)),
        text=df[~anomaly_mask]['year'].astype(str),
        textposition='top center',
        textfont=dict(size=8, color=COLORS['text']),
        hovertemplate='%{text}<br>N: %{x} Mt<br>Area: %{y:,.0f} km²<extra></extra>',
    ))

    fig.add_trace(go.Scatter(
        x=df[anomaly_mask]['nitrogen_load'],
        y=df[anomaly_mask]['area_km2'],
        mode='markers+text',
        name='Anomaly',
        marker=dict(size=11, color=COLORS['red'],
                    line=dict(color='white', width=1.5)),
        text=df[anomaly_mask]['year'].astype(str),
        textposition='top center',
        textfont=dict(size=8, color=COLORS['red']),
        hovertemplate='%{text}<br>N: %{x} Mt<br>Area: %{y:,.0f} km²<extra>Anomaly</extra>',
    ))

    layout = base_layout()
    layout.update(dict(
        xaxis=dict(showgrid=True, gridcolor=COLORS['grid'],
                   tickfont=dict(size=10, color=COLORS['text']),
                   title=dict(text='Spring N load (million kg)',
                              font=dict(size=11, color=COLORS['text']))),
        yaxis=dict(showgrid=True, gridcolor=COLORS['grid'],
                   tickfont=dict(size=10, color=COLORS['text']),
                   tickformat=',.0f', zeroline=False, title=''),
        legend=dict(orientation='h', y=1.1, x=0,
                    font=dict(size=11), bgcolor='rgba(0,0,0,0)'),
        showlegend=True,
    ))
    fig.update_layout(layout)
    return fig


@callback(Output('importance-chart', 'figure'), Input('importance-chart', 'id'))
def render_importance(_):
    features = ['Nitrogen load', 'Sea surface temp']
    values = [80.4, 19.6]
    colors = [COLORS['blue'], COLORS['blue_light']]

    fig = go.Figure(go.Bar(
        x=values, y=features,
        orientation='h',
        marker_color=colors,
        marker_line_width=0,
        text=[f'{v}%' for v in values],
        textposition='inside',
        textfont=dict(size=12, color='white'),
        hovertemplate='%{y}: %{x}%<extra></extra>',
    ))

    layout = base_layout()
    layout.update(dict(
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, tickfont=dict(size=12, color='#1a1a18')),
        bargap=0.4,
        margin=dict(l=20, r=20, t=16, b=20),
    ))
    fig.update_layout(layout)
    return fig


@callback(Output('residuals-chart', 'figure'), Input('residuals-chart', 'id'))
def render_residuals(_):
    colors = [COLORS['red'] if abs(r) > 4000 else COLORS['blue_light']
              for r in df['residual']]

    fig = go.Figure(go.Bar(
        x=df['year'], y=df['residual'],
        marker_color=colors,
        marker_line_width=0,
        hovertemplate='%{x}: %{y:+,.0f} km²<extra></extra>',
    ))

    fig.add_hline(y=0, line_color='#1a1a18', line_width=1)

    layout = base_layout()
    layout.update(dict(
        xaxis=dict(showgrid=False, tickfont=dict(size=10, color=COLORS['text'])),
        yaxis=dict(showgrid=True, gridcolor=COLORS['grid'],
                   tickfont=dict(size=10, color=COLORS['text']),
                   tickformat='+,.0f', zeroline=False, title=''),
        bargap=0.25,
        annotations=[dict(
            text='Red = model prediction error > 4,000 km²',
            x=0.01, y=0.97, xref='paper', yref='paper',
            showarrow=False, font=dict(size=10, color=COLORS['text']),
            align='left',
        )]
    ))
    fig.update_layout(layout)
    return fig


@callback(Output('anomaly-list', 'children'), Input('anomaly-list', 'id'))
def render_anomalies(_):
    anomalies = df[df['anomaly'] == -1].sort_values('year')
    items = []
    for _, row in anomalies.iterrows():
        year = int(row['year'])
        note = ANOMALY_NOTES.get(year, ('', 'Unusual nitrogen-area relationship'))
        direction, reason = note
        color = COLORS['red'] if direction == 'Larger' else COLORS['blue']
        arrow = '↑' if direction == 'Larger' else '↓'
        items.append(html.Div([
            html.Div([
                html.Span(str(year), className='anomaly-year'),
                html.Span(f"{arrow} {direction}", className='anomaly-dir',
                          style={'color': color}),
            ], className='anomaly-header'),
            html.P(reason, className='anomaly-reason'),
        ], className='anomaly-item'))
    return items