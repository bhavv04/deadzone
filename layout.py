from dash import dcc, html


def create_layout():
    return html.Div([

        # paper header
        html.Div([
            html.P("Oceanography · Hypoxia · Predictive Modeling", className='hero-eyebrow'),
            html.H1("Dead Zones on a Clock", className='paper-title'),
            html.P("Modeling the seasonal collapse and recovery of Gulf of Mexico hypoxic zones using four decades of observational data.",
                   className='paper-subtitle'),
            html.P("Bhavdeep Arora", className='paper-meta'),
        ], className='paper-header'),

        # abstract
        html.Div([
            html.Div([
                html.P("Abstract", className='section-label'),
                html.P("Every summer, a hypoxic zone - a region where dissolved oxygen drops below levels that can support marine life forms in the Gulf of Mexico near the mouth of the Mississippi River. This study analyzes 40 years of annual cruise measurements (1985–2024) from NOAA and LUMCON to model the drivers of dead zone size. A Random Forest regression model trained on spring nitrogen loading and sea surface temperature achieves R² = 0.52 with leave-one-out cross-validation. Nitrogen flux alone accounts for 80.4% of predictive importance. Six anomalous years are identified where discrete meteorological events, including hurricanes and record flooding caused the dead zone to deviate sharply from model predictions.",
                       className='abstract-text'),
            ], className='abstract-box'),
        ], className='paper-section'),

        # key numbers
        html.Div([
            html.Div([
                html.P("Key figures", className='section-label'),
                html.Div([
                    html.Div([
                        html.P("15,154 km²", className='kf-val'),
                        html.P("40-year mean dead zone area", className='kf-label'),
                    ], className='kf-item'),
                    html.Div([html.Div(className='kf-divider')]),
                    html.Div([
                        html.P("22,720 km²", className='kf-val'),
                        html.P("Record extent — 2017", className='kf-label'),
                    ], className='kf-item'),
                    html.Div([html.Div(className='kf-divider')]),
                    html.Div([
                        html.P("r = 0.788", className='kf-val'),
                        html.P("Nitrogen-area correlation", className='kf-label'),
                    ], className='kf-item'),
                    html.Div([html.Div(className='kf-divider')]),
                    html.Div([
                        html.P("80.4%", className='kf-val'),
                        html.P("N-load feature importance", className='kf-label'),
                    ], className='kf-item'),
                    html.Div([html.Div(className='kf-divider')]),
                    html.Div([
                        html.P("R² = 0.52", className='kf-val'),
                        html.P("Model performance (LOO-CV)", className='kf-label'),
                    ], className='kf-item'),
                ], className='kf-row'),
            ], className='paper-content'),
        ], className='paper-section paper-section-tinted'),

        # section 1
        html.Div([
            html.Div([
                html.P("1. Background", className='section-label'),
                html.P("The cause is fertilizer, not weather.", className='section-heading'),
                html.P("Every spring, nitrogen fertilizer from Midwest farms drains into the Mississippi River and flows 1,500 miles south into the Gulf. This triggers massive algal blooms in the shallow coastal shelf near Louisiana. When the algae die and decompose, the bacterial breakdown process consumes all available dissolved oxygen, creating a hypoxic zone where fish, shrimp, and bottom-dwelling life suffocate. The Gulf Hypoxia Task Force set a target of reducing the dead zone to under 4,921 km² by 2035. The 40-year mean is 15,154 km², more than three times that target.",
                       className='section-text'),
            ], className='paper-content'),
        ], className='paper-section'),

        # figure 1
        html.Div([
            html.Div([
                html.P("2. Results", className='section-label'),
                html.P("Dead zone area fluctuates dramatically year to year but shows no long-term decline.", className='section-heading'),
            ], className='paper-content'),
            html.Div([
                dcc.Graph(id='timeseries-chart', style={'height': '280px'},
                          config={'displayModeBar': False}),
                html.P("Figure 1. Annual Gulf of Mexico dead zone area (km²), 1985–2024. Blue bars show observed extent; red bars indicate years flagged as anomalous by Isolation Forest. The dashed line shows model predictions; the horizontal line marks the 40-year mean of 15,154 km².",
                       className='figure-caption'),
            ], className='figure-block'),
        ], className='paper-section'),

        # figure 2 + 3 side by side
        html.Div([
            html.Div([
                html.P("The dominant driver is nitrogen, not temperature.", className='section-heading'),
                html.P("Spring nitrogen loading from the Mississippi River correlates strongly with summer dead zone size (r = 0.788). Sea surface temperature adds marginal predictive value. This confirms that agricultural runoff, not climate variability, is the primary lever controlling hypoxic zone extent.",
                       className='section-text'),
            ], className='paper-content'),
            html.Div([
                html.Div([
                    dcc.Graph(id='scatter-chart', style={'height': '260px'},
                              config={'displayModeBar': False}),
                    html.P("Figure 2. Scatter plot of spring nitrogen load vs dead zone area. Each point represents one year. Red points are anomalous years identified by Isolation Forest.",
                           className='figure-caption'),
                ], className='figure-half'),
                html.Div([
                    dcc.Graph(id='importance-chart', style={'height': '260px'},
                              config={'displayModeBar': False}),
                    html.P("Figure 3. Random Forest feature importance. Nitrogen loading accounts for 80.4% of predictive power; sea surface temperature contributes 19.6%.",
                           className='figure-caption'),
                ], className='figure-half'),
            ], className='figure-two-col'),
        ], className='paper-section'),

        # figure 4
        html.Div([
            html.Div([
                html.P("3. Anomaly Detection", className='section-label'),
                html.P("Six years defy the model — each for a distinct reason.", className='section-heading'),
                html.P("Isolation Forest identifies years where the dead zone was dramatically larger or smaller than nitrogen load alone would predict. In 2017, record spring flooding pushed the zone to 22,720 km², the largest ever measured. In 2020, Hurricane Hanna hit the Gulf days before the annual survey cruise, physically mixing the water column and collapsing the zone before measurement.",
                       className='section-text'),
            ], className='paper-content'),
            html.Div([
                dcc.Graph(id='residuals-chart', style={'height': '240px'},
                          config={'displayModeBar': False}),
                html.P("Figure 4. Model residuals (actual minus predicted) by year. Red bars indicate years where the absolute residual exceeds 4,000 km², each corresponding to a discrete meteorological event.",
                       className='figure-caption'),
            ], className='figure-block'),
        ], className='paper-section'),

        # anomaly table + model stats
        html.Div([
            html.Div([
                html.P("4. Summary tables", className='section-label'),
                html.Div([
                    html.Div([
                        html.P("Table 1. Anomalous years", className='table-title'),
                        html.Div(id='anomaly-list'),
                    ], className='table-block'),
                    html.Div([
                        html.P("Table 2. Model statistics", className='table-title'),
                        html.Div([
                            html.Div([html.Span("R²", className='stat-name'), html.Span("0.52", className='stat-number')], className='stat-item'),
                            html.Div([html.Span("MAE", className='stat-name'), html.Span("2,517 km²", className='stat-number')], className='stat-item'),
                            html.Div([html.Span("Validation", className='stat-name'), html.Span("Leave-one-out CV", className='stat-number')], className='stat-item'),
                            html.Div([html.Span("Years (n)", className='stat-name'), html.Span("40", className='stat-number')], className='stat-item'),
                            html.Div([html.Span("N-load importance", className='stat-name'), html.Span("80.4%", className='stat-number')], className='stat-item'),
                            html.Div([html.Span("SST importance", className='stat-name'), html.Span("19.6%", className='stat-number')], className='stat-item'),
                            html.Div([html.Span("Anomalies flagged", className='stat-name'), html.Span("6 years", className='stat-number')], className='stat-item'),
                        ]),
                    ], className='table-block'),
                ], className='tables-row'),
            ], className='paper-content'),
        ], className='paper-section'),

        # footer
        html.Div([
            html.Div([
                html.P("Data sources: LUMCON / NOAA NCCOS Gulf of Mexico Hypoxia Program · USGS Mississippi River Nutrient Flux · NOAA OISST", className='footer-line'),
            ], className='paper-content'),
        ], className='paper-footer'),

    ], className='app-wrapper')