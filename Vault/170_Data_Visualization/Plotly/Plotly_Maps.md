---
tags:
  - plotly
  - python
  - data_visualization
  - interactive_plotting
  - maps
  - geospatial
  - choropleth
  - scatter_geo
  - mapbox
  - concept
  - example
aliases:
  - Plotly Maps
  - Plotly Geospatial Visualization
  - Choropleth Maps Plotly
  - Scatter Geo Plotly
related:
  - "[[170_Data_Visualization/Plotly/_Plotly_MOC|_Plotly_MOC]]"
  - "[[Plotly_Express_Quickstarts]]"
  - "[[Plotly_Graph_Objects_Detailed]]"
  - "[[GeoJSON_TopoJSON]]"
worksheet:
  - WS_DataViz_1
date_created: 2025-06-11
---
# Plotly: Plotting Maps (Geospatial Visualization)

Plotly provides excellent capabilities for creating interactive maps to visualize geospatial data. It supports several types of map plots, primarily through [[Plotly_Express_Quickstarts|Plotly Express]] and [[Plotly_Graph_Objects_Detailed|Graph Objects]].

There are two main categories of map types in Plotly:
1.  **Geo plots (`scatter_geo`, `choropleth`, `line_geo`):** Use natural Earth projections. Good for global or regional maps where a specific map projection is desired.
2.  **Mapbox plots (`scatter_mapbox`, `choropleth_mapbox`, `density_mapbox`, `line_mapbox`):** Use tile-based maps from Mapbox (requires a Mapbox access token for some styles/features, though a default open style is often available). Offer more detailed base maps with streets, terrain, satellite imagery.

## 1. Geo Plots (e.g., `px.scatter_geo`, `px.choropleth`)

-   **Projections:** Support various map projections (e.g., 'natural earth', 'orthographic', 'mercator').
-   **Scope:** Can define the geographical scope (e.g., 'world', 'usa', 'europe', or specific continents/countries).

