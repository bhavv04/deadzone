from dash import dcc, html


def create_layout():
    return html.Div([

        # navbar
        html.Div([
            html.Div([
                html.H1("Dead Zones on a Clock", className='nav-title'),
            ], className='nav-brand'),
            html.Span("Gulf of Mexico · 1985–2024", className='nav-tag'),
        ], className='navbar'),

        # hero
        html.Div([
            html.P("40 years of NOAA/LUMCON hypoxia data", className='hero-eyebrow'),
            html.H2("Every summer, an area the size of New Jersey suffocates in the Gulf of Mexico.",
                    className='hero-title'),
            html.P("This dashboard models the annual collapse and recovery of the Gulf of Mexico dead zone using nitrogen loading, sea surface temperature, and Random Forest regression.",
                   className='hero-sub'),

            # stat pills
            html.Div([
                html.Div([
                    html.P("15,154 km²", className='stat-val'),
                    html.P("40-year mean", className='stat-label'),
                ], className='stat-pill'),
                html.Div([
                    html.P("22,720 km²", className='stat-val'),
                    html.P("Record (2017)", className='stat-label'),
                ], className='stat-pill'),
                html.Div([
                    html.P("r = 0.788", className='stat-val'),
                    html.P("Nitrogen correlation", className='stat-label'),
                ], className='stat-pill'),
                html.Div([
                    html.P("80.4%", className='stat-val'),
                    html.P("N load importance", className='stat-label'),
                ], className='stat-pill'),
                html.Div([
                    html.P("R² = 0.52", className='stat-val'),
                    html.P("Model performance", className='stat-label'),
                ], className='stat-pill'),
            ], className='stat-row'),

        ], className='hero'),

        # findings summary
        html.Div([
            html.Div([
                html.P("What this research finds", className='summary-label'),
                html.Div([
                    html.Div([
                        html.P("The cause is fertilizer, not weather", className='summary-title'),
                        html.P("Every spring, nitrogen fertilizer from Midwest farms drains into the Mississippi River and flows into the Gulf. This triggers massive algal blooms. When the algae die and decompose, they consume all the oxygen in the water — suffocating fish, shrimp, and everything else on the seafloor. Our model shows that the amount of nitrogen entering the river in spring predicts the size of the dead zone that summer with a correlation of r = 0.788. Weather plays a secondary role.", className='summary-text'),
                    ], className='summary-block'),
                    html.Div([
                        html.P("Some years defy the model", className='summary-title'),
                        html.P("Six years had dead zones dramatically larger or smaller than the nitrogen load would predict. In 2017, record spring flooding pushed the zone to 22,720 km² — the largest ever recorded. In 2020, Hurricane Hanna hit the Gulf just days before the annual survey cruise, physically mixing the water column and breaking up the dead zone before it could be measured. These anomalies are flagged in red throughout the charts.", className='summary-text'),
                    ], className='summary-block'),
                    html.Div([
                        html.P("Policy has not worked", className='summary-title'),
                        html.P("The Gulf Hypoxia Task Force set a target of reducing the dead zone to under 4,921 km² by 2035. The 40-year average is 15,154 km² — more than three times that target. Despite decades of awareness, the zone has not meaningfully shrunk. Reducing it requires cutting nitrogen runoff from agriculture across 40% of the continental United States.", className='summary-text'),
                    ], className='summary-block'),
                ], className='summary-grid'),
            ], className='summary-inner'),
        ], className='summary-section'),

        # main grid
        html.Div([

            # left column
            html.Div([

                html.Div([
                    html.Div([
                        html.P("Dead zone area 1985–2024", className='card-label'),
                        html.P("Actual vs model prediction. Red bars = anomalous years.", className='card-sublabel'),
                    ], className='card-header'),
                    dcc.Graph(id='timeseries-chart', style={'height': '260px'},
                              config={'displayModeBar': False}),
                ], className='card'),

                html.Div([
                    html.Div([
                        html.Div([
                            html.P("Nitrogen load vs dead zone size", className='card-label'),
                            html.P("Each dot is one year. Higher nitrogen generally means a larger dead zone.", className='card-sublabel'),
                        ], className='card-header'),
                        dcc.Graph(id='scatter-chart', style={'height': '240px'},
                                  config={'displayModeBar': False}),
                    ], className='card'),

                    html.Div([
                        html.Div([
                            html.P("What drives the model", className='card-label'),
                            html.P("Nitrogen loading accounts for 80% of the model's predictive power.", className='card-sublabel'),
                        ], className='card-header'),
                        dcc.Graph(id='importance-chart', style={'height': '240px'},
                                  config={'displayModeBar': False}),
                    ], className='card'),

                ], className='two-col'),

                html.Div([
                    html.Div([
                        html.P("Model residuals", className='card-label'),
                        html.P("How far off was the model each year? Large gaps (red) correspond to hurricanes, droughts, or record flooding.", className='card-sublabel'),
                    ], className='card-header'),
                    dcc.Graph(id='residuals-chart', style={'height': '220px'},
                              config={'displayModeBar': False}),
                ], className='card'),

            ], className='left-col'),

            # right column
            html.Div([

                html.Div([
                    html.P("Model performance", className='card-label'),
                    html.Div([
                        html.Div([
                            html.P("R²", className='metric-label'),
                            html.P("0.52", className='metric-value', style={'color': '#1a6b8a'}),
                            html.P("variance explained", className='metric-sub'),
                        ], className='metric-card'),
                        html.Div([
                            html.P("MAE", className='metric-label'),
                            html.P("2,517", className='metric-value', style={'color': '#1a6b8a'}),
                            html.P("km² avg error", className='metric-sub'),
                        ], className='metric-card'),
                    ], className='metric-grid'),
                ], className='card', style={'marginBottom': '16px'}),

                html.Div([
                    html.P("Anomalous years", className='card-label'),
                    html.P("Years where the dead zone was far larger or smaller than the nitrogen load alone would predict.", className='card-sublabel'),
                    html.Div(id='anomaly-list', style={'marginTop': '12px'}),
                ], className='card', style={'padding': '18px 20px 20px'}),

            ], className='right-col'),

        ], className='main-grid'),

        # footer
        html.Div([
            html.P("Data: LUMCON / NOAA NCCOS · USGS Mississippi Nutrient Flux · NOAA OISST · Built by @bhavv04 · Source code on GitHub",
                   className='footer-text'),
        ], className='footer'),

    ], className='app-wrapper')