[list2tab|#Geo Plot Types]
- `px.scatter_geo` / `go.Scattergeo`
    -   **Purpose:** Plots individual data points (scatter markers) on a map based on their latitude and longitude.
    -   **Key Parameters (`px.scatter_geo`):**
        -   `data_frame`: Pandas DataFrame.
        -   `lat`, `lon`: Column names for latitude and longitude.
        -   `locations`: Column name for location codes (e.g., ISO-3 country codes, USA state abbreviations). If used, `locationmode` must be set.
        -   `locationmode`: e.g., `'ISO-3'`, `'USA-states'`.
        -   `color`: Column to map to marker color.
        -   `size`: Column to map to marker size.
        -   `hover_name`, `hover_data`: For tooltips.
        -   `projection`: Type of map projection.
        -   `scope`: Defines the geographic scope of the map.
    -   **Example (Plotting major e-commerce warehouse locations):**
        ```python
        import plotly.express as px
        import pandas as pd

        # Conceptual warehouse locations
        warehouse_data = pd.DataFrame({
            'name': ['WH North America', 'WH Europe', 'WH Asia', 'WH South America'],
            'lat': [39.8283, 50.1109, 35.6895, -14.2350],
            'lon': [-98.5795, 8.6821, 139.6917, -51.9253],
            'capacity_units': [100000, 80000, 120000, 50000]
        })

        # fig_scatter_geo = px.scatter_geo(
        #     warehouse_data,
        #     lat="lat",
        #     lon="lon",
        #     hover_name="name",
        #     size="capacity_units",  # Size markers by capacity
        #     color="capacity_units", # Color markers by capacity (optional, can be different var)
        #     color_continuous_scale=px.colors.sequential.Plasma,
        #     projection="natural earth",
        #     title="E-commerce Warehouse Locations and Capacities"
        # )
        # fig_scatter_geo.update_layout(geo=dict(showland=True, landcolor="lightgray", showocean=True, oceancolor="lightblue"))
        # fig_scatter_geo.show()
        ```
- `px.choropleth` / `go.Choropleth`
    -   **Purpose:** Creates choropleth maps, where geographical regions (countries, states, counties) are colored according to a numerical variable.
    -   **Key Parameters (`px.choropleth`):**
        -   `data_frame`.
        -   `locations`: Column with location identifiers (e.g., ISO codes, FIPS codes, country names).
        -   `locationmode`: e.g., `'ISO-3'`, `'USA-states'`, `'country names'`.
        -   `color`: Column whose values determine the color of regions.
        -   `geojson` (for `go.Choropleth` or complex `px.choropleth`): GeoJSON object defining region boundaries if not using built-in geometries.
        -   `featureidkey` (for `go.Choropleth`): Path to the feature ID in the GeoJSON (e.g., `properties. sovereignt`).
        -   `scope`, `projection`, `color_continuous_scale`, `hover_name`.
    -   **Example (Sales per country):**
        ```python
        import plotly.express as px
        import pandas as pd

        # Conceptual sales data per country
        # In a real scenario, you'd have proper ISO codes or country names
        # Plotly Express can often match country names, but ISO codes are more robust
        country_sales_data = pd.DataFrame({
            'country_iso_alpha': ['USA', 'CAN', 'MEX', 'GBR', 'DEU', 'FRA', 'JPN', 'AUS', 'BRA'], # ISO 3166-1 alpha-3
            'total_sales': [500000, 150000, 120000, 200000, 180000, 160000, 250000, 90000, 70000],
            'country_name': ['United States', 'Canada', 'Mexico', 'United Kingdom', 'Germany', 'France', 'Japan', 'Australia', 'Brazil']
        })

        # fig_choropleth = px.choropleth(
        #     country_sales_data,
        #     locations="country_iso_alpha", # Column with ISO codes
        #     color="total_sales",
        #     hover_name="country_name",
        #     color_continuous_scale=px.colors.sequential.Blues,
        #     projection="robinson", # Another projection type
        #     title="Total E-commerce Sales by Country"
        # )
        # fig_choropleth.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
        # fig_choropleth.show()
        ```

## 2. Mapbox Plots (e.g., `px.scatter_mapbox`, `px.choropleth_mapbox`)

-   **Basemaps:** Use tile-based maps provided by Mapbox. Offer detailed street maps, satellite imagery, terrain, etc.
-   **Access Token:** For many Mapbox styles (beyond basic open ones like "open-street-map"), you need a Mapbox access token. You can set it using `px.set_mapbox_access_token("YOUR_TOKEN")` or pass it to layout.
-   **Interactivity:** Generally offer smoother zoom/pan due to tile-based rendering.

[list2tab|#Mapbox Plot Types]
- `px.scatter_mapbox` / `go.Scattermapbox`
    -   **Purpose:** Similar to `scatter_geo` but plots points on a Mapbox tile layer.
    -   **Key Parameters (`px.scatter_mapbox`):** `data_frame`, `lat`, `lon`, `color`, `size`, `hover_name`, `zoom`, `center`, `mapbox_style`.
    -   **Example (Plotting customer locations):**
        ```python
        import plotly.express as px
        import pandas as pd
        import numpy as np

        # Conceptual customer locations
        # np.random.seed(101)
        # customer_locations = pd.DataFrame({
        #     'customer_id': range(100),
        #     'lat': np.random.uniform(34.0, 40.0, 100), # Example: US West Coast area
        #     'lon': np.random.uniform(-122.0, -118.0, 100),
        #     'order_value': np.random.poisson(50, 100)
        # })

        # You might need a Mapbox access token for styles other than 'open-street-map'
        # px.set_mapbox_access_token("YOUR_MAPBOX_ACCESS_TOKEN") # Set if you have one

        # fig_scatter_mapbox = px.scatter_mapbox(
        #     customer_locations,
        #     lat="lat",
        #     lon="lon",
        #     color="order_value",
        #     size="order_value",
        #     color_continuous_scale=px.colors.cyclical.IceFire,
        #     size_max=15,
        #     zoom=6, # Initial zoom level
        #     center={"lat": 37.0902, "lon": -120.7129}, # Center map
        #     mapbox_style="open-street-map", # Basic style, no token needed
        #     # mapbox_style="carto-positron", # Another good open style
        #     # mapbox_style="satellite-streets", # Example requiring token
        #     hover_name="customer_id",
        #     title="Customer Order Locations and Values"
        # )
        # fig_scatter_mapbox.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
        # fig_scatter_mapbox.show()
        ```
- `px.choropleth_mapbox` / `go.Choroplethmapbox`
    -   **Purpose:** Choropleth maps using Mapbox tiles. Requires GeoJSON defining region boundaries.
    -   **Key Parameters:** `data_frame`, `geojson`, `locations` (column in df matching a key in GeoJSON features), `featureidkey` (path to ID in GeoJSON, e.g., "properties.STATEFP"), `color`, `center`, `zoom`, `mapbox_style`.
    -   **Example (Sales density by US states - conceptual, needs GeoJSON):**
        ```python
        # This example requires a GeoJSON file for US states.
        # import plotly.express as px
        # import pandas as pd
        # import json # For loading GeoJSON

        # Conceptual state sales data
        # state_sales = pd.DataFrame({
        #     'state_name': ['California', 'Texas', 'New York', 'Florida'],
        #     'sales_metric': [1000, 800, 900, 600],
        #     'FIPS_CODE': ['06', '48', '36', '12'] # Example FIPS codes
        # })

        # Load GeoJSON for US States (replace with actual path or URL)
        # try:
        #     with open('us_states_geojson.json') as f: # You'd need this file
        #         geojson_states = json.load(f)
        # except FileNotFoundError:
        #     print("GeoJSON file for states not found. Choropleth Mapbox example skipped.")
        #     geojson_states = None

        # if geojson_states:
        #     fig_choropleth_mapbox = px.choropleth_mapbox(
        #         state_sales,
        #         geojson=geojson_states,
        #         locations="FIPS_CODE",         # Column in df matching GeoJSON feature ID
        #         featureidkey="properties.STATEFP", # Path to ID in GeoJSON properties (example)
        #         color="sales_metric",
        #         color_continuous_scale="Viridis",
        #         mapbox_style="carto-positron",
        #         zoom=3,
        #         center={"lat": 37.0902, "lon": -95.7129},
        #         opacity=0.6,
        #         hover_name="state_name",
        #         title="Sales Metric by US State (Mapbox)"
        #     )
        #     fig_choropleth_mapbox.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
        #     fig_choropleth_mapbox.show()
        ```
- `px.density_mapbox` / `go.Densitymapbox`
    -   **Purpose:** Creates a heatmap layer showing point density on a Mapbox map.
    -   **Key Parameters:** `data_frame`, `lat`, `lon`, `z` (values for density calculation), `radius`, `center`, `zoom`, `mapbox_style`.

## Choosing Between Geo and Mapbox
-   **Geo Plots:**
    -   Good for statistical or thematic maps where specific projections are important.
    -   Self-contained (doesn't rely on external tile servers for basic rendering).
    -   Built-in geometries for world countries and US states simplify choropleths for these common cases.
-   **Mapbox Plots:**
    -   Provide richer, more detailed base maps (streets, satellite).
    -   Smoother zooming and panning experience.
    -   Better for applications requiring detailed geographical context.
    -   May require a Mapbox access token for full functionality and more styles.

Plotly's mapping capabilities are extensive, allowing for the creation of visually rich and interactive geospatial visualizations.

